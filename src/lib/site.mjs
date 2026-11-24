// Shared site facts and URL rules. Plain JS so astro.config.mjs, Astro code and
// the check script all use the same rules.

// The public address, including the sub-path of a GitHub Pages project site, without a
// trailing slash. SITE_URL overrides it for local agent tests (see tests/agent-eval/README.md).
export const SITE = (process.env.SITE_URL ?? 'https://yuanaruru.com/reverse1999-wiki').replace(/\/+$/, '');
/** Scheme and host of SITE. */
export const ORIGIN = new URL(SITE).origin;
/** Sub-path the site is served under: `/reverse1999-wiki`, or the empty string at a domain root. */
export const BASE = new URL(SITE).pathname.replace(/\/+$/, '');
export const TITLE = { en: 'Reverse: 1999 Wiki', 'zh-TW': '重返未來：1999 Wiki', 'zh-CN': '重返未来：1999 Wiki', ja: 'リバース：1999 Wiki', ko: '리버스: 1999 위키' };
export const DESCRIPTION =
	'Unofficial reference for the game Reverse: 1999 (重返未來：1999): arcanists, their skills and upgrades, and what the mainland China service has that the global one does not yet, read from the game data.';

/** Root-relative address for an `href` or `src` in HTML: the site path behind BASE. */
export function withBase(path) {
	return BASE + path;
}

/**
 * Locales: `dir` is the content sub-folder and URL prefix ('' = root); `maxDescription` is the
 * length limit of the one-sentence answer, in characters. A language may lack pages for a
 * time: `records/pending.json` lists the English pages it does not have yet.
 */
export const LOCALES = [
	{ dir: '', lang: 'en', label: 'English', maxDescription: 110 },
	{ dir: 'zh-tw', lang: 'zh-TW', label: '繁體中文', maxDescription: 70 },
	{ dir: 'zh-cn', lang: 'zh-CN', label: '简体中文', maxDescription: 70 },
	{ dir: 'ja', lang: 'ja', label: '日本語', maxDescription: 70 },
	{ dir: 'ko', lang: 'ko', label: '한국어', maxDescription: 90 },
];

/** Starlight's route data gives the home page an empty id; the collection calls it `index`. */
export function pageId(id) {
	return id === '' ? 'index' : id;
}

/** Locale of a content entry id such as `operators/laevatain`, `zh-tw/operators/laevatain`, `index`, `zh-tw`. */
export function localeOf(id) {
	return (
		LOCALES.find((l) => l.dir && (id === l.dir || id.startsWith(l.dir + '/'))) ?? LOCALES[0]
	);
}

/** Entry id without its locale prefix. The home page is `index` in every locale. */
export function bareId(id) {
	const { dir } = localeOf(id);
	if (!dir) return id;
	return id === dir ? 'index' : id.slice(dir.length + 1);
}

/** Entry id of the same page in another locale. */
export function idInLocale(id, locale) {
	const bare = bareId(id);
	if (!locale.dir) return bare;
	return bare === 'index' ? locale.dir : `${locale.dir}/${bare}`;
}

/** Site path of the HTML page for an entry id. */
export function htmlPath(id) {
	return id === 'index' ? '/' : `/${id}/`;
}

/** Site path of the Markdown twin: drop the trailing slash, append `.md`; home is `/index.md`. */
export function mdPath(id) {
	return `/${id}.md`;
}

/** Markdown twin of an internal HTML path such as `/operators/laevatain/` or `/`. */
export function mdPathFromHtmlPath(path) {
	const trimmed = path.replace(/^\/+|\/+$/g, '');
	return mdPath(trimmed === '' ? 'index' : trimmed);
}

/** Site path of a language's page index: `/llms.txt`, `/zh-tw/llms.txt`. */
export function llmsPath(locale) {
	return `${locale.dir ? '/' + locale.dir : ''}/llms.txt`;
}

/**
 * The opening of each language's llms.txt: what a reader gets wrong without being told.
 * Site-specific. Keep it short: it shares the first 5,000 characters with the page list.
 */
/** A story stage page (`story/<chapter>/<stage>`, any language): reached from its chapter page, not listed in llms.txt or the bundles. */
export function isStage(id) {
	return /^story\/[^/]+\/[^/]+$/.test(bareId(id));
}

/** An arcanist's profile page (`arcanists/<slug>/profile`, pipeline/profile.py): reached from the arcanist's page, listed in llms.txt, not in the bundles. */
export function isProfile(id) {
	return /^arcanists\/[^/]+\/profile$/.test(bareId(id));
}

/** A page of the game's own text: a story chapter or stage, or an arcanist's profile (pipeline/profile.py). */
export function isGameText(id) {
	return isStoryText(id) || isProfile(id);
}

/** A page with no answer line under its title: an arcanist's profile and a story stage, whose
 * title and the first lines of the body already say what the page holds. The hidden note at the
 * top of the article carries the description instead. */
export function hidesAnswer(id) {
	return isProfile(id) || isStage(id);
}

/** A story chapter or stage page (not one of the five story index pages): game text, with a short sidebar. */
export function isStoryText(id) {
	return isStage(id) || (/^story\/[^/]+$/.test(bareId(id)) && !/^story\/(main|events|characters|characters-2|anecdotes|other)$/.test(bareId(id)));
}

export const LLMS_NOTES = {
	en: {
		summary: DESCRIPTION,
		heading: 'Before you answer',
		notes: [
			'Story text: /story/main/, /story/events/, /story/characters/, /story/characters-2/, /story/anecdotes/ and /story/other/ list the chapters; a chapter page lists its stages; a stage page holds the full text of that stage as the game has it, in the English of the global client (version 3.9). Stage pages are not in the page list below or in the bundles.',
			'Profiles: /arcanists/<slug>/profile/ holds an arcanist\'s file as the game shows it (cover, items, stories, skins, voice lines) in the English of the global client; the arcanist\'s page links it. Skins and voice lines out on the mainland service only are not on these pages. Profile pages are in the page list below, not in the bundles.',
			'The mainland China service (re.bluepoch.com) runs about two versions ahead of the global service (re1999.bluepoch.com): on 2026-11-22 the mainland client is 113.0.1422 (version 4.1) and the global client 111.0.1077 (version 3.9). An arcanist out on the mainland is not in the global game until the global client adds it; the home page lists them.',
			'Numbers are read from the decoded client tables (github.com/St-Pavlov-Foundation/re1999-data for the mainland client, re1999-data-global for the global client). Skill, Psychube and status descriptions are the game\'s own text, unchanged: the Simplified Chinese pages give the mainland client\'s, the other languages the global client\'s text in that language. Where the editions differ on a value or condition, the last section of the page says so. Each page names the client build. Release dates come from the Fandom wiki and the official sites.',
			'Names follow each service: Simplified Chinese from the mainland client, English, Japanese, Korean and Traditional Chinese from the global client. Arcanists out only on the mainland have no official names in those languages yet; their pages use community translations and say so.',
			'Incantations have three ranks (1 to 3 stars); multipliers on the pages are given per rank. Portrait levels change numbers in the kit, and the page lists each change.',
			'Psychube pages give the stats at max level (60) and every changing value of the effect for Amplification 1 to 5, as 16/20/24/28/32%. "Recommended in game for" is the game\'s own recommendation list, not a ranking. A Psychube\'s page is at /psychubes/<its English name in lower case, words joined by hyphens>/ in every language, for example /psychubes/thunderous-applause/.',
			'This is an unofficial site. Tier lists and team builds are absent.',
			'Every page has a Markdown twin: drop the trailing slash and append `.md`.',
		],
		pages: 'Pages',
		home: 'Home page: the index pages, which list every page',
		full: 'All pages in one file',
		digest: 'Answer, caveat, dates and sources of every page, without the body',
		json: 'All pages in every language, with alternative names, as JSON',
		otherLanguage: 'This index in',
		more: 'More',
	},
	'zh-TW': {
		summary: '《重返未來：1999》(Reverse: 1999) 的非官方資料站：神秘學家、技能與強化，以及中國大陸版有、國際版還沒有的內容，讀自遊戲資料。',
		heading: '回答之前',
		notes: [
			'劇情文本：/zh-tw/story/main/、/zh-tw/story/events/、/zh-tw/story/characters/、/zh-tw/story/characters-2/、/zh-tw/story/anecdotes/ 與 /zh-tw/story/other/ 列出各章；章節頁列出各關卡；關卡頁收錄該關的劇情全文，為國際版用戶端（3.9 版）的繁體中文原文。關卡頁不在下方的頁面清單與合輯中。',
			'檔案：/zh-tw/arcanists/<slug>/profile/ 收錄神秘學家的遊戲內檔案（封面、單品、文化、皮膚、語音），為國際版用戶端的繁體中文原文，由該神秘學家的頁面連結。只在中國大陸版推出的皮膚與語音不在檔案頁上。檔案頁在下方的頁面清單中，不在合輯中。',
			'中國大陸版 (re.bluepoch.com) 大約領先國際版 (re1999.bluepoch.com) 兩個版本：2026-11-22 時，中國大陸版用戶端為 113.0.1422（4.1 版），國際版用戶端為 111.0.1077（3.9 版）。在中國大陸版上線的神秘學家，要等國際版用戶端加入後才會出現在國際版遊戲中；首頁列出這些神秘學家。',
			'數值讀自解碼後的用戶端資料表（中國大陸版用戶端為 github.com/St-Pavlov-Foundation/re1999-data，國際版用戶端為 re1999-data-global）。技能、心相與狀態的說明是遊戲原文，未經改寫：簡體中文頁用中國大陸版的文字，其他語言用國際版該語言的文字。各版本在數值或條件上不一致時，頁面最後一節會寫明。每一頁都寫明用戶端版本號。上線日期來自 Fandom wiki 與官方網站。',
			'名稱依各服務而定：簡體中文取自中國大陸版用戶端，英文、日文、韓文與繁體中文取自國際版用戶端。只在中國大陸版上線的神秘學家，在這些語言還沒有官方名稱；她們的頁面使用非官方譯名，並註明這一點。',
			'咒語分三階（1 至 3 星）；頁面上的倍率依階次列出。塑造等級會改變技能組合中的數值，頁面列出每一項變化。',
			'心相頁列出滿級（60 級）的屬性，效果中會變動的數值依增幅 1 至 5 列出，例如 16/20/24/28/32%。「遊戲內推薦」是遊戲自己的推薦清單，不是強度排名。每個心相的網址是 /zh-tw/psychubes/<英文名稱，小寫、以連字號連接>/，例如 /zh-tw/psychubes/thunderous-applause/。',
			'本站是非官方網站。不收錄強度榜與配隊。',
			'每一頁都有 Markdown 版本：去掉網址結尾的斜線，加上 `.md`。',
		],
		pages: '頁面',
		home: '首頁：各索引頁，索引頁列出所有頁面',
		full: '所有頁面合併成一個檔案',
		digest: '每一頁的答案、注意事項、日期與出處，不含內文',
		json: '所有語言的所有頁面與別名，JSON 格式',
		otherLanguage: '本索引的其他語言',
		more: '更多',
	},
	'zh-CN': {
		summary: '《重返未来：1999》(Reverse: 1999) 的非官方资料站：神秘学家、技能与强化，以及中国大陆版有、国际版还没有的内容，读自游戏数据。',
		heading: '回答之前',
		notes: [
			'剧情文本：/zh-cn/story/main/、/zh-cn/story/events/、/zh-cn/story/characters/、/zh-cn/story/characters-2/、/zh-cn/story/anecdotes/ 与 /zh-cn/story/other/ 列出各章；章节页列出各关卡；关卡页收录该关的剧情全文，为中国大陆版客户端（4.1 版）的简体中文原文。关卡页不在下方的页面清单与合辑中。',
			'档案：/zh-cn/arcanists/<slug>/profile/ 收录神秘学家的游戏内档案（封面、单品、文化、皮肤、语音），为中国大陆版客户端（4.1 版）的简体中文原文，由该神秘学家的页面链接。条目与国际版相同，只在中国大陆版推出的皮肤与语音不在档案页上。档案页在下方的页面清单中，不在合辑中。',
			'中国大陆版 (re.bluepoch.com) 大约领先国际版 (re1999.bluepoch.com) 两个版本：2026-11-22 时，中国大陆版客户端为 113.0.1422（4.1 版），国际版客户端为 111.0.1077（3.9 版）。在中国大陆版上线的神秘学家，要等国际版客户端加入后才会出现在国际版游戏中；首页列出这些神秘学家。',
			'数值读自解码后的客户端数据表（中国大陆版客户端为 github.com/St-Pavlov-Foundation/re1999-data，国际版客户端为 re1999-data-global）。技能、心相与状态的说明是游戏原文，未经改写：简体中文页用中国大陆版的文字，其他语言用国际版该语言的文字。各版本在数值或条件上不一致时，页面最后一节会写明。每一页都写明客户端版本号。上线日期来自 Fandom wiki 与官方网站。',
			'名称依各服务而定：简体中文取自中国大陆版客户端，英文、日文、韩文与繁体中文取自国际版客户端。只在中国大陆版上线的神秘学家，在这些语言还没有官方名称；她们的页面使用非官方译名，并注明这一点。',
			'咒语分三阶（1 至 3 星）；页面上的倍率按阶次列出。塑造等级会改变技能组合中的数值，页面列出每一项变化。',
			'心相页列出满级（60 级）的属性，效果中会变动的数值按增幅 1 至 5 列出，例如 16/20/24/28/32%。“游戏内推荐”是游戏自己的推荐清单，不是强度排名。每个心相的网址是 /zh-cn/psychubes/<英文名称，小写、以连字号连接>/，例如 /zh-cn/psychubes/thunderous-applause/。',
			'本站是非官方网站。不收录强度榜与配队。',
			'每一页都有 Markdown 版本：去掉网址结尾的斜线，加上 `.md`。',
		],
		pages: '页面',
		home: '首页：各索引页，索引页列出所有页面',
		full: '所有页面合并成一个文件',
		digest: '每一页的答案、注意事项、日期与出处，不含正文',
		json: '所有语言的所有页面与别名，JSON 格式',
		otherLanguage: '本索引的其他语言',
		more: '更多',
	},
	ja: {
		summary: '『リバース：1999』(Reverse: 1999) の非公式資料サイト。神秘学家、そのスキルと強化、そして中国本土版にあってグローバル版にまだないものを、ゲームデータから読み取ってまとめている。',
		heading: '回答の前に',
		notes: [
			'ストーリーのテキスト：/ja/story/main/、/ja/story/events/、/ja/story/characters/、/ja/story/characters-2/、/ja/story/anecdotes/、/ja/story/other/ が章を挙げ、章のページがステージを挙げ、ステージのページにそのステージの全文がグローバル版クライアント（バージョン 3.9）の日本語のまま載っている。ステージのページは下のページ一覧とバンドルには含まれない。',
			'プロフィール：/ja/arcanists/<slug>/profile/ に神秘学家のゲーム内の資料（表紙、単品、文化、コスチューム、ボイス）がグローバル版クライアントの日本語のまま載っており、その神秘学家のページからリンクされている。中国本土版だけで登場したコスチュームとボイスは載っていない。プロフィールのページは下のページ一覧にあり、バンドルには含まれない。',
			'中国本土版 (re.bluepoch.com) はグローバル版 (re1999.bluepoch.com) よりおよそ2バージョン先を進んでいる。2026-11-22 の中国本土版クライアントは 113.0.1422（バージョン 4.1）、グローバル版クライアントは 111.0.1077（バージョン 3.9）である。中国本土版で実装された神秘学家は、グローバル版クライアントに追加されるまでグローバル版のゲームにはいない。ホームページにその一覧がある。',
			'数値は、デコードされたクライアントのテーブル（中国本土版クライアントは github.com/St-Pavlov-Foundation/re1999-data、グローバル版クライアントは re1999-data-global）から読み取っている。スキル・心相・状態の説明はゲームの原文そのままで、簡体字中国語のページは中国本土版、ほかの言語はグローバル版のその言語のテキストである。版によって数値や条件が違う場合は、ページ最後の節に記している。各ページにクライアントのビルドを記している。実装日は Fandom wiki と公式サイトから取っている。',
			'名前は各サービスに従う。簡体字中国語は中国本土版クライアント、英語、日本語、韓国語、繁体字中国語はグローバル版クライアントから取る。中国本土版にしかいない神秘学家には、これらの言語の公式名がまだない。そのページは非公式の訳を使い、そのことを明記している。',
			'スペルには3つのランク（★1〜★3）がある。ページの倍率はランクごとに記している。塑造のレベルはスキル構成の数値を変え、ページはその変化を1つずつ載せている。',
			'心相のページは最大レベル（60）のステータスと、効果の変わる値を増幅1〜5の順に 16/20/24/28/32% の形で載せている。「ゲーム内のおすすめ」はゲーム自身のおすすめ一覧で、強さの順位ではない。各心相のページは /ja/psychubes/<英語名を小文字にしてハイフンでつないだもの>/ にある（例：/ja/psychubes/thunderous-applause/）。',
			'このサイトは非公式である。ティアリストと編成は載せていない。',
			'どのページにも Markdown 版がある。URL 末尾のスラッシュを取り、`.md` を付ける。',
		],
		pages: 'ページ',
		home: 'ホームページ：各索引ページ。索引ページがすべてのページを載せています',
		full: 'すべてのページを1つのファイルにまとめたもの',
		digest: '各ページの答え、注意点、日付、出典（本文なし）',
		json: 'すべての言語のすべてのページと別名（JSON）',
		otherLanguage: 'この索引の他の言語',
		more: 'その他',
	},
	ko: {
		summary: '「리버스: 1999」(Reverse: 1999)의 비공식 자료 사이트. 마도학자와 그 스킬과 강화, 그리고 중국 본토 서비스에는 있고 글로벌 서비스에는 아직 없는 것을 게임 데이터에서 읽어 정리한다.',
		heading: '답하기 전에',
		notes: [
			'스토리 텍스트: /ko/story/main/, /ko/story/events/, /ko/story/characters/, /ko/story/characters-2/, /ko/story/anecdotes/, /ko/story/other/가 장을 나열하고, 장 페이지가 스테이지를 나열하며, 스테이지 페이지에는 글로벌 클라이언트(3.9 버전)의 한국어 원문 그대로 그 스테이지의 전문이 있다. 스테이지 페이지는 아래 페이지 목록과 번들에 없다.',
			'프로필: /ko/arcanists/<slug>/profile/에 마도학자의 게임 내 파일(표지, 물품, 문화, 스킨, 음성)이 글로벌 클라이언트의 한국어 원문 그대로 있으며, 그 마도학자의 페이지가 링크한다. 중국 본토 서비스에만 나온 스킨과 음성은 없다. 프로필 페이지는 아래 페이지 목록에 있고 번들에는 없다.',
			'중국 본토 서비스(re.bluepoch.com)는 글로벌 서비스(re1999.bluepoch.com)보다 약 두 버전 앞서 있다. 2026-11-22 기준 중국 본토 클라이언트는 113.0.1422(4.1 버전), 글로벌 클라이언트는 111.0.1077(3.9 버전)이다. 중국 본토에 출시된 마도학자는 글로벌 클라이언트에 추가되기 전까지 글로벌 게임에 없다. 홈페이지에 그 목록이 있다.',
			'수치는 디코딩된 클라이언트 테이블(중국 본토 클라이언트는 github.com/St-Pavlov-Foundation/re1999-data, 글로벌 클라이언트는 re1999-data-global)에서 읽었다. 스킬·의지·상태 설명은 게임 원문 그대로이며, 간체 중국어 페이지는 중국 본토 클라이언트, 다른 언어는 글로벌 클라이언트의 해당 언어 텍스트다. 판본마다 수치나 조건이 다르면 페이지 마지막 절에 적는다. 각 페이지에 클라이언트 빌드를 적는다. 출시일은 Fandom 위키와 공식 사이트에서 가져왔다.',
			'이름은 각 서비스를 따른다. 간체 중국어는 중국 본토 클라이언트, 영어, 일본어, 한국어, 번체 중국어는 글로벌 클라이언트에서 가져온다. 중국 본토에만 출시된 마도학자는 이들 언어의 공식 이름이 아직 없다. 그 페이지는 비공식 번역을 쓰며 그 사실을 밝힌다.',
			'주문에는 세 단계(1~3성)가 있으며, 페이지의 계수는 단계별로 적는다. 형상 레벨은 스킬 구성의 수치를 바꾸며, 페이지는 각 변화를 나열한다.',
			'의지 페이지는 최대 레벨(60)의 스탯과, 효과에서 바뀌는 값을 증폭 1~5 순서로 16/20/24/28/32% 형태로 적는다. "게임 내 추천"은 게임 자체의 추천 목록이며 강함의 순위가 아니다. 각 의지 페이지는 /ko/psychubes/<영어 이름을 소문자로, 단어를 하이픈으로 이은 것>/에 있다(예: /ko/psychubes/thunderous-applause/).',
			'이 사이트는 비공식 사이트다. 티어 리스트와 덱 구성은 없다.',
			'모든 페이지에 Markdown 버전이 있다. URL 끝의 슬래시를 빼고 `.md`를 붙인다.',
		],
		pages: '페이지',
		home: '홈페이지: 각 색인 페이지. 색인 페이지가 모든 페이지를 나열합니다',
		full: '모든 페이지를 한 파일로 합친 것',
		digest: '각 페이지의 답, 주의 사항, 날짜, 출처(본문 제외)',
		json: '모든 언어의 모든 페이지와 다른 이름(JSON)',
		otherLanguage: '이 색인의 다른 언어',
		more: '더 보기',
	},
};

/** UI labels for the facts shown on every page, in both outputs. */
export const LABELS = {
	en: {
		appliesTo: 'Applies to',
		caveat: 'Caveat',
		effectiveDate: 'Source dated',
		lastVerified: 'Last verified',
		aliases: 'Also written',
		sources: 'Sources',
		art: 'Art',
		artBy: 'Bluepoch; files from the Reverse: 1999 Wiki (Fandom)',
		markdown: 'Markdown',
		page: 'Page',
		otherLanguage: 'Other language',
		allPages: 'All pages',
		home: 'Home',
		pageList: 'list of all pages',
		unofficial: 'unofficial',
		sections: 'Sections',
	},
	'zh-TW': {
		appliesTo: '適用範圍',
		caveat: '注意事項',
		effectiveDate: '來源日期',
		lastVerified: '最後查證',
		aliases: '其他寫法',
		sources: '出處',
		art: '美術',
		artBy: '深藍互動；檔案取自 Reverse: 1999 Wiki（Fandom）',
		markdown: 'Markdown',
		page: '頁面',
		otherLanguage: '其他語言',
		allPages: '所有頁面',
		home: '首頁',
		pageList: '所有頁面清單',
		unofficial: '非官方',
		sections: '分類',
	},
	'zh-CN': {
		appliesTo: '适用范围',
		caveat: '注意事项',
		effectiveDate: '来源日期',
		lastVerified: '最后查证',
		aliases: '其他写法',
		sources: '出处',
		art: '美术',
		artBy: '深蓝互动；文件取自 Reverse: 1999 Wiki（Fandom）',
		markdown: 'Markdown',
		page: '页面',
		otherLanguage: '其他语言',
		allPages: '所有页面',
		home: '首页',
		pageList: '所有页面清单',
		unofficial: '非官方',
		sections: '分类',
	},
	ja: {
		appliesTo: '対象',
		caveat: '注意点',
		effectiveDate: '出典の日付',
		lastVerified: '最終確認',
		aliases: '別表記',
		sources: '出典',
		art: 'アート',
		artBy: 'Bluepoch、ファイルは Reverse: 1999 Wiki（Fandom）より',
		markdown: 'Markdown',
		page: 'ページ',
		otherLanguage: '他の言語',
		allPages: 'すべてのページ',
		home: 'ホーム',
		pageList: 'ページ一覧',
		unofficial: '非公式',
		sections: 'セクション',
	},
	ko: {
		appliesTo: '적용 범위',
		caveat: '주의 사항',
		effectiveDate: '출처 날짜',
		lastVerified: '마지막 확인',
		aliases: '다른 표기',
		sources: '출처',
		art: '아트',
		artBy: 'Bluepoch, 파일은 Reverse: 1999 Wiki(Fandom)에서',
		markdown: 'Markdown',
		page: '페이지',
		otherLanguage: '다른 언어',
		allPages: '모든 페이지',
		home: '홈',
		pageList: '페이지 목록',
		unofficial: '비공식',
		sections: '섹션',
	},
};

/** Format a Date (or date string) as YYYY-MM-DD. */
export function isoDate(d) {
	return new Date(d).toISOString().slice(0, 10);
}
