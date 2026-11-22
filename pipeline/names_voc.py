"""Write records/names-voc.json: names whose mainland Simplified Chinese string is not the plain
conversion of the global client's Traditional Chinese string.

scripts/to-zh-cn.py applies these pairs before the character conversion, so the zh-cn pages use
the mainland client's own names. Compared by id: arcanist names, skill names, status names
(skill_eff_desc) and item names, between the global client's Traditional Chinese text and the
mainland client's text.

  uv run --with opencc-python-reimplemented python3 -I pipeline/names_voc.py
"""
import json
import re
from pathlib import Path

from opencc import OpenCC

ROOT = Path(__file__).resolve().parent.parent
PINS = json.loads((ROOT / 'records' / 'sources.json').read_text())
cc = OpenCC('tw2s')


def table(key, name):
	return json.loads((ROOT / 'cache' / key / PINS[key]['commit'] / 'data' / 'json' / f'{name}.json').read_text())


def plain(s):
	return re.sub(r'<[^>]+>', '', s or '').strip()


def main():
	g = PINS['gl']['commit']
	tw = {r['key']: r['content'] for r in json.loads(
		(ROOT / 'cache' / 'gl' / g / 'data' / 'configs' / 'language' / 'language_tw.json').read_text())}
	pairs = {}
	for name, field in (('character', 'name'), ('skill', 'name'), ('skill_eff_desc', 'name'), ('item', 'name')):
		cn = {r['id']: r[field] for r in table('cn', name)}
		for r in table('gl', name):
			t, c = plain(tw.get(r[field], '')), plain(cn.get(r['id'], ''))
			# Only names written in Chinese characters; a bare number ("10") or a name with a
			# note for developers would rewrite ordinary text.
			if not t or not c or not re.search(r'[\u4e00-\u9fff]', t) or re.search(r'[（(§]', t + c):
				continue
			if cc.convert(t) != c and len(t) >= 2:
				pairs.setdefault(t, set()).add(c)
	# Keep only unambiguous pairs; longest first, so that a longer name wins over a part of it.
	out = sorted(((t, next(iter(c))) for t, c in pairs.items() if len(c) == 1), key=lambda p: -len(p[0]))
	(ROOT / 'records' / 'names-voc.json').write_text(json.dumps(out, ensure_ascii=False, indent=0) + '\n')
	print(len(out), 'pairs;', len(pairs) - len(out), 'ambiguous left out')


if __name__ == '__main__':
	main()
