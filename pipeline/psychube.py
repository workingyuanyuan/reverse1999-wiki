"""Psychube pages: records, page skeletons, the game text for writers, a check, and the index pages.

  python3 -I pipeline/psychube.py list                       slug, rarity and names of every Psychube
  python3 -I pipeline/psychube.py text <slug> [lang ...]     effect text by Amplification (default zh-CN en)
  python3 -I pipeline/psychube.py write <lang> <slug|all> ...   page skeletons (never overwrites)
  python3 -I pipeline/psychube.py check <page.md> ...        exit 1 on a difference
  python3 -I pipeline/psychube.py indexes                    the four index pages in en, zh-tw, ja, ko; records/psychubes.json
  python3 -I pipeline/psychube.py art                        put the art line and credits of records/art-psychubes.json in every page

<lang> is en, zh-tw, ja or ko (zh-cn is written by scripts/to-zh-cn.py).

A Psychube is a row of equip.json with five rows in equip_skill.json (Amplification 1 to 5) and
not an experience item. Stats at the maximum level are the base values of equip_strengthen.json
times attributeRate / 1000 at that level (equip_strengthen_cost.json; 1000 at level 60, checked
against Fandom, Thunderous Applause, revision 6676); the extra stat is the row of
equip_break_attr.json at the highest break level, in tenths of a percent. The game's own
recommendations are character_recommend.json, field equipRec.

The skeleton holds the frontmatter but description and caveat, the profile table and the names
table; the writer restates the effect in the marked places. `check` fails on a changed generated
block, a mark left, or a number in the written parts that is not in the game text of that
Psychube (any language, any Amplification).
"""
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamedata as g  # noqa: E402
import scaffold as s  # noqa: E402

LAST_VERIFIED = '2026-11-23'
LANGS = ['en', 'zh-tw', 'ja', 'ko']
GLK = {'en': 'en', 'zh-tw': 'zh-TW', 'ja': 'ja', 'ko': 'ko'}
# Names that no global client has yet: English from the mainland client's name_en field, Traditional
# Chinese from the Simplified name with OpenCC s2tw, Japanese and Korean translated by us.
UNOFFICIAL = {
	1451: {'zh-tw': '當下之喜', 'ja': '今この時の喜び', 'ko': '지금 이 순간의 기쁨'},
	1452: {'zh-tw': '完滿之路', 'ja': '完全への道', 'ko': '완벽으로 가는 길'},
	1577: {'zh-tw': '立於風暴脊', 'ja': '嵐の稜線に立つ', 'ko': '폭풍의 능선에 서서'},
	1578: {'zh-tw': '宿命之向背', 'ja': '宿命に背いて', 'ko': '운명을 거슬러'},
	1579: {'zh-tw': '靈知當齊一', 'ja': '霊知は等しく巡る', 'ko': '영지는 하나로'},
	1580: {'zh-tw': '純潔的棺床', 'ja': '純潔なる棺', 'ko': '순결한 관'},
}
# Extra stat field of equip_break_attr.json -> attrType of character_attribute.json
STAT = {'attack': 'attack', 'hp': 'hp', 'def': 'defense', 'mdef': 'mdefense', 'cri': 'cri', 'criDmg': 'criDmg',
	'addDmg': 'addDmg', 'normalSkillRate': 'normalSkillRate', 'clutch': 'clutch', 'heal': 'heal', 'dropDmg': 'dropDmg',
	'revive': 'revive'}
BASE = [('hp', 'hp'), ('atk', 'attack'), ('def', 'defense'), ('mdef', 'mdefense')]
# The Psychube's illustration from Fandom (pipeline/fetch_art.py --psychubes); a Psychube with no file there has none.
_ART = Path(__file__).resolve().parent.parent / 'records' / 'art-psychubes.json'
ART = json.loads(_ART.read_text()) if _ART.exists() else {}
ALT = {'en': '{n}, Psychube art', 'zh-tw': '{n}心相插圖', 'ja': '{n}の心相イラスト', 'ko': '{n} 의지 일러스트'}

L = {
	'en': dict(
		dir='', head=('Field', 'Value'), stars='{n} stars', tagsep=', ', sep=', ',
		rows=dict(rarity='Rarity', tags='Tags', skill='Effect name', level='Max level', at='{s} at max level',
			extra='Extra stat at max level', rec='Recommended in game for', gl='Global client'),
		yes='yes', notyet='not yet, mainland China client only', none='—',
		sec=dict(effect='Effect', names='Names'),
		names=('English', 'Simplified Chinese', 'Traditional Chinese', 'Japanese', 'Korean'),
		unofficial='{n} (not yet official)', nonename='not yet official',
		index=dict(
			titles={'critical': 'Critical Psychubes', 'damage-6': '6-star damage Psychubes', 'damage-5': '5-star damage Psychubes', 'might': 'Might Psychubes', 'survival': 'Survival and healing Psychubes'},
			desc={'critical': 'Reverse: 1999 Psychubes that add Critical Rate or Critical DMG: extra stat and recommended arcanists.',
				'might': 'Reverse: 1999 Psychubes that add Incantation Might or Ultimate Might: extra stat and recommended arcanists.',
				'damage-6': 'Reverse: 1999 6-star Psychubes that add ATK or DMG Bonus: extra stat and recommended arcanists.',
				'damage-5': 'Reverse: 1999 5-star Psychubes that add ATK or DMG Bonus: extra stat and recommended arcanists.',
				'survival': 'Reverse: 1999 Psychubes that add HP, healing or defense: extra stat and recommended arcanists.'},
			caveat='The extra stat is the value at max level; a Psychube whose name says not yet official is in the mainland China client only.',
			cols=('Psychube', 'Rarity', 'Extra stat', 'Recommended in game for')),
		src=lambda: [(f're1999-data, mainland client {s.CN["build"]}: equip.json, equip_skill.json, equip_strengthen.json, equip_break_attr.json, character_recommend.json', s.CN_TREE),
			(f're1999-data-global, global client {s.GL["build"]}: equip.json and equip_skill.json', s.GL_TREE),
			(f're1999-data-global, global client {s.GL["build"]}: English text', s.GL_EN)],
	),
	'zh-tw': dict(
		dir='zh-tw/', head=('項目', '內容'), stars='{n} 星', tagsep='、', sep='、',
		rows=dict(rarity='稀有度', tags='標籤', skill='效果名稱', level='等級上限', at='滿級{s}',
			extra='滿級附加屬性', rec='遊戲內推薦的神秘學家', gl='國際版用戶端'),
		yes='有', notyet='尚未收錄，僅中國大陸版用戶端', none='—',
		sec=dict(effect='效果', names='名稱'),
		names=('英文', '簡體中文', '繁體中文', '日文', '韓文'),
		unofficial='{n}（非官方）', nonename='尚無官方譯名',
		index=dict(
			titles={'critical': '暴擊心相', 'damage-6': '6 星輸出心相', 'damage-5': '5 星輸出心相', 'might': '威力心相', 'survival': '生存與治療心相'},
			desc={'critical': '重返未來：1999 附加暴擊率或暴擊創傷的心相：附加屬性與遊戲推薦的神秘學家。',
				'might': '重返未來：1999 附加術法威力或儀式威力的心相：附加屬性與遊戲推薦的神秘學家。',
				'damage-6': '重返未來：1999 附加攻擊或創傷加成的 6 星心相：附加屬性與遊戲推薦的神秘學家。',
				'damage-5': '重返未來：1999 附加攻擊或創傷加成的 5 星心相：附加屬性與遊戲推薦的神秘學家。',
				'survival': '重返未來：1999 附加生命、治療或防禦的心相：附加屬性與遊戲推薦的神秘學家。'},
			caveat='附加屬性為滿級數值；名稱標示非官方的心相只收錄在中國大陸版用戶端。',
			cols=('心相', '稀有度', '附加屬性', '遊戲內推薦')),
		src=lambda: [(f're1999-data，中國大陸版用戶端 {s.CN["build"]}：equip.json、equip_skill.json、equip_strengthen.json、equip_break_attr.json、character_recommend.json', s.CN_TREE),
			(f're1999-data-global，國際版用戶端 {s.GL["build"]}：equip.json 與 equip_skill.json', s.GL_TREE),
			(f're1999-data-global，國際版用戶端 {s.GL["build"]}：英文文字', s.GL_EN)],
	),
	'ja': dict(
		dir='ja/', head=('項目', '内容'), stars='★{n}', tagsep='、', sep='、',
		rows=dict(rarity='レア度', tags='タグ', skill='効果名', level='最大レベル', at='最大レベルの{s}',
			extra='最大レベルの追加ステータス', rec='ゲーム内のおすすめ神秘学家', gl='グローバル版クライアント'),
		yes='収録', notyet='未収録、中国本土版クライアントのみ', none='—',
		sec=dict(effect='効果', names='名前'),
		names=('英語', '簡体字中国語', '繁体字中国語', '日本語', '韓国語'),
		unofficial='{n}（非公式）', nonename='公式名なし',
		index=dict(
			titles={'critical': 'クリティカルの心相', 'damage-6': '★6の攻撃心相', 'damage-5': '★5の攻撃心相', 'might': '威力の心相', 'survival': '生存と回復の心相'},
			desc={'critical': 'リバース：1999 のクリティカル率かクリティカルダメージを上げる心相：追加ステータスとゲームのおすすめ。',
				'might': 'リバース：1999 のスペル威力かアルティメット威力を上げる心相：追加ステータスとゲームのおすすめ。',
				'damage-6': 'リバース：1999 の攻撃力かダメージボーナスを上げる★6の心相：追加ステータスとゲームのおすすめ。',
				'damage-5': 'リバース：1999 の攻撃力かダメージボーナスを上げる★5の心相：追加ステータスとゲームのおすすめ。',
				'survival': 'リバース：1999 のHP、回復、防御を上げる心相：追加ステータスとゲームのおすすめ。'},
			caveat='追加ステータスは最大レベルの値。名前に非公式とある心相は中国本土版クライアントにのみ収録されている。',
			cols=('心相', 'レア度', '追加ステータス', 'ゲーム内のおすすめ')),
		src=lambda: [(f're1999-data、中国本土版クライアント {s.CN["build"]}：equip.json、equip_skill.json、equip_strengthen.json、equip_break_attr.json、character_recommend.json', s.CN_TREE),
			(f're1999-data-global、グローバル版クライアント {s.GL["build"]}：equip.json と equip_skill.json', s.GL_TREE),
			(f're1999-data-global、グローバル版クライアント {s.GL["build"]}：英語テキスト', s.GL_EN)],
	),
	'ko': dict(
		dir='ko/', head=('항목', '내용'), stars='{n}성', tagsep=', ', sep=', ',
		rows=dict(rarity='희귀도', tags='태그', skill='효과 이름', level='최대 레벨', at='최대 레벨 {s}',
			extra='최대 레벨 추가 스탯', rec='게임 내 추천 마도학자', gl='글로벌 클라이언트'),
		yes='있음', notyet='없음, 중국 본토 클라이언트만', none='—',
		sec=dict(effect='효과', names='이름'),
		names=('영어', '간체 중국어', '번체 중국어', '일본어', '한국어'),
		unofficial='{n} (비공식)', nonename='공식 명칭 없음',
		index=dict(
			titles={'critical': '치명타 의지', 'damage-6': '6성 공격 의지', 'damage-5': '5성 공격 의지', 'might': '위력 의지', 'survival': '생존과 치료 의지'},
			desc={'critical': '리버스: 1999 치명타율이나 치명타 피해를 올리는 의지: 추가 스탯과 게임 추천 마도학자.',
				'might': '리버스: 1999 마법 위력이나 최종 술식 위력을 올리는 의지: 추가 스탯과 게임 추천 마도학자.',
				'damage-6': '리버스: 1999 공격이나 피해 보너스를 올리는 6성 의지: 추가 스탯과 게임 추천 마도학자.',
				'damage-5': '리버스: 1999 공격이나 피해 보너스를 올리는 5성 의지: 추가 스탯과 게임 추천 마도학자.',
				'survival': '리버스: 1999 HP, 치료, 방어를 올리는 의지: 추가 스탯과 게임 추천 마도학자.'},
			caveat='추가 스탯은 최대 레벨의 값이다. 이름에 비공식이라고 적힌 의지는 중국 본토 클라이언트에만 있다.',
			cols=('의지', '희귀도', '추가 스탯', '게임 내 추천')),
		src=lambda: [(f're1999-data, 중국 본토 클라이언트 {s.CN["build"]}: equip.json, equip_skill.json, equip_strengthen.json, equip_break_attr.json, character_recommend.json', s.CN_TREE),
			(f're1999-data-global, 글로벌 클라이언트 {s.GL["build"]}: equip.json과 equip_skill.json', s.GL_TREE),
			(f're1999-data-global, 글로벌 클라이언트 {s.GL["build"]}: 영어 텍스트', s.GL_EN)],
	),
}


def slugify(name):
	return re.sub(r'[^a-z0-9]+', '-', name.lower().replace("'", '').replace('’', '')).strip('-')


def _attr_name(attr_type, lang):
	"""Official stat name: global client by language, mainland text for zh-CN."""
	row = next(r for r in g.cn('character_attribute') if r['attrType'] == attr_type)
	if lang == 'zh-CN':
		return row['name']
	return g.gl_text('character_attribute', row['id'], 'name', GLK.get(lang, lang))


def records():
	"""Every Psychube as a dict, by slug, in the order of the game's id."""
	skills = collections.defaultdict(dict)
	for r in g.cn('equip_skill'):
		skills[r['id']][r['skillLv']] = r
	gl_skills = collections.defaultdict(dict)
	for r in g.gl('equip_skill'):
		gl_skills[r['id']][r['skillLv']] = r
	rec_by = collections.defaultdict(list)
	heroes = {a['id']: a for a in s.REC.values()}
	for r in g.cn('character_recommend'):
		if r['id'] in heroes and r.get('equipRec'):
			for e in re.split(r'[|#]', r['equipRec']):
				if e and heroes[r['id']]['slug'] not in rec_by[int(e)]:
					rec_by[int(e)].append(heroes[r['id']]['slug'])
	tags = {r['id']: r for r in g.cn('equip_tag')}
	out = {}
	for e in g.cn('equip'):
		if e['isExpEquip'] or len(skills.get(e['id'], {})) != 5 or e['id'] >= 10000:
			continue
		rare = e['rare']
		max_level = max(r['level'] for r in g.cn('equip_break_cost') if r['rare'] == rare)
		rate = next(r['attributeRate'] for r in g.cn('equip_strengthen_cost') if r['rare'] == rare and r['level'] == max_level)
		base = next(r for r in g.cn('equip_strengthen') if r['strengthType'] == e['strengthType'])
		brk = max((r for r in g.cn('equip_break_attr') if r['id'] == e['id']), key=lambda r: r['breakLevel'])
		extra = [(k, v) for k, v in brk.items() if k in STAT and v]
		ge = g.gl_row('equip', e['id'])
		names = {'en': e['name_en'], 'zh-CN': e['name']}
		skill = {'zh-CN': e['skillName']}
		for lang in ('en', 'ja', 'ko', 'zh-TW'):
			if ge:
				names[lang] = g.text(ge['name'], lang) or names.get(lang, '')
				skill[lang] = g.text(ge['skillName'], lang) if ge.get('skillName') else ''
		text = {'zh-CN': [g.clean(skills[e['id']][lv]['baseDesc']) for lv in range(1, 6)]}
		if ge:
			for lang in ('en', 'ja', 'ko', 'zh-TW'):
				text[lang] = [g.text(gl_skills[e['id']][lv]['baseDesc'], lang) for lv in range(1, 6)]
		slug = slugify(names['en'])  # the global client's English name where it has one
		out[slug] = {
			'id': e['id'], 'slug': slug, 'stars': rare + 1, 'inGlobal': bool(ge), 'names': names, 'skill': skill,
			'tags': [tags[int(t)] for t in e['tag'].split('#') if t],
			'maxLevel': max_level, 'stats': {f: round(base[f] * rate / 1000) for f, _ in BASE},
			'extra': [(STAT[k], v / 10) for k, v in extra], 'recommended': rec_by.get(e['id'], []), 'text': text,
		}
	return out


REC = records()


def name(p, lang):
	key = GLK[lang]
	if p['inGlobal'] and p['names'].get(key):
		return p['names'][key]
	if lang == 'en':
		return p['names']['en']
	return UNOFFICIAL[p['id']][lang]


def fmt(x):
	return f'{x:g}%'


def blocks(slug, lang):
	p, t = REC[slug], L[lang]
	title = name(p, lang)
	out = {}
	all_names = [name(p, 'en'), name(p, 'zh-tw'), p['names']['zh-CN'], name(p, 'ja'), name(p, 'ko')]
	aliases = []
	for n in all_names:
		if n != title and n not in aliases:
			aliases.append(n)
	out['title'] = f'title: "{title}"'
	out['appliesTo'] = f'appliesTo: "{s.L[lang]["applies_gl"] if p["inGlobal"] else s.L[lang]["applies_cn"]}"'
	out['lastVerified'] = f'lastVerified: {LAST_VERIFIED}'
	out['aliases'] = 'aliases:\n' + '\n'.join(f'  - "{n}"' for n in aliases) if aliases else ''
	out['sources'] = 'sources:\n' + '\n'.join(f'  - title: "{x}"\n    url: {u}' for x, u in t['src']())
	if slug in ART:
		f, c = ART[slug], s.L[lang]['art']
		out['art'] = (f'art:\n  - title: "{c[0].format(f=f["file"])}"\n    url: {f["page"]}\n'
			f'  - title: "{c[1].format(d=f["uploaded"])}"\n    url: {f["url"]}')
		out['art line'] = f'![{ALT[lang].format(n=title)}](/art/psychubes/{slug}.webp)'
	tagnames = [g.gl_text('equip_tag', tg['id'], 'name', GLK[lang]) or tg['name'] for tg in p['tags']]
	rows = [(t['rows']['rarity'], t['stars'].format(n=p['stars']))]
	if tagnames:
		rows.append((t['rows']['tags'], t['tagsep'].join(tagnames)))
	sk = p['skill'].get(GLK[lang]) if p['inGlobal'] else ''
	if sk:
		rows.append((t['rows']['skill'], sk))
	rows.append((t['rows']['level'], str(p['maxLevel'])))
	for k, attr in BASE:
		rows.append((t['rows']['at'].format(s=_attr_name(attr, lang)), f'{p["stats"][k]:,}'))
	for attr, v in p['extra']:
		rows.append((t['rows']['extra'], f'{_attr_name(attr, lang)} +{fmt(v)}'))
	who = sorted((s.REC[x] for x in p['recommended']), key=lambda a: s.name(a, 'en').lower())
	if who:
		rows.append((t['rows']['rec'], t['sep'].join(f'[{s.name(a, lang)}](/{t["dir"]}arcanists/{a["slug"]}/)'
			if (s.DOCS / 'arcanists' / f'{a["slug"]}.md').exists() else s.name(a, lang) for a in who)))
	rows.append((t['rows']['gl'], t['yes'] if p['inGlobal'] else t['notyet']))
	out['profile'] = '\n'.join([f'| {t["head"][0]} | {t["head"][1]} |', '| --- | --- |'] + [f'| {k} | {v} |' for k, v in rows])

	def cell(lang2):
		key2 = GLK[lang2]
		if p['inGlobal'] and p['names'].get(key2):
			return p['names'][key2]
		if lang == 'en' and lang2 != 'zh-tw':
			return t['nonename']
		return t['unofficial'].format(n=name(p, lang2))
	en = p['names']['en'] if p['inGlobal'] else t['unofficial'].format(n=p['names']['en'])
	row = [en, p['names']['zh-CN'], cell('zh-tw'), cell('ja'), cell('ko')]
	out['names'] = '\n'.join([f'| {" | ".join(t["names"])} |', '| --- | --- | --- | --- | --- |', f'| {" | ".join(row)} |'])
	return out


def skeleton(slug, lang):
	b, t = blocks(slug, lang), L[lang]
	fm = ['---', b['title'], 'description: "<!-- WRITE: one sentence, what the Psychube is and does -->"', b['appliesTo'],
		'caveat: "<!-- WRITE: the one qualifier a reader most likely misses -->"', b['lastVerified']]
	fm += ([b['aliases']] if b['aliases'] else []) + ([b['art']] if 'art' in b else []) + [b['sources'], '---', '']
	body = ([b['art line'], ''] if 'art line' in b else []) + [b['profile'], '', f'## {t["sec"]["effect"]}', '',
		'<!-- WRITE: the effect in our words, every value that changes given for Amplification 1 to 5 as 16/20/24/28/32% -->', '',
		f'## {t["sec"]["names"]}', '', b['names'], '']
	return '\n'.join(fm + body)


GENERATED = ('profile', 'names')


def source_numbers(p):
	return s.numbers(json.dumps(p['text'], ensure_ascii=False))


def check(path):
	path = Path(path).resolve()
	rel = path.relative_to(s.DOCS).as_posix()
	m = re.match(r'(?:(zh-tw|ja|ko)/)?psychubes/([^/]+)\.md$', rel)
	if not m or m.group(2) not in REC:
		return [f'{rel}: not a Psychube page in en, zh-tw, ja or ko']
	lang, slug = m.group(1) or 'en', m.group(2)
	text = path.read_text()
	errors = []
	b = blocks(slug, lang)
	for k, v in b.items():
		if v not in text:
			errors.append(f'{rel}: {k} differs from the records:\n{v}')
	for mark in re.findall(r'<!-- WRITE[^>]*-->|TODO', text):
		errors.append(f'{rel}: unwritten: {mark}')
	allowed = source_numbers(REC[slug]) | {str(i) for i in range(11)} | {s.CN_VER, s.GL_VER} | s.numbers(' '.join(b.values()))
	written = text
	for k in GENERATED:
		written = written.replace(b[k], '')
	written = re.sub(r'^sources:\n(?:  .*\n)+', '', written, flags=re.M)
	written = re.sub(r'^(?:appliesTo|lastVerified|title): .*\n', '', written, flags=re.M)
	for n in sorted(s.numbers(written) - allowed, key=float):
		line = next((x for x in written.split('\n') if re.search(rf'(?<![\d.]){re.escape(n)}(?![\d.])', x.replace(',', ''))), '')
		errors.append(f'{rel}: number {n} is not in the game text of {slug}: {line.strip()[:120]}')
	return errors


GROUPS = ['critical', 'damage-6', 'damage-5', 'might', 'survival']
CRIT = {'cri', 'criDmg'}
DAMAGE = {'attack', 'addDmg'}
MIGHT = {'clutch', 'normalSkillRate'}


def group(p):
	"""Index page of a Psychube, by the stat it adds: one index of every Psychube would pass the
	5,000 characters a fetch returns, and players look for Psychubes by that stat."""
	stat = p['extra'][0][0] if p['extra'] else ''
	if stat in CRIT:
		return 'critical'
	if stat in DAMAGE:
		return f'damage-{p["stars"]}'
	if stat in MIGHT:
		return 'might'
	return 'survival'


def index_page(lang, key):
	t, l = L[lang], L[lang]['index']
	members = sorted((p for p in REC.values() if group(p) == key), key=lambda p: (-p['stars'], name(p, 'en').lower()))
	rows = []
	for p in members:
		n = name(p, lang) if p['inGlobal'] else t['unofficial'].format(n=name(p, lang))
		if (s.DOCS / t['dir'] / 'psychubes' / f'{p["slug"]}.md').exists():
			n = f'[{n}](/{t["dir"]}psychubes/{p["slug"]}/)'
		extra = t['sep'].join(f'{_attr_name(a, lang)} +{fmt(v)}' for a, v in p['extra'])
		who = t['sep'].join(s.name(s.REC[x], lang) for x in sorted(p['recommended'], key=lambda x: s.name(s.REC[x], 'en').lower()))
		# One rarity per damage page: no rarity column there, which keeps every link within 5,000 characters.
		cells = [n] + ([] if key.startswith('damage') else [t['stars'].format(n=p['stars'])]) + [extra or t['none'], who or t['none']]
		rows.append('| ' + ' | '.join(cells) + ' |')
	others = [L[o]['index']['titles'][key] for o in LANGS if o != lang]
	others.append({'critical': '暴击心相', 'damage-6': '6 星输出心相', 'damage-5': '5 星输出心相', 'might': '威力心相', 'survival': '生存与治疗心相'}[key])
	others = [x for i, x in enumerate(others) if x != l['titles'][key] and x not in others[:i]]
	fm = ['---', f'title: "{l["titles"][key]}"', f'description: "{l["desc"][key]}"',
		f'appliesTo: "{s.L[lang]["applies_gl"]}"', f'caveat: "{l["caveat"]}"', f'lastVerified: {LAST_VERIFIED}',
		'aliases:\n' + '\n'.join(f'  - "{x}"' for x in others),
		'sources:\n' + '\n'.join(f'  - title: "{x}"\n    url: {u}' for x, u in t['src']()), '---', '']
	cols = [c for i, c in enumerate(l['cols']) if not (key.startswith('damage') and i == 1)]
	table = [f'| {" | ".join(cols)} |', '| ' + ' | '.join(['---'] * len(cols)) + ' |'] + rows
	return '\n'.join(fm + table) + '\n'


def main(argv):
	if argv[:1] == ['list']:
		for p in REC.values():
			print(p['slug'], p['stars'], p['id'], 'global' if p['inGlobal'] else 'mainland', p['names']['zh-CN'], '|', p['names']['en'])
		return 0
	if argv[:1] == ['text'] and len(argv) >= 2:
		p = REC[argv[1]]
		langs = argv[2:] or ['zh-CN', 'en']
		print(p['slug'], p['stars'], 'stars;', 'global' if p['inGlobal'] else 'mainland only', '; effect name:', p['skill'])
		for lang in langs:
			for i, x in enumerate(p['text'].get(lang, []), 1):
				print(f'[{lang} Amplification {i}] {x}')
		return 0
	if argv[:1] == ['write'] and len(argv) >= 3:
		lang = argv[1]
		slugs = list(REC) if argv[2:] == ['all'] else argv[2:]
		for slug in slugs:
			p = s.DOCS / L[lang]['dir'] / 'psychubes' / f'{slug}.md'
			p.parent.mkdir(parents=True, exist_ok=True)
			if p.exists():
				print(f'exists, left as it is: {p.relative_to(s.ROOT)}')
				continue
			p.write_text(skeleton(slug, lang))
		print(f'{len(slugs)} skeleton(s) considered')
		return 0
	if argv[:1] == ['check'] and len(argv) >= 2:
		errors = [e for x in argv[1:] for e in check(x)]
		for e in errors:
			print(e)
		print(f'{len(argv) - 1} page(s), {len(errors)} problem(s)')
		return 1 if errors else 0
	if argv[:1] == ['indexes']:
		# The list the sidebar reads (src/lib/sidebar.mjs): slug, rarity and English name, no game text.
		lst = [{'slug': p['slug'], 'id': p['id'], 'stars': p['stars'], 'group': group(p), 'inGlobal': p['inGlobal'], 'en': p['names']['en']} for p in REC.values()]
		(s.ROOT / 'records' / 'psychubes.json').write_text(json.dumps({'psychubes': lst}, ensure_ascii=False, indent='\t') + '\n')
		for lang in LANGS:
			d = s.DOCS / L[lang]['dir'] / 'psychubes'
			d.mkdir(parents=True, exist_ok=True)
			for key in GROUPS:
				(d / f'{key}.md').write_text(index_page(lang, key))
		print(f'{len(GROUPS) * len(LANGS)} index pages written')
		return 0
	if argv[:1] == ['art']:
		# Pages already written: the credits go before sources, the art line before the profile table.
		n = 0
		for lang in LANGS:
			for slug in REC:
				path = s.DOCS / L[lang]['dir'] / 'psychubes' / f'{slug}.md'
				b = blocks(slug, lang)
				if 'art' not in b or not path.exists():
					continue
				text = re.sub(r'^art:\n(?:  .*\n)+', '', path.read_text(), flags=re.M)
				text = re.sub(r'^!\[[^\]]*\]\(/art/psychubes/[^)]+\)\n\n', '', text, flags=re.M)
				text = text.replace(b['sources'], f'{b["art"]}\n{b["sources"]}', 1)
				text = text.replace(b['profile'], f'{b["art line"]}\n\n{b["profile"]}', 1)
				path.write_text(text)
				n += 1
		print(f'{n} page(s) given art')
		return 0
	print(__doc__)
	return 2


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
