#!/usr/bin/env python3
"""Put the notes on differences between the editions of the game's text at the end of a page.

  python3 -I pipeline/edition_notes.py write     every arcanist and Psychube page in en, zh-tw, ja and ko

A kit or Psychube page shows each language's own text of the game, so where the editions say
different things (the global client's English against its other languages, or the global client
against the mainland one), each page shows one side only. The notes say what differs. They come
from records/edition-notes.json (written by hand, per language) and, for an arcanist whose
Euphoria or one of its Epiphanies is out on the mainland service only, from the kit records. zh-cn
pages get the notes when scripts/to-zh-cn.py converts the zh-tw page, so run this before it.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'pipeline'))
import scaffold as sc  # noqa: E402

DOCS = ROOT / 'src' / 'content' / 'docs'
LANGS = {'en': '', 'zh-tw': 'zh-tw/', 'ja': 'ja/', 'ko': 'ko/'}
HEAD = {'en': 'Edition differences', 'zh-tw': '版本差異', 'ja': '版による違い', 'ko': '판본 차이'}
EUPHORIA = {
	'en': ("{n}'s Euphoria is out only on the mainland China service.", "{n}'s Epiphany {k} is out only on the mainland China service."),
	'zh-tw': ('{n}的狂想只在中國大陸版上線。', '{n}的閃念 {k} 只在中國大陸版上線。'),
	'ja': ('{n}の狂想は中国本土版にのみ実装されている。', '{n}の瞬想 {k} は中国本土版にのみ実装されている。'),
	'ko': ('{n}의 광상은 중국 본토 서비스에만 출시되었다.', '{n}의 발상 {k}는 중국 본토 서비스에만 출시되었다.'),
}
NOTES = json.loads((ROOT / 'records' / 'edition-notes.json').read_text())


def euphoria_notes(slug, lang):
	f = ROOT / 'cache' / 'source' / f'{slug}.json'
	if not f.exists():
		return []
	d = json.loads(f.read_text())
	if 'zh-TW' not in d:
		return []
	cn, gl = d['zh-CN']['euphoria'], d['zh-TW']['euphoria']
	facets = list(dict.fromkeys(e['facet'] for e in cn))
	have = {e['facet'] for e in gl}
	n = sc.name(sc.REC[slug], lang)
	if cn and not gl:
		return [EUPHORIA[lang][0].format(n=n)]
	return [EUPHORIA[lang][1].format(n=n, k=facets.index(fc) + 1) for fc in facets if fc not in have]


def notes(page, lang):
	kind, slug = page.split('/')
	out = list(NOTES.get(page, {}).get(lang, []))
	if kind == 'arcanists':
		out += euphoria_notes(slug, lang)
	return out


def rewrite(path, page, lang):
	text = path.read_text()
	# The notes are the last section: drop the old one, then add the new one.
	text = re.sub(rf'\n## {re.escape(HEAD[lang])}\n.*\Z', '\n', text, flags=re.S).rstrip('\n') + '\n'
	got = notes(page, lang)
	if got:
		text += f'\n## {HEAD[lang]}\n\n' + '\n'.join(f'- {x}' for x in got) + '\n'
	if text != path.read_text():
		path.write_text(text)
		return True
	return False


def main(argv):
	if argv != ['write']:
		print(__doc__)
		return 2
	missing = [k for k, v in NOTES.items() if not k.startswith('_') and set(v) != set(LANGS)]
	if missing:
		raise SystemExit(f'records/edition-notes.json: not in every language: {missing}')
	n = 0
	for kind in ('arcanists', 'psychubes'):
		for path in sorted((DOCS / kind).glob('*.md')):
			page = f'{kind}/{path.stem}'
			if kind == 'arcanists' and path.stem not in sc.REC:
				continue
			for lang, d in LANGS.items():
				p = DOCS / f'{d}{page}.md'
				if p.exists():
					n += rewrite(p, page, lang)
	print(f'{n} page(s) changed')
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
