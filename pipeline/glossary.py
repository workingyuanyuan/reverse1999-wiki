"""Write a glossary of official strings for translators: cache/glossary.json.

For each English term it gives the global client's own string in Traditional Chinese, Japanese
and Korean, and the mainland client's Simplified Chinese where one is found. Sources: the
language files of the global client (by the key the English string has) and the mainland
tables (by the same table id). Terms: game words (Insight, Portrait, ...), status names,
skill names and Insight materials of the arcanists named on the command line.

  python3 -I pipeline/glossary.py sonetto druvis-iii [--out cache/glossary-<batch>.json]
"""
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINS = json.loads((ROOT / 'records' / 'sources.json').read_text())
LANG_FILES = {'zh-TW': 'tw', 'ja': 'jp', 'ko': 'kr', 'zh-CN-global': 'zh'}

WORDS = ['Insight', 'Portrait', 'Euphoria', 'Epiphany', 'Inheritance', 'Incantation', 'Ultimate', 'Moxie',
	'Genesis DMG', 'Reality DMG', 'Mental DMG', 'Penetration Rate', 'DMG Bonus', 'Critical DMG', 'Critical Rate',
	'DMG Taken Reduction', 'DMG Dealt', 'DMG Taken', 'Stats Up', 'Pos Status', 'Stats Down', 'Neg Status', 'Control',
	'Afflatus', 'Star', 'Mineral', 'Beast', 'Plant', 'Spirit', 'Intellect', 'Max HP', 'ATK', 'Reality DEF', 'Mental DEF',
	'Critical Resist', 'Critical DEF', 'Critical Resist Rate', 'Leech Rate', 'DMG Heal', 'Healing Done', 'Precognition',
	'Resonance', 'Psychube', 'Arcanist', 'DPS', 'Support', 'Heal', 'Remove Debuffs', 'Sharpodonty', 'Petrify', 'Disarm',
	'Circle of Life', 'Firebud', 'Mass attack', '1-target attack', 'Mass buff', 'Mass heal', 'Dispel', 'Purify']


# System words found by their Simplified Chinese string in the global client, where the
# English string is shared with other UI ("Portrait" is also the profile picture).
WORDS_ZH = ['洞悉', '塑造', '狂想', '传承', '咒语', '至终的仪式', '激情', '本源创伤', '先觉', '共鸣', '心相', '灵感', '洞知',
	'顿悟', '属性削弱', '状态异常', '控制', '受创减免', '治疗率', '暴击创伤', '创伤加成', '穿透率', '利齿子儿', '启示', '净化', '治疗']


def main(slugs, out=None):
	g = PINS['gl']['commit']
	langs = {}
	for lang, code in LANG_FILES.items():
		rows = json.loads((ROOT / 'cache' / 'gl' / g / 'data' / 'configs' / 'language' / f'language_{code}.json').read_text())
		langs[lang] = {r['key']: r['content'] for r in rows}
	en_rows = json.loads((ROOT / 'cache' / 'gl' / g / 'data' / 'configs' / 'language' / 'language_en.json').read_text())
	by_text = collections.defaultdict(list)
	for r in en_rows:
		by_text[r['content'].strip()].append(r['key'])

	def lookup(term):
		keys = by_text.get(term, [])
		if not keys:
			return None
		out = {}
		for lang, m in langs.items():
			vals = collections.Counter(re.sub(r'<[^>]+>', '', m[k]).strip() for k in keys if m.get(k))
			if vals:
				out[lang] = vals.most_common(1)[0][0]
		return out

	zh_rows = json.loads((ROOT / 'cache' / 'gl' / g / 'data' / 'configs' / 'language' / 'language_zh.json').read_text())
	by_zh = collections.defaultdict(list)
	for r in zh_rows:
		by_zh[r['content'].strip()].append(r['key'])
	en_map = {r['key']: r['content'] for r in en_rows}

	def lookup_zh(term):
		keys = by_zh.get(term, [])
		out = {}
		for lang, m in (('en', en_map), *langs.items()):
			vals = collections.Counter(re.sub(r'<[^>]+>', '', m[k]).strip() for k in keys if m.get(k))
			if vals:
				out[lang] = vals.most_common(1)[0][0]
		return out or None

	gloss = {'wordsByChinese': {}, 'words': {}, 'arcanists': {}}
	for w in WORDS_ZH:
		hit = lookup_zh(w)
		if hit:
			gloss['wordsByChinese'][w] = hit
	for w in WORDS:
		hit = lookup(w)
		if hit:
			gloss['words'][w] = hit
	records = {r['slug']: r for r in json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']}
	for slug in slugs:
		src = json.loads((ROOT / 'cache' / 'source' / f'{slug}.json').read_text())
		entry = {'names': records[slug]['names'], 'skills': [], 'statuses': {}, 'materials': {}}
		if 'en' in src:
			def name_rows(lang):
				"""Skill id -> name: incantations (every form), Ultimate, passives, other skills."""
				k = src[lang]
				rows = [f for group in k['incantations'] for forms in group for f in forms if f]
				rows += [k['ultimate']] if k.get('ultimate') else []
				rows += [p for p in k['passives'] if p.get('id')] + k.get('otherSkills', [])
				return {r['id']: r['name'] for r in rows}
			per = {lang: name_rows(lang) for lang in ('en', 'zh-TW', 'ja', 'ko', 'zh-CN')}
			seen = set()
			for sid, en in per['en'].items():
				row = {'en': en, **{l: per[l].get(sid) for l in ('zh-TW', 'ja', 'ko', 'zh-CN')}}
				key = tuple(row.values())
				if key not in seen:
					seen.add(key)
					entry['skills'].append(row)
			text = json.dumps(src['en'], ensure_ascii=False)
			for term in sorted(set(re.findall(r'\[([^\[\]<]+)', text))):
				hit = lookup(term)
				if hit:
					entry['statuses'][term] = hit
		for step in records[slug]['insight']:
			for m in step['materials']:
				if m['names'].get('en'):
					entry['materials'][m['names']['en']] = m['names']
		gloss['arcanists'][slug] = entry
	(Path(out) if out else ROOT / 'cache' / 'glossary.json').write_text(json.dumps(gloss, ensure_ascii=False, indent=1))
	print(len(gloss['words']), 'words;', {s: (len(e['skills']), len(e['statuses']), len(e['materials'])) for s, e in gloss['arcanists'].items()})


if __name__ == '__main__':
	args = sys.argv[1:]
	out = None
	if '--out' in args:
		i = args.index('--out')
		out = args[i + 1]
		del args[i:i + 2]
	main(args, out)
