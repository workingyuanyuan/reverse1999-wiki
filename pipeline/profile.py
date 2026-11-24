#!/usr/bin/env python3
"""Write the profile page of every arcanist in the global client, in all five languages (Schneider,
who was never playable, included).

  python3 -I pipeline/profile.py write [slug ...]   arcanists/<slug>/profile.md in every language (zh-cn included)
  python3 -I pipeline/profile.py list               the arcanists that get a page

A profile page holds the arcanist's file as the game shows it: the cover, the three items, the
three stories (文化), the skins with their descriptions, stories and items, and the voice lines.
The text is the game's own, from the pinned tables (records/sources.json): English, Japanese,
Korean and Traditional Chinese from the global client, Simplified Chinese from the mainland
client. Only what the global client has is written, so that every language holds the same
entries: a skin or a voice line out on the mainland service only has no row on any page.
The pages are never edited by hand; scripts/to-zh-cn.py skips them.
"""
import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'pipeline'))
import gamedata as g  # noqa: E402

DOCS = ROOT / 'src' / 'content' / 'docs'
ARC = json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']
LAST_VERIFIED = '2026-11-24'
LANGS = {'en': 'en', 'zh-tw': 'zh-TW', 'zh-cn': 'zh-CN', 'ja': 'ja', 'ko': 'ko'}
DIR = {'en': '', 'zh-tw': 'zh-tw/', 'zh-cn': 'zh-cn/', 'ja': 'ja/', 'ko': 'ko/'}
VOICE = {'en': 'encontent', 'zh-tw': 'twcontent', 'ja': 'jpcontent', 'ko': 'kocontent'}
CJK = {'zh-tw', 'zh-cn', 'ja'}
LIMIT = {'en': 110, 'zh-tw': 70, 'zh-cn': 70, 'ja': 70, 'ko': 70}
# Labels of the game's own file screen, by key of the global client's text.
UI = {'cover': 'language_10030422', 'voice': 'language_10030423', 'item': 'language_10030424',
	'story': 'language_10030425', 'default': 'language_10005329', 'insight': 'language_10005330'}

T = {
	'en': dict(title='{n} profile', skins='Skins', line='Line', label='Voice',
		desc=['{n}\'s profile in Reverse: 1999: {s} skins and {v} voice lines in the global client.',
			'{n}\'s profile in Reverse: 1999: {s} skins and {v} voice lines.', '{n}\'s profile in Reverse: 1999.'],
		applies='Reverse: 1999, global client {b} (version 3.9), English text',
		caveat_skin='A voice line with a skin name in brackets after its label plays only while {n} wears that skin.',
		caveat='The text is the global client\'s, version 3.9; the mainland client is two versions ahead.',
		src=['re1999-data-global, global client {b}: character_data.json, character_voice.json and skin.json',
			're1999-data-global, global client {b}: text in English, Japanese, Korean and Traditional Chinese; the text belongs to Bluepoch',
			're1999-data, mainland client {c}: the same tables with the Simplified Chinese text']),
	'zh-tw': dict(title='{n} 檔案', skins='皮膚', line='台詞', label='語音',
		desc=['重返未來：1999 {n}的檔案：國際版用戶端有 {s} 套皮膚、{v} 句語音。', '重返未來：1999 {n}的檔案：{s} 套皮膚、{v} 句語音。', '重返未來：1999 {n}的檔案。'],
		applies='重返未來：1999，國際版用戶端 {b}（3.9 版），繁體中文文本',
		caveat_skin='標籤後括號內寫有皮膚名的語音，只在{n}換上該皮膚時播放。',
		caveat='文本是國際版用戶端 3.9 版的；中國大陸版領先兩個版本。',
		src=['re1999-data-global，國際版用戶端 {b}：character_data.json、character_voice.json 與 skin.json',
			're1999-data-global，國際版用戶端 {b}：英文、日文、韓文與繁體中文文本；文本的權利屬於深藍互動（Bluepoch）',
			're1999-data，中國大陸版用戶端 {c}：同一批資料表的簡體中文文本']),
	'zh-cn': dict(title='{n} 档案', skins='皮肤', line='台词', label='语音',
		desc=['重返未来：1999 {n}的档案：国际版客户端有 {s} 套皮肤、{v} 句语音。', '重返未来：1999 {n}的档案：{s} 套皮肤、{v} 句语音。', '重返未来：1999 {n}的档案。'],
		applies='重返未来：1999，中国大陆版客户端 {b}（4.1 版），简体中文文本',
		caveat_skin='标签后括号内写有皮肤名的语音，只在{n}换上该皮肤时播放。',
		caveat='简体中文是中国大陆版客户端 4.1 版的文本，其他语言是国际版 3.9 版的。',
		src=['re1999-data-global，国际版客户端 {b}：character_data.json、character_voice.json 与 skin.json',
			're1999-data-global，国际版客户端 {b}：英文、日文、韩文与繁体中文文本；文本的权利属于深蓝互动（Bluepoch）',
			're1999-data，中国大陆版客户端 {c}：同一批数据表的简体中文文本']),
	'ja': dict(title='{n} プロフィール', skins='コスチューム', line='セリフ', label='ボイス',
		desc=['リバース：1999 の{n}のプロフィール：グローバル版クライアントにコスチューム{s}着、ボイス{v}件。', 'リバース：1999 の{n}のプロフィール：コスチューム{s}着、ボイス{v}件。', 'リバース：1999 の{n}のプロフィール。'],
		applies='リバース：1999、グローバル版クライアント {b}（バージョン 3.9）、日本語テキスト',
		caveat_skin='ラベルの後の括弧にコスチューム名があるボイスは、{n}がそのコスチュームを着ているときだけ流れる。',
		caveat='テキストはグローバル版クライアント 3.9 のもの。中国本土版は 2 バージョン先行している。',
		src=['re1999-data-global、グローバル版クライアント {b}：character_data.json、character_voice.json、skin.json',
			're1999-data-global、グローバル版クライアント {b}：英語、日本語、韓国語、繁体字中国語のテキスト。テキストの権利は Bluepoch に帰属',
			're1999-data、中国本土版クライアント {c}：同じテーブルの簡体字中国語テキスト']),
	'ko': dict(title='{n} 프로필', skins='스킨', line='대사', label='음성',
		desc=['리버스: 1999 {n}의 프로필: 글로벌 클라이언트에 스킨 {s}개, 음성 {v}개.', '리버스: 1999 {n}의 프로필: 스킨 {s}개, 음성 {v}개.', '리버스: 1999 {n}의 프로필.'],
		applies='리버스: 1999, 글로벌 클라이언트 {b}(3.9 버전), 한국어 텍스트',
		caveat_skin='라벨 뒤 괄호에 스킨 이름이 있는 음성은 {n}에게 그 스킨을 입혔을 때만 나온다.',
		caveat='텍스트는 글로벌 클라이언트 3.9 버전의 것이다. 중국 본토 클라이언트는 두 버전 앞서 있다.',
		src=['re1999-data-global, 글로벌 클라이언트 {b}: character_data.json, character_voice.json, skin.json',
			're1999-data-global, 글로벌 클라이언트 {b}: 영어, 일본어, 한국어, 번체 중국어 텍스트. 텍스트의 권리는 Bluepoch에 있다',
			're1999-data, 중국 본토 클라이언트 {c}: 같은 테이블의 간체 중국어 텍스트']),
}
LANG_FILE = {'en': 'en', 'zh-tw': 'tw', 'ja': 'jp', 'ko': 'kr', 'zh-cn': 'zh'}

# Rich-text tags of the client. <i>, <b> and <s> become Markdown; ruby (<marktop=reading>) is
# written after its word in brackets, as the Story Compendium writes it; the rest is layout.
TAG = re.compile(r'</?(?:i|b|u|s|sup|sub|nobr|br|UTTU|marktop|color|size|indent|space|cspace|align|font|line-height|voffset|alpha|mark|pos|margin|width|noparse)(?:=[^>]*)?>', re.I)
MD = {'i': '*', 'b': '**', 's': '~~'}


def esc(s):
	s = re.sub(r'([\\`*_\[\]~|<>])', r'\\\1', s)
	return s


SUP = str.maketrans('0123456789+-−０１２３４５６７８９＋－', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻')


def sup(x):
	if re.fullmatch(r'[0-9+\-−０-９＋－]+', x.strip()):
		return x.strip().translate(SUP)
	return '^(' + x + ')'


def _punct(c):
	return unicodedata.category(c)[0] in 'PS'


def inline(s):
	"""One line of client rich text as Markdown.

	<i>, <b> and <s> become *, ** and ~~ where CommonMark will read them as marks: a mark must
	touch its words, and next to punctuation it needs a space or punctuation on its outer side
	(the flanking rules), which Chinese and Japanese text seldom has. Punctuation at the edge of a
	span moves outside the mark until it parses; a span that still would not parse loses its mark.
	"""
	s = re.sub(r'<marktop=([^>]*)>(.*?)</marktop>', r'\2（\1）', s, flags=re.S)
	# Exponents (10<sup>35</sup>) keep their place as superscript figures.
	s = re.sub(r'<sup>([^<]*)</sup>', lambda m: sup(m.group(1)), s)
	# Alternate text and marks: parts[0] text, parts[1] mark, parts[2] text, ...
	parts, pos = [], 0
	for m in TAG.finditer(s):
		name = re.match(r'</?([a-zA-Z-]+)', m.group(0)).group(1).lower()
		if name not in MD:
			continue
		parts += [s[pos:m.start()], ['c' if m.group(0).startswith('</') else 'o', MD[name]]]
		pos = m.end()
	s = re.sub(TAG, '', s[pos:])
	parts.append(s)
	for i in range(0, len(parts), 2):
		parts[i] = re.sub(TAG, '', parts[i])
	# Pair each closing mark with the nearest open one of its kind; drop the rest.
	stack, pairs = [], []
	for i in range(1, len(parts), 2):
		kind, mark = parts[i]
		if kind == 'o':
			stack.append(i)
		else:
			j = next((k for k in reversed(stack) if parts[k][1] == mark), None)
			if j is None:
				parts[i] = None
			else:
				stack.remove(j)
				pairs.append((j, i))
	for j in stack:
		parts[j] = None
	alive = lambda k: parts[k] is not None  # noqa: E731
	# A span that closes where the next of its kind opens is one span (<b>A</b><b>B</b>).
	for k in range(1, len(parts) - 2, 2):
		if alive(k) and alive(k + 2) and parts[k][0] == 'c' and parts[k + 2][0] == 'o' and parts[k][1] == parts[k + 2][1] and not parts[k + 1]:
			for n, (j, i) in enumerate(pairs):
				if i == k:
					later = next(p for p in pairs if p[0] == k + 2)
					pairs[n] = (j, later[1])
					pairs.remove(later)
					break
			parts[k] = parts[k + 2] = None

	def neighbour(k, step):
		"""The character a mark at k sees on one side: ' ' at the line's edge, '.' at another kind of mark."""
		mark = parts[k][1][0]
		while True:
			k += step
			if k < 0 or k >= len(parts):
				return ' '
			if k % 2 == 0:
				if parts[k]:
					return parts[k][-1] if step < 0 else parts[k][0]
				continue
			if alive(k) and parts[k][1][0] != mark:
				return '.'

	def opens(k):
		before, after = neighbour(k, -1), neighbour(k, 1)
		return not after.isspace() and (not _punct(after) or before.isspace() or _punct(before))

	def closes(k):
		before, after = neighbour(k, -1), neighbour(k, 1)
		return not before.isspace() and (not _punct(before) or after.isspace() or _punct(after))

	for _ in range(4):
		for j, i in pairs:
			if not (alive(j) and alive(i)):
				continue
			inner = ''.join(parts[k] for k in range(j + 1, i, 2))
			if not inner.strip():
				parts[j] = parts[i] = None
				continue
			# Spaces and, where needed, punctuation step outside the mark.
			t = parts[j + 1]
			lead = re.match(r'\s*', t).group(0)
			if lead:
				parts[j - 1] += lead
				parts[j + 1] = t = t[len(lead):]
			if not opens(j):
				m = re.match(r'[^\w\s]+', t)
				if m and inner.strip()[len(m.group(0)):].strip():
					parts[j - 1] += m.group(0)
					parts[j + 1] = t[m.end():]
			t = parts[i - 1]
			trail = re.search(r'\s*$', t).group(0)
			if trail:
				parts[i + 1] = trail + parts[i + 1]
				parts[i - 1] = t = t[:len(t) - len(trail)]
			if not closes(i):
				m = re.search(r'[^\w\s]+$', t)
				if m and inner.strip()[:-len(m.group(0))].strip():
					parts[i + 1] = m.group(0) + parts[i + 1]
					parts[i - 1] = t[:m.start()]
					# Brackets and quotes leave the span in pairs.
					m = re.match(r'[^\w\s]+', parts[j + 1])
					if m and parts[j + 1] != m.group(0):
						parts[j - 1] += m.group(0)
						parts[j + 1] = parts[j + 1][m.end():]
	for j, i in pairs:
		if alive(j) and alive(i) and not (opens(j) and closes(i)):
			parts[j] = parts[i] = None
	out = ''.join(esc(x) if k % 2 == 0 else (x[1] if x else '') for k, x in enumerate(parts))
	out = re.sub(r'^(\s*)(>|[#+-](?=\s|$)|\d+[.)](?=\s|$))', r'\1\\\2', out)
	return out.strip()


def para(s):
	"""Client text as Markdown paragraphs: each line of the client is a paragraph."""
	s = s.replace('\r', '')
	blocks = [inline(x) for x in re.split(r'\n|\\&', s)]
	return '\n\n'.join(b for b in blocks if b.strip())


def one_line(s, lang):
	joiner = '' if lang in CJK else ' '
	return joiner.join(inline(x) for x in s.replace('\r', '').split('\n') if x.strip())


def voice_text(s, lang):
	"""A voice line: segments split by '|', each ending in '#<seconds>' (a few in two of them)."""
	segs = [re.sub(r'(?:#[\d.]+\s*)+$', '', x).strip() for x in s.split('|')]  # some end in two, '#3.8#0'
	joiner = '' if lang in CJK else ' '
	# Join before the marks are placed: a mark at the end of one segment touches the next one.
	return one_line(joiner.join(x for x in segs if x), lang)


def gl_str(key, lang):
	return g._lang(LANG_FILE[lang]).get(key, '') if key else ''


def q(s):
	return s.replace('\\', '\\\\').replace('"', '\\"')


def fit(lang, options, **kw):
	for o in options:
		s = o.format(**kw)
		if len(s) <= LIMIT[lang]:
			return s
	return options[-1].format(**kw)


def name(a, lang):
	return a['names'].get(LANGS[lang]) or a['names']['en']


def model(a):
	"""Every entry of one arcanist, with its text in each language; None if the global client has none."""
	hid = a['id']
	gl_data = [r for r in g.gl('character_data') if r['heroId'] == hid]
	if not gl_data:
		return None
	cn_data = {r['id']: r for r in g.cn('character_data') if r['heroId'] == hid}
	gl_skins = {r['id']: r for r in g.gl('skin') if r.get('characterId') == hid}
	cn_skins = {r['id']: r for r in g.cn('skin') if r.get('characterId') == hid}
	mainland_only = set(cn_skins) - set(gl_skins)
	problems = []

	def data_text(r, field, lang):
		if lang == 'zh-cn':
			c = cn_data.get(r['id'])
			return c[field] if c else None
		return gl_str(r[field], lang)

	def entry(r):
		e = {'title': {}, 'text': {}}
		for lang in LANGS:
			t, x = data_text(r, 'title', lang), data_text(r, 'text', lang)
			if x is None or not x.strip():
				problems.append(f'{a["slug"]}: character_data {r["id"]} has no {lang} text')
				return None
			e['title'][lang] = one_line(t or '', lang)
			e['text'][lang] = para(x)
		return e

	cover = [entry(r) for r in gl_data if r['type'] == 1 and not r['skinId']]
	items = [entry(r) for r in gl_data if r['type'] == 2 and not r['skinId']]
	stories = [entry(r) for r in gl_data if r['type'] == 3 and not r['skinId']]

	skins, skin_name = [], {}
	for sid in sorted(gl_skins):
		s, c = gl_skins[sid], cn_skins.get(sid)
		default = sid % 100 == 1
		# The default and the Insight skin are named by kind ("Default Skin", "Advanced Skin"), as the game lists them.
		label = s.get('des') if s.get('des') in (UI['default'], UI['insight']) else None
		sk = {'id': sid, 'name': {}, 'desc': {}, 'story': {}, 'default': default,
			'items': [entry(r) for r in gl_data if r['type'] == 2 and r['skinId'] == sid]}
		for lang in LANGS:
			if lang == 'zh-cn':
				nm = (c or {}).get('name') or gl_str(s.get('name'), lang)
				ds, st = (c or {}).get('skinDescription', ''), (c or {}).get('skinStory', '')
			else:
				nm, ds, st = gl_str(s.get('name'), lang), gl_str(s.get('skinDescription'), lang), gl_str(s.get('skinStory'), lang)
			sk['name'][lang] = one_line(gl_str(label, lang) if label else nm, lang)
			sk['desc'][lang] = para(ds or '')
			sk['story'][lang] = para(st or '')
		if s.get('skinStory') and not all(sk['story'].values()):
			problems.append(f'{a["slug"]}: skin {sid} lacks story text in a language')
			sk['story'] = {lang: '' for lang in LANGS}
		if any(sk['desc'].values()) or any(sk['story'].values()) or any(sk['items']):
			skins.append(sk)
		skin_name[sid] = sk['name']

	cn_voice = {r['audio']: r for r in g.cn('character_voice') if r['heroId'] == hid}
	groups = collections.OrderedDict()
	for r in sorted((r for r in g.gl('character_voice') if r['heroId'] == hid), key=lambda r: r['sortId']):
		label = {lang: gl_str(r['name'], lang).strip() for lang in LANGS if lang != 'zh-cn'}
		if not r['name'] or label['en'] in ('', '0'):
			continue  # home-screen touches of a skin, which the voice list does not show
		if r['stateCondition'] > 1:
			continue  # Lucy's lines come twice, once per state, with the same words
		ids = {int(x) for x in r['skins'].split('#') if x.strip()}
		if ids and ids <= mainland_only:
			continue
		c = cn_voice.get(r['audio'])
		label['zh-cn'] = (c['name'] if c else gl_str(r['name'], 'zh-cn')).strip()
		text = {lang: voice_text(r[VOICE[lang]], lang) for lang in VOICE}
		text['zh-cn'] = voice_text(c['content'] if c else r['content'], 'zh-cn')
		if not all(text.values()):
			problems.append(f'{a["slug"]}: voice {r["sortId"]} has no text in every language')
			continue
		g_ = groups.setdefault(r['name'], {'label': label, 'variants': []})
		for v in g_['variants']:
			if v['text'] == text:
				v['skins'] |= ids
				break
		else:
			g_['variants'].append({'text': text, 'skins': set(ids)})
	voices, skin_lines = [], False
	for g_ in groups.values():
		vs = g_['variants']
		for v in vs:
			label = dict(g_['label'])
			named = sorted(s for s in v['skins'] if s in skin_name)
			general = not v['skins'] or any(s % 100 == 1 for s in v['skins'])
			if len(vs) > 1 and not general and named:
				for lang in LANGS:
					sep = '、' if lang in CJK else ', '
					inner = sep.join(skin_name[s][lang] for s in named)
					label[lang] = f'{label[lang]}（{inner}）' if lang in CJK else f'{label[lang]} ({inner})'
				skin_lines = True
			voices.append({'label': {k: one_line(x, k) for k, x in label.items()}, 'text': v['text']})
	return {'cover': [e for e in cover if e], 'items': [e for e in items if e], 'stories': [e for e in stories if e],
		'skins': skins, 'voices': voices, 'skin_lines': skin_lines, 'problems': problems}


def cell(s):
	return s.replace('\n\n', ' ')


def page(a, m, lang):
	t = T[lang]
	n = name(a, lang)
	ui = {k: one_line(gl_str(v, lang), lang) for k, v in UI.items()}
	title = t['title'].format(n=n)
	desc = fit(lang, t['desc'], n=n, s=len(m['skins']), v=len(m['voices']))
	if lang == 'zh-cn':
		applies = t['applies'].format(b=g.CN['build'])
	else:
		applies = t['applies'].format(b=g.GL['build'])
	# The qualifier a reader most likely misses: lines heard only in one skin, where the page has them.
	caveat = (t['caveat_skin'] if m['skin_lines'] else t['caveat']).format(n=n)
	# The same set of names in every language: the title of each language's page.
	aliases = [x for x in dict.fromkeys(T[o]['title'].format(n=name(a, o)) for o in LANGS) if x != title]
	urls = [f'https://github.com/{g.GL["repo"]}/tree/{g.GL["commit"]}/data/json',
		f'https://github.com/{g.GL["repo"]}/tree/{g.GL["commit"]}/data/configs/language',
		f'https://github.com/{g.CN["repo"]}/tree/{g.CN["commit"]}/data/json']
	src = '\n'.join(f'  - title: "{q(s.format(b=g.GL["build"], c=g.CN["build"]))}"\n    url: {u}' for s, u in zip(t['src'], urls))
	fm = ['---', f'title: "{q(title)}"', f'description: "{q(desc)}"', f'appliesTo: "{applies}"', f'caveat: "{q(caveat)}"',
		f'lastVerified: {LAST_VERIFIED}', 'aliases:'] + [f'  - "{q(x)}"' for x in aliases] + [f'sources:\n{src}', '---', '']
	body = []
	if m['cover']:
		body += [f'## {ui["cover"]}', ''] + ['\n\n'.join(e['text'][lang] for e in m['cover'])]
	for key, entries in (('item', m['items']), ('story', m['stories'])):
		if entries:
			body += ['', f'## {ui[key]}']
			for e in entries:
				body += ['', f'### {e["title"][lang]}', '', e['text'][lang]]
	if m['skins']:
		body += ['', f'## {t["skins"]}']
		for sk in m['skins']:
			body += ['', f'### {sk["name"][lang]}']
			if sk['desc'][lang]:
				body += ['', '\n'.join('> ' + x if x else '>' for x in sk['desc'][lang].split('\n'))]
			if sk['story'][lang]:
				body += ['', sk['story'][lang]]
			for e in sk['items']:
				if e:
					body += ['', f'#### {e["title"][lang]}', '', e['text'][lang]]
	if m['voices']:
		body += ['', f'## {ui["voice"]}', '', f'| {t["label"]} | {t["line"]} |', '| --- | --- |']
		body += [f'| {v["label"][lang]} | {cell(v["text"][lang])} |' for v in m['voices']]
	return '\n'.join(fm) + '\n'.join(body) + '\n'


def targets(slugs=None):
	return [a for a in ARC if a['inGlobal'] and (not slugs or a['slug'] in slugs)]


def write(slugs=None):
	problems, n = [], 0
	for a in targets(slugs):
		m = model(a)
		if not m:
			problems.append(f'{a["slug"]}: no rows in the global character_data.json')
			continue
		problems += m['problems']
		for lang in LANGS:
			p = DOCS / DIR[lang] / 'arcanists' / a['slug'] / 'profile.md'
			p.parent.mkdir(parents=True, exist_ok=True)
			p.write_text(page(a, m, lang))
		n += 1
	for x in problems:
		print('note:', x, file=sys.stderr)
	print(f'profile pages: {n} arcanists x {len(LANGS)} languages')


def main(argv):
	if argv[:1] == ['write']:
		write(argv[1:] or None)
	elif argv[:1] == ['list']:
		print('\n'.join(a['slug'] for a in targets()))
	else:
		print(__doc__)
		return 2
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
