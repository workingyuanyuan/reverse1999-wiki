"""Write the system pages that the records decide entirely, in every language but zh-cn.

  python3 -I pipeline/write_systems.py [lang ...]     (default: en zh-tw ja ko)

Writes src/content/docs/{,zh-tw/,ja/,ko/}systems/{releases,insight,statuses,resonance}.md (zh-cn: scripts/to-zh-cn.py).
Overwrites them; they are not edited by hand. Change the wording here.

releases: every arcanist's release date on the mainland and the global service (records/releases.json,
  read from the Fandom infobox), newest first, with the days between them.
insight: what each Insight gives and costs by rarity, from character_rank.json of the mainland client.
  Levels in that table run on across Insight stages (caps 30, 70, 120, 180): the cap of Insight n is the
  difference. Level costs (character_cosume.json) are left out: their rows do not line up one to one with
  the levels of a stage, and no second source gives the totals.
resonance: Resonance levels, grid, main Idea, materials and Resonance Patterns by rarity, from
  character_talent.json, talent_mould.json, talent_style.json, talent_style_cost.json and talent_cube_attr.json
  of the mainland client; every value is checked to agree within a rarity. What a pattern raises or lowers
  is the sign of the difference between its main Idea and Placidity's at the main Idea's top level; the
  values themselves are left out, as no second source gives their unit.
"""
import collections
import datetime as dt
import json
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gamedata as g  # noqa: E402
import scaffold as s  # noqa: E402
import write_indexes as wi  # noqa: E402

LAST_VERIFIED = '2026-11-23'
LANGS = ['en', 'zh-tw', 'ja', 'ko']
GLK = {'en': 'en', 'zh-tw': 'zh-TW', 'ja': 'ja', 'ko': 'ko'}
FANDOM_INSIGHT = 'https://reverse1999.fandom.com/wiki/Insight?oldid=20796'


# The heading of each page's first section: a page's body starts with a heading, not with a
# paragraph (root AGENTS.md, Visible page).
FIRST = {
	'releases': {'en': 'Days between the services', 'zh-tw': '兩版上線相隔天數', 'ja': '両版の実装の間隔', 'ko': '두 서비스 사이의 출시 간격'},
	'insight': {'en': 'How Insight works', 'zh-tw': '洞悉的作用', 'ja': '洞察の仕組み', 'ko': '통찰의 작동 방식'},
	'statuses': {'en': 'Kinds of status', 'zh-tw': '狀態的種類', 'ja': '状態の種類', 'ko': '상태의 종류'},
	'resonance': {'en': 'How Resonance works', 'zh-tw': '共鳴的作用', 'ja': '共鳴の仕組み', 'ko': '공명의 작동 방식'},
}


def fm(title, desc, applies, caveat, aliases, sources):
	aliases = [a for a in aliases if a != title]
	src = '\n'.join(f'  - title: "{t}"\n    url: {u}' for t, u in sources)
	return '\n'.join([
		'---', f'title: "{title}"', f'description: "{desc}"', f'appliesTo: "{applies}"', f'caveat: "{caveat}"',
		f'lastVerified: {LAST_VERIFIED}', 'aliases:\n' + '\n'.join(f'  - "{a}"' for a in aliases), 'sources:\n' + src, '---', ''])


def link(a, lang):
	n = s.name(a, lang)
	if (s.DOCS / 'arcanists' / f'{a["slug"]}.md').exists():
		return f'[{n}](/{s.L[lang]["dir"]}arcanists/{a["slug"]}/)'
	return n


def num(n):
	return f'{n:,}'


# ---------------------------------------------------------------- releases

# Title and aliases name the same set in every language (scripts/check-dist.mjs): the titles in the
# five languages and the same extra search words; each page drops its own title.
REL_ALIASES = ['Release dates', '上線日期', '上线日期', '実装日', '출시일', 'CN and global release dates', '國服 國際服 上線時間', '国服 国际服 上线时间', '중섭 글섭 출시']
INS_ALIASES = ['Insight and levels', '洞悉與等級', '洞悉与等级', '洞察とレベル', '통찰과 레벨', 'Insight materials', 'Level cap', 'Sharpodonty', '利齒子兒', '利齿子儿', '咬噛銭貨', '톱니 동전']

RT = {
	'en': dict(
		title='Release dates', desc='Most Reverse: 1999 arcanists reach the global service {lo2} to {hi} days after the mainland China service.',
		caveat='The global service has brought arcanists between {lo} and {hi} days after the mainland service; an arcanist out only on the mainland service has no global date until one is announced.',
		lead='Of the {n} arcanists out on both services, {same} came to the global service on the same day as the mainland service: {samelist}. The others came {lo2} to {hi} days later, {med} days at the median; for those released on the mainland since 2025-06-01, the median is {med2} days.',
		only='Out only on the mainland service', all='Release dates of every arcanist',
		cols=('Arcanist', 'Rarity', 'Mainland release', 'Global release', 'Days later'),
		src='Reverse: 1999 Wiki (Fandom): release dates in each arcanist\'s infobox, read 2026-11-22',
		aliases=REL_ALIASES),
	'zh-tw': dict(
		title='上線日期', desc='重返未來：1999 多數神秘學家在國際版上線的時間比中國大陸版晚 {lo2} 到 {hi} 天。',
		caveat='國際版的神秘學家比中國大陸版晚 {lo} 到 {hi} 天上線；只在中國大陸版推出的神秘學家，在公布之前沒有國際版日期。',
		lead='兩個版本都已上線的 {n} 位神秘學家中，有 {same} 位在國際版與中國大陸版同一天上線：{samelist}。其餘晚 {lo2} 到 {hi} 天，中位數 {med} 天；2025-06-01 以後在中國大陸版上線的，中位數 {med2} 天。',
		only='僅中國大陸版', all='全部神秘學家的上線日期',
		cols=('神秘學家', '稀有度', '中國大陸版上線', '國際版上線', '相隔天數'),
		src='Reverse: 1999 Wiki (Fandom)：各神秘學家資訊框的上線日期，2026-11-22 讀取',
		aliases=REL_ALIASES),
	'ja': dict(
		title='実装日', desc='リバース：1999 の神秘学家の多くは、中国本土版の{lo2}〜{hi}日後にグローバル版へ実装される。',
		caveat='グローバル版の実装は中国本土版の {lo} 日後から {hi} 日後まで。中国本土版にのみ実装された神秘学家には、発表されるまでグローバル版の日付がない。',
		lead='両方の版に実装された {n} 人の神秘学家のうち、{same} 人はグローバル版にも中国本土版と同じ日に実装された：{samelist}。ほかは {lo2} 日後から {hi} 日後で、中央値は {med} 日。2025-06-01 以降に中国本土版に実装された神秘学家では、中央値は {med2} 日。',
		only='中国本土版のみ', all='すべての神秘学家の実装日',
		cols=('神秘学家', 'レア度', '中国本土版の実装', 'グローバル版の実装', '日数'),
		src='Reverse: 1999 Wiki (Fandom)：各神秘学家のインフォボックスの実装日、2026-11-22 に読んだもの',
		aliases=REL_ALIASES),
	'ko': dict(
		title='출시일', desc='리버스: 1999 마도학자 대부분은 중국 본토보다 {lo2}~{hi}일 늦게 글로벌 서비스에 나온다.',
		caveat='글로벌 서비스의 출시는 중국 본토 서비스보다 {lo}일에서 {hi}일 늦었다. 중국 본토 서비스에만 나온 마도학자는 발표되기 전까지 글로벌 날짜가 없다.',
		lead='두 서비스에 모두 나온 마도학자 {n}명 중 {same}명은 글로벌 서비스에도 중국 본토와 같은 날 나왔다: {samelist}. 나머지는 {lo2}일에서 {hi}일 늦었고 중앙값은 {med}일이다. 2025-06-01 이후 중국 본토에 나온 마도학자의 중앙값은 {med2}일이다.',
		only='중국 본토 한정', all='모든 마도학자의 출시일',
		cols=('마도학자', '희귀도', '중국 본토 출시', '글로벌 출시', '일수'),
		src='Reverse: 1999 Wiki (Fandom): 각 마도학자 정보 상자의 출시일, 2026-11-22에 읽음',
		aliases=REL_ALIASES),
}


def releases(lang):
	t, l = RT[lang], s.L[lang]
	arc = [a for a in s.REC.values() if a['slug'] not in wi.SKIP]
	both = []
	for a in arc:
		r = s.REL.get(a['slug'], {})
		if a['inGlobal'] and r.get('cn') and r.get('global'):
			both.append(((dt.date.fromisoformat(r['global']) - dt.date.fromisoformat(r['cn'])).days, a))
	same = sorted((a for d, a in both if d == 0), key=lambda a: a['names']['en'])
	later = [d for d, _ in both if d > 0]
	recent = [d for d, a in both if s.REL[a['slug']]['cn'] >= '2025-06-01']
	sep = ', ' if lang in ('en', 'ko') else '、'
	lead = t['lead'].format(n=len(both), same=len(same), samelist=sep.join(link(a, lang) for a in same),
		lo2=min(later), hi=max(later), med=round(statistics.median(later)), med2=round(statistics.median(recent)))
	caveat = t['caveat'].format(lo=min(d for d, _ in both), hi=max(later))
	days = {a['slug']: d for d, a in both}

	def key(a):
		# Dated rows newest first, then rows with a version only, then rows with neither.
		r = s.REL.get(a['slug'], {})
		if r.get('cn'):
			return (0, ''.join(chr(0x10FFFF - ord(c)) for c in r['cn']), a['names']['en'])
		return (1 if a['slug'] in s.VERSION_ONLY else 2, '', a['names']['en'])
	rows = []
	for a in sorted(arc, key=key):
		mainland, glob = s.release(a, lang)
		d = days.get(a['slug'])
		rows.append(f'| {link(a, lang)} | {l["stars"].format(n=a["stars"])} | {mainland} | {glob} | {l["unknown"] if d is None else d} |')
	only, _ = wi.home(lang)
	head = '| ' + ' | '.join(t['cols']) + ' |\n| --- | --- | --- | --- | --- |'
	srcs = [(t['src'], 'https://reverse1999.fandom.com/'),
		(wi.T[lang]['src'][1][0].format(gl=s.GL['build']), s.GL_CHAR),
		(wi.T[lang]['src'][0][0].format(cn=s.CN['build']), s.CN_CHAR)]
	body = [f'## {FIRST["releases"][lang]}', '', lead, '', f'## {t["only"]}', '', only, '', f'## {t["all"]}', '', head] + rows
	return fm(t['title'], t['desc'].format(lo2=min(later), hi=max(later)), l['applies_gl'], caveat, t['aliases'], srcs) + '\n'.join(body) + '\n'


# ---------------------------------------------------------------- insight

IT = {
	'en': dict(
		title='Insight and levels', desc='Reverse: 1999 Insight: 5- and 6-star arcanists reach level 60 at Insight III, 2- to 4-star ones level 50.',
		caveat='Insight resets the arcanist to level 1 with a higher cap; 2-, 3- and 4-star arcanists stop at Insight II, level 50.',
		lead='Insight raises an arcanist\'s level cap once the arcanist reaches it. Each Insight costs {sharp} and materials that depend on the arcanist, and returns the arcanist to level 1 of the new cap.',
		caps='Level caps', capcols=('Rarity', 'Insight 0', 'Insight I', 'Insight II', 'Insight III'),
		cost='Cost of each Insight', costcols=('Rarity', 'Insight I', 'Insight II', 'Insight III'),
		costnote='Insight III also takes a Tome of the arcanist\'s Afflatus and higher-rarity materials.',
		gives='What each Insight unlocks',
		givesrows=[('Insight I', 'level cap {c1}; the first Inheritance passive'),
			('Insight II', 'level cap {c2}; the second Inheritance passive; for 4-star and higher arcanists, a garment (all but Sonetto)'),
			('Insight III', 'level cap {c3}; the third Inheritance passive (5 and 6 stars only); opens Euphoria for arcanists that have it')],
		givescols=('Insight', 'Unlocks'),
		eup='Euphoria opens at Insight III level 30 for a 6-star arcanist and at Insight III level 1 for a 5-star.',
		por='Portrait', porline='A duplicate of an arcanist raises its Portrait by one level, up to Portrait 5; each level changes one skill.',
		level='level {n}', none='—', stars='{n} stars', stars23='2 and 3 stars',
		src=[('re1999-data, mainland client {cn}: character_rank.json', 'character_rank'),
			('re1999-data-global, global client {gl}: character_rank.json and the names of materials', 'gl'),
			('Reverse: 1999 Wiki (Fandom), Insight, revision 20796', FANDOM_INSIGHT)],
		aliases=INS_ALIASES),
	'zh-tw': dict(
		title='洞悉與等級', desc='重返未來：1999 的洞悉：5、6 星神秘學家在洞悉三達到 60 級，2 至 4 星最高 50 級。',
		caveat='洞悉後神秘學家回到 1 級、上限提高；2、3、4 星神秘學家最高到洞悉二 50 級。',
		lead='神秘學家達到等級上限後，洞悉可以提高上限。每次洞悉消耗{sharp}與因神秘學家而異的材料，洞悉後回到新上限的 1 級。',
		caps='等級上限', capcols=('稀有度', '洞悉零', '洞悉一', '洞悉二', '洞悉三'),
		cost='每次洞悉的消耗', costcols=('稀有度', '洞悉一', '洞悉二', '洞悉三'),
		costnote='洞悉三另需該神秘學家靈感的典籍與更高稀有度的材料。',
		gives='每階洞悉解鎖的內容',
		givesrows=[('洞悉一', '等級上限 {c1}；第一個傳承被動'),
			('洞悉二', '等級上限 {c2}；第二個傳承被動；4 星以上的神秘學家另得一套服裝（十四行詩除外）'),
			('洞悉三', '等級上限 {c3}；第三個傳承被動（僅 5、6 星）；擁有狂想的神秘學家開放狂想')],
		givescols=('洞悉', '解鎖'),
		eup='6 星神秘學家在洞悉三 30 級開放狂想，5 星神秘學家在洞悉三 1 級開放。',
		por='塑造', porline='重複獲得同一位神秘學家，塑造提升一級，最高塑造五；每一級改變一個技能。',
		level='{n} 級', none='—', stars='{n} 星', stars23='2 星與 3 星',
		src=[('re1999-data，中國大陸版用戶端 {cn}：character_rank.json', 'character_rank'),
			('re1999-data-global，國際版用戶端 {gl}：character_rank.json 與材料名稱', 'gl'),
			('Reverse: 1999 Wiki (Fandom)，Insight，修訂版 20796', FANDOM_INSIGHT)],
		aliases=INS_ALIASES),
	'ja': dict(
		title='洞察とレベル', desc='リバース：1999 の洞察：★5・★6は洞察3でレベル60、★2〜★4はレベル50まで。',
		caveat='洞察するとレベル1に戻り、上限が上がる。★2、★3、★4の神秘学家は洞察2のレベル50が最大。',
		lead='神秘学家が今のレベル上限に達すると、洞察で上限を上げられる。洞察のたびに{sharp}と神秘学家ごとに異なる素材を消費し、新しい上限のレベル1に戻る。',
		caps='レベル上限', capcols=('レア度', '洞察0', '洞察1', '洞察2', '洞察3'),
		cost='洞察ごとの消費', costcols=('レア度', '洞察1', '洞察2', '洞察3'),
		costnote='洞察3ではその神秘学家の本源の典籍と、より高いレア度の素材も必要。',
		gives='洞察ごとに解放されるもの',
		givesrows=[('洞察1', 'レベル上限 {c1}、1つ目の伝承パッシブ'),
			('洞察2', 'レベル上限 {c2}、2つ目の伝承パッシブ、★4以上の神秘学家は衣装（ソネット以外）'),
			('洞察3', 'レベル上限 {c3}、3つ目の伝承パッシブ（★5と★6のみ）、狂想を持つ神秘学家は狂想が開放')],
		givescols=('洞察', '解放'),
		eup='狂想は★6の神秘学家では洞察3のレベル30、★5では洞察3のレベル1で開放される。',
		por='塑造', porline='同じ神秘学家を重ねて入手すると塑造が1段階上がり、塑造5が最大。各段階で1つのスキルが変わる。',
		level='レベル{n}', none='—', stars='★{n}', stars23='★2と★3',
		src=[('re1999-data、中国本土版クライアント {cn}：character_rank.json', 'character_rank'),
			('re1999-data-global、グローバル版クライアント {gl}：character_rank.json と素材名', 'gl'),
			('Reverse: 1999 Wiki (Fandom)、Insight、版 20796', FANDOM_INSIGHT)],
		aliases=INS_ALIASES),
	'ko': dict(
		title='통찰과 레벨', desc='리버스: 1999 통찰: 5·6성은 통찰 3에서 레벨 60, 2~4성은 레벨 50까지다.',
		caveat='통찰하면 마도학자는 레벨 1로 돌아가고 상한이 오른다. 2, 3, 4성 마도학자는 통찰 2 레벨 50이 최대다.',
		lead='마도학자가 레벨 상한에 이르면 통찰로 상한을 올릴 수 있다. 통찰할 때마다 {sharp}과 마도학자마다 다른 재료가 들고, 새 상한의 레벨 1로 돌아간다.',
		caps='레벨 상한', capcols=('희귀도', '통찰 0', '통찰 1', '통찰 2', '통찰 3'),
		cost='통찰별 소모', costcols=('희귀도', '통찰 1', '통찰 2', '통찰 3'),
		costnote='통찰 3에는 그 마도학자 영감의 서적과 더 높은 희귀도의 재료도 든다.',
		gives='통찰마다 해금되는 것',
		givesrows=[('통찰 1', '레벨 상한 {c1}, 첫 번째 계승 패시브'),
			('통찰 2', '레벨 상한 {c2}, 두 번째 계승 패시브, 4성 이상 마도학자는 의상(소네트 제외)'),
			('통찰 3', '레벨 상한 {c3}, 세 번째 계승 패시브(5성과 6성만), 광상이 있는 마도학자는 광상 개방')],
		givescols=('통찰', '해금'),
		eup='광상은 6성 마도학자는 통찰 3 레벨 30, 5성은 통찰 3 레벨 1에 열린다.',
		por='형상', porline='같은 마도학자를 중복으로 얻으면 형상이 한 단계 오르고 형상 5가 최대다. 단계마다 스킬 하나가 바뀐다.',
		level='레벨 {n}', none='—', stars='{n}성', stars23='2성과 3성',
		src=[('re1999-data, 중국 본토 클라이언트 {cn}: character_rank.json', 'character_rank'),
			('re1999-data-global, 글로벌 클라이언트 {gl}: character_rank.json과 재료 이름', 'gl'),
			('Reverse: 1999 Wiki (Fandom), Insight, 판 20796', FANDOM_INSIGHT)],
		aliases=INS_ALIASES),
}


def insight_data():
	"""{stars: {'caps': [cap per Insight stage], 'sharp': [Sharpodonty per Insight]}}, checked to agree within a rarity."""
	rec = {a['id']: a for a in s.REC.values() if a['slug'] not in wi.SKIP}
	per = collections.defaultdict(lambda: collections.defaultdict(set))
	for r in g.cn('character_rank'):
		a = rec.get(r['heroId'])
		if not a:
			continue
		cap = int(next(p for p in r['effect'].split('|') if p.startswith('1#')).split('#')[1])
		per[a['stars']][('cap', r['rank'])].add(cap)
		for p in filter(None, r['consume'].split('|')):
			kind, item, n = p.split('#')
			if kind == '2' and item == '3':
				per[a['stars']][('sharp', r['rank'])].add(int(n))
	out = {}
	for stars, d in per.items():
		for k, v in d.items():
			if len(v) != 1:
				sys.exit(f'{stars} stars, {k}: values differ between arcanists: {sorted(v)}')
		ranks = sorted(r for kind, r in d if kind == 'cap')
		cum = [next(iter(d[('cap', r)])) for r in ranks]
		out[stars] = {'caps': [c - p for c, p in zip(cum, [0] + cum[:-1])],
			'sharp': [next(iter(d[('sharp', r)])) for r in ranks[1:]]}
	return out


def insight(lang):
	t, l = IT[lang], s.L[lang]
	data = insight_data()
	sharp_name = g.gl_text('currency', 3, 'name', GLK[lang])
	groups = [('6', [6]), ('5', [5]), ('4', [4]), ('23', [3, 2])]
	for _, members in groups:
		if len({str(data[m]) for m in members}) != 1:
			sys.exit(f'rarities {members} differ')

	def label(k):
		return t['stars23'] if k == '23' else t['stars'].format(n=int(k))
	cap_rows, cost_rows = [], []
	for k, members in groups:
		d = data[members[0]]
		caps = [t['level'].format(n=c) for c in d['caps']] + [t['none']] * (4 - len(d['caps']))
		cost = [f'{num(x)} {sharp_name}' for x in d['sharp']] + [t['none']] * (3 - len(d['sharp']))
		cap_rows.append(f'| {label(k)} | ' + ' | '.join(caps) + ' |')
		cost_rows.append(f'| {label(k)} | ' + ' | '.join(cost) + ' |')
	c = data[6]['caps']
	gives = [f'| {n} | {x.format(c1=c[1], c2=c[2], c3=c[3])} |' for n, x in t['givesrows']]
	srcs = []
	for title, u in t['src']:
		title = title.format(cn=s.CN['build'], gl=s.GL['build'])
		srcs.append((title, g.CN_JSON + 'character_rank.json' if u == 'character_rank' else g.GL_JSON + 'character_rank.json' if u == 'gl' else u))
	body = [f'## {FIRST["insight"][lang]}', '', t['lead'].format(sharp=sharp_name), '',
		f'## {t["caps"]}', '', '| ' + ' | '.join(t['capcols']) + ' |', '| --- | --- | --- | --- | --- |'] + cap_rows + [
		'', f'## {t["cost"]}', '', '| ' + ' | '.join(t['costcols']) + ' |', '| --- | --- | --- | --- |'] + cost_rows + [
		'', t['costnote'], '', f'## {t["gives"]}', '', '| ' + ' | '.join(t['givescols']) + ' |', '| --- | --- |'] + gives + [
		'', t['eup'], '', f'## {t["por"]}', '', t['porline']]
	text = fm(t['title'], t['desc'], l['applies_gl'], t['caveat'], t['aliases'], srcs) + '\n'.join(body) + '\n'
	return text


# ---------------------------------------------------------------- statuses

ST = json.loads((s.ROOT / 'records' / 'statuses.json').read_text())
MARK = {'en': '{n} (not yet official)', 'zh-tw': '{n}（非官方）', 'ja': '{n}（非公式）', 'ko': '{n} (비공식)'}
ST_SRC = {
	'en': [('re1999-data, mainland client {cn}: skill_eff_desc.json (statuses) and the skill text of every arcanist', 'cn'),
		('re1999-data-global, global client {gl}: skill_eff_desc.json and its text in each language', 'gl'),
		('re1999-data-global, global client {gl}: loading_text.json (Field Manual tips)', 'tips')],
	'zh-tw': [('re1999-data，中國大陸版用戶端 {cn}：skill_eff_desc.json（狀態）與每位神秘學家的技能文字', 'cn'),
		('re1999-data-global，國際版用戶端 {gl}：skill_eff_desc.json 與各語言文字', 'gl'),
		('re1999-data-global，國際版用戶端 {gl}：loading_text.json（作戰手冊提示）', 'tips')],
	'ja': [('re1999-data、中国本土版クライアント {cn}：skill_eff_desc.json（状態）と全神秘学家のスキルテキスト', 'cn'),
		('re1999-data-global、グローバル版クライアント {gl}：skill_eff_desc.json と各言語のテキスト', 'gl'),
		('re1999-data-global、グローバル版クライアント {gl}：loading_text.json（作戦マニュアルのヒント）', 'tips')],
	'ko': [('re1999-data, 중국 본토 클라이언트 {cn}: skill_eff_desc.json(상태)과 모든 마도학자의 스킬 텍스트', 'cn'),
		('re1999-data-global, 글로벌 클라이언트 {gl}: skill_eff_desc.json과 언어별 텍스트', 'gl'),
		('re1999-data-global, 글로벌 클라이언트 {gl}: loading_text.json(작전 매뉴얼 팁)', 'tips')],
}


def _strings(x):
	if isinstance(x, dict):
		for k, v in x.items():
			if k == 'desc' and isinstance(v, str):
				yield v
			elif k != 'statuses':
				yield from _strings(v)
	elif isinstance(x, list):
		for v in x:
			yield from _strings(v)


def mentions():
	"""Status name (mainland text) -> slugs of the arcanists whose own kit text names it in brackets.
	Terms named only inside another status's description do not count."""
	out = collections.defaultdict(set)
	for f in (s.ROOT / 'cache' / 'source').glob('*.json'):
		d = json.loads(f.read_text())
		if d['slug'] in wi.SKIP or d['slug'] not in s.REC:
			continue
		for t in _strings({k: v for k, v in d['zh-CN'].items() if k != 'statuses'}):
			for a, b in re.findall(r'【([^】]+)】|\[([^\]]+)\]', t):
				out[a or b].add(d['slug'])
	return out


# A status the global client has no text for (a mainland-only one): what its effect cell says.
NO_GL_TEXT = {'en': 'Not in the global client yet', 'zh-tw': '國際版尚無此狀態', 'ja': 'グローバル版には未実装', 'ko': '글로벌 클라이언트에는 아직 없음'}


def status_desc(row, lang):
	"""The game's own description of a status, as one table cell: the global client's text in that
	language, the mainland client's on zh-cn pages. A line break of the client is <br>; the term ids
	after a bracketed name (<id:N>) and the highlight marks ({...}) are not shown."""
	import profile as pf
	if lang == 'zh-cn':
		raw = g.cn_row('skill_eff_desc', row['id'])['desc']
	else:
		r = g.gl_row('skill_eff_desc', row['id'])
		raw = g._lang(g.LANG_FILE[GLK[lang]]).get(r['desc'], '') if r and r.get('desc') else ''
	if not (raw or '').strip():
		return NO_GL_TEXT[lang]
	x = re.sub(r'\{([^{}]*)\}', r'\1', re.sub(r'<id:\d+>', '', raw.replace('\r', '')))
	if re.search(r'▩|%s|[{}]', x):
		raise SystemExit(f'status {row["id"]} {lang}: unresolved mark in {x[:80]!r}')
	return '<br>'.join(pf.inline(y).replace('|', '\\|') for y in x.split('\n') if y.strip())


def zh_cn_statuses(text):
	"""The zh-cn Statuses page, converted from zh-tw by scripts/to-zh-cn.py, with each row's name and
	effect cells taken from the mainland client: the rows come in the order of records/statuses.json."""
	rows = [r for sec in ST['sections'] for r in sec['rows']]
	lines, i = text.split('\n'), 0
	for n, line in enumerate(lines):
		if line.startswith('| ') and not line.startswith('| ---') and n + 1 < len(lines) and not lines[n + 1].startswith('| ---'):
			if i >= len(rows):
				raise SystemExit('zh-cn statuses page: more rows than records/statuses.json')
			cells = line.split(' | ')
			name = re.sub(r'<id:\d+>', '', g.cn_row('skill_eff_desc', rows[i]['id'])['name'])
			lines[n] = ' | '.join([f'| {name}', status_desc(rows[i], 'zh-cn')] + cells[2:])
			i += 1
	if i != len(rows):
		raise SystemExit(f'zh-cn statuses page: {i} rows, records/statuses.json has {len(rows)}')
	return '\n'.join(lines)


def status_name(row, lang):
	n = g.gl_text('skill_eff_desc', row['id'], 'name', GLK[lang])
	if n:
		return re.sub(r'<id:\d+>', '', n)
	return MARK[lang].format(n=row['unofficial'])


def st_text(lang):
	"""The Statuses page text in one language: records/statuses.json (English) or records/statuses.<lang>.json,
	the same structure with the same section keys and row ids."""
	f = s.ROOT / 'records' / ('statuses.json' if lang == 'en' else f'statuses.{lang}.json')
	if not f.exists():
		return None
	d = json.loads(f.read_text())
	if lang != 'en':
		ids = lambda x: [(sec['key'], [r['id'] for r in sec['rows']]) for sec in x['sections']]  # noqa: E731
		if ids(d) != ids(ST):
			sys.exit(f'{f.name}: sections or row ids differ from statuses.json')
	return d


def statuses(lang):
	l, m, d = s.L[lang], mentions(), st_text(lang)
	body = [f'## {FIRST["statuses"][lang]}', '']
	for para in d['lead']:
		body += [para, '']
	head = '| ' + ' | '.join(d['col']) + ' |\n| --- | --- | --- |'
	for sec in d['sections']:
		body += [f'## {sec["title"]}', '', sec['intro'], '', head]
		for row in sec['rows']:
			cn = g.cn_row('skill_eff_desc', row['id'])['name']
			who = sorted((s.REC[x] for x in m.get(cn, ())), key=lambda a: s.name(a, 'en').lower())
			sep = ', ' if lang in ('en', 'ko') else '、'
			body.append(f'| {status_name(row, lang)} | {status_desc(row, lang)} | {sep.join(link(a, lang) for a in who) or l["unknown"]} |')
		body.append('')
	srcs = [(t.format(cn=s.CN['build'], gl=s.GL['build']),
		{'cn': g.CN_JSON + 'skill_eff_desc.json', 'gl': g.GL_JSON + 'skill_eff_desc.json', 'tips': g.GL_JSON + 'loading_text.json'}[k])
		for t, k in ST_SRC[lang]]
	return fm(d['title'], d['description'], l['applies_cn'], d['caveat'], d['aliases'], srcs) + '\n'.join(body).rstrip() + '\n'


# ---------------------------------------------------------------- resonance

RES_ALIASES = ['Resonance', '共鳴', '共鸣', '공명', 'Resonance Patterns', '共鳴調頻', '共鸣调频', '共鳴の変調', '공명 변조',
	'Reasoning', '覺察', '觉察', '察知', '감지']
CUBE = {'hp': 'hp', 'atk': 'attack', 'def': 'defense', 'mdef': 'mdefense', 'cri': 'cri', 'recri': 'recri',
	'cri_dmg': 'criDmg', 'cri_def': 'criDef', 'add_dmg': 'addDmg', 'drop_dmg': 'dropDmg', 'revive': 'revive',
	'absorb': 'absorb', 'clutch': 'clutch', 'heal': 'heal', 'defenseIgnore': 'defenseIgnore', 'normalSkillRate': 'normalSkillRate'}
RES_ITEMS = {'dissonance': 120011, 'cacophony': 120012, 'knell': 120013}
RES_ADV = [120001, 120002, 120003, 120004]
# Language keys of the global client: Resonance, Resonance Patterns, Idea Level, Reasoning, Reasoning Patterns.
RES_KEYS = {'resonance': 'language_10005055', 'patterns': 'language_10047749', 'idea': 'language_10030990',
	'reasoning': 'language_10030057', 'rpatterns': 'language_10047750'}
RT2 = {
	'en': dict(
		title='Resonance', desc='Reverse: 1999 Resonance opens at Insight I and goes to level 15 for 5- and 6-star arcanists, 10 for the rest.',
		caveat='Resonance levels 11 to 15 exist for 5- and 6-star arcanists only and need Insight III; 2-, 3- and 4-star arcanists stop at level 10.',
		lead='Resonance raises an arcanist\'s stats with Ideas: pieces of several shapes placed on a grid. Each level enlarges the grid, adds Ideas or raises their level, and raises the main Idea, the piece in the shape of the arcanist\'s own set. Resonance opens at Insight I. Some arcanists show the same system as {reasoning}, with {rpatterns}.',
		head=('Field', 'Value'),
		rows=[('Opens at', 'Insight I'), ('Max level', '{max56} for 5- and 6-star arcanists, {max24} for 2-, 3- and 4-star'),
			('Resonance Patterns', 'from Resonance level {style}'), ('Main Idea, max level', '{m56} (5 and 6 stars), {m24} (2 to 4 stars)')],
		levels='Levels', levcols=('Resonance level', 'Insight needed', 'Grid', 'Main Idea level'), ins={2: 'Insight I', 3: 'Insight II', 4: 'Insight III'},
		mats='Materials', matnote='Totals over every level. Each level also takes general materials that differ by arcanist.',
		matcols=('Material', 'Levels', '6 stars', '5 stars', '4 stars', '2 and 3 stars'), adv='one of {names}, by arcanist', lv='{a} to {b}', lv2='{a} and {b}',
		pat='Resonance Patterns', patlead='Patterns open at Resonance level {style}. Each arcanist has one of four sets, told apart by the shape of their main Idea; every set has the default pattern {default} and five more. A pattern changes the stats of the main Idea, and changing pattern keeps the Idea level. Compared with {default}:',
		patcols=('Set', 'Pattern', 'Raises', 'Lowers'), shapes={1: 'Z-shaped', 2: 'Cross-shaped', 3: 'T-shaped', 4: 'U-shaped'},
		patdiff='For 2-, 3- and 4-star arcanists the same, except: {items}.', patdiffitem='{p} does not lower {s}',
		cost='Each pattern other than {default} costs Sharpodonty and materials that differ by arcanist:', costcols=('Rarity', 'Each pattern', 'All five'),
		who='Arcanists by set', whocols=('Set', 'Arcanists'),
		names='Names', namecols=('English', 'Simplified Chinese', 'Traditional Chinese', 'Japanese', 'Korean'),
		stars='{n} stars', stars23='2 and 3 stars', none='—', sep=', ', orw=' or ',
		src=[('re1999-data, mainland client {cn}: character_talent.json, talent_mould.json, talent_style.json, talent_style_cost.json, talent_cube_attr.json', 'cn'),
			('re1999-data-global, global client {gl}: talent_style.json and the names of materials and patterns', 'gl'),
			('BWIKI, 十四行诗, revision 26647 (Resonance and pattern materials)', 'bwiki')]),
	'zh-tw': dict(
		title='共鳴', desc='重返未來：1999 的共鳴在洞悉一開放，5、6 星最高 15 級，其他最高 10 級。',
		caveat='共鳴 11 到 15 級只有 5、6 星神秘學家有，且需要洞悉三；2、3、4 星神秘學家最高 10 級。',
		lead='共鳴以思緒提升神秘學家的屬性：思緒是形狀各異的方塊，放在格子上。每升一級，格子變大、思緒增加或升級，主思緒也隨之升級；主思緒是神秘學家所屬組別形狀的方塊。洞悉一後開放共鳴。部分神秘學家的同一系統顯示為{reasoning}，調頻顯示為{rpatterns}。',
		head=('項目', '內容'),
		rows=[('開放條件', '洞悉一'), ('等級上限', '5、6 星神秘學家 {max56} 級，2、3、4 星 {max24} 級'),
			('共鳴調頻', '共鳴 {style} 級起'), ('主思緒等級上限', '{m56}（5、6 星）、{m24}（2 至 4 星）')],
		levels='等級', levcols=('共鳴等級', '所需洞悉', '格子', '主思緒等級'), ins={2: '洞悉一', 3: '洞悉二', 4: '洞悉三'},
		mats='材料', matnote='以下為所有等級的合計。每一級另需因神秘學家而異的一般材料。',
		matcols=('材料', '等級', '6 星', '5 星', '4 星', '2 星與 3 星'), adv='{names}其中一種，因神秘學家而異', lv='{a} 至 {b}', lv2='{a} 與 {b}',
		pat='共鳴調頻', patlead='共鳴 {style} 級開放調頻。每位神秘學家屬於四組之一，各組以主思緒的形狀區分；每組有預設調頻{default}和另外五種。調頻改變主思緒的屬性，更換調頻不會重置思緒等級。與{default}相比：',
		patcols=('組別', '調頻', '提高', '降低'), shapes={1: 'Z 形', 2: '十字形', 3: 'T 形', 4: 'U 形'},
		patdiff='2、3、4 星神秘學家相同，但{items}。', patdiffitem='{p}不降低{s}',
		cost='{default}以外的每種調頻消耗利齒子兒與因神秘學家而異的材料：', costcols=('稀有度', '每種調頻', '五種合計'),
		who='各組的神秘學家', whocols=('組別', '神秘學家'),
		names='名稱', namecols=('英文', '簡體中文', '繁體中文', '日文', '韓文'),
		stars='{n} 星', stars23='2 星與 3 星', none='—', sep='、', orw='或',
		src=[('re1999-data，中國大陸版用戶端 {cn}：character_talent.json、talent_mould.json、talent_style.json、talent_style_cost.json、talent_cube_attr.json', 'cn'),
			('re1999-data-global，國際版用戶端 {gl}：talent_style.json 與材料、調頻名稱', 'gl'),
			('BWIKI，十四行诗，修訂版 26647（共鳴與調頻材料）', 'bwiki')]),
	'ja': dict(
		title='共鳴', desc='リバース：1999 の共鳴は洞察1で開放され、★5・★6は最大レベル15、ほかは10。',
		caveat='共鳴レベル11から15は★5と★6の神秘学家だけにあり、洞察3が必要。★2、★3、★4の神秘学家はレベル10まで。',
		lead='共鳴は思念で神秘学家のステータスを上げる。思念はさまざまな形のピースで、マスに配置する。レベルが上がるごとにマスが広がり、思念が増えるかレベルが上がり、メイン思念も上がる。メイン思念はその神秘学家が属するグループの形のピース。共鳴は洞察1で開放される。一部の神秘学家では同じシステムが{reasoning}、変調が{rpatterns}と表示される。',
		head=('項目', '内容'),
		rows=[('開放条件', '洞察1'), ('最大レベル', '★5と★6の神秘学家は{max56}、★2、★3、★4は{max24}'),
			('共鳴の変調', '共鳴レベル{style}から'), ('メイン思念の最大レベル', '{m56}（★5と★6）、{m24}（★2から★4）')],
		levels='レベル', levcols=('共鳴レベル', '必要な洞察', 'マス', 'メイン思念レベル'), ins={2: '洞察1', 3: '洞察2', 4: '洞察3'},
		mats='素材', matnote='全レベルの合計。各レベルでは神秘学家ごとに異なる一般素材も必要。',
		matcols=('素材', 'レベル', '★6', '★5', '★4', '★2と★3'), adv='{names}のうち1種、神秘学家ごとに異なる', lv='{a}から{b}', lv2='{a}と{b}',
		pat='共鳴の変調', patlead='変調は共鳴レベル{style}で開放される。神秘学家はそれぞれ4つのグループのどれかに属し、グループはメイン思念の形で見分けられる。どのグループにもデフォルトの{default}とほかに5つの変調がある。変調はメイン思念のステータスを変え、変調を切り替えても思念レベルは変わらない。{default}と比べて：',
		patcols=('グループ', '変調', '上がる', '下がる'), shapes={1: 'Z字型', 2: '十字型', 3: 'T字型', 4: 'U字型'},
		patdiff='★2、★3、★4の神秘学家も同じ。ただし{items}。', patdiffitem='{p}は{s}が下がらない',
		cost='{default}以外の変調にはそれぞれ咬噛銭貨と神秘学家ごとに異なる素材が必要：', costcols=('レア度', '変調1つ', '5つの合計'),
		who='グループ別の神秘学家', whocols=('グループ', '神秘学家'),
		names='名前', namecols=('英語', '簡体字中国語', '繁体字中国語', '日本語', '韓国語'),
		stars='★{n}', stars23='★2と★3', none='—', sep='、', orw='か',
		src=[('re1999-data、中国本土版クライアント {cn}：character_talent.json、talent_mould.json、talent_style.json、talent_style_cost.json、talent_cube_attr.json', 'cn'),
			('re1999-data-global、グローバル版クライアント {gl}：talent_style.json と素材名、変調名', 'gl'),
			('BWIKI、十四行诗、版 26647（共鳴と変調の素材）', 'bwiki')]),
	'ko': dict(
		title='공명', desc='리버스: 1999 공명은 통찰 1에 열리며, 5·6성은 최대 레벨 15, 나머지는 10이다.',
		caveat='공명 레벨 11부터 15는 5성과 6성 마도학자에게만 있고 통찰 3이 필요하다. 2, 3, 4성 마도학자는 레벨 10까지다.',
		lead='공명은 생각으로 마도학자의 스탯을 올린다. 생각은 여러 모양의 조각이며 칸 위에 배치한다. 레벨이 오를 때마다 칸이 넓어지고, 생각이 늘거나 레벨이 오르며, 주요 생각도 오른다. 주요 생각은 마도학자가 속한 그룹 모양의 조각이다. 공명은 통찰 1에 열린다. 일부 마도학자에게는 같은 시스템의 이름이 {reasoning}, 변조의 이름이 {rpatterns}이다.',
		head=('항목', '내용'),
		rows=[('개방 조건', '통찰 1'), ('최대 레벨', '5성과 6성 마도학자는 {max56}, 2, 3, 4성은 {max24}'),
			('공명 변조', '공명 레벨 {style}부터'), ('주요 생각 최대 레벨', '{m56}(5성과 6성), {m24}(2성부터 4성)')],
		levels='레벨', levcols=('공명 레벨', '필요한 통찰', '칸', '주요 생각 레벨'), ins={2: '통찰 1', 3: '통찰 2', 4: '통찰 3'},
		mats='재료', matnote='모든 레벨의 합계다. 레벨마다 마도학자에 따라 다른 일반 재료도 든다.',
		matcols=('재료', '레벨', '6성', '5성', '4성', '2성과 3성'), adv='{names} 중 하나, 마도학자에 따라 다름', lv='{a}부터 {b}', lv2='{a}와 {b}',
		pat='공명 변조', patlead='변조는 공명 레벨 {style}에 열린다. 마도학자는 네 그룹 중 하나에 속하며, 그룹은 주요 생각의 모양으로 구별된다. 모든 그룹에 기본 변조 {default}와 다섯 가지가 더 있다. 변조는 주요 생각의 스탯을 바꾸며, 변조를 바꿔도 생각 레벨은 그대로다. {default}와 비교하면:',
		patcols=('그룹', '변조', '오름', '내림'), shapes={1: 'Z자형', 2: '십자형', 3: 'T자형', 4: 'U자형'},
		patdiff='2, 3, 4성 마도학자도 같다. 다만 {items}.', patdiffitem='{p}에서는 {s} 감소가 없다',
		cost='{default} 외의 변조는 각각 톱니 동전과 마도학자에 따라 다른 재료가 든다:', costcols=('희귀도', '변조 하나', '다섯 가지 합계'),
		who='그룹별 마도학자', whocols=('그룹', '마도학자'),
		names='이름', namecols=('영어', '간체 중국어', '번체 중국어', '일본어', '한국어'),
		stars='{n}성', stars23='2성과 3성', none='—', sep=', ', orw=' 또는 ',
		src=[('re1999-data, 중국 본토 클라이언트 {cn}: character_talent.json, talent_mould.json, talent_style.json, talent_style_cost.json, talent_cube_attr.json', 'cn'),
			('re1999-data-global, 글로벌 클라이언트 {gl}: talent_style.json과 재료, 변조 이름', 'gl'),
			('BWIKI, 十四行诗, 판 26647 (공명과 변조 재료)', 'bwiki')]),
}
BWIKI_SONETTO = 'https://wiki.biligame.com/reverse1999/%E5%8D%81%E5%9B%9B%E8%A1%8C%E8%AF%97?oldid=26647'


def _parts(consume):
	for part in filter(None, (consume or '').split('|')):
		kind, item, n = part.split('#')
		yield kind, int(item), int(n)


def resonance_data():
	"""Everything the Resonance page states, checked to agree within a rarity (2 and 3 stars together)."""
	rec = {a['id']: a for a in s.REC.values() if a['slug'] not in wi.SKIP}
	rows = collections.defaultdict(list)
	for r in g.cn('character_talent'):
		if r['heroId'] in rec:
			rows[r['heroId']].append(r)
	band = lambda st: '23' if st in (2, 3) else str(st)  # noqa: E731
	per = collections.defaultdict(set)
	sets = collections.defaultdict(list)
	for h, rs in rows.items():
		a, rs = rec[h], sorted(rows[h], key=lambda r: r['talentId'])
		b = band(a['stars'])
		moulds = {r['talentMould'] for r in rs}
		if len(moulds) != 1:
			sys.exit(f'{a["slug"]}: more than one Resonance set')
		sets[next(iter(moulds))].append(a)
		per[(b, 'max')].add(len(rs))
		per[(b, 'req')].add(tuple(r['requirement'] for r in rs))
		per[(b, 'main')].add(tuple(int(r['exclusive'].split('#')[1]) for r in rs))
		per[(b, 'sharp')].add(tuple(sum(n for k, i, n in _parts(r['consume']) if k == '2' and i == 3) for r in rs))
		for key, item in RES_ITEMS.items():
			per[(b, key)].add(tuple(sum(n for k, i, n in _parts(r['consume']) if k == '1' and i == item) for r in rs))
		per[(b, 'adv')].add(tuple(sum(n for k, i, n in _parts(r['consume']) if k == '1' and i in RES_ADV) for r in rs))
	for h in rows:
		for r in g.cn('talent_style_cost'):
			if r['heroId'] == h:
				per[(band(rec[h]['stars']), 'style')].add(sum(n for k, i, n in _parts(r['consume']) if k == '2' and i == 3))
	for k, v in per.items():
		if len(v) != 1:
			sys.exit(f'Resonance {k}: values differ between arcanists: {sorted(v)}')
	d = {k: next(iter(v)) for k, v in per.items()}
	grid = {}
	for r in g.cn('talent_mould'):
		grid.setdefault(r['talentId'], set()).add(r['allShape'])
	if any(len(v) != 1 for v in grid.values()):
		sys.exit('Resonance grid differs between sets')
	styles = collections.defaultdict(dict)
	for r in g.cn('talent_style'):
		styles[r['talentMould']][r['styleId']] = r
	opens = {r['level'] for m in styles.values() for r in m.values() if r['styleId']}
	if len(opens) != 1:
		sys.exit(f'Resonance Patterns open at different levels: {opens}')
	cube = collections.defaultdict(dict)
	for r in g.cn('talent_cube_attr'):
		cube[r['id']][r['level']] = r
	gl_style = {(r['talentMould'], r['styleId']): r['name'] for r in g.gl('talent_style')}

	def change(base, new):
		a, b = cube[base][max(cube[base])], cube[new][max(cube[new])]
		return ([c for c in CUBE if b.get(c, 0) > a.get(c, 0)], [c for c in CUBE if b.get(c, 0) < a.get(c, 0)])
	pats = {}
	for m, st in styles.items():
		for sid, r in st.items():
			if sid:
				big, small = change(60 + m, (60 + m) * 10 + sid), change(40 + m, (40 + m) * 10 + sid)
				pats[(m, sid)] = {'big': big, 'small': small, 'cn': r['name'], 'gl': gl_style.get((m, sid))}
	default = styles[1][0]
	return {'d': d, 'grid': {k: next(iter(v)) for k, v in grid.items()}, 'sets': sets, 'opens': opens.pop(),
		'pats': pats, 'default': {'cn': default['name'], 'gl': gl_style[(1, 0)]}}


def resonance(lang):
	t, l, key = RT2[lang], s.L[lang], GLK[lang]
	R = resonance_data()
	d = R['d']
	stat = lambda c: _stat(CUBE[c], lang)  # noqa: E731
	item = lambda i: g.gl_text('item', i, 'name', key)  # noqa: E731
	sharp = g.gl_text('currency', 3, 'name', key)
	pname = lambda p: g.text(p['gl'], key) if p['gl'] else p['cn']  # noqa: E731
	default = pname(R['default'])
	main56, main24 = d[('6', 'main')], d[('4', 'main')]
	vals = dict(max56=d[('6', 'max')], max24=d[('4', 'max')], style=R['opens'], m56=max(main56), m24=max(main24))
	for b in ('5', '23'):
		if d[(b, 'max')] != (vals['max56'] if b == '5' else vals['max24']) or d[(b, 'req')] != d[('6' if b == '5' else '4', 'req')][:d[(b, 'max')]]:
			sys.exit(f'Resonance: {b} stars differ in levels or Insight')
	req = d[('6', 'req')]
	if req[:vals['max24']] != d[('4', 'req')] or main56[:vals['max24']] != main24:
		sys.exit('Resonance: levels 1 to 10 differ between rarities')
	words = {k: g.text(v, key) for k, v in RES_KEYS.items()}
	body = [f'## {FIRST["resonance"][lang]}', '', t['lead'].format(**words), '', f'| {t["head"][0]} | {t["head"][1]} |', '| --- | --- |']
	body += [f'| {a} | {b.format(**vals)} |' for a, b in t['rows']]
	body += ['', f'## {t["levels"]}', '', '| ' + ' | '.join(t['levcols']) + ' |', '| --- | --- | --- | --- |']
	for n in range(1, vals['max56'] + 1):
		w, h = R['grid'][n].split(',')
		body.append(f'| {n} | {t["ins"][req[n - 1]]} | {w} × {h} | {main56[n - 1]} |')
	cols = ['6', '5', '4', '23']

	def first_last(seq):
		idx = [i + 1 for i, x in enumerate(seq) if x]
		return idx[0], idx[-1]

	def lv(seq):
		a, b = first_last(seq)
		return str(a) if a == b else t['lv'].format(a=a, b=b)
	body += ['', f'## {t["mats"]}', '', t['matnote'], '', '| ' + ' | '.join(t['matcols']) + ' |', '| --- | --- | --- | --- | --- | --- |']
	adv = t['adv'].format(names=t['sep'].join(item(i) for i in RES_ADV[:-1]) + t['orw'] + item(RES_ADV[-1]))
	for name, k in [(item(RES_ITEMS['dissonance']), 'dissonance'), (item(RES_ITEMS['cacophony']), 'cacophony'), (adv, 'adv'), (item(RES_ITEMS['knell']), 'knell')]:
		body.append(f'| {name} | {lv(d[("6", k)])} | ' + ' | '.join(str(sum(d[(c, k)])) for c in cols) + ' |')
	sh = d[('6', 'sharp')]
	where = [i + 1 for i, x in enumerate(sh) if x]
	body.append(f'| {sharp} | {t["lv2"].format(a=where[0], b=where[1])} | ' + ' | '.join(num(sum(d[(c, "sharp")])) for c in cols) + ' |')
	body += ['', f'## {t["pat"]}', '', t['patlead'].format(style=R['opens'], default=default), '',
		'| ' + ' | '.join(t['patcols']) + ' |', '| --- | --- | --- | --- |']
	diffs = []
	for (m, sid), p in sorted(R['pats'].items()):
		up, down = p['big']
		body.append(f'| {t["shapes"][m]} | {pname(p)} | {t["sep"].join(stat(c) for c in up) or t["none"]} | {t["sep"].join(stat(c) for c in down) or t["none"]} |')
		if p['small'] != p['big']:
			if p['small'][0] != up or not set(p['small'][1]) <= set(down):
				sys.exit(f'Resonance pattern {m}/{sid}: lower rarities differ in another way')
			for c in down:
				if c not in p['small'][1]:
					diffs.append(t['patdiffitem'].format(p=pname(p), s=stat(c)))
	if diffs:
		body += ['', t['patdiff'].format(items=t['sep'].join(diffs))]
	body += ['', t['cost'].format(default=default), '', '| ' + ' | '.join(t['costcols']) + ' |', '| --- | --- | --- |']
	for c in cols:
		lab = t['stars23'] if c == '23' else t['stars'].format(n=int(c))
		body.append(f'| {lab} | {num(d[(c, "style")])} {sharp} | {num(d[(c, "style")] * 5)} {sharp} |')
	body += ['', f'## {t["who"]}', '', '| ' + ' | '.join(t['whocols']) + ' |', '| --- | --- |']
	for m in sorted(R['sets']):
		names = sorted({s.name(a, lang) for a in R['sets'][m]}, key=lambda n: n.lower())
		body.append(f'| {t["shapes"][m]} | {t["sep"].join(names)} |')
	body += ['', f'## {t["names"]}', '', '| ' + ' | '.join(t['namecols']) + ' |', '| --- | --- | --- | --- | --- |']
	terms = [(g.text(RES_KEYS[k], 'en'), g.text(RES_KEYS[k], 'zh-CN'), g.text(RES_KEYS[k], 'zh-TW'), g.text(RES_KEYS[k], 'ja'), g.text(RES_KEYS[k], 'ko'))
		for k in ('resonance', 'patterns', 'idea', 'reasoning', 'rpatterns')]
	seen = set()
	for p in [R['default']] + [p for _, p in sorted(R['pats'].items())]:
		if p['cn'] in seen:
			continue
		seen.add(p['cn'])
		terms.append((g.text(p['gl'], 'en'), p['cn'], g.text(p['gl'], 'zh-TW'), g.text(p['gl'], 'ja'), g.text(p['gl'], 'ko')))
	body += ['| ' + ' | '.join(row) + ' |' for row in terms]
	srcs = [(x.format(cn=s.CN['build'], gl=s.GL['build']),
		{'cn': g.CN_JSON.replace('/blob/', '/tree/').rstrip('/'), 'gl': g.GL_JSON + 'talent_style.json', 'bwiki': BWIKI_SONETTO}[u]) for x, u in t['src']]
	return fm(t['title'], t['desc'], l['applies_gl'], t['caveat'], RES_ALIASES, srcs) + '\n'.join(body) + '\n'


def _stat(attr, lang):
	import psychube
	return psychube._attr_name(attr, lang)


PAGES = {'releases': releases, 'insight': insight, 'statuses': statuses, 'resonance': resonance}


def main():
	n = 0
	for lang in (sys.argv[1:] or LANGS):
		d = s.DOCS / s.L[lang]['dir'] / 'systems'
		d.mkdir(parents=True, exist_ok=True)
		for slug, fn in PAGES.items():
			if slug == 'statuses' and not st_text(lang):
				continue
			(d / f'{slug}.md').write_text(fn(lang))
			n += 1
	print(f'{n} system pages written')
	return 0


if __name__ == '__main__':
	sys.exit(main())
