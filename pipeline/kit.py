"""Print an arcanist's kit text from the game data, side by side in the languages asked for.

  python3 -I pipeline/kit.py <slug> [lang ...]      (default: zh-CN en)

Reads cache/source/<slug>.json (pipeline/build_records.py). For each incantation rank, the
Ultimate, each Insight passive, each Portrait level, each Euphoria level and each status the
kit names, one line per language. Markup is removed. A language the client lacks is skipped.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def clean(s):
	return re.sub(r'\s+', ' ', re.sub(r'</?(?:nobr|color[^>]*|b|i|u|size[^>]*)>', '', s or '')).strip()


def main(slug, langs):
	src = json.loads((ROOT / 'cache' / 'source' / f'{slug}.json').read_text())
	rec = next(a for a in json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists'] if a['slug'] == slug)
	langs = [l for l in langs if l in src]
	print(f'# {slug}: {rec["names"]}')
	print(f'stars {rec["stars"]}, afflatus {rec["afflatus"]}, damage {rec["damage"]}, in global client {rec["inGlobal"]}, '
		f'released on mainland {rec["online"]}, Euphoria mainland {rec["euphoria"]} / global {rec["euphoriaGlobal"]}')
	print(f'languages here: {", ".join(langs)}\n')

	def show(label, get):
		print(f'## {label}')
		for l in langs:
			try:
				v = get(src[l])
			except (IndexError, KeyError, TypeError):
				v = None
			if v:
				print(f'{l}: {v}')
		print()

	for g in range(len(src['zh-CN']['incantations'])):
		for r in range(len(src['zh-CN']['incantations'][g])):
			for f in range(len(src['zh-CN']['incantations'][g][r])):
				show(f'incantation {g + 1}, rank {r + 1}' + (f', form {f + 1}' if f else ''),
					lambda k: (lambda x: f'{x["name"]}: {clean(x["desc"])}')(k['incantations'][g][r][f]))
	show('ultimate', lambda k: f'{k["ultimate"]["name"]}: {clean(k["ultimate"]["desc"])}')
	for i in range(len(src['zh-CN']['passives'])):
		show(f'insight passive {src["zh-CN"]["passives"][i]["insight"]}', lambda k: f'{k["passives"][i].get("name")}: {clean(k["passives"][i].get("desc"))}')
	for i in range(len(src['zh-CN']['portray'])):
		show(f'portrait {i + 1}', lambda k: clean(k['portray'][i]['desc']))
	for i in range(len(src['zh-CN']['euphoria'])):
		e = src['zh-CN']['euphoria'][i]
		show(f'euphoria facet {e["facet"]} level {e["level"]}', lambda k: clean(k['euphoria'][i]['desc']))
	print('# other skills with this arcanist\'s id (forms, granted cards, a kit the main list misses)')
	for l in langs:
		for o in src[l].get('otherSkills', []):
			print(f'{l}: {o["id"]} {o["name"]}: {clean(o["desc"])}')
		print()
	print('# statuses named in the kit')
	for l in langs:
		for st in src[l].get('statuses', []):
			print(f'{l}: [{st["name"]}] {clean(st["desc"])}')
		print()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(__doc__)
		sys.exit(2)
	main(sys.argv[1], sys.argv[2:] or ['zh-CN', 'en'])
