"""Build records from the pinned game data (pipeline/fetch_data.py fills cache/).

Writes two things:
  records/arcanists.json         facts for every arcanist: ids, names per language, rarity,
                                 afflatus, damage type, tags, whether the global client has it,
                                 Insight costs. Committed.
  cache/source/<slug>.json       the game's own text of each kit (skills, passives, Portray,
                                 Euphoria) in Simplified Chinese from the mainland client and, where
                                 the global client has the arcanist, in en, ja, ko, zh-TW. Not
                                 committed: writers restate it in records/text/.

  python3 -I pipeline/build_records.py
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINS = json.loads((ROOT / 'records' / 'sources.json').read_text())
LANGS = {'en': 'en', 'ja': 'jp', 'ko': 'kr', 'zh-TW': 'tw'}

AFFLATUS = {1: 'Mineral', 2: 'Star', 3: 'Plant', 4: 'Beast', 5: 'Spirit', 6: 'Intellect'}
DAMAGE = {1: 'Reality', 2: 'Mental'}


def table(key, name):
	sha = PINS[key]['commit']
	return json.loads((ROOT / 'cache' / key / sha / 'data' / 'json' / f'{name}.json').read_text())


def lang_map(code):
	sha = PINS['gl']['commit']
	rows = json.loads((ROOT / 'cache' / 'gl' / sha / 'data' / 'configs' / 'language' / f'language_{code}.json').read_text())
	return {r['key']: r['content'] for r in rows}


# Names that give no ASCII slug of their own.
SLUG_OVERRIDES = {3013: 'zima'}  # Зима, written in Cyrillic in the English text


def plain(name):
	"""A name without the markup the client puts in some (`<i>Lady by the Lake</i>`)."""
	return re.sub(r'<[^>]+>', '', name).strip()


def slug_of(name):
	s = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode()
	return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def by_id(rows, key='id'):
	return {r[key]: r for r in rows}


def group_rows(rows, key='heroId'):
	out = {}
	for r in rows:
		out.setdefault(r[key], []).append(r)
	return out


class Side:
	"""One client's tables, with a text function that resolves language keys."""

	def __init__(self, key, text):
		self.key = key
		self.text = text
		self.char = by_id(table(key, 'character'))
		self.skill = by_id(table(key, 'skill'))
		self.effect = by_id(table(key, 'skill_effect'))
		self.rank = group_rows(table(key, 'character_rank'))
		self.ex = group_rows(table(key, 'skill_ex_level'))
		self.passive = group_rows(table(key, 'skill_passive_level'))
		self.destiny = by_id(table(key, 'character_destiny'), 'heroId')
		self.facets = group_rows(table(key, 'character_destiny_facets'), 'facetsId')
		self.tags = by_id(table(key, 'character_battle_tag'))
		# Statuses and terms named in brackets in the skill text: name -> description.
		self.terms = {}
		for r in table(key, 'skill_eff_desc'):
			name, desc = self.text(r['name']), self.text(r['desc'])
			if desc and name not in self.terms:
				self.terms[name] = desc

	def statuses(self, texts):
		"""The bracketed terms of the kit text with their descriptions, and the terms those name."""
		seen, out, todo = set(), [], list(texts)
		while todo:
			for term in re.findall(r'【([^】]+)】|\[([^\]]+)\]', todo.pop(0)):
				term = term[0] or term[1]
				for name in (term, re.sub(r'<id:\d+>', '', term)):
					if name in self.terms and name not in seen:
						seen.add(name)
						out.append({'name': name, 'desc': self.terms[name]})
						todo.append(self.terms[name])
						break
		return out

	def skill_text(self, sid):
		s = self.skill.get(sid)
		if not s:
			return None
		eff = self.effect.get(s['skillEffect'], {})
		return {'id': sid, 'name': self.text(s['name']), 'desc': self.text(eff.get('desc', ''))}

	def kit(self, hid):
		c = self.char[hid]
		groups = []
		for part in c['skill'].split('|'):
			# A rank may list several forms of one card: `a,b`.
			ranks = [[int(y) for y in x.split(',')] for x in part.split('#')[1:]]
			groups.append([[self.skill_text(i) for i in forms] for forms in ranks])
		passives = []
		for p in sorted(self.passive.get(hid, []), key=lambda r: r['skillLevel']):
			passives.append({'insight': p['skillLevel'], **(self.skill_text(p['skillPassive']) or {})})
		portray = [{'level': r['skillLevel'], 'desc': self.text(r['desc'])}
			for r in sorted(self.ex.get(hid, []), key=lambda r: r['skillLevel'])]
		euphoria = []
		d = self.destiny.get(hid)
		if d:
			for fid in str(d['facetsId']).split('#'):
				for f in sorted(self.facets.get(int(fid), []), key=lambda r: r['level']):
					euphoria.append({'facet': int(fid), 'level': f['level'], 'desc': self.text(f['desc'])})
		texts = [f['desc'] for g in groups for r in g for f in r if f] + [p.get('desc', '') for p in passives]
		texts += [r['desc'] for r in portray + euphoria]
		ult = self.skill_text(c['exSkill'])
		texts.append((ult or {}).get('desc', ''))
		# Every other skill whose id starts with the arcanist's id: forms an incantation turns into,
		# cards a set or Euphoria grants, and the real kit where `skill` points at stand-in cards
		# (Nautika). Their text is part of what a page may state.
		used = {f['id'] for g in groups for r in g for f in r if f} | {p.get('id') for p in passives} | {(ult or {}).get('id')}
		other = [self.skill_text(sid) for sid in sorted(self.skill) if str(sid).startswith(str(hid)) and len(str(sid)) >= len(str(hid)) + 4 and sid not in used]
		other = [o for o in other if o and o['desc']]
		texts += [o['desc'] for o in other]
		return {
			'otherSkills': other,
			'statuses': self.statuses(texts),
			'incantations': groups,
			'ultimate': self.skill_text(c['exSkill']),
			'passives': passives,
			'portray': portray,
			'euphoria': euphoria,
			'tags': [self.text(self.tags[t]['tagName']) for t in str(c['battleTag']).split('#') if t in self.tags],
		}


class Items:
	"""Names of items and currencies, from the mainland client (zh-CN) and the global client."""

	def __init__(self, maps):
		self.cn = {('1', r['id']): r['name'] for r in table('cn', 'item')}
		self.cn.update({('2', r['id']): r['name'] for r in table('cn', 'currency')})
		self.gl = {}
		for kind, name in (('1', 'item'), ('2', 'currency')):
			for r in table('gl', name):
				self.gl[(kind, r['id'])] = {lang: plain(m.get(r['name'], r['name'])) for lang, m in maps.items()}

	def parse(self, consume):
		out = []
		for part in filter(None, consume.split('|')):
			kind, iid, count = part.split('#')
			key = (kind, int(iid))
			out.append({'id': int(iid), 'kind': 'item' if kind == '1' else 'currency', 'count': int(count),
				'names': {'zh-CN': self.cn.get(key), **self.gl.get(key, {})}})
		return out


def insight_step(r, items):
	"""Insight rank r['rank'] - 1, reached from the level cap of the rank before it."""
	effect = dict(e.split('#', 1) for e in r['effect'].split('|'))
	return {'insight': r['rank'] - 1, 'requiresLevel': int(r['requirement'].split('#')[1]),
		'levelCap': int(effect['1']), 'materials': items.parse(r['consume'])}


def main():
	cn = Side('cn', lambda s: s)
	maps = {lang: lang_map(code) for lang, code in LANGS.items()}
	gls = {lang: Side('gl', lambda s, m=m: m.get(s, s)) for lang, m in maps.items()}
	gl_en = gls['en']

	items = Items(maps)
	records = []
	(ROOT / 'cache' / 'source').mkdir(parents=True, exist_ok=True)
	for hid, c in sorted(cn.char.items()):
		if c['heroType'] == 0:  # story-only stand-ins
			continue
		in_gl = hid in gl_en.char
		names = {'zh-CN': plain(c['name']), 'en': plain(c['nameEng'])}
		if in_gl:
			for lang, side in gls.items():
				names[lang] = plain(side.text(side.char[hid]['name']))
		slug = SLUG_OVERRIDES.get(hid) or slug_of(names['en'])
		ranks = sorted(cn.rank.get(hid, []), key=lambda r: r['rank'])
		rec = {
			'id': hid,
			'slug': slug,
			'names': names,
			'stars': c['rare'] + 1,
			'afflatus': AFFLATUS.get(c['career'], c['career']),
			'damage': DAMAGE.get(c['dmgType'], c['dmgType']),
			'tagsZh': cn.kit(hid)['tags'],
			'inGlobal': in_gl,
			'online': c['isOnline'] == '1',
			'birthday': c['roleBirthday'],
			'euphoria': hid in cn.destiny,
			'euphoriaGlobal': in_gl and hid in gl_en.destiny,
			'insight': [insight_step(r, items) for r in ranks if r['rank'] > 1],
		}
		records.append(rec)
		source = {'id': hid, 'slug': slug, 'build': {k: PINS[k]['build'] for k in PINS},
			'zh-CN': cn.kit(hid)}
		if in_gl:
			for lang, side in gls.items():
				source[lang] = side.kit(hid)
		(ROOT / 'cache' / 'source' / f'{slug}.json').write_text(json.dumps(source, ensure_ascii=False, indent=1))
	out = ROOT / 'records' / 'arcanists.json'
	out.write_text(json.dumps({'build': {k: PINS[k]['build'] for k in PINS}, 'arcanists': records},
		ensure_ascii=False, indent='\t') + '\n')
	slugs = [r['slug'] for r in records]
	dupes = {s for s in slugs if slugs.count(s) > 1}
	print(len(records), 'arcanists;', sum(r['inGlobal'] for r in records), 'in the global client;',
		'duplicate slugs:', sorted(dupes) or 'none')
	return 1 if dupes else 0


if __name__ == '__main__':
	sys.exit(main())
