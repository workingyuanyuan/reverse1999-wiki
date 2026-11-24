"""Write the arcanist index pages, one per Afflatus and language, from the records.

  python3 -I pipeline/write_indexes.py

Writes src/content/docs/{,zh-tw/,ja/,ko/}afflatus/<afflatus>.md (zh-cn: scripts/to-zh-cn.py).
One index of all arcanists would pass the 5,000 characters a fetch returns, so the home page
links these six. An arcanist is linked once its English page exists; The Twins, of two
Afflatus, are listed under both. Overwrites the index pages; they are not edited by hand.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scaffold as s  # noqa: E402

AFFLATUS = ['Star', 'Mineral', 'Beast', 'Plant', 'Spirit', 'Intellect']
TWO = {101: ('Mineral', 'Star')}  # career code of The Twins -> both Afflatus
SKIP = {'schneider'}  # in the tables, never released as a playable arcanist: not in release counts

T = {
	'en': dict(
		title='{a} arcanists', desc='Reverse: 1999 has {n} arcanists of the {a} Afflatus.',
		caveat='An arcanist whose global release says not yet is out only on the mainland China service; the mainland service runs about two versions ahead.',
		cols=('Arcanist', 'Rarity', 'Damage', 'Euphoria', 'Mainland release', 'Global release'), yes='yes', no='no', cnonly='mainland only',
		src=[('re1999-data, mainland client {cn}: character.json', s.CN_CHAR), ('re1999-data-global, global client {gl}: character.json', s.GL_CHAR),
			('Reverse: 1999 Wiki (Fandom): release dates', 'https://reverse1999.fandom.com/')],
	),
	'zh-tw': dict(
		title='{a}靈感神秘學家', desc='重返未來：1999 {a}靈感的神秘學家共 {n} 位。',
		caveat='國際版上線欄寫尚未上線的神秘學家只在中國大陸版推出；中國大陸版的進度約領先兩個版本。',
		cols=('神秘學家', '稀有度', '創傷類型', '狂想', '中國大陸版上線', '國際版上線'), yes='有', no='無', cnonly='僅中國大陸版',
		src=[('re1999-data，中國大陸版用戶端 {cn}：character.json', s.CN_CHAR), ('re1999-data-global，國際版用戶端 {gl}：character.json', s.GL_CHAR),
			('Reverse: 1999 Wiki (Fandom)：上線日期', 'https://reverse1999.fandom.com/')],
	),
	'ja': dict(
		title='{a}本源の神秘学家', desc='リバース：1999 の{a}本源の神秘学家は{n}人。',
		caveat='グローバル版の実装が未実装の神秘学家は中国本土版にのみ実装されている。中国本土版はおよそ2バージョン先行している。',
		cols=('神秘学家', 'レア度', 'ダメージタイプ', '狂想', '中国本土版の実装', 'グローバル版の実装'), yes='あり', no='なし', cnonly='中国本土版のみ',
		src=[('re1999-data、中国本土版クライアント {cn}：character.json', s.CN_CHAR), ('re1999-data-global、グローバル版クライアント {gl}：character.json', s.GL_CHAR),
			('Reverse: 1999 Wiki (Fandom)：実装日', 'https://reverse1999.fandom.com/')],
	),
	'ko': dict(
		title='{a} 영감 마도학자', desc='리버스: 1999의 {a} 영감 마도학자는 {n}명이다.',
		caveat='글로벌 출시가 출시 전인 마도학자는 중국 본토 서비스에만 나와 있다. 중국 본토 서비스는 약 두 버전 앞서 있다.',
		cols=('마도학자', '희귀도', '피해 유형', '광상', '중국 본토 출시', '글로벌 출시'), yes='있음', no='없음', cnonly='중국 본토만',
		src=[('re1999-data, 중국 본토 클라이언트 {cn}: character.json', s.CN_CHAR), ('re1999-data-global, 글로벌 클라이언트 {gl}: character.json', s.GL_CHAR),
			('Reverse: 1999 Wiki (Fandom): 출시일', 'https://reverse1999.fandom.com/')],
	),
}


def afflatus_of(a):
	return TWO.get(a['afflatus'], (a['afflatus'],))


def title(lang, aff):
	return T[lang]['title'].format(a=s.L[lang]['afflatus'][aff])


def page(lang, aff):
	t, l = T[lang], s.L[lang]
	# Schneider (SKIP) is listed too: she has a page, and her release cells say she is not playable.
	members = [a for a in s.REC.values() if aff in afflatus_of(a)]
	members.sort(key=lambda a: (-a['stars'], a['names']['en'].lower()))
	zh_cn = {'Star': '星', 'Mineral': '岩', 'Beast': '兽', 'Plant': '木', 'Spirit': '灵', 'Intellect': '智'}[aff] + '灵感神秘学家'
	aliases = [title(o, aff) for o in T if o != lang] + [zh_cn]
	rows = []
	for a in members:
		n = s.name(a, lang)
		if (s.DOCS / 'arcanists' / f'{a["slug"]}.md').exists():
			n = f'[{n}](/{l["dir"]}arcanists/{a["slug"]}/)'
		mainland, glob = s.release(a, lang)
		# Euphoria on the mainland service only, for an arcanist that is out on both.
		eup = t['no'] if not a['euphoria'] else t['cnonly'] if a['inGlobal'] and not a['euphoriaGlobal'] else t['yes']
		rows.append(f'| {n} | {l["stars"].format(n=a["stars"])} | {l["damage"][a["damage"]]} | {eup} | {mainland} | {glob} |')
	src = '\n'.join(f'  - title: "{x.format(cn=s.CN["build"], gl=s.GL["build"])}"\n    url: {u}' for x, u in t['src'])
	fm = [
		'---', f'title: "{title(lang, aff)}"', f'description: "{t["desc"].format(a=l["afflatus"][aff], n=len(members))}"',
		f'appliesTo: "{l["applies_gl"]}"', f'caveat: "{t["caveat"]}"', f'lastVerified: {s.LAST_VERIFIED}',
		'aliases:\n' + '\n'.join(f'  - "{x}"' for x in aliases), 'sources:\n' + src, '---', '']
	table = [f'| {" | ".join(t["cols"])} |', '| --- | --- | --- | --- | --- | --- |'] + rows
	return '\n'.join(fm + table) + '\n'


HOME = {
	'en': ('Mainland only', 'Arcanists', ('Arcanist', 'Rarity', 'Afflatus', 'Damage', 'Mainland release')),
	'zh-tw': ('中國大陸版限定', '神秘學家', ('神秘學家', '稀有度', '靈感', '創傷類型', '中國大陸版上線')),
	'ja': ('中国本土版のみ', '神秘学家', ('神秘学家', 'レア度', '本源', 'ダメージタイプ', '中国本土版の実装')),
	'ko': ('중국 본토 한정', '마도학자', ('마도학자', '희귀도', '영감', '피해 유형', '중국 본토 출시')),
}


def home(lang):
	"""The home page's two generated parts: the mainland-only table and the links to the index pages."""
	l = s.L[lang]
	mine = sorted((a for a in s.REC.values() if not a['inGlobal'] and a['slug'] not in SKIP),
		key=lambda a: (s.REL.get(a['slug'], {}).get('cn') or '9', a['names']['en']))
	rows = []
	for a in mine:
		n = s.name(a, lang)
		if (s.DOCS / 'arcanists' / f'{a["slug"]}.md').exists():
			n = f'[{n}](/{l["dir"]}arcanists/{a["slug"]}/)'
		# Beside the name, the form a reader may search by: the English name on the Chinese page,
		# the mainland name elsewhere.
		other = a['names']['en'] if lang == 'zh-tw' else a['names']['zh-CN']
		cell = f'{n} ({other})' if lang in ('en', 'ko', 'zh-tw') else f'{n}（{other}）'
		rows.append(f'| {cell} | {l["stars"].format(n=a["stars"])} | {" / ".join(l["afflatus"][x] for x in afflatus_of(a))} | '
			f'{l["damage"][a["damage"]]} | {s.release(a, lang)[0]} |')
	cols = HOME[lang][2]
	table = '\n'.join([f'| {" | ".join(cols)} |', '| --- | --- | --- | --- | --- |'] + rows)
	links = '\n'.join(f'- [{title(lang, x)}](/{l["dir"]}afflatus/{x.lower()}/)' for x in AFFLATUS)
	return table, links


def write_home(lang):
	import re
	p = s.DOCS / s.L[lang]['dir'] / 'index.md'
	text = p.read_text()
	only, arc, _ = HOME[lang]
	table, links = home(lang)
	text = re.sub(rf'(## {re.escape(only)}\n\n[^\n]*\n\n)(?:\|.*\n)+', lambda m: m.group(1) + table + '\n', text, count=1)
	text = re.sub(rf'(## {re.escape(arc)}\n\n)(?:(?:\||- \[).*\n)+', lambda m: m.group(1) + links + '\n', text, count=1)
	p.write_text(text)


def main():
	for lang in T:
		write_home(lang)
	for lang in T:
		d = s.DOCS / s.L[lang]['dir'] / 'afflatus'
		d.mkdir(parents=True, exist_ok=True)
		for aff in AFFLATUS:
			(d / f'{aff.lower()}.md').write_text(page(lang, aff))
	print(f'{len(T) * len(AFFLATUS)} index pages written')
	return 0


if __name__ == '__main__':
	sys.exit(main())
