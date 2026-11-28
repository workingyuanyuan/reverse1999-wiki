"""Write the story pages: an index page per kind of story, a page per chapter, a page per stage.

  python3 -I pipeline/story.py fetch            the Compendium at the pinned commit -> cache/story/repo
  python3 -I pipeline/story.py write            pages in en, zh-tw, zh-cn, ja, ko; the home page's story section

The text of each stage is the reading text of the Reverse: 1999 Story Compendium
(records/story.json: repository and commit): the story, then the Trails the stage opens. The
Compendium's second copy of each stage (the client transcript, folded) is left out. English,
Japanese, Korean and Traditional Chinese follow the global client, Simplified Chinese the mainland
client, so zh-cn is written here from the Compendium's zh-CN files, not converted from zh-tw.

Chapters with a file in all five languages get pages. A chapter in the zh-CN folder only is out on
the mainland service only: the index lists it by its Simplified Chinese name, without a page.
Names of chapters and stages are the Compendium's headings in each language; stage codes of the
main story (1ST-01) and in-game dates come from the global client's chapter and episode tables.
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'pipeline'))
import gamedata as g  # noqa: E402

DOCS = ROOT / 'src' / 'content' / 'docs'
STORY = json.loads((ROOT / 'records' / 'story.json').read_text())
REPO, COMMIT = STORY['repo'], STORY['commit']
CLONE = ROOT / 'cache' / 'story' / 'repo'
READER = 'readable/story_reader_linked'
TREE = f'https://github.com/{REPO}/tree/{COMMIT}/{READER}'
ARC = json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']
LAST_VERIFIED = '2026-11-23'
LANGS = {'en': 'en', 'zh-tw': 'zh-TW', 'zh-cn': 'zh-CN', 'ja': 'ja', 'ko': 'ko'}
DIR = {'en': '', 'zh-tw': 'zh-tw/', 'zh-cn': 'zh-cn/', 'ja': 'ja/', 'ko': 'ko/'}
# Compendium folder -> index page. The two chapters of standalone Trails go with the other stories.
CATS = [('mainline', 'main'), ('activity', 'events'), ('character', 'characters'), ('anecdote', 'anecdotes'),
	('other', 'other'), ('trails', 'other')]
INDEXES = ['main', 'events', 'characters', 'characters-2', 'anecdotes', 'other']
# An index page links each chapter with the full address, about 140 characters a row: past about 28
# rows the last links fall beyond the first 5,000 characters, so the character stories take two pages.
SPLIT = {'characters': 'characters-2'}
LIMIT = {'en': 110, 'zh-tw': 70, 'zh-cn': 70, 'ja': 70, 'ko': 70}

T = {
	'en': dict(
		cats={'main': 'Main story', 'events': 'Event stories', 'characters': 'Character stories I', 'characters-2': 'Character stories II', 'anecdotes': 'Anecdotes', 'other': 'Other stories'},
		# The category inside a sentence.
		inner={'main': 'main story', 'events': 'event stories', 'characters': 'character stories I', 'characters-2': 'character stories II', 'anecdotes': 'anecdotes', 'other': 'other stories'},
		cat_desc='The {n} chapters and {k} stages of the Reverse: 1999 {ci}.',
		ch_desc=['{n} is a chapter of the {ci}, in {k} stages.', '{n} is a chapter of the {ci}.', '{n} is a story chapter.'],
		ch_desc_main=['{n} is chapter {i} of the main story, in {k} stages.', '{n} is chapter {i} of the main story.', '{n} is a main story chapter.'],
		st_desc=['{s} is stage {k} of {n}, a chapter of the {ci}.', '{s} is stage {k} of {n}.',
			'{s} is a stage of {n}.', '{s} is a story stage.'],
		applies_gl='Reverse: 1999, global client {b} (version {v}), English text',
		caveat_gl='The text is the global client\'s English; the mainland client, two versions ahead, words some lines differently.',
		head=('Field', 'Value'), stage='Stage', name='Name', when='In-game time', trails='Trails', chapter='Chapter',
		stages='Stages', speak='Arcanists who speak', names='Names', count='Stages', mainland='Mainland service only (Simplified Chinese names)',
		langs=('English', 'Simplified Chinese', 'Traditional Chinese', 'Japanese', 'Korean'),
		prev='Previous stage', next='Next stage', story='Story', trail='Trails', none='—', sep=', ', home='Story',
		date=lambda y, m, d, t: (f'{["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][m - 1]} {d}, {y}' if y else f'{["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][m - 1]} {d}') + (f', {t}' if t else ''),
		src=[('Reverse: 1999 Story Compendium, commit {c}: reading text in five languages; the story text belongs to Bluepoch', 'tree'),
			('re1999-data-global, global client {gl}: chapter.json and episode.json (stage codes, in-game dates)', 'gl')]),
	'zh-tw': dict(
		cats={'main': '主線', 'events': '活動劇情', 'characters': '角色劇情 I', 'characters-2': '角色劇情 II', 'anecdotes': '軼事', 'other': '其他劇情'},
		cat_desc='重返未來：1999 的{c}共 {n} 章、{k} 關。',
		ch_desc=['{n}是{c}，共 {k} 關。', '{n}是{c}。', '{n}是劇情章節。'],
		ch_desc_main=['{n}是主線第 {i} 章，共 {k} 關。', '{n}是主線第 {i} 章。', '{n}是主線章節。'],
		st_desc=['{s}是{c}「{n}」的第 {k} 關。', '{s}是「{n}」的第 {k} 關。', '{s}是劇情關卡。', '劇情關卡。'],
		applies_gl='重返未來：1999，國際版用戶端 {b}（{v} 版），繁體中文文本',
		caveat_gl='文本是國際版的繁體中文；中國大陸版領先兩個版本，部分台詞措辭不同。',
		head=('項目', '內容'), stage='關卡', name='名稱', when='遊戲內時間', trails='小徑', chapter='章節',
		stages='關卡', speak='登場的神秘學家', names='名稱', count='關卡數', mainland='僅中國大陸版（簡體中文名稱）',
		langs=('英文', '簡體中文', '繁體中文', '日文', '韓文'),
		prev='上一關', next='下一關', story='劇情', trail='小徑', none='—', sep='、', home='劇情',
		date=lambda y, m, d, t: (f'{y} 年 ' if y else '') + f'{m} 月 {d} 日' + (f' {t}' if t else ''),
		src=[('Reverse: 1999 Story Compendium，commit {c}：五種語言的閱讀版文本；劇情文本的權利屬於深藍互動（Bluepoch）', 'tree'),
			('re1999-data-global，國際版用戶端 {gl}：chapter.json 與 episode.json（關卡編號、遊戲內時間）', 'gl')]),
	'zh-cn': dict(
		cats={'main': '主线', 'events': '活动剧情', 'characters': '角色剧情 I', 'characters-2': '角色剧情 II', 'anecdotes': '轶事', 'other': '其他剧情'},
		cat_desc='重返未来：1999 的{c}共 {n} 章、{k} 关。',
		ch_desc=['{n}是{c}，共 {k} 关。', '{n}是{c}。', '{n}是剧情章节。'],
		ch_desc_main=['{n}是主线第 {i} 章，共 {k} 关。', '{n}是主线第 {i} 章。', '{n}是主线章节。'],
		st_desc=['{s}是{c}「{n}」的第 {k} 关。', '{s}是「{n}」的第 {k} 关。', '{s}是剧情关卡。', '剧情关卡。'],
		applies_cn='重返未来：1999，中国大陆版客户端 {b}（{v} 版），简体中文文本',
		caveat_cn='文本是中国大陆版的简体中文；国际版落后两个版本，繁体中文等语言的部分台词措辞不同。',
		head=('项目', '内容'), stage='关卡', name='名称', when='游戏内时间', trails='小径', chapter='章节',
		stages='关卡', speak='登场的神秘学家', names='名称', count='关卡数', mainland='仅中国大陆版（简体中文名称）',
		langs=('英文', '简体中文', '繁体中文', '日文', '韩文'),
		prev='上一关', next='下一关', story='剧情', trail='小径', none='—', sep='、', home='剧情',
		date=lambda y, m, d, t: (f'{y} 年 ' if y else '') + f'{m} 月 {d} 日' + (f' {t}' if t else ''),
		src=[('Reverse: 1999 Story Compendium，commit {c}：五种语言的阅读版文本；剧情文本的权利属于深蓝互动（Bluepoch）', 'tree'),
			('re1999-data-global，国际版客户端 {gl}：chapter.json 与 episode.json（关卡编号、游戏内时间）', 'gl')]),
	'ja': dict(
		cats={'main': 'メインストーリー', 'events': 'イベントストーリー', 'characters': 'キャラクターストーリー I', 'characters-2': 'キャラクターストーリー II', 'anecdotes': 'エピソード', 'other': 'その他のストーリー'},
		cat_desc='リバース：1999 の{c}は全{n}章、{k}ステージ。',
		ch_desc=['{n}は{c}で、全{k}ステージ。', '{n}は{c}。', '{n}はストーリーの章。'],
		ch_desc_main=['{n}はメインストーリー第{i}章で、全{k}ステージ。', '{n}はメインストーリー第{i}章。', '{n}はメインストーリーの章。'],
		st_desc=['{s}は{c}「{n}」の第{k}ステージ。', '{s}は「{n}」の第{k}ステージ。', '{s}はストーリーのステージ。', 'ストーリーのステージ。'],
		applies_gl='リバース：1999、グローバル版クライアント {b}（バージョン {v}）、日本語テキスト',
		caveat_gl='テキストはグローバル版の日本語。2バージョン先行する中国本土版では一部のセリフの言い回しが異なる。',
		head=('項目', '内容'), stage='ステージ', name='名前', when='ゲーム内の時刻', trails='小径', chapter='章',
		stages='ステージ', speak='登場する神秘学家', names='名前', count='ステージ数', mainland='中国本土版のみ（簡体字中国語の名前）',
		langs=('英語', '簡体字中国語', '繁体字中国語', '日本語', '韓国語'),
		prev='前のステージ', next='次のステージ', story='ストーリー', trail='小径', none='—', sep='、', home='ストーリー',
		date=lambda y, m, d, t: (f'{y}年' if y else '') + f'{m}月{d}日' + (f' {t}' if t else ''),
		src=[('Reverse: 1999 Story Compendium、commit {c}：5言語の閲覧用テキスト。ストーリーのテキストの権利は Bluepoch に帰属', 'tree'),
			('re1999-data-global、グローバル版クライアント {gl}：chapter.json と episode.json（ステージ番号、ゲーム内の時刻）', 'gl')]),
	'ko': dict(
		cats={'main': '메인 스토리', 'events': '이벤트 스토리', 'characters': '캐릭터 스토리 I', 'characters-2': '캐릭터 스토리 II', 'anecdotes': '일화', 'other': '기타 스토리'},
		cat_desc='리버스: 1999의 {c}, 모두 {n}개 장과 {k}개 스테이지.',
		ch_desc=['「{n}」{neun} {c}이며, 모두 {k}개 스테이지다.', '「{n}」{neun} {c}다.', '「{n}」{neun} 스토리의 장이다.'],
		ch_desc_main=['「{n}」{neun} 메인 스토리 {i}장이며, 모두 {k}개 스테이지다.', '「{n}」{neun} 메인 스토리 {i}장이다.', '「{n}」{neun} 메인 스토리의 장이다.'],
		st_desc=['「{s}」{sneun} {c} 「{n}」의 {k}번째 스테이지다.', '「{s}」{sneun} 「{n}」의 {k}번째 스테이지다.', '「{s}」{sneun} 스토리의 스테이지다.', '스토리의 스테이지.'],
		applies_gl='리버스: 1999, 글로벌 클라이언트 {b}({v} 버전), 한국어 텍스트',
		caveat_gl='텍스트는 글로벌 클라이언트의 한국어다. 두 버전 앞선 중국 본토 클라이언트는 일부 대사의 표현이 다르다.',
		head=('항목', '내용'), stage='스테이지', name='이름', when='게임 내 시각', trails='트레일', chapter='장',
		stages='스테이지', speak='등장하는 마도학자', names='이름', count='스테이지 수', mainland='중국 본토 한정 (간체 중국어 이름)',
		langs=('영어', '간체 중국어', '번체 중국어', '일본어', '한국어'),
		prev='이전 스테이지', next='다음 스테이지', story='스토리', trail='트레일', none='—', sep=', ', home='스토리',
		date=lambda y, m, d, t: (f'{y}년 ' if y else '') + f'{m}월 {d}일' + (f' {t}' if t else ''),
		src=[('Reverse: 1999 Story Compendium, commit {c}: 5개 언어 읽기용 텍스트. 스토리 텍스트의 권리는 Bluepoch에 있다', 'tree'),
			('re1999-data-global, 글로벌 클라이언트 {gl}: chapter.json과 episode.json(스테이지 번호, 게임 내 시각)', 'gl')]),
}
# The home page's story section goes before the section named here.
HOME_BEFORE = {'en': 'Summoning', 'zh-tw': '徵集', 'ja': '召喚', 'ko': '모집'}


# ---------------------------------------------------------------- source

def fetch():
	"""A sparse clone of the Compendium's reading text at the pinned commit."""
	if not (CLONE / '.git').exists():
		CLONE.parent.mkdir(parents=True, exist_ok=True)
		subprocess.run(['git', 'clone', '-q', '--filter=blob:none', '--no-checkout', f'https://github.com/{REPO}', str(CLONE)], check=True)
		subprocess.run(['git', '-C', str(CLONE), 'sparse-checkout', 'set', '--no-cone', f'{READER}/'], check=True)
	subprocess.run(['git', '-C', str(CLONE), 'fetch', '-q', 'origin'], check=True)
	subprocess.run(['git', '-C', str(CLONE), 'checkout', '-q', COMMIT], check=True)
	print(f'cache/story/repo at {COMMIT[:7]}')


def check_clone():
	head = subprocess.run(['git', '-C', str(CLONE), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
	if head != COMMIT:
		sys.exit(f'cache/story/repo is at {head[:7] or "nothing"}, records/story.json pins {COMMIT[:7]}: run fetch')


def files():
	"""{(folder, chapter id): {compendium language: path}}, and the chapter order of the English index."""
	out = {}
	for key in LANGS.values():
		for f in (CLONE / READER / key).glob('*/*.md'):
			out.setdefault((f.parent.name, f.name.split('-')[0]), {})[key] = f
	order = re.findall(r'\]\(([a-z]+)/(\d+)-', (CLONE / READER / 'zh-CN' / 'README.md').read_text())
	return out, order


def parse(text):
	"""(chapter name, [episode]) where an episode is {'id', 'name', 'subtitle', 'body', 'trails': [(name, text)]}."""
	text = re.sub(r'<!-- reading-navigation:start -->.*?<!-- reading-navigation:end -->', '', text, flags=re.S)
	# The client's no-break markup, escaped by the Compendium, is not part of the text.
	text = re.sub(r'\\?<\\?/?nobr\\?>', '', text)
	name = re.match(r'# \S+ · (.+)', text).group(1).strip()
	eps = []
	# A unit can carry older anchors before its own; the last one is the unit's id.
	parts = re.split(r'^(?:<a id="[^"]+"></a>\n)*<a id="episode-(\d+)"></a>\n', text, flags=re.M)
	for eid, block in zip(parts[1::2], parts[2::2]):
		head = re.match(r'## \S+ · (.+)', block).group(1).strip()
		m = re.search(r'<!-- reader-body:start -->\n?(.*?)\n?<!-- reader-body:end -->', block, flags=re.S)
		body = m.group(1).strip() if m else ''
		end = m.end() if m else block.find('\n') + 1
		sub = re.search(r'^> (.+)$', block[:m.start()] if m else '', flags=re.M)
		rest = block[end:]
		if '</details>' in rest:
			rest = rest[rest.find('</details>') + len('</details>'):]
		trails = []
		for t in re.split(r'^### ', rest, flags=re.M)[1:]:
			th, _, tb = t.partition('\n')
			tb = re.sub(r'^- \S+：`\d+`\n', '', tb.strip() + '\n', flags=re.M)  # element id
			tb = re.sub(r'\n-{3,}\s*$', '', tb.strip())
			trails.append((th.split(' · ', 1)[-1].strip(), tb.strip()))
		eps.append({'id': int(eid), 'name': head, 'subtitle': (sub.group(1).strip().strip('​') if sub else ''), 'body': body, 'trails': trails})
	return name, eps


def speakers(text, lang):
	"""Slugs of the arcanists who speak, in order of their first line."""
	key = LANGS[lang]
	names = {}
	for a in ARC:
		n = a['names'].get(key)
		if n:
			names.setdefault(n, a['slug'])
	seen = []
	for n in re.findall(r'^\*\*(.+?)[:：]\*\*', text, flags=re.M):
		slug = names.get(n.strip())
		if slug and slug not in seen:
			seen.append(slug)
	return seen


# ---------------------------------------------------------------- model

def slug_of(s):
	return re.sub(r'[^a-z0-9]+', '-', s.lower().replace('\xa0', ' ')).strip('-')


def models():
	"""Every chapter in five languages, in the order of the Compendium's index, and the mainland-only ones."""
	check_clone()
	found, order = files()
	eps_gl = {r['id']: r for r in g.gl('episode')}
	ch_gl = {r['id']: r for r in g.gl('chapter')}
	chapters, mainland, slugs = [], [], set()
	for folder, cid in order:
		paths = found.get((folder, cid), {})
		cat = dict(CATS)[folder]
		if set(paths) != set(LANGS.values()):
			if set(paths) == {'zh-CN'}:
				mainland.append({'cat': cat, 'id': cid, 'name': parse(paths['zh-CN'].read_text())[0]})
			continue
		parsed = {lang: parse(paths[key].read_text()) for lang, key in LANGS.items()}
		ids = [e['id'] for e in parsed['en'][1]]
		for lang, (_, eps) in parsed.items():
			if [e['id'] for e in eps] != ids:
				sys.exit(f'chapter {cid}: the stages of {lang} differ from English')
		index = ch_gl.get(int(cid), {}).get('chapterIndex', '') if folder == 'mainline' else ''
		slug = slug_of(parsed['en'][0])
		if slug in slugs:
			slug = f'{slug}-{cid}'
		slugs.add(slug)
		stages = []
		for k, eid in enumerate(ids, 1):
			e = eps_gl.get(eid, {})
			time = (e.get('time') or '').strip()
			mo = d = None
			if re.match(r'\d+/\d+', time):
				mo, d = (int(x) for x in time.split()[0].split('/'))
			text = {lang: parsed[lang][1][k - 1] for lang in LANGS}
			speak = []
			for lang in LANGS:
				x = text[lang]
				speak += [s for s in speakers(x['body'] + '\n' + '\n'.join(b for _, b in x['trails']), lang) if s not in speak]
			stages.append({'id': eid, 'k': k, 'code': f'{index}-{k:02d}' if index else f'{k:02d}', 'slug': f'{index.lower()}-{k:02d}' if index else f'{k:02d}',
				'year': e.get('year') or None, 'month': mo, 'day': d, 'clock': time.split()[1] if mo and ' ' in time else '',
				'names': {lang: text[lang]['name'] for lang in LANGS}, 'text': text, 'speak': speak,
				'page': bool(any(text[lang]['body'] or text[lang]['trails'] for lang in LANGS))})
		chapters.append({'id': cid, 'cat': cat, 'index': index, 'slug': slug,
			'names': {lang: parsed[lang][0].replace('\xa0', ' ') for lang in LANGS}, 'stages': stages})
	for one, two in SPLIT.items():
		mine = [c for c in chapters if c['cat'] == one]
		for c in mine[(len(mine) + 1) // 2:]:
			c['cat'] = two
	titles(chapters)
	return chapters, mainland


def other_titles(lang):
	out = set()
	for p in (DOCS / DIR[lang]).rglob('*.md') if lang != 'en' else [p for p in DOCS.rglob('*.md') if p.relative_to(DOCS).parts[0] not in DIR.values() and p.relative_to(DOCS).parts[0] not in ('zh-tw', 'zh-cn', 'ja', 'ko')]:
		if 'story' in p.relative_to(DOCS).parts:
			continue
		m = re.search(r'^title: "(.*)"$', p.read_text(), flags=re.M)
		if m:
			out.add(m.group(1))
	return out


def titles(chapters):
	"""Stage titles: the code and name in the main story, the name elsewhere; a name that another stage,
	a chapter or another page of the site also has in any language gets its chapter in brackets, in every language."""
	taken = {lang: other_titles(lang) for lang in LANGS}
	count = {lang: {} for lang in LANGS}
	for c in chapters:
		for lang in LANGS:
			taken[lang].add(c['names'][lang])
		for s in c['stages']:
			for lang in LANGS:
				n = s['names'][lang]
				count[lang][n] = count[lang].get(n, 0) + 1
	for c in chapters:
		for s in c['stages']:
			if c['index']:
				s['titles'] = {lang: f'{s["code"]} {s["names"][lang]}' for lang in LANGS}
				continue
			clash = any(count[lang][s['names'][lang]] > 1 or s['names'][lang] in taken[lang] for lang in LANGS)
			s['titles'] = {lang: (f'{s["names"][lang]} ({c["names"][lang]})' if lang in ('en', 'ko') else f'{s["names"][lang]}（{c["names"][lang]}）')
				if clash else s['names'][lang] for lang in LANGS}
	# Two stages that still share a title: add the stage number.
	for lang in LANGS:
		seen = {}
		for c in chapters:
			for s in c['stages']:
				seen.setdefault(s['titles'][lang], []).append(s)
		for t, ss in seen.items():
			if len(ss) > 1:
				for s in ss:
					for l2 in LANGS:
						if not s['titles'][l2].endswith(f' {s["code"]}'):
							s['titles'][l2] = f'{s["titles"][l2]} {s["code"]}'


# ---------------------------------------------------------------- pages

def arc_link(slug, lang):
	a = next(a for a in ARC if a['slug'] == slug)
	n = a['names'].get(LANGS[lang]) or a['names']['en']
	if (DOCS / DIR[lang] / 'arcanists' / f'{slug}.md').exists() and (DOCS / 'arcanists' / f'{slug}.md').exists():
		return f'[{n}](/{DIR[lang]}arcanists/{slug}/)'
	return n


def q(s):
	return s.replace('\\', '\\\\').replace('"', '\\"')


def neun(word):
	"""The Korean topic particle after a word: 은 after a final consonant, 는 after a vowel or a non-Hangul end."""
	w = re.sub(r'[\s」』"\'.,!?…)）]+$', '', word)
	c = w[-1:] if w else ''
	if '가' <= c <= '힣':
		return '은' if (ord(c) - 0xAC00) % 28 else '는'
	return '은(는)'


def fit(lang, options, **kw):
	for o in options:
		s = o.format(**kw)
		if len(s) <= LIMIT[lang]:
			return s
	return options[-1].format(**kw)


def frontmatter(lang, title, desc, aliases):
	t = T[lang]
	if lang == 'zh-cn':
		applies, caveat = t['applies_cn'].format(b=g.CN['build'], v='4.1'), t['caveat_cn']
	else:
		applies, caveat = t['applies_gl'].format(b=g.GL['build'], v='3.9'), t['caveat_gl']
	al = [a for a in dict.fromkeys(aliases) if a != title]
	url = {'tree': TREE, 'gl': g.GL_JSON + 'episode.json'}
	src = '\n'.join(f'  - title: "{q(s.format(c=COMMIT[:7], gl=g.GL["build"]))}"\n    url: {url[k]}' for s, k in t['src'])
	return '\n'.join(['---', f'title: "{q(title)}"', f'description: "{q(desc)}"', f'appliesTo: "{applies}"', f'caveat: "{caveat}"',
		f'lastVerified: {LAST_VERIFIED}'] + (['aliases:'] + [f'  - "{q(a)}"' for a in al] if al else []) + [f'sources:\n{src}', '---', ''])


def cell(s):
	return s.replace('|', '\\|')


def when(st, lang):
	if not st['month']:
		return T[lang]['none']
	return T[lang]['date'](st['year'], st['month'], st['day'], st['clock'])


def stage_link(c, s, lang):
	return f'/{DIR[lang]}story/{c["slug"]}/{s["slug"]}/'


def index_page(cat, chapters, mainland, lang):
	t = T[lang]
	label = t['cats'][cat]
	mine = [c for c in chapters if c['cat'] == cat]
	body = [f'| {t["chapter"]} | {t["count"]} | {t["trails"]} |', '| --- | --- | --- |']
	for c in mine:
		code = f' ({c["index"]})' if c['index'] else ''
		body.append(f'| [{cell(c["names"][lang])}](/{DIR[lang]}story/{c["slug"]}/){code} | {len(c["stages"])} | '
			f'{sum(len(s["text"][lang]["trails"]) for s in c["stages"])} |')
	ml = [m for m in mainland if m['cat'] == cat]  # a split category lists them on its first page
	if ml:
		body += ['', f'## {t["mainland"]}', '', '\n'.join(f'- {m["name"]}' for m in ml)]
	names = [T[x]['cats'][cat] for x in LANGS]
	desc = t['cat_desc'].format(c=label, ci=t.get('inner', {}).get(cat, label), n=len(mine), k=sum(len(c['stages']) for c in mine))
	return frontmatter(lang, label, desc, names) + '\n'.join(body) + '\n'


def chapter_page(c, lang):
	t = T[lang]
	n, sts, label = c['names'][lang], c['stages'], t['cats'][c['cat']]
	# No lead paragraph: the answer line is the page's only opening (root AGENTS.md, Visible page),
	# and the date the story begins is the first row of the table.
	body = [f'## {t["stages"]}', '', f'| {t["stage"]} | {t["name"]} | {t["when"]} | {t["trails"]} |', '| --- | --- | --- | --- |']
	for s in sts:
		nm = cell(s['names'][lang])
		nm = f'[{nm}]({stage_link(c, s, lang)})' if s['page'] else nm
		body.append(f'| {s["code"]} | {nm} | {when(s, lang)} | {len(s["text"][lang]["trails"])} |')
	speak = []
	for s in sts:
		speak += [x for x in s['speak'] if x not in speak]
	if speak:
		body += ['', f'## {t["speak"]}', '', t['sep'].join(arc_link(x, lang) for x in speak)]
	body += ['', f'## {t["names"]}', '', '| ' + ' | '.join(t['langs']) + ' |', '| --- | --- | --- | --- | --- |',
		'| ' + ' | '.join(cell(c['names'][x]) for x in ('en', 'zh-cn', 'zh-tw', 'ja', 'ko')) + ' |']
	# The main story's chapter codes are ordinals (10TH): the description gives the number.
	desc = fit(lang, t['ch_desc_main'] if c['index'] else t['ch_desc'], n=n, i=re.sub(r'\D', '', str(c['index'])), k=len(sts), c=label,
		ci=t.get('inner', {}).get(c['cat'], label), neun=neun(n))
	return frontmatter(lang, n, desc, [c['names'][x] for x in LANGS]) + '\n'.join(body) + '\n'


# (chapter id, unit id) -> (chapter slug, stage slug) of every stage with a page; set by write().
PAGES = {}


def relink(text, lang):
	"""Links of the Compendium between its own files point at our stage pages; a link to a unit with no
	page, or to another site (pictures of in-game items), keeps only its text."""
	def to_page(m):
		label, cid, eid = m.group(1), m.group(2), m.group(3)
		hit = PAGES.get((cid, int(eid))) if eid else None
		if not hit and not eid:
			hit = next((v for (c2, _), v in PAGES.items() if c2 == cid), None)
			hit = hit and (hit[0], None)
		if not hit:
			return label
		return f'[{label}](/{DIR[lang]}story/{hit[0]}/{hit[1] + "/" if hit[1] else ""})'
	text = re.sub(r'\[([^\]]*)\]\((?![/#]|https?:)(?:[^)]*/)?(\d+)-[^)/]*?\.md(?:#episode-(\d+))?\)', to_page, text)
	text = re.sub(r'\[([^\]]*)\]\(#[^)]*\)', r'\1', text)
	text = re.sub(r'\[([^\]]*)\]\(https?://[^)]*\)', r'\1', text)
	return text


ESC = '\ue000'  # an escaped asterisk (backslash, asterisk) while the marks are read: punctuation, never a mark


def _punct(c):
	return c == ESC or unicodedata.category(c)[0] in 'PS'


def _units(s):
	"""Characters of Markdown text, an escape (\\*) counted as one unit."""
	return re.findall(r'\\.|.', s, flags=re.S)


def _flank(before, after):
	"""(left-flanking, right-flanking) of a delimiter run between two characters (CommonMark)."""
	b = before[-1] if before else ' '
	a = after[0] if after else ' '
	ws = lambda c: c.isspace()  # noqa: E731
	pu = lambda c: _punct(c) or c == '\\'  # noqa: E731
	left = not ws(a) and (not pu(a) or ws(b) or pu(b))
	right = not ws(b) and (not pu(b) or ws(a) or pu(a))
	return left, right


PAIRS = {ESC: ESC, '）': '（', ')': '(', '」': '「', '』': '『', '”': '“', '"': '"', '’': '‘', "'": "'", '》': '《', '〉': '〈', '】': '【', ']': '[', '］': '［'}


def _fix_paragraph(p):
	"""The bold spans of one paragraph, made to parse: punctuation at an edge of a span moves
	outside it (brackets and quotes in pairs); a span that still would not parse loses its marks."""
	parts = re.split(r'(?<!\*)\*\*(?!\*)', p.replace('\\*', ESC))
	if len(parts) % 2 == 0:
		# An odd number of marks pairs with nothing (a garbled note: App&^**le ... Hea*<hy): every
		# asterisk of the paragraph is a character of the text.
		return re.sub(r'(?<!\\)\*', r'\\*', p)
	# parts: text, inner, text, inner, text ...
	out = list(parts)
	for i in range(1, len(out), 2):
		inner = out[i]
		for _ in range(3):
			left_open, _r = _flank(out[i - 1], inner)
			_l, right_close = _flank(inner, out[i + 1])
			if left_open and right_close or not inner.strip():
				break
			u = _units(inner)
			if not left_open:
				k = 0
				while k < len(u) and (u[k].isspace() or _punct(u[k][-1]) or u[k].startswith('\\')):
					k += 1
				out[i - 1] += ''.join(u[:k])
				u = u[k:]
			if not right_close:
				k = len(u)
				while k > 0 and (u[k - 1].isspace() or _punct(u[k - 1][-1]) or u[k - 1].startswith('\\')):
					k -= 1
				moved = u[k:]
				u = u[:k]
				out[i + 1] = ''.join(moved) + out[i + 1]
				# A closing bracket or quote that left takes its opening one along.
				opens = [PAIRS[m] for m in moved if m in PAIRS]
				while u and opens and u[0] in opens:
					opens.remove(u[0])
					out[i - 1] += u.pop(0)
			inner = ''.join(u)
		left_open, _r = _flank(out[i - 1], inner)
		_l, right_close = _flank(inner, out[i + 1])
		out[i] = (inner, left_open and right_close and bool(inner.strip()))
	return ''.join(x if k % 2 == 0 else (f'**{x[0]}**' if x[1] else x[0]) for k, x in enumerate(out)).replace(ESC, '\\*')


def fix_marks(text):
	"""Make the Compendium's bold marks parse in CommonMark without changing a word.

	- A line whose words follow the speaker with no space (**斯奈德:****請記得我**。, **Adèle:**Byfire)
	  gets one.
	- Two bold runs that touch (**Title****1. Section**), in documents whose line breaks the
	  Compendium dropped, get a space between them.
	- A bold span that runs over a blank line (verses, songs) is closed at the end of each
	  paragraph and opened again at the start of the next: CommonMark ends a span at a paragraph.
	- Asterisks inside a word (f**cking: lower-case letters on both sides; **Hypothesis**This is a
	  span whose line break the Compendium dropped) are characters, and so are all of a
	  paragraph whose marks do not pair.
	- Within a paragraph, punctuation at the edge of a span moves outside the marks until
	  CommonMark reads them (the flanking rules, which Chinese and Japanese text seldom meets),
	  brackets and quotes in pairs; a span that still would not parse is shown without marks.
	"""
	text = re.sub(r'^((?:> )?\*\*[^*\n]+[:：]\*\*)(?=\S)', r'\1 ', text, flags=re.M)
	text = re.sub(r'(?<=\S)\*\*\*\*(?=\S)', '** **', text)
	text = re.sub(r'(?<=[a-z])\*\*(?=[a-z])', r'\\*\\*', text)
	paras = re.split(r'(\n[ \t>]*\n)', text)
	marks = [len(re.findall(r'(?<!\*)\*\*(?!\*)', paras[k].replace('\\*', ESC))) for k in range(0, len(paras), 2)]
	if sum(marks) % 2 == 0:
		carry = False
		for n, k in enumerate(range(0, len(paras), 2)):
			p = paras[k]
			quote = re.match(r'(?:> ?)*', p).group(0)
			if carry:
				p = quote + '**' + p[len(quote):]
			count = marks[n] + carry
			carry = count % 2 == 1
			if carry:
				p += '**'
			paras[k] = p
	return ''.join(_fix_paragraph(p) if k % 2 == 0 else p for k, p in enumerate(paras))


def stage_page(c, s, lang):
	t = T[lang]
	x = s['text'][lang]
	pages = [o for o in c['stages'] if o['page']]
	i = pages.index(s)
	prev = pages[i - 1] if i > 0 else None
	nxt = pages[i + 1] if i + 1 < len(pages) else None
	link = lambda o: f'[{cell(o["titles"][lang])}]({stage_link(c, o, lang)})' if o else t['none']  # noqa: E731
	code = f' ({c["index"]})' if c['index'] else ''
	body = []
	if x['subtitle']:
		body += [f'> {x["subtitle"]}', '']
	body += [f'| {t["head"][0]} | {t["head"][1]} |', '| --- | --- |',
		f'| {t["chapter"]} | [{cell(c["names"][lang])}](/{DIR[lang]}story/{c["slug"]}/){code} |',
		f'| {t["stage"]} | {s["code"]} |',
		f'| {t["when"]} | {when(s, lang)} |',
		f'| {t["speak"]} | {t["sep"].join(arc_link(a, lang) for a in s["speak"]) or t["none"]} |',
		f'| {t["prev"]} | {link(prev)} |', f'| {t["next"]} | {link(nxt)} |']
	if x['body']:
		body += ['', f'## {t["story"]}', '', fix_marks(relink(x['body'], lang))]
	if x['trails']:
		body += ['', f'## {t["trail"]}']
		for name, text in x['trails']:
			body += ['', f'### {name}', '', fix_marks(relink(text, lang))]
	desc = fit(lang, t['st_desc'], s=s['titles'][lang], k=s['k'], n=c['names'][lang], c=t['cats'][c['cat']],
		ci=t.get('inner', {}).get(c['cat'], t['cats'][c['cat']]), sneun=neun(s['titles'][lang]))
	return frontmatter(lang, s['titles'][lang], desc, [s['titles'][o] for o in LANGS]) + '\n'.join(body) + '\n'


def write_home():
	"""The home page's story section: a link to each index page (zh-cn: scripts/to-zh-cn.py)."""
	for lang, before in HOME_BEFORE.items():
		t = T[lang]
		p = DOCS / DIR[lang] / 'index.md'
		text = p.read_text()
		links = '\n'.join(f'- [{t["cats"][x]}](/{DIR[lang]}story/{x}/)' for x in INDEXES)
		section = f'## {t["home"]}\n\n{links}\n\n'
		if f'## {t["home"]}\n' in text:
			text = re.sub(rf'## {re.escape(t["home"])}\n\n(?:- .*\n)+\n', lambda _: section, text, count=1)
		else:
			text = text.replace(f'## {before}\n', section + f'## {before}\n', 1)
		p.write_text(text)


def write():
	chapters, mainland = models()
	PAGES.update({(c['id'], s['id']): (c['slug'], s['slug']) for c in chapters for s in c['stages'] if s['page']})
	for lang in LANGS:
		root = DOCS / DIR[lang] / 'story'
		if root.exists():
			for f in root.rglob('*.md'):
				f.unlink()
		root.mkdir(parents=True, exist_ok=True)
		for cat in INDEXES:
			(root / f'{cat}.md').write_text(index_page(cat, chapters, mainland, lang))
		for c in chapters:
			(root / f'{c["slug"]}.md').write_text(chapter_page(c, lang))
			(root / c['slug']).mkdir(exist_ok=True)
			for s in c['stages']:
				if s['page']:
					(root / c['slug'] / f'{s["slug"]}.md').write_text(stage_page(c, s, lang))
	write_home()
	n = sum(s['page'] for c in chapters for s in c['stages'])
	print(f'{len(chapters)} chapters, {n} stage pages in each of {len(LANGS)} languages; mainland only, no page: {len(mainland)}')
	if any(c['slug'] in INDEXES for c in chapters):
		sys.exit('a chapter slug is the name of an index page')


def main(argv):
	if argv[:1] == ['fetch']:
		fetch()
		return 0
	if argv[:1] == ['write']:
		write()
		return 0
	print(__doc__)
	return 2


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
