#!/usr/bin/env python3
"""Write the kit of an arcanist page in the game's own words.

  python3 -I pipeline/kit_text.py write <slug> ...     rewrite the kit sections of the page in every language
  python3 -I pipeline/kit_text.py show <lang> <slug>   print the kit sections

The kit sections run from the end of the profile table to the names table: the incantations by
rank, the Ultimate, the status terms the kit names, the Insight passives with the material
table, the Portray levels and Euphoria. Every description is the game's text as the client
gives it (cache/source/<slug>.json, written by build_records.py): English, Japanese, Korean
and Traditional Chinese from the global client, Simplified Chinese from the mainland client.
Only the headings and the column labels are ours. zh-cn pages are converted from zh-tw by
scripts/to-zh-cn.py and then get their kit from here, so run `write` after it.

The client's marks are resolved as the game shows them (checked against the Reverse: 1999
Wiki on Fandom for Sonetto, Lucy, the Twins and Aleph): ▩0%s is the name of the arcanist's
passive, ▩1%s and ▩2%s the incantations, ▩3%s the Ultimate, ▩NM%s incantation N at rank M;
a form mark after it (<1>) is not shown; {name} is the arcanist's name; <id:N> after a term is
not shown. A mark that cannot be resolved stops the script.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'pipeline'))
import profile as pf  # noqa: E402  the rich-text conversion of the profile pages
import scaffold as sc  # noqa: E402  section names, the material table and the arcanists' names

DOCS = ROOT / 'src' / 'content' / 'docs'
KEY = {'en': 'en', 'zh-tw': 'zh-TW', 'zh-cn': 'zh-CN', 'ja': 'ja', 'ko': 'ko'}
DIRS = {'en': '', 'zh-tw': 'zh-tw/', 'zh-cn': 'zh-cn/', 'ja': 'ja/', 'ko': 'ko/'}
CJK = {'zh-tw', 'zh-cn', 'ja'}
# Our own headings and column labels.
LAB = {
	'en': dict(rank='Rank {n}', inc='Incantation', eff='Effect', st='Statuses', st_col='Status', ins='Insight', name='Name',
		por='Portrait', epi_lv='Epiphany {f}, level {n}'),
	'zh-tw': dict(rank='{n} 階', inc='咒語', eff='效果', st='狀態', st_col='狀態', ins='洞悉', name='名稱',
		por='塑造', epi_lv='閃念 {f}・等級 {n}'),
	'zh-cn': dict(rank='{n} 阶', inc='咒语', eff='效果', st='状态', st_col='状态', ins='洞悉', name='名称',
		por='塑造', epi_lv='闪念 {f}・等级 {n}'),
	'ja': dict(rank='ランク{n}', inc='スペル', eff='効果', st='状態', st_col='状態', ins='洞察', name='名前',
		por='塑造', epi_lv='瞬想 {f}・レベル {n}'),
	'ko': dict(rank='{n}단계', inc='주문', eff='효과', st='상태', st_col='상태', ins='통찰', name='이름',
		por='형상', epi_lv='발상 {f} · 레벨 {n}'),
}
SEC = {**{k: sc.L[k]['sec'] for k in ('en', 'zh-tw', 'ja', 'ko')},
	'zh-cn': dict(inc='咒语', ult='至终的仪式：{n}', inh='传承', por='塑造', eup='狂想', names='名称')}


def kit_of(slug, lang):
	src = json.loads((ROOT / 'cache' / 'source' / f'{slug}.json').read_text())
	return src.get(KEY[lang])


def arcanist_name(slug, lang):
	a = sc.REC[slug]
	return a['names']['zh-CN'] if lang == 'zh-cn' else sc.name(a, lang)


class Text:
	"""The game's text of one kit in one language, with the client's marks resolved."""

	def __init__(self, slug, lang, kit):
		self.slug, self.lang, self.kit = slug, lang, kit
		self.name = arcanist_name(slug, lang)

	def ref(self, m):
		# The game shows the name in a colour of its own; here it is bold.
		return f'<b>{self.ref_name(m)}</b>'

	def ref_name(self, m):
		n, k = m.group(1), self.kit
		try:
			if n == '0':
				return k['passives'][0]['name']
			if n == '3':
				return k['ultimate']['name']
			if len(n) == 1:
				return k['incantations'][int(n) - 1][0][0]['name']
			return k['incantations'][int(n[0]) - 1][int(n[1]) - 1][0]['name']
		except (IndexError, KeyError, TypeError):
			raise SystemExit(f'{self.slug} {self.lang}: cannot resolve {m.group(0)}')

	def plain(self, s):
		s = (s or '').replace('\r', '')
		s = re.sub(r'▩(\d+)%s(?:<\d+>)?', self.ref, s)
		s = s.replace('{name}', self.name)
		s = re.sub(r'<id:\d+>', '', s)
		if re.search(r'▩|%s|\{\w*\}', s):
			raise SystemExit(f'{self.slug} {self.lang}: unresolved mark in {s[:80]!r}')
		return s

	def lines(self, s):
		"""The text as Markdown, one string per line of the client."""
		return [pf.inline(x) for x in self.plain(s).split('\n') if x.strip()]

	def cell(self, s):
		return '<br>'.join(self.lines(s))

	def paras(self, s):
		return '\n\n'.join(self.lines(s))

	def term(self, s):
		return pf.one_line(re.sub(r'<id:\d+>', '', s or ''), self.lang)


def has_game_kit(slug):
	"""Whether the arcanist page's kit is written by this script: every arcanist the game has text for."""
	return slug in GAME_KIT


# Every arcanist with a page and a kit record.
GAME_KIT = {p.stem for p in (ROOT / 'cache' / 'source').glob('*.json')
	if (DOCS / 'arcanists' / f'{p.stem}.md').exists()}

# A kit the battle logic swaps in at an Insight rank, which no table records. Read from the Insight II
# tab of the Reverse: 1999 Wiki on Fandom (Nautika) and matched to the skill ids, whose text is the
# game's: from that rank on, these incantations and this Ultimate replace the ones the character
# record lists, and the cards a choice card casts are listed after them.
AFTER_INSIGHT = {
	'nautika': dict(insight=2, incantations=[[31200111, 31200112, 31200113], [31200121, 31200122, 31200123]],
		cast=[[31200151, 31200152, 31200153], [31200161, 31200162, 31200163]], ultimate=31200131),
}


def by_rank(group):
	"""The forms of an incantation by rank. Where a card casts forms of its own (Brume), the character
	record lists them in one run whose commas do not fall at the ranks; the rank is then the
	second-to-last digit of the form's id (base card 31350111, its forms 313501111 and 313501112)."""
	forms = [f for r in group for f in r or [] if f]
	if not any(len(str(f['id'])) > len(str(forms[0]['id'])) for f in forms):
		return group
	out = {}
	for f in forms:
		i = str(f['id'])
		r = int(i[-1] if len(i) == len(str(forms[0]['id'])) else i[-2])
		out.setdefault(r, []).append(f)
	return [out.get(r, []) for r in range(1, max(out) + 1)]


def with_insight_kit(slug, kit):
	"""The kit with the incantations and Ultimate an Insight rank swaps in (AFTER_INSIGHT), taken from
	the arcanist's other skills by id. The Ultimate is the swapped-in one: the character record has none."""
	swap = AFTER_INSIGHT.get(slug)
	if not swap:
		return kit
	by_id = {o['id']: o for o in kit['otherSkills']}
	try:
		pick = lambda groups: [[[by_id[i]] for i in g] for g in groups]  # noqa: E731
		later = dict(insight=swap['insight'], incantations=pick(swap['incantations']), cast=pick(swap['cast']))
		ult = by_id[swap['ultimate']]
	except KeyError as e:
		raise SystemExit(f'{slug}: skill {e} of AFTER_INSIGHT is not in the record')
	return {**kit, 'afterInsight': later, 'ultimate': kit.get('ultimate') or ult}


def same_entries(kit, gl):
	"""The mainland kit cut to the entries the global client has, so that every language holds the
	same rows: an Insight passive, Portray level or Epiphany out on the mainland service only is left out."""
	ids = lambda k: [[[f and f['id'] for f in forms or []] for forms in g] for g in k['incantations']]  # noqa: E731
	if ids(kit) != ids(gl):
		raise SystemExit('the incantations of the two clients differ')
	kit = dict(kit)
	keep = {p['id'] for p in gl['passives']}
	kit['passives'] = [p for p in kit['passives'] if p['id'] in keep]
	keep = {p['level'] for p in gl['portray']}
	kit['portray'] = [p for p in kit['portray'] if p['level'] in keep]
	keep = {(e['facet'], e['level']) for e in gl['euphoria']}
	kit['euphoria'] = [e for e in kit['euphoria'] if (e['facet'], e['level']) in keep]
	return kit


def sections(slug, lang):
	"""The kit sections of the page as Markdown, from the end of the profile table to the names table.

	Each entry is a bold label of ours, then the game's text; a line break of the client starts a
	new paragraph. No table holds the game's text: its lines do not fit in a cell.
	"""
	kit = kit_of(slug, lang)
	if not kit:
		# An arcanist out on the mainland service only has no text in this language: the page keeps
		# the Insight materials, a fact, and the zh-cn page has the kit.
		mats = sc.blocks(slug, lang).get('materials')
		if lang == 'zh-cn' or not mats:
			raise SystemExit(f'{slug}: the game has no {lang} text')
		return f'## {SEC[lang]["inh"]}\n\n{mats}'
	gl = kit_of(slug, 'zh-tw')
	if lang == 'zh-cn' and gl:
		try:
			kit = same_entries(kit, gl)
		except SystemExit as e:
			raise SystemExit(f'{slug}: {e}')
	kit = with_insight_kit(slug, kit)
	t, lab, sec = Text(slug, lang, kit), LAB[lang], SEC[lang]
	colon = '：' if lang in CJK else ': '
	dot = '・' if lang in CJK else ' · '

	def entry(label, desc, indent=''):
		lines = t.lines(desc)
		first = f'**{label}**{colon}{lines[0]}' if lines else f'**{label}**'
		return [first] + [x for line in lines[1:] for x in ('', indent + line)]

	def cards(groups, prefix=''):
		got = []
		for group in groups:
			# A rank the card does not have is empty (Coppelia's incantations have one rank).
			ranks = [(r, [f for f in forms if f]) for r, forms in enumerate(group, 1) if forms]
			ranks = [(r, forms) for r, forms in ranks if forms]
			if not ranks:
				continue
			first = ranks[0][1][0]
			got += ['', f'### {t.term(first["name"])}']
			for r, forms in ranks:
				for f in forms:
					label = prefix + lab['rank'].format(n=r)
					# A form with a name of its own (the Twins' rank 2 and 3) is named in its label.
					if f['name'] != first['name'] or len(forms) > 1:
						label += dot + t.term(f['name'])
					got += [''] + entry(label, f['desc'])
		return got

	out = [f'## {sec["inc"]}'] + cards([by_rank(g) for g in kit['incantations']])
	later = kit.get('afterInsight')
	if later:
		out += cards(later['incantations'] + later['cast'], f'{lab["ins"]} {later["insight"]}{dot}')
	ult = kit.get('ultimate')
	if ult:
		out += ['', f'## {sec["ult"].format(n=t.term(ult["name"]))}', '', t.paras(ult['desc'])]
	out += ['', f'## {sec["inh"]}']
	for p in kit['passives']:
		out += [''] + entry(f'{lab["ins"]} {p["insight"]}{dot}{t.term(p["name"])}', p['desc'])
	mats = sc.blocks(slug, 'zh-tw' if lang == 'zh-cn' else lang).get('materials')
	if mats:
		out += ['', mats]
	# Schneider, never released, has five Portrait levels with no text.
	if any(p['desc'] for p in kit.get('portray', [])):
		out += ['', f'## {sec["por"]}']
		for p in kit['portray']:
			out += [''] + entry(f'{lab["por"]} {p["level"]}', p['desc'])
	if kit.get('euphoria'):
		facets = list(dict.fromkeys(e['facet'] for e in kit['euphoria']))
		out += ['', f'## {sec["eup"]}']
		for e in kit['euphoria']:
			out += [''] + entry(lab['epi_lv'].format(f=facets.index(e['facet']) + 1, n=e['level']), e['desc'])
	# Status terms the text names, each name once, with the wording of its first mention. A
	# stronger version of a term (its own <id:N>, named by a Portray level or an Epiphany) is not
	# shown: which level an <id:N> belongs to is not in the data, and that level's text states the change.
	terms = {x['name']: x['desc'] for x in kit.get('statuses', [])}
	shown, found = set(), []
	every = kit['incantations'] + (later['incantations'] + later['cast'] if later else [])
	todo = [f['desc'] for g in every for r in g if r for f in r if f] + [(ult or {}).get('desc', '')]
	todo += [p['desc'] for p in kit['passives']] + [p['desc'] for p in kit.get('portray', [])]
	todo += [e['desc'] for e in kit.get('euphoria', [])]
	while todo:
		for a, b in re.findall(r'【([^】]+)】|\[([^\]]+)\]', todo.pop(0) or ''):
			tok = a or b
			desc = terms.get(tok) or terms.get(re.sub(r'<id:\d+>', '', tok))
			base_name = re.sub(r'<id:\d+>', '', tok)
			if desc and desc.strip() and base_name not in shown:
				shown.add(base_name)
				found.append((base_name, desc))
				todo.append(desc)
	if found:
		out += ['', f'## {lab["st"]}', '']
		for n, d in found:
			out += ['- ' + entry(t.term(n), d, '  ')[0]] + entry(t.term(n), d, '  ')[1:]
	return '\n'.join(out)


def rewrite(slug, lang):
	path = DOCS / f'{DIRS[lang]}arcanists/{slug}.md'
	text = path.read_text()
	head, sep, body = text.partition('\n---\n')
	names = f'\n## {SEC[lang]["names"]}\n'
	# The kit starts after the profile table (the first table of the body) and its paragraph.
	m = re.search(r'^\|.*\|\n(?!\|)', body, re.M)
	end = body.find(names)
	if not m or end < 0:
		raise SystemExit(f'{path.relative_to(ROOT)}: no profile table or names heading')
	new = body[:m.end()] + '\n' + sections(slug, lang) + '\n' + body[end:]
	if new != body:
		path.write_text(head + sep + new)
		return True
	return False


def main(argv):
	if argv[:1] == ['show'] and len(argv) == 3:
		print(sections(argv[2], argv[1]))
		return 0
	if argv[:1] == ['write'] and len(argv) > 1:
		for slug in argv[1:]:
			changed = [lang for lang in DIRS if rewrite(slug, lang)]
			print(f'{slug}: {", ".join(changed) or "unchanged"}')
		return 0
	print(__doc__)
	return 2


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
