"""Write the skeleton of an arcanist page from the records; check a finished page against them.

  python3 -I pipeline/scaffold.py write <lang> <slug> ...    new page files (never overwrites)
  python3 -I pipeline/scaffold.py check <page.md> ...        exit 1 on a difference
  python3 -I pipeline/scaffold.py profile <page.md> ...      rewrite the profile table from the records

<lang> is en, zh-tw, ja or ko (zh-cn is written by scripts/to-zh-cn.py).

The skeleton holds everything the records decide: the frontmatter except description and caveat,
the art line, the profile table (with the Resonance set and its patterns), the Insight material table, the Ultimate heading and the names
table. The rest is marked <!-- WRITE ... -->: the writer restates the kit in the site's words.

`check` regenerates those blocks and fails when the page lacks one of them word for word, when a
WRITE or TODO mark is left, or when a number in the written parts (description, caveat and every
section but the generated tables) is not in the game's text of that arcanist in any language
(cache/source/<slug>.json). Whole numbers up to 10 pass: ranks, Insight steps, levels, counts.
"""
import functools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'pipeline'))  # gamedata and write_systems, read for the Resonance set
DOCS = ROOT / 'src' / 'content' / 'docs'
REC = {a['slug']: a for a in json.loads((ROOT / 'records' / 'arcanists.json').read_text())['arcanists']}
REL = json.loads((ROOT / 'records' / 'releases.json').read_text())['arcanists']
ART = json.loads((ROOT / 'records' / 'art.json').read_text()) if (ROOT / 'records' / 'art.json').exists() else {}
PINS = json.loads((ROOT / 'records' / 'sources.json').read_text())
CN, GL = PINS['cn'], PINS['gl']
CN_TREE = f'https://github.com/St-Pavlov-Foundation/re1999-data/tree/{CN["commit"]}/data/json'
CN_CHAR = f'https://github.com/St-Pavlov-Foundation/re1999-data/blob/{CN["commit"]}/data/json/character.json'
GL_TREE = f'https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/{GL["commit"]}/data/json'
GL_CHAR = f'https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/{GL["commit"]}/data/json/character.json'
GL_EN = f'https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/{GL["commit"]}/data/configs/language/language_en.json'
CN_VER, GL_VER = '4.1', '3.9'
LAST_VERIFIED = '2026-11-22'
# Names that no client has yet in that language: translated (site AGENTS.md, Languages); the
# Traditional Chinese one is the Simplified name converted with OpenCC s2tw.
UNOFFICIAL = {
	'perchta': {'zh-tw': '佩施塔', 'ja': 'ペルヒタ', 'ko': '페르히타'},
	'huntsworn-lilya': {'zh-tw': '狩勳女巫紅弩箭', 'ja': '狩勲の魔女リーリャ', 'ko': '사냥 훈장의 마녀 릴리아'},
	'drake': {'zh-tw': '德雷克', 'ja': 'ドレイク', 'ko': '드레이크'},
	'glyndwr': {'zh-tw': '格林杜爾', 'ja': 'グリンドゥール', 'ko': '글린두르'},
	# The global client's Korean name of Lady by the Lake is empty.
	'lady-by-the-lake': {'ko': '《호숫가의 여인》'},
	'evelyn': {'zh-tw': '伊芙琳', 'ja': 'エヴリン', 'ko': '에블린'},
}
KEY = {'en': 'en', 'zh-tw': 'zh-TW', 'ja': 'ja', 'ko': 'ko'}
# A version with no date: the Fandom page text says the arcanist was introduced in that version.
VERSION_ONLY = {'drake': '4.0', 'glyndwr': '4.0'}

L = {
	'en': dict(
		dir='', stars='{n} stars', head=('Field', 'Value'),
		rows=('Rarity', 'Afflatus', 'Damage', 'Tags', 'Resonance Patterns', 'Mainland release', 'Global release'),
		res='[{s} set](/systems/resonance/): {p}',
		afflatus={'Star': 'Star', 'Mineral': 'Mineral', 'Beast': 'Beast', 'Plant': 'Plant', 'Spirit': 'Spirit', 'Intellect': 'Intellect', 101: 'Mineral and Star'},
		damage={'Reality': 'Reality', 'Mental': 'Mental'}, tagsep=', ',
		version='version {v}', unknown='—', notyet='not yet', notreleased='{d}, not yet released', inclient='in the global client',
		mat=('Insight', 'Max level', 'Materials'), matsep='; ', num='{:,}',
		names=('English', 'Simplified Chinese', 'Traditional Chinese', 'Japanese', 'Korean'),
		unofficial='{n} (not yet official)', none='not yet official',
		sec=dict(inc='Incantations', ult='Ultimate: {n}', inh='Inheritance', por='Portrait', eup='Euphoria', names='Names'),
		alt='{n}, full-length art',
		applies_gl=f'Reverse: 1999, global client {GL["build"]} (version {GL_VER}) and mainland China client {CN["build"]} (version {CN_VER})',
		applies_cn=f'Reverse: 1999, mainland China client {CN["build"]} (version {CN_VER}); global client {GL["build"]} (version {GL_VER})',
		src_gl=lambda e: [
			(f're1999-data-global, global client {GL["build"]}: character{", skill and Euphoria" if e else " and skill"} tables', GL_TREE),
			(f're1999-data-global, global client {GL["build"]}: English text', GL_EN),
			(f're1999-data, mainland client {CN["build"]}: character.json', CN_CHAR)],
		src_cn=lambda n: [
			(f're1999-data, mainland client {CN["build"]}: character.json', CN_CHAR),
			(f're1999-data, mainland client {CN["build"]}: skill.json and skill_effect.json', CN_TREE),
			(f're1999-data-global, global client {GL["build"]} (no entry for {n})', GL_CHAR)],
		fandom='Reverse: 1999 Wiki (Fandom), {p}, revision {r}',
		official=('Mainland official site: version 4.1, updated 2026-11-05', 'https://re.bluepoch.com/'),
		art=('Reverse: 1999 Wiki (Fandom), {f}', 'Image file, uploaded {d}'),
	),
	'zh-tw': dict(
		dir='zh-tw/', stars='{n} 星', head=('項目', '內容'),
		rows=('稀有度', '靈感', '創傷類型', '標籤', '共鳴調頻', '中國大陸版上線', '國際版上線'),
		res='[{s}組](/zh-tw/systems/resonance/)：{p}',
		afflatus={'Star': '星', 'Mineral': '岩', 'Beast': '獸', 'Plant': '木', 'Spirit': '靈', 'Intellect': '智', 101: '岩與星'},
		damage={'Reality': '現實', 'Mental': '精神'}, tagsep='、',
		version='{v} 版', unknown='—', notyet='尚未上線', notreleased='{d}，尚未上線', inclient='已在國際版用戶端中',
		mat=('洞悉', '等級上限', '材料'), matsep='；', num='{:,}',
		names=('英文', '簡體中文', '繁體中文', '日文', '韓文'),
		unofficial='{n}（非官方）', none='尚無官方譯名',
		sec=dict(inc='咒語', ult='至終的儀式：{n}', inh='傳承', por='塑造', eup='狂想', names='名稱'),
		alt='{n}全身立繪',
		applies_gl=f'重返未來：1999，國際版用戶端 {GL["build"]}（{GL_VER} 版）與中國大陸版用戶端 {CN["build"]}（{CN_VER} 版）',
		applies_cn=f'重返未來：1999，中國大陸版用戶端 {CN["build"]}（{CN_VER} 版）；國際版用戶端 {GL["build"]}（{GL_VER} 版）',
		src_gl=lambda e: [
			(f're1999-data-global，國際版用戶端 {GL["build"]}：角色{"、技能與狂想" if e else "與技能"}資料表', GL_TREE),
			(f're1999-data-global，國際版用戶端 {GL["build"]}：英文文字', GL_EN),
			(f're1999-data，中國大陸版用戶端 {CN["build"]}：character.json', CN_CHAR)],
		src_cn=lambda n: [
			(f're1999-data，中國大陸版用戶端 {CN["build"]}：character.json', CN_CHAR),
			(f're1999-data，中國大陸版用戶端 {CN["build"]}：skill.json 與 skill_effect.json', CN_TREE),
			(f're1999-data-global，國際版用戶端 {GL["build"]}（沒有{n}的條目）', GL_CHAR)],
		fandom='Reverse: 1999 Wiki (Fandom)，{p}，修訂版 {r}',
		official=('中國大陸版官方網站：4.1 版，2026-11-05 更新', 'https://re.bluepoch.com/'),
		art=('Reverse: 1999 Wiki (Fandom)，{f}', '圖片檔，{d} 上傳'),
	),
	'ja': dict(
		dir='ja/', stars='★{n}', head=('項目', '内容'),
		rows=('レア度', '本源', 'ダメージタイプ', 'タグ', '共鳴の変調', '中国本土版の実装', 'グローバル版の実装'),
		res='[{s}グループ](/ja/systems/resonance/)：{p}',
		afflatus={'Star': '星', 'Mineral': '岩', 'Beast': '獣', 'Plant': '木', 'Spirit': '霊', 'Intellect': '知', 101: '岩と星'},
		damage={'Reality': 'リアル', 'Mental': 'メンタル'}, tagsep='、',
		version='バージョン {v}', unknown='—', notyet='未実装', notreleased='{d}、未実装', inclient='グローバル版クライアントに収録',
		mat=('洞察', '最大レベル', '素材'), matsep='、', num='{:,}',
		names=('英語', '簡体字中国語', '繁体字中国語', '日本語', '韓国語'),
		unofficial='{n}（非公式）', none='公式名なし',
		sec=dict(inc='スペル', ult='アルティメット：{n}', inh='伝承', por='塑造', eup='狂想', names='名前'),
		alt='{n}の全身立ち絵',
		applies_gl=f'リバース：1999、グローバル版クライアント {GL["build"]}（バージョン {GL_VER}）と中国本土版クライアント {CN["build"]}（バージョン {CN_VER}）',
		applies_cn=f'リバース：1999、中国本土版クライアント {CN["build"]}（バージョン {CN_VER}）。グローバル版クライアント {GL["build"]}（バージョン {GL_VER}）',
		src_gl=lambda e: [
			(f're1999-data-global、グローバル版クライアント {GL["build"]}：キャラクター{"、スキル、狂想" if e else "とスキル"}のテーブル', GL_TREE),
			(f're1999-data-global、グローバル版クライアント {GL["build"]}：英語テキスト', GL_EN),
			(f're1999-data、中国本土版クライアント {CN["build"]}：character.json', CN_CHAR)],
		src_cn=lambda n: [
			(f're1999-data、中国本土版クライアント {CN["build"]}：character.json', CN_CHAR),
			(f're1999-data、中国本土版クライアント {CN["build"]}：skill.json と skill_effect.json', CN_TREE),
			(f're1999-data-global、グローバル版クライアント {GL["build"]}（{n}の項目なし）', GL_CHAR)],
		fandom='Reverse: 1999 Wiki (Fandom)、{p}、版 {r}',
		official=('中国本土版公式サイト：バージョン 4.1、2026-11-05 更新', 'https://re.bluepoch.com/'),
		art=('Reverse: 1999 Wiki (Fandom)、{f}', '画像ファイル、{d} アップロード'),
	),
	'ko': dict(
		dir='ko/', stars='{n}성', head=('항목', '내용'),
		rows=('희귀도', '영감', '피해 유형', '태그', '공명 변조', '중국 본토 출시', '글로벌 출시'),
		res='[{s} 그룹](/ko/systems/resonance/): {p}',
		afflatus={'Star': '천체', 'Mineral': '암석', 'Beast': '야수', 'Plant': '나무', 'Spirit': '영혼', 'Intellect': '지능', 101: '암석과 천체'},
		damage={'Reality': '현실', 'Mental': '정신'}, tagsep=', ',
		version='{v} 버전', unknown='—', notyet='출시 전', notreleased='{d}, 출시 전', inclient='글로벌 클라이언트에 있음',
		mat=('통찰', '최대 레벨', '재료'), matsep=', ', num='{:,}',
		names=('영어', '간체 중국어', '번체 중국어', '일본어', '한국어'),
		unofficial='{n} (비공식)', none='공식 명칭 없음',
		sec=dict(inc='주문', ult='최종 술식: {n}', inh='계승', por='형상', eup='광상', names='이름'),
		alt='{n} 전신 일러스트',
		applies_gl=f'리버스: 1999, 글로벌 클라이언트 {GL["build"]}({GL_VER} 버전)와 중국 본토 클라이언트 {CN["build"]}({CN_VER} 버전)',
		applies_cn=f'리버스: 1999, 중국 본토 클라이언트 {CN["build"]}({CN_VER} 버전). 글로벌 클라이언트 {GL["build"]}({GL_VER} 버전)',
		src_gl=lambda e: [
			(f're1999-data-global, 글로벌 클라이언트 {GL["build"]}: 캐릭터{", 스킬, 광상" if e else "와 스킬"} 테이블', GL_TREE),
			(f're1999-data-global, 글로벌 클라이언트 {GL["build"]}: 영어 텍스트', GL_EN),
			(f're1999-data, 중국 본토 클라이언트 {CN["build"]}: character.json', CN_CHAR)],
		src_cn=lambda n: [
			(f're1999-data, 중국 본토 클라이언트 {CN["build"]}: character.json', CN_CHAR),
			(f're1999-data, 중국 본토 클라이언트 {CN["build"]}: skill.json과 skill_effect.json', CN_TREE),
			(f're1999-data-global, 글로벌 클라이언트 {GL["build"]} ({n} 항목 없음)', GL_CHAR)],
		fandom='Reverse: 1999 Wiki (Fandom), {p}, 판 {r}',
		official=('중국 본토 공식 사이트: 4.1 버전, 2026-11-05 업데이트', 'https://re.bluepoch.com/'),
		art=('Reverse: 1999 Wiki (Fandom), {f}', '이미지 파일, {d} 업로드'),
	),
}


def source(slug):
	return json.loads((ROOT / 'cache' / 'source' / f'{slug}.json').read_text())


def tag_map():
	"""Battle tags: Simplified Chinese -> the global client's string in each language."""
	out = {}
	for p in (ROOT / 'cache' / 'source').glob('*.json'):
		s = json.loads(p.read_text())
		if 'en' not in s:
			continue
		for i, zh in enumerate(s['zh-CN'].get('tags', [])):
			for lang, key in KEY.items():
				tags = s.get(key, {}).get('tags', [])
				if i < len(tags):
					out.setdefault(zh, {})[lang] = re.sub(r'<[^>]+>', '', tags[i])  # <nobr>Follow-Up</nobr>
	return out


TAGS = tag_map()


def name(a, lang):
	"""The arcanist's name in a language: official, else translated."""
	key = KEY[lang]
	if a['names'].get(key):
		return a['names'][key]
	return UNOFFICIAL[a['slug']][lang]


def release(a, lang):
	t, r = L[lang], REL.get(a['slug'], {})
	cn = r.get('cn')
	if not cn and a['slug'] in VERSION_ONLY:
		cn = t['version'].format(v=VERSION_ONLY[a['slug']])
	mainland = (t['notreleased'].format(d=cn) if not a['online'] and cn else cn) or t['unknown']
	if not a['inGlobal']:
		glob = t['notyet']
	else:
		glob = r.get('global') or t['inclient']
	return mainland, glob


@functools.cache
def _resonance():
	"""Each arcanist's Resonance set and its patterns, as the Resonance page states them."""
	import write_systems
	return write_systems.resonance_data()


def resonance(slug, lang):
	"""The Resonance Patterns cell: the arcanist's set (the shape of the main Idea) and its five patterns besides the default."""
	import gamedata
	r, t = _resonance(), L[lang]
	m = next((m for m, arcs in r['sets'].items() if any(a['slug'] == slug for a in arcs)), None)
	if m is None:
		return None
	pats = [gamedata.text(p['gl'], KEY[lang]) if p['gl'] else p['cn'] for (m2, _), p in sorted(r['pats'].items()) if m2 == m]
	import write_systems
	return t['res'].format(s=write_systems.RT2[lang]['shapes'][m], p=t['tagsep'].join(pats))


def blocks(slug, lang):
	"""The parts of the page the records decide, as {name: text}."""
	a, t = REC[slug], L[lang]
	gl = a['inGlobal']
	title = name(a, lang)
	out = {}
	# frontmatter
	all_names = [name(a, 'en'), name(a, 'zh-tw'), a['names']['zh-CN'], name(a, 'ja'), name(a, 'ko')]
	aliases = []
	for n in all_names:
		if n != title and n not in aliases:
			aliases.append(n)
	out['title'] = f'title: "{title}"'
	out['appliesTo'] = f'appliesTo: "{t["applies_gl"] if gl else t["applies_cn"]}"'
	out['lastVerified'] = f'lastVerified: {LAST_VERIFIED}'
	# No aliases line when every language has the same name (37).
	out['aliases'] = 'aliases:\n' + '\n'.join(f'  - "{n}"' for n in aliases) if aliases else ''
	src = t['src_gl'](a['euphoria']) if gl else t['src_cn'](title)
	rel = REL.get(slug)
	if rel:
		src.append((t['fandom'].format(p=rel['page'], r=rel['revid']),
			f'https://reverse1999.fandom.com/wiki/{rel["page"].replace(" ", "_")}?oldid={rel["revid"]}'))
	if not gl:
		src.append(t['official'])
	out['sources'] = 'sources:\n' + '\n'.join(f'  - title: "{s}"\n    url: {u}' for s, u in src)
	if slug in ART:
		f = ART[slug]
		out['art'] = (f'art:\n  - title: "{t["art"][0].format(f=f["file"])}"\n    url: {f["page"]}\n'
			f'  - title: "{t["art"][1].format(d=f["uploaded"])}"\n    url: {f["url"]}')
		out['art line'] = f'![{t["alt"].format(n=title)}](/art/characters/{slug}.webp)'
	# profile
	tags = t['tagsep'].join(TAGS.get(z, {}).get(lang, z) for z in a['tagsZh'])
	mainland, glob = release(a, lang)
	vals = (t['stars'].format(n=a['stars']), t['afflatus'][a['afflatus']], t['damage'][a['damage']], tags, resonance(slug, lang), mainland, glob)
	out['profile'] = '\n'.join([f'| {t["head"][0]} | {t["head"][1]} |', '| --- | --- |']
		+ [f'| {k} | {v} |' for k, v in zip(t['rows'], vals) if v is not None])
	# Insight materials
	key = KEY[lang]
	rows = []
	for step in a['insight']:
		mats = []
		for m in step['materials']:
			n = m['names'].get(key) or m['names']['en']
			mats.append(f'{n} {t["num"].format(m["count"])}' if m['kind'] == 'currency' else f'{n} ×{m["count"]}')
		rows.append(f'| {step["insight"]} | {step["levelCap"] - step["requiresLevel"]} | {t["matsep"].join(mats)} |')
	if rows:
		out['materials'] = '\n'.join([f'| {" | ".join(t["mat"])} |', '| --- | --- | --- |'] + rows)
	# Ultimate heading (official name where the client has one in this language)
	ult = ((source(slug).get(key if gl else 'zh-CN') or {}).get('ultimate') or {}).get('name')
	if gl and ult:
		out['ultimate'] = f'## {t["sec"]["ult"].format(n=re.sub(r"<[^>]+>|[\"“”「」『』‘’]", "", ult))}'
	# names
	def cell(lang2, key2):
		if a['names'].get(key2):
			return a['names'][key2]
		if lang2 == 'zh-tw':
			return t['unofficial'].format(n=name(a, 'zh-tw'))
		if lang == 'en' and lang2 != 'en':
			return t['none']
		return t['unofficial'].format(n=name(a, lang2))
	row = [a['names']['en'], a['names']['zh-CN'], cell('zh-tw', 'zh-TW'), cell('ja', 'ja'), cell('ko', 'ko')]
	out['names'] = '\n'.join([f'| {" | ".join(t["names"])} |', '| --- | --- | --- | --- | --- |', f'| {" | ".join(row)} |'])
	return out


def skeleton(slug, lang):
	a, t, b = REC[slug], L[lang], blocks(slug, lang)
	sec = t['sec']
	fm = [ '---', b['title'], 'description: "<!-- WRITE: one sentence, what the arcanist is -->"', b['appliesTo'],
		'caveat: "<!-- WRITE: the one qualifier a reader most likely misses -->"', b['lastVerified']] + ([b['aliases']] if b['aliases'] else [])
	if 'art' in b:
		fm.append(b['art'])
	fm += [b['sources'], '---', '']
	body = []
	if 'art line' in b:
		body += [b['art line'], '']
	body += [b['profile'], '', '<!-- WRITE: a short paragraph on how the kit works -->', '',
		f'## {sec["inc"]}', '', '<!-- WRITE: table of the two incantations by rank, then notes -->', '',
		b.get('ultimate', f'## {sec["ult"].format(n="<!-- WRITE: name -->")}'), '', '<!-- WRITE: what the Ultimate does; statuses the kit uses -->', '',
		f'## {sec["inh"]}', '', '<!-- WRITE: table of the Insight passives -->', '']
	if 'materials' in b:
		body += [b['materials'], '']
	body += [f'## {sec["por"]}', '', '<!-- WRITE: table of the five Portrait levels -->', '']
	if a['euphoria']:
		body += [f'## {sec["eup"]}', '', '<!-- WRITE: when it opens, then a table of the Epiphanies -->', '']
	body += [f'## {sec["names"]}', '', b['names'], '']
	return '\n'.join(fm + body)


GENERATED = ('profile', 'materials', 'names')


def numbers(text):
	return set(re.findall(r'\d+(?:\.\d+)?', text.replace(',', '')))


def check(path):
	path = Path(path).resolve()
	rel = path.relative_to(DOCS).as_posix()
	m = re.match(r'(?:(zh-tw|ja|ko)/)?arcanists/([^/]+)\.md$', rel)
	if not m:
		return [f'{rel}: not an arcanist page in en, zh-tw, ja or ko']
	lang, slug = m.group(1) or 'en', m.group(2)
	text = path.read_text()
	errors = []
	for k, v in blocks(slug, lang).items():
		if v not in text:
			errors.append(f'{rel}: {k} differs from the records:\n{v}')
	for mark in re.findall(r'<!-- WRITE[^>]*-->|TODO', text):
		errors.append(f'{rel}: unwritten: {mark}')
	# Also allowed: the numbers of the generated blocks (dates, counts) and the client versions.
	allowed = numbers(json.dumps(source(slug), ensure_ascii=False)) | {str(i) for i in range(11)} | {CN_VER, GL_VER}
	allowed |= numbers(' '.join(blocks(slug, lang).values()))
	# Euphoria opens at Insight III level 30 (6-star) or level 1 (5-star): the Fandom Euphoria
	# page (revision 91875); the client tables do not hold the unlock level.
	if REC[slug]['euphoria']:
		allowed |= {'30', '1'}
	written = text
	for k in GENERATED:
		written = written.replace(blocks(slug, lang).get(k, '\0'), '')
	written = re.sub(r'^(?:sources|art):\n(?:  .*\n)+', '', written, flags=re.M)
	written = re.sub(r'^(?:appliesTo|lastVerified|title): .*\n', '', written, flags=re.M)
	written = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', written)
	for n in sorted(numbers(written) - allowed, key=lambda x: float(x)):
		line = next((l for l in written.split('\n') if re.search(rf'(?<![\d.]){re.escape(n)}(?![\d.])', l.replace(',', ''))), '')
		errors.append(f'{rel}: number {n} is not in the game text of {slug}: {line.strip()[:120]}')
	return errors


def main(argv):
	if len(argv) >= 2 and argv[0] == 'write':
		lang, slugs = argv[1], argv[2:]
		for slug in slugs:
			p = DOCS / L[lang]['dir'] / 'arcanists' / f'{slug}.md'
			if p.exists():
				print(f'exists, left as it is: {p.relative_to(ROOT)}')
				continue
			p.write_text(skeleton(slug, lang))
			print(f'wrote {p.relative_to(ROOT)}')
		return 0
	if len(argv) >= 2 and argv[0] == 'profile':
		# Rewrite the profile table of finished pages from the records; the rest of the page stays.
		for arg in argv[1:]:
			path = Path(arg).resolve()
			m = re.match(r'(?:(zh-tw|ja|ko)/)?arcanists/([^/]+)\.md$', path.relative_to(DOCS).as_posix())
			lang, slug = m.group(1) or 'en', m.group(2)
			head = f'| {L[lang]["head"][0]} | {L[lang]["head"][1]} |\n| --- | --- |\n'
			text = path.read_text()
			new = re.sub(re.escape(head) + r'(?:\|.*\|\n)+', lambda _: blocks(slug, lang)['profile'] + '\n', text, count=1)
			if new != text:
				path.write_text(new)
				print(f'profile rewritten: {path.relative_to(ROOT)}')
		return 0
	if len(argv) >= 2 and argv[0] == 'check':
		errors = [e for p in argv[1:] for e in check(p)]
		for e in errors:
			print(e)
		print(f'{len(argv) - 1} page(s), {len(errors)} problem(s)')
		return 1 if errors else 0
	print(__doc__)
	return 2


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
