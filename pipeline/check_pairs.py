"""Psychube and arcanist pages list each other: a link on one side needs the link back.

Usage: python3 -I pipeline/check_pairs.py      (run by `pnpm verify`; exit 1 on a problem)

Reads only the page files, in every language folder (zh-cn included), so it runs on a fresh
checkout without the game-data cache. Each Psychube page's Recommended row and each arcanist
page's recommended-Psychube row are found by their label; a link in any other row or in prose
does not count. Both rows are written by the pipeline from character_recommend.json
(pipeline/psychube.py, pipeline/scaffold.py). A link in those rows must stay in the page's own
language folder and point at a page that exists.
"""
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / 'src' / 'content' / 'docs'
LANGS = ['', 'zh-tw/', 'zh-cn/', 'ja/', 'ko/']
# Row labels: (on arcanist pages, on Psychube pages); zh-cn is converted from zh-tw by scripts/to-zh-cn.py.
LABELS = {
	'': ('Psychubes recommended in game', 'Recommended in game for'),
	'zh-tw/': ('遊戲內推薦的心相', '遊戲內推薦的神秘學家'),
	'zh-cn/': ('游戏内推荐的心相', '游戏内推荐的神秘学家'),
	'ja/': ('ゲーム内のおすすめ心相', 'ゲーム内のおすすめ神秘学家'),
	'ko/': ('게임 내 추천 의지', '게임 내 추천 마도학자'),
}
LINK = re.compile(r'\]\((/[^)\s]*)\)')


def rows(d, kind, label, target, errors):
	"""{page slug: set of linked target slugs} from the row with that label."""
	out = {}
	for f in sorted((DOCS / d / kind).glob('*.md')):
		found = set()
		for line in f.read_text().split('\n'):
			if not line.startswith(f'| {label} | '):
				continue
			for url in LINK.findall(line):
				m = re.fullmatch(rf'/{re.escape(d)}{target}/([^/#]+)/(?:#[^)]*)?', url)
				if not m:
					errors.append(f'{d}{kind}/{f.name}: link {url} is not a {target} page in this language')
				elif not (DOCS / d / target / f'{m.group(1)}.md').exists():
					errors.append(f'{d}{kind}/{f.name}: link {url} has no page')
				else:
					found.add(m.group(1))
		out[f.stem] = found
	return out


def main():
	errors, n = [], 0
	for d in LANGS:
		a_label, p_label = LABELS[d]
		arc = rows(d, 'arcanists', a_label, 'psychubes', errors)
		psy = rows(d, 'psychubes', p_label, 'arcanists', errors)
		for x, ps in arc.items():
			for y in sorted(ps):
				n += 1
				if x not in psy.get(y, ()):
					errors.append(f'{d}arcanists/{x}.md lists {y}; {d}psychubes/{y}.md does not list {x}')
		for y, xs in psy.items():
			for x in sorted(xs):
				if y not in arc.get(x, ()):
					errors.append(f'{d}psychubes/{y}.md lists {x}; {d}arcanists/{x}.md does not list {y}')
	for e in errors:
		print(e)
	print(f'psychube pairs: {n} link(s), {len(errors)} problem(s)')
	return 1 if errors else 0


if __name__ == '__main__':
	sys.exit(main())
