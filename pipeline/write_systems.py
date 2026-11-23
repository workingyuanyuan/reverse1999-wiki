"""Write the system pages that the records decide entirely, in every language but zh-cn.

  python3 -I pipeline/write_systems.py [lang ...]     (default: en zh-tw ja ko)

Writes src/content/docs/{,zh-tw/,ja/,ko/}systems/{releases,insight}.md (zh-cn: scripts/to-zh-cn.py).
Overwrites them; they are not edited by hand. Change the wording here.

releases: every arcanist's release date on the mainland and the global service (records/releases.json,
  read from the Fandom infobox), newest first, with the days between them.
insight: what each Insight gives and costs by rarity, from character_rank.json of the mainland client.
  Levels in that table run on across Insight stages (caps 30, 70, 120, 180): the cap of Insight n is the
  difference. Level costs (character_cosume.json) are left out: their rows do not line up one to one with
  the levels of a stage, and no second source gives the totals.
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
		title='Release dates', desc='Reverse: 1999 arcanists by release date on the mainland China and global services, and the days between.',
		caveat='The global service has brought arcanists between {lo} and {hi} days after the mainland service; an arcanist out only on the mainland service has no global date until one is announced.',
		lead='Of the {n} arcanists out on both services, {same} came to the global service on the same day as the mainland service: {samelist}. The others came {lo2} to {hi} days later, {med} days at the median; for those released on the mainland since 2025-06-01, the median is {med2} days.',
		only='Out only on the mainland service', all='All arcanists, newest first',
		cols=('Arcanist', 'Rarity', 'Mainland release', 'Global release', 'Days later'),
		src='Reverse: 1999 Wiki (Fandom): release dates in each arcanist\'s infobox, read 2026-11-22',
		aliases=REL_ALIASES),
	'zh-tw': dict(
		title='上線日期', desc='重返未來：1999 神秘學家在中國大陸版與國際版的上線日期，以及兩者相隔的天數。',
		caveat='國際版的神秘學家比中國大陸版晚 {lo} 到 {hi} 天上線；只在中國大陸版推出的神秘學家，在公布之前沒有國際版日期。',
		lead='兩個版本都已上線的 {n} 位神秘學家中，有 {same} 位在國際版與中國大陸版同一天上線：{samelist}。其餘晚 {lo2} 到 {hi} 天，中位數 {med} 天；2025-06-01 以後在中國大陸版上線的，中位數 {med2} 天。',
		only='僅中國大陸版', all='全部神秘學家，由新到舊',
		cols=('神秘學家', '稀有度', '中國大陸版上線', '國際版上線', '相隔天數'),
		src='Reverse: 1999 Wiki (Fandom)：各神秘學家資訊框的上線日期，2026-11-22 讀取',
		aliases=REL_ALIASES),
	'ja': dict(
		title='実装日', desc='リバース：1999 の神秘学家の中国本土版とグローバル版での実装日と、その間の日数。',
		caveat='グローバル版の実装は中国本土版の {lo} 日後から {hi} 日後まで。中国本土版にのみ実装された神秘学家には、発表されるまでグローバル版の日付がない。',
		lead='両方の版に実装された {n} 人の神秘学家のうち、{same} 人はグローバル版にも中国本土版と同じ日に実装された：{samelist}。ほかは {lo2} 日後から {hi} 日後で、中央値は {med} 日。2025-06-01 以降に中国本土版に実装された神秘学家では、中央値は {med2} 日。',
		only='中国本土版のみ', all='すべての神秘学家（新しい順）',
		cols=('神秘学家', 'レア度', '中国本土版の実装', 'グローバル版の実装', '日数'),
		src='Reverse: 1999 Wiki (Fandom)：各神秘学家のインフォボックスの実装日、2026-11-22 に読んだもの',
		aliases=REL_ALIASES),
	'ko': dict(
		title='출시일', desc='리버스: 1999 마도학자의 중국 본토와 글로벌 서비스 출시일, 그리고 그 사이의 일수.',
		caveat='글로벌 서비스의 출시는 중국 본토 서비스보다 {lo}일에서 {hi}일 늦었다. 중국 본토 서비스에만 나온 마도학자는 발표되기 전까지 글로벌 날짜가 없다.',
		lead='두 서비스에 모두 나온 마도학자 {n}명 중 {same}명은 글로벌 서비스에도 중국 본토와 같은 날 나왔다: {samelist}. 나머지는 {lo2}일에서 {hi}일 늦었고 중앙값은 {med}일이다. 2025-06-01 이후 중국 본토에 나온 마도학자의 중앙값은 {med2}일이다.',
		only='중국 본토 한정', all='모든 마도학자, 최신순',
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
	body = [lead, '', f'## {t["only"]}', '', only, '', f'## {t["all"]}', '', head] + rows
	return fm(t['title'], t['desc'], l['applies_gl'], caveat, t['aliases'], srcs) + '\n'.join(body) + '\n'


# ---------------------------------------------------------------- insight

IT = {
	'en': dict(
		title='Insight and levels', desc='Reverse: 1999 Insight: level caps, Sharpodonty cost and what each Insight unlocks, by rarity.',
		caveat='Insight resets the arcanist to level 1 with a higher cap; 2-, 3- and 4-star arcanists stop at Insight II, level 50.',
		lead='Insight raises an arcanist\'s level cap once the arcanist reaches it. Each Insight costs {sharp} and materials that depend on the arcanist (listed on each arcanist\'s page), and returns the arcanist to level 1 of the new cap.',
		caps='Level caps', capcols=('Rarity', 'Insight 0', 'Insight I', 'Insight II', 'Insight III'),
		cost='Cost of each Insight', costcols=('Rarity', 'Insight I', 'Insight II', 'Insight III'),
		costnote='Insight III also takes a Tome of the arcanist\'s Afflatus and higher-rarity materials; each arcanist\'s page gives the full list.',
		gives='What each Insight unlocks',
		givesrows=[('Insight I', 'level cap {c1}; the first Inheritance passive'),
			('Insight II', 'level cap {c2}; the second Inheritance passive; for 4-star and higher arcanists, a garment (all but Sonetto)'),
			('Insight III', 'level cap {c3}; the third Inheritance passive (5 and 6 stars only); opens Euphoria for arcanists that have it')],
		givescols=('Insight', 'Unlocks'),
		eup='Euphoria opens at Insight III level 30 for a 6-star arcanist and at Insight III level 1 for a 5-star.',
		por='Portrait', porline='A duplicate of an arcanist raises its Portrait by one level, up to Portrait 5; each level changes one skill, given on the arcanist\'s page. What later duplicates turn into is on [Summoning and pity](/systems/summoning/).',
		level='level {n}', none='—', stars='{n} stars', stars23='2 and 3 stars',
		src=[('re1999-data, mainland client {cn}: character_rank.json', 'character_rank'),
			('re1999-data-global, global client {gl}: character_rank.json and the names of materials', 'gl'),
			('Reverse: 1999 Wiki (Fandom), Insight, revision 20796', FANDOM_INSIGHT)],
		aliases=INS_ALIASES),
	'zh-tw': dict(
		title='洞悉與等級', desc='重返未來：1999 的洞悉：各稀有度的等級上限、利齒子兒消耗與每階洞悉解鎖的內容。',
		caveat='洞悉後神秘學家回到 1 級、上限提高；2、3、4 星神秘學家最高到洞悉二 50 級。',
		lead='神秘學家達到等級上限後，洞悉可以提高上限。每次洞悉消耗{sharp}與因神秘學家而異的材料（列在各神秘學家的頁面），洞悉後回到新上限的 1 級。',
		caps='等級上限', capcols=('稀有度', '洞悉零', '洞悉一', '洞悉二', '洞悉三'),
		cost='每次洞悉的消耗', costcols=('稀有度', '洞悉一', '洞悉二', '洞悉三'),
		costnote='洞悉三另需該神秘學家靈感的典籍與更高稀有度的材料；完整清單在各神秘學家的頁面。',
		gives='每階洞悉解鎖的內容',
		givesrows=[('洞悉一', '等級上限 {c1}；第一個傳承被動'),
			('洞悉二', '等級上限 {c2}；第二個傳承被動；4 星以上的神秘學家另得一套服裝（十四行詩除外）'),
			('洞悉三', '等級上限 {c3}；第三個傳承被動（僅 5、6 星）；擁有狂想的神秘學家開放狂想')],
		givescols=('洞悉', '解鎖'),
		eup='6 星神秘學家在洞悉三 30 級開放狂想，5 星神秘學家在洞悉三 1 級開放。',
		por='塑造', porline='重複獲得同一位神秘學家，塑造提升一級，最高塑造五；每一級改變一個技能，內容在各神秘學家的頁面。之後再重複獲得會轉換成什麼，見[徵集與保底](/zh-tw/systems/summoning/)。',
		level='{n} 級', none='—', stars='{n} 星', stars23='2 星與 3 星',
		src=[('re1999-data，中國大陸版用戶端 {cn}：character_rank.json', 'character_rank'),
			('re1999-data-global，國際版用戶端 {gl}：character_rank.json 與材料名稱', 'gl'),
			('Reverse: 1999 Wiki (Fandom)，Insight，修訂版 20796', FANDOM_INSIGHT)],
		aliases=INS_ALIASES),
	'ja': dict(
		title='洞察とレベル', desc='リバース：1999 の洞察：レア度ごとのレベル上限、咬噛銭貨の消費、洞察ごとに解放されるもの。',
		caveat='洞察するとレベル1に戻り、上限が上がる。★2、★3、★4の神秘学家は洞察2のレベル50が最大。',
		lead='神秘学家が今のレベル上限に達すると、洞察で上限を上げられる。洞察のたびに{sharp}と神秘学家ごとに異なる素材（各神秘学家のページにある）を消費し、新しい上限のレベル1に戻る。',
		caps='レベル上限', capcols=('レア度', '洞察0', '洞察1', '洞察2', '洞察3'),
		cost='洞察ごとの消費', costcols=('レア度', '洞察1', '洞察2', '洞察3'),
		costnote='洞察3ではその神秘学家の本源の典籍と、より高いレア度の素材も必要。素材の一覧は各神秘学家のページにある。',
		gives='洞察ごとに解放されるもの',
		givesrows=[('洞察1', 'レベル上限 {c1}、1つ目の伝承パッシブ'),
			('洞察2', 'レベル上限 {c2}、2つ目の伝承パッシブ、★4以上の神秘学家は衣装（ソネット以外）'),
			('洞察3', 'レベル上限 {c3}、3つ目の伝承パッシブ（★5と★6のみ）、狂想を持つ神秘学家は狂想が開放')],
		givescols=('洞察', '解放'),
		eup='狂想は★6の神秘学家では洞察3のレベル30、★5では洞察3のレベル1で開放される。',
		por='塑造', porline='同じ神秘学家を重ねて入手すると塑造が1段階上がり、塑造5が最大。各段階で1つのスキルが変わり、内容は各神秘学家のページにある。それ以降の重複が何に変わるかは[召喚と天井](/ja/systems/summoning/)にある。',
		level='レベル{n}', none='—', stars='★{n}', stars23='★2と★3',
		src=[('re1999-data、中国本土版クライアント {cn}：character_rank.json', 'character_rank'),
			('re1999-data-global、グローバル版クライアント {gl}：character_rank.json と素材名', 'gl'),
			('Reverse: 1999 Wiki (Fandom)、Insight、版 20796', FANDOM_INSIGHT)],
		aliases=INS_ALIASES),
	'ko': dict(
		title='통찰과 레벨', desc='리버스: 1999 통찰: 희귀도별 레벨 상한, 톱니 동전 소모, 통찰마다 해금되는 것.',
		caveat='통찰하면 마도학자는 레벨 1로 돌아가고 상한이 오른다. 2, 3, 4성 마도학자는 통찰 2 레벨 50이 최대다.',
		lead='마도학자가 레벨 상한에 이르면 통찰로 상한을 올릴 수 있다. 통찰할 때마다 {sharp}과 마도학자마다 다른 재료(각 마도학자 페이지에 있음)가 들고, 새 상한의 레벨 1로 돌아간다.',
		caps='레벨 상한', capcols=('희귀도', '통찰 0', '통찰 1', '통찰 2', '통찰 3'),
		cost='통찰별 소모', costcols=('희귀도', '통찰 1', '통찰 2', '통찰 3'),
		costnote='통찰 3에는 그 마도학자 영감의 서적과 더 높은 희귀도의 재료도 든다. 전체 목록은 각 마도학자 페이지에 있다.',
		gives='통찰마다 해금되는 것',
		givesrows=[('통찰 1', '레벨 상한 {c1}, 첫 번째 계승 패시브'),
			('통찰 2', '레벨 상한 {c2}, 두 번째 계승 패시브, 4성 이상 마도학자는 의상(소네트 제외)'),
			('통찰 3', '레벨 상한 {c3}, 세 번째 계승 패시브(5성과 6성만), 광상이 있는 마도학자는 광상 개방')],
		givescols=('통찰', '해금'),
		eup='광상은 6성 마도학자는 통찰 3 레벨 30, 5성은 통찰 3 레벨 1에 열린다.',
		por='형상', porline='같은 마도학자를 중복으로 얻으면 형상이 한 단계 오르고 형상 5가 최대다. 단계마다 스킬 하나가 바뀌며 내용은 각 마도학자 페이지에 있다. 그 뒤의 중복이 무엇으로 바뀌는지는 [모집과 천장](/ko/systems/summoning/)에 있다.',
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
	body = [t['lead'].format(sharp=sharp_name), '',
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
	body = []
	for para in d['lead']:
		body += [para, '']
	head = '| ' + ' | '.join(d['col']) + ' |\n| --- | --- | --- |'
	for sec in d['sections']:
		body += [f'## {sec["title"]}', '', sec['intro'], '', head]
		for row in sec['rows']:
			cn = g.cn_row('skill_eff_desc', row['id'])['name']
			who = sorted((s.REC[x] for x in m.get(cn, ())), key=lambda a: s.name(a, 'en').lower())
			sep = ', ' if lang in ('en', 'ko') else '、'
			body.append(f'| {status_name(row, lang)} | {row["desc"]} | {sep.join(link(a, lang) for a in who) or l["unknown"]} |')
		body.append('')
	srcs = [(t.format(cn=s.CN['build'], gl=s.GL['build']),
		{'cn': g.CN_JSON + 'skill_eff_desc.json', 'gl': g.GL_JSON + 'skill_eff_desc.json', 'tips': g.GL_JSON + 'loading_text.json'}[k])
		for t, k in ST_SRC[lang]]
	return fm(d['title'], d['description'], l['applies_cn'], d['caveat'], d['aliases'], srcs) + '\n'.join(body).rstrip() + '\n'


PAGES = {'releases': releases, 'insight': insight, 'statuses': statuses}


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
