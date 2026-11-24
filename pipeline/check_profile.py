#!/usr/bin/env python3
"""Check that the game's text on the site is the game's and nothing in our own words: every profile
page, the kit of every arcanist page, the effect of every Psychube page and the effect column of
the Statuses page.

  python3 -I pipeline/check_profile.py [slug ...]   (with slugs: those arcanists and Psychubes only)

Reads the pinned tables in cache/ directly, not through pipeline/profile.py, so that a fault in
the writer's conversions shows here. For each page it removes every string of the arcanist's
rows in character_data, skin and character_voice (and the labels of the game's file screen)
from the page text, compared on letters and digits only. What is left must be our own two
headings (the skins section and the column of lines); anything else is text the game does not
have. Strings of the tables that the page lacks are not faults: the writer leaves out
mainland-only skins and lines, and unlabelled home-screen touches.

The cache is not in the repository; without it the check prints that it was skipped.
Exit 0: every page passes or the cache is missing. 1: a page has text that is not the game's.
"""
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'src' / 'content' / 'docs'
PINS = json.loads((ROOT / 'records' / 'sources.json').read_text())
DIRS = {'en': '', 'zh-tw': 'zh-tw/', 'zh-cn': 'zh-cn/', 'ja': 'ja/', 'ko': 'ko/'}
LANG_FILE = {'en': 'en', 'zh-tw': 'tw', 'ja': 'jp', 'ko': 'kr', 'zh-cn': 'zh'}
VOICE = {'en': 'encontent', 'zh-tw': 'twcontent', 'ja': 'jpcontent', 'ko': 'kocontent', 'zh-cn': 'content'}
UI_KEYS = ['language_10030422', 'language_10030423', 'language_10030424', 'language_10030425',
	'language_10005329', 'language_10005330']
# Our own headings: the skins section and the column of lines in the voice table.
OURS = {'en': ['Skins', 'Line'], 'zh-tw': ['皮膚', '台詞'], 'zh-cn': ['皮肤', '台词'],
	'ja': ['コスチューム', 'セリフ'], 'ko': ['스킨', '대사']}


def norm(s):
	s = re.sub(r'<marktop=([^>]*)>(.*?)</marktop>', r'\2\1', s or '')
	s = re.sub(r'<[^>]+>', '', s)
	s = re.sub(r'(?:#[\d.]+\s*)+(?=\||$)', '', s)  # timing of each segment of a voice line (a few have two)
	s = unicodedata.normalize('NFKC', s)
	return ''.join(c for c in s if c.isalnum())


def covered(seg, strings):
	"""Whether a cell is the game's strings end to end. Removing the longest first can fail: in
	'Cast Arcane Skill I (Idyll of the Luberon)' the label 'Cast Arcane Skill II' takes the I of Idyll."""
	ok = [True] + [False] * len(seg)
	for i in range(len(seg)):
		if ok[i]:
			for x in strings:
				if seg.startswith(x, i):
					ok[i + len(x)] = True
	return ok[-1]


def main(argv):
	gl = ROOT / 'cache' / 'gl' / PINS['gl']['commit']
	cn = ROOT / 'cache' / 'cn' / PINS['cn']['commit']
	if not (gl / 'data' / 'json' / 'skin.json').exists() or not (cn / 'data' / 'json' / 'skin.json').exists():
		print('check_profile: skipped, the pinned tables are not in cache/ (python3 -I pipeline/fetch_data.py)')
		return 0
	tab = lambda base, t: json.loads((base / 'data' / 'json' / f'{t}.json').read_text())
	text = {lang: {r['key']: r['content'] for r in json.loads((gl / 'data' / 'configs' / 'language' / f'language_{code}.json').read_text())}
		for lang, code in LANG_FILE.items()}
	tables = {srv: {t: tab(base, t) for t in ('character_data', 'skin', 'character_voice')} for srv, base in (('gl', gl), ('cn', cn))}
	arcs = {a['slug']: a for a in json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']}
	slugs = [s for s in argv if s in arcs] if argv else sorted(p.parent.name for p in (DOCS / 'arcanists').glob('*/profile.md'))
	faults = pages = 0
	for slug in slugs:
		hid = arcs[slug]['id']
		for lang, d in DIRS.items():
			path = DOCS / f'{d}arcanists/{slug}/profile.md'
			if not path.exists():
				print(f'{os.path.relpath(path, ROOT)}: missing')
				faults += 1
				continue
			pages += 1
			body = path.read_text().split('\n---\n', 1)[1]
			body = re.sub(r'\]\([^)]*\)', ']', body)
			# A string of the tables never runs across a table cell or a heading: keep those borders.
			# An escaped pipe is the game's own character, and '#74' with no space is not a heading.
			segs = [norm(x) for x in re.split(r'(?<!\\)\||^#+ |\n(?=#+ )', body, flags=re.M)]
			if lang == 'zh-cn':
				t, get = tables['cn'], (lambda v: v)
			else:
				t, get = tables['gl'], (lambda v: text[lang].get(v, v) if isinstance(v, str) else v)
			found = [text[lang].get(k, '') for k in UI_KEYS]
			for r in t['character_data']:
				if r['heroId'] == hid:
					found += [get(r['title']), get(r['text'])]
			for r in t['skin']:
				if r.get('characterId') == hid:
					found += [get(r.get(f, '')) for f in ('name', 'skinDescription', 'skinStory')]
			for r in t['character_voice']:
				if r['heroId'] == hid:
					found += [get(r['name']), r[VOICE[lang]]]
			ours = {norm(x) for x in OURS[lang]}
			strings = sorted({norm(x) for x in found if isinstance(x, str)} - {''}, key=lambda x: (-len(x), x))
			left = []
			for seg in segs:
				if not seg or seg in ours or covered(seg, strings):
					continue
				for x in strings:
					seg = seg.replace(x, '\x00')
				left += [p for p in seg.split('\x00') if p and p not in ours]
			if left:
				faults += 1
				print(f'{os.path.relpath(path, ROOT)}: text that is not the game\'s: {" | ".join(left)[:300]}')
	print(f'check_profile: {pages} pages, {faults} with faults')
	kit_faults = check_kits(argv)
	cube_faults = check_psychubes(argv, gl, cn)
	status_faults = 0 if argv else check_statuses(gl, cn)
	return 1 if faults or kit_faults or cube_faults or status_faults else 0


def check_statuses(gl, cn):
	"""The effect column of the Statuses page in every language, against skill_eff_desc.json: the rows
	come in the order of records/statuses.json, and each effect cell is the game's text of that id
	(the mainland client's on zh-cn) or, for a status the global client lacks, the one phrase saying so."""
	sys.path.insert(0, str(ROOT / 'pipeline'))
	from write_systems import NO_GL_TEXT
	st = json.loads((ROOT / 'records' / 'statuses.json').read_text())
	ids = [r['id'] for sec in st['sections'] for r in sec['rows']]
	desc = {srv: {r['id']: r.get('desc', '') for r in json.loads((base / 'data' / 'json' / 'skill_eff_desc.json').read_text())}
		for srv, base in (('gl', gl), ('cn', cn))}
	text = {lang: {r['key']: r['content'] for r in json.loads((gl / 'data' / 'configs' / 'language' / f'language_{code}.json').read_text())}
		for lang, code in LANG_FILE.items() if lang != 'zh-cn'}
	faults = 0
	for lang, d in DIRS.items():
		path = DOCS / f'{d}systems/statuses.md'
		lines = path.read_text().split('\n')
		rows = [l for n, l in enumerate(lines) if l.startswith('| ') and not l.startswith('| ---') and not lines[n + 1].startswith('| ---')]
		bad = [] if len(rows) == len(ids) else [f'{len(rows)} rows, {len(ids)} statuses']
		for i, line in zip(ids, rows):
			cell = re.split(r'(?<!\\)\|', line)[2]
			want = desc['cn'].get(i, '') if lang == 'zh-cn' else text[lang].get(desc['gl'].get(i, ''), '')
			want = re.sub(r'<id:\d+>', '', want or '')
			if norm(cell) != norm(want) and not (not want.strip() and cell.strip() == NO_GL_TEXT.get(lang)):
				bad.append(f'{i}: {cell.strip()[:60]}')
		if bad:
			faults += 1
			print(f'{os.path.relpath(path, ROOT)}: effect is not the game\'s: {" | ".join(bad)[:300]}')
	print(f'check_profile: 5 Statuses pages, {faults} with faults')
	return faults


def check_psychubes(argv, gl, cn):
	"""The effect section of every Psychube page (pipeline/psychube.py), against equip_skill.json and
	the language files: each paragraph is a label of ours (an Amplification level) and baseDesc of
	that level, the mainland client's on zh-cn pages, the global client's elsewhere."""
	sys.path.insert(0, str(ROOT / 'pipeline'))
	from psychube import AMP, EFFECT_HEAD, NAMES_HEAD
	cubes = json.loads((ROOT / 'records' / 'psychubes.json').read_text())['psychubes']
	rows = {srv: {} for srv in ('gl', 'cn')}
	for srv, base in (('gl', gl), ('cn', cn)):
		for r in json.loads((base / 'data' / 'json' / 'equip_skill.json').read_text()):
			rows[srv].setdefault(r['id'], {})[r['skillLv']] = r['baseDesc']
	text = {lang: {r['key']: r['content'] for r in json.loads((gl / 'data' / 'configs' / 'language' / f'language_{code}.json').read_text())}
		for lang, code in LANG_FILE.items() if lang != 'zh-cn'}
	faults = pages = 0
	for c in cubes:
		if argv and c['slug'] not in argv:
			continue
		for lang, d in DIRS.items():
			path = DOCS / f'{d}psychubes/{c["slug"]}.md'
			body = path.read_text().split('\n---\n', 1)[1]
			start, end = body.find(f'\n## {EFFECT_HEAD[lang]}\n'), body.find(f'\n## {NAMES_HEAD[lang]}\n')
			if lang != 'zh-cn' and not c['inGlobal']:
				if start >= 0:
					faults += 1
					print(f'{os.path.relpath(path, ROOT)}: an effect section, but the global client lacks this Psychube')
				continue
			pages += 1
			want = [rows['cn'][c['id']][lv] if lang == 'zh-cn' else text[lang].get(rows['gl'][c['id']][lv], '') for lv in range(1, 6)]
			paras = [x for x in body[start:end].split('\n\n')[1:] if x.strip()] if start >= 0 else []
			got, n, bad = [], 0, []
			for x in paras:
				m = re.match(r'\*\*([^*]+)\*\*[：:] ?', x)
				if m:
					n += 1
					if m.group(1) != AMP[lang].format(n=n):
						bad.append(f'label {m.group(1)}')
					got.append([x[m.end():]])
				elif got:
					got[-1].append(x)
				else:
					bad.append(x[:40])
			if len(got) != 5:
				bad.append(f'{len(got)} Amplification levels')
			for lv, (w, g) in enumerate(zip(want, got), 1):
				if norm(w) != norm(''.join(g)):
					bad.append(f'Amplification {lv}: {"".join(g)[:60]}')
			if bad:
				faults += 1
				print(f'{os.path.relpath(path, ROOT)}: effect is not the game\'s: {" | ".join(bad)[:300]}')
	print(f'check_profile: {pages} Psychube effects, {faults} with faults')
	return faults


def check_kits(argv):
	"""The kit of an arcanist page (pipeline/kit_text.py), against cache/source/<slug>.json.

	The kit runs from the first section heading to the names heading; the Insight material table
	is ours and is skipped. Every string of the arcanist's game text in that language is removed;
	what is left must be our labels (section names, a rank, Insight, Portray or Epiphany with its
	number) or the arcanist's name.
	"""
	sys.path.insert(0, str(ROOT / 'pipeline'))
	from kit_text import GAME_KIT, LAB, SEC, KEY, arcanist_name
	faults = pages = 0
	for slug in sorted(s for s in GAME_KIT if not argv or s in argv):
		src = json.loads((ROOT / 'cache' / 'source' / f'{slug}.json').read_text())
		for lang, d in DIRS.items():
			kit = src.get(KEY[lang])
			if not kit:
				continue
			pages += 1
			path = DOCS / f'{d}arcanists/{slug}.md'
			body = path.read_text().split('\n---\n', 1)[1]
			start = body.find(f'\n## {SEC[lang]["inc"]}\n')
			end = body.find(f'\n## {SEC[lang]["names"]}\n')
			region = '\n'.join(l for l in body[start:end].split('\n') if not l.startswith('|'))
			# A bold label of ours (`**Rank 1**`) is its own segment, apart from the text after it.
			segs = [(i % 2 == 1 or line.startswith('#'), norm(x)) for line in region.split('\n') for i, x in enumerate(line.split('**'))]
			strings = []

			def walk(o):
				if isinstance(o, dict):
					for k, v in o.items():
						if k in ('name', 'desc'):
							strings.append(re.sub(r'▩\d+%s(<\d+>)?|\{name\}', '\n', v or ''))
						else:
							walk(v)
				elif isinstance(o, list):
					for v in o:
						walk(v)
			walk(kit)
			pieces = {norm(y) for x in strings for y in x.split('\n')}
			pieces |= {norm(x) for x in re.split(r'<id:\d+>', ' '.join(strings))}
			pieces.add(norm(arcanist_name(slug, lang)))
			pieces = sorted((p for p in pieces if p), key=lambda x: (-len(x), x))
			lab, sec = LAB[lang], SEC[lang]
			ours = sorted({o for v in (*lab.values(), *sec.values()) for o in map(norm, re.split(r'\{\w*\}', v)) if o}, key=len, reverse=True)

			def strip(x, words):
				for w in words:
					x = x.replace(w, '\x00')
				return x

			left = []
			for is_label, seg in segs:
				# A label is ours with a game name in it (or a status name of the game alone); the text after
				# it is the game's.
				tries = [strip(strip(seg, pieces), ours)] + ([strip(strip(seg, ours), pieces)] if is_label else [])
				rests = [[x for x in re.sub(r'\d+', '', r).split('\x00') if x] for r in tries]
				left += min(rests, key=len)
			if left:
				faults += 1
				print(f'{os.path.relpath(path, ROOT)}: kit text that is not the game\'s: {" | ".join(left)[:300]}')
	print(f'check_profile: {pages} arcanist kits, {faults} with faults')
	return faults


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
