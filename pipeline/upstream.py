"""Compare the game data the pages were written from with the current game data. Changes no page.

  python3 -I pipeline/upstream.py        (pnpm upstream)

The pages rest on two repositories of decoded client tables, pinned in records/sources.json.
This script reads the current head of each, fetches the same tables at that head into cache/,
and compares, page by page, the facts each page rests on:

  arcanists/<slug>   the arcanist's record (rarity, Afflatus, damage type, whether the global
                     client has it, Euphoria, Insight materials) and the game's text of the kit
                     in every language the clients carry
  index              which arcanists are out only on the mainland service
  systems/summoning  the summon rule texts of every banner type, in the mainland client and in
                     the global client's English text, and the base rates and pity of every pool
  psychubes/<slug>   the Psychube's record: rarity, tags, stats at max level, extra stat, the game's
                     recommendations, names and effect text in every language (pipeline/psychube.py)
  systems/statuses   the text of every status the page describes (records/statuses.json), both clients
  systems/insight    level caps and Sharpodonty cost of each Insight by rarity
  systems/combat     the Field Manual tips, the stat names and the Moxie cost of every Ultimate

Report: one line per difference, naming the page; lines starting "note" do not fail the check
(a new client build, a newer revision of a cited wiki page).
Exit 0: no difference. 1: differences. 2: the comparison could not be made.
upstream/README.md says how to update the pages after a difference.
"""
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'pipeline'))
import build_records as br  # noqa: E402
import fetch_data  # noqa: E402

PINNED = json.loads((ROOT / 'records' / 'sources.json').read_text())
DOCS = ROOT / 'src' / 'content' / 'docs'


def head(repo):
	out = subprocess.run(['git', 'ls-remote', f'https://github.com/{repo}', 'refs/heads/main'],
		capture_output=True, text=True, timeout=60, check=True)
	return out.stdout.split()[0]


def table(pins, key, name):
	return json.loads((ROOT / 'cache' / key / pins[key]['commit'] / 'data' / 'json' / f'{name}.json').read_text())


def facts(pins):
	"""Everything the pages rest on, for one pair of commits."""
	br.PINS = pins
	cn = br.Side('cn', lambda s: s)
	maps = {lang: br.lang_map(code) for lang, code in br.LANGS.items()}
	gls = {lang: br.Side('gl', lambda s, m=m: m.get(s, s)) for lang, m in maps.items()}
	items = br.Items(maps)
	out = {'arcanists': {}, 'mainland-only': {}, 'summoning': {}}
	for hid, c in sorted(cn.char.items()):
		if c['heroType'] == 0:
			continue
		in_gl = hid in gls['en'].char
		slug = br.SLUG_OVERRIDES.get(hid) or br.slug_of(br.plain(c['nameEng']))
		ranks = sorted(cn.rank.get(hid, []), key=lambda r: r['rank'])
		rec = {
			'record': {'stars': c['rare'] + 1, 'afflatus': c['career'], 'damage': c['dmgType'], 'inGlobal': in_gl,
				'euphoria': hid in cn.destiny, 'insight': [br.insight_step(r, items) for r in ranks if r['rank'] > 1]},
			'zh-CN': cn.kit(hid),
		}
		if in_gl:
			for lang, side in gls.items():
				rec[lang] = side.kit(hid)
				rec['record'][f'name-{lang}'] = br.plain(side.text(side.char[hid]['name']))
		out['arcanists'][slug] = rec
		if not in_gl:
			out['mainland-only'][slug] = br.plain(c['name'])
	# Summon rules: the text of every banner type (const.json, referenced from summon_pool_detail)
	# and the rates and pity of every pool.
	en = maps['en']
	for key in ('cn', 'gl'):
		const = {str(r['id']): r for r in table(pins, key, 'const')}
		for d in table(pins, key, 'summon_pool_detail'):
			info = d['info'].strip()
			text = const.get(info, {}).get('value2', '')
			if key == 'gl':
				text = en.get(text, text)
			# Markup and line breaks change with the layout of the in-game window, not with the rule.
			out['summoning'][f'{key} banner type {d["id"]}'] = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', text)).strip()
		out['summoning'][f'{key} rates and pity'] = sorted({(p['initWeight'], p['awardTime']) for p in table(pins, key, 'summon_pool')})
	out.update(system_facts(pins))
	return out


def system_facts(pins):
	"""What the Psychube pages and the newer system pages rest on, read through pipeline/gamedata.py."""
	import importlib
	import gamedata
	gamedata.use(pins)
	import psychube
	import write_systems
	psychube = importlib.reload(psychube)
	out = {'psychubes': {slug: {k: v for k, v in p.items() if k != 'slug'} for slug, p in psychube.REC.items()}}
	st = json.loads((ROOT / 'records' / 'statuses.json').read_text())
	ids = [r['id'] for sec in st['sections'] for r in sec['rows']]
	out['statuses'] = {f'{key} {i}': ((gamedata.cn_row if key == 'cn' else gamedata.gl_row)('skill_eff_desc', i) or {}).get('desc')
		for key in ('cn', 'gl') for i in ids}
	for i in ids:
		row = gamedata.gl_row('skill_eff_desc', i)
		out['statuses'][f'en {i}'] = gamedata.text(row['desc'], 'en') if row else None
	out['insight'] = {str(k): v for k, v in write_systems.insight_data().items()}
	out['combat'] = {
		'cn tips': [r['content'] for r in gamedata.cn('loading_text')],
		'en tips': [gamedata.text(r['content'], 'en') for r in gamedata.gl('loading_text')],
		'stats': [(r['id'], r['name']) for r in gamedata.cn('character_attribute')],
		'ultimate cost': sorted(str(c['uniqueSkill_point']) for c in gamedata.cn('character')),
	}
	gamedata.use(PINNED)
	return out


def diff_parts(a, b):
	return sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))


def fandom_notes():
	"""Cited Fandom revisions that are no longer the latest: notes, since Fandom is a second witness."""
	notes = []
	for page in sorted(DOCS.glob('arcanists/*.md')) + [DOCS / 'systems' / f'{p}.md' for p in ('summoning', 'combat', 'insight')]:
		for title, oldid in re.findall(r'fandom\.com/wiki/([^?\s]+)\?oldid=(\d+)', page.read_text()):
			q = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions', 'titles': urllib.parse.unquote(title),
				'rvprop': 'ids', 'format': 'json'})
			req = urllib.request.Request(f'https://reverse1999.fandom.com/api.php?{q}', headers={'User-Agent': 'Mozilla/5.0'})
			with urllib.request.urlopen(req, timeout=60) as r:
				pages = json.load(r)['query']['pages']
			rev = next(iter(pages.values()))['revisions'][0]['revid']
			if str(rev) != oldid:
				notes.append(f'note {page.relative_to(DOCS).with_suffix("")}: Fandom {urllib.parse.unquote(title)} has revision {rev}; the page cites {oldid}')
	# The art (records/art.json, written by pipeline/fetch_art.py): a newer upload of the file.
	art = json.loads((ROOT / 'records' / 'art.json').read_text()) if (ROOT / 'records' / 'art.json').exists() else {}
	for slug, a in sorted(art.items()):
		q = urllib.parse.urlencode({'action': 'query', 'titles': a['file'], 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json'})
		req = urllib.request.Request(f'https://reverse1999.fandom.com/api.php?{q}', headers={'User-Agent': 'Mozilla/5.0'})
		with urllib.request.urlopen(req, timeout=60) as r:
			page = next(iter(json.load(r)['query']['pages'].values()))
		url = (page.get('imageinfo') or [{}])[0].get('url')
		if url != a['url']:
			now = 'is gone' if not url else 'has a newer upload'
			notes.append(f'note arcanists/{slug}: Fandom {a["file"]} {now}; the page shows the upload of {a["uploaded"]}')
	return notes


def main():
	try:
		current = {}
		for key, pin in PINNED.items():
			sha = head(pin['repo'])
			current[key] = {**pin, 'commit': sha}
			if fetch_data.fetch(key, sha, quiet=True) or fetch_data.fetch(key, pin['commit'], quiet=True):
				raise RuntimeError(f'could not fetch the tables of {key}')
			current[key]['build'] = json.loads(fetch_data.path_of(key, sha, 'data/meta.json').read_text())['version']
		lines = [f'note: {k} client {PINNED[k]["build"]} -> {current[k]["build"]} (commit {current[k]["commit"][:7]})'
			for k in PINNED if current[k]['commit'] != PINNED[k]['commit']]
		if lines:
			old, new = facts(PINNED), facts(current)
			pages = {p.stem for p in DOCS.glob('arcanists/*.md')}
			for slug in sorted(pages):
				a, b = old['arcanists'].get(slug, {}), new['arcanists'].get(slug, {})
				parts = diff_parts(a, b)
				if parts:
					lines.append(f'arcanists/{slug}: changed in {", ".join(parts)}')
			for slug in diff_parts(old['mainland-only'], new['mainland-only']):
				what = 'now in the global client' if slug in old['mainland-only'] else 'new, mainland client only'
				lines.append(f'index: {slug} ({new["mainland-only"].get(slug) or old["mainland-only"][slug]}) {what}')
			for slug in sorted(set(new['arcanists']) - set(old['arcanists']) - set(new['mainland-only'])):
				lines.append(f'note: new arcanist {slug} in both clients')
			for part in diff_parts(old['summoning'], new['summoning']):
				lines.append(f'systems/summoning: {part} changed')
			for slug in diff_parts(old['psychubes'], new['psychubes']):
				if slug not in old['psychubes']:
					lines.append(f'psychubes: new Psychube {slug}')
				elif slug not in new['psychubes']:
					lines.append(f'psychubes/{slug}: gone from the mainland client')
				else:
					lines.append(f'psychubes/{slug}: changed in {", ".join(diff_parts(old["psychubes"][slug], new["psychubes"][slug]))}')
			for page in ('statuses', 'insight', 'combat'):
				for part in diff_parts(old[page], new[page]):
					lines.append(f'systems/{page}: {part} changed')
		lines += fandom_notes()
	except Exception as e:  # noqa: BLE001
		print(f'comparison failed: {e}', file=sys.stderr)
		return 2
	for line in lines:
		print(line)
	differences = [l for l in lines if not l.startswith('note')]
	print(f'{len(differences)} difference(s), {len(lines) - len(differences)} note(s)')
	return 1 if differences else 0


if __name__ == '__main__':
	sys.exit(main())
