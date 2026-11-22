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
export const LLMS_NOTES = {
	en: {
		summary: DESCRIPTION,
		heading: 'Before you answer',
		notes: [
			'The mainland China service (re.bluepoch.com) runs about two versions ahead of the global service (re1999.bluepoch.com): on 2026-11-22 the mainland client is 113.0.1422 (version 4.1) and the global client 111.0.1077 (version 3.9). An arcanist out on the mainland is not in the global game until the global client adds it; the home page lists them.',
			'Skill text and numbers are read from the decoded client tables (github.com/St-Pavlov-Foundation/re1999-data for the mainland client, re1999-data-global for the global client) and restated; each page names the client build. Release dates come from the Fandom wiki and the official sites.',
			'Names follow each service: Simplified Chinese from the mainland client, English, Japanese, Korean and Traditional Chinese from the global client. Arcanists out only on the mainland have no official names in those languages yet; their pages use community translations and say so.',
			'Incantations have three ranks (1 to 3 stars); multipliers on the pages are given per rank. Portrait levels change numbers in the kit, and the page lists each change.',
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
			'中國大陸版 (re.bluepoch.com) 大約領先國際版 (re1999.bluepoch.com) 兩個版本：2026-11-22 時，中國大陸版用戶端為 113.0.1422（4.1 版），國際版用戶端為 111.0.1077（3.9 版）。在中國大陸版上線的神秘學家，要等國際版用戶端加入後才會出現在國際版遊戲中；首頁列出這些神秘學家。',
			'技能文字與數值讀自解碼後的用戶端資料表（中國大陸版用戶端為 github.com/St-Pavlov-Foundation/re1999-data，國際版用戶端為 re1999-data-global），並重新改寫；每一頁都寫明用戶端版本號。上線日期來自 Fandom wiki 與官方網站。',
			'名稱依各服務而定：簡體中文取自中國大陸版用戶端，英文、日文、韓文與繁體中文取自國際版用戶端。只在中國大陸版上線的神秘學家，在這些語言還沒有官方名稱；她們的頁面使用非官方譯名，並註明這一點。',
			'咒語分三階（1 至 3 星）；頁面上的倍率依階次列出。塑造等級會改變技能組合中的數值，頁面列出每一項變化。',
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
			'中国大陆版 (re.bluepoch.com) 大约领先国际版 (re1999.bluepoch.com) 两个版本：2026-11-22 时，中国大陆版客户端为 113.0.1422（4.1 版），国际版客户端为 111.0.1077（3.9 版）。在中国大陆版上线的神秘学家，要等国际版客户端加入后才会出现在国际版游戏中；首页列出这些神秘学家。',
			'技能文字与数值读自解码后的客户端数据表（中国大陆版客户端为 github.com/St-Pavlov-Foundation/re1999-data，国际版客户端为 re1999-data-global），并重新改写；每一页都写明客户端版本号。上线日期来自 Fandom wiki 与官方网站。',
			'名称依各服务而定：简体中文取自中国大陆版客户端，英文、日文、韩文与繁体中文取自国际版客户端。只在中国大陆版上线的神秘学家，在这些语言还没有官方名称；她们的页面使用非官方译名，并注明这一点。',
			'咒语分三阶（1 至 3 星）；页面上的倍率按阶次列出。塑造等级会改变技能组合中的数值，页面列出每一项变化。',
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
			'中国本土版 (re.bluepoch.com) はグローバル版 (re1999.bluepoch.com) よりおよそ2バージョン先を進んでいる。2026-11-22 の中国本土版クライアントは 113.0.1422（バージョン 4.1）、グローバル版クライアントは 111.0.1077（バージョン 3.9）である。中国本土版で実装された神秘学家は、グローバル版クライアントに追加されるまでグローバル版のゲームにはいない。ホームページにその一覧がある。',
			'スキルの説明と数値は、デコードされたクライアントのテーブル（中国本土版クライアントは github.com/St-Pavlov-Foundation/re1999-data、グローバル版クライアントは re1999-data-global）から読み取り、書き直したものである。各ページにクライアントのビルドを記している。実装日は Fandom wiki と公式サイトから取っている。',
			'名前は各サービスに従う。簡体字中国語は中国本土版クライアント、英語、日本語、韓国語、繁体字中国語はグローバル版クライアントから取る。中国本土版にしかいない神秘学家には、これらの言語の公式名がまだない。そのページは非公式の訳を使い、そのことを明記している。',
			'スペルには3つのランク（★1〜★3）がある。ページの倍率はランクごとに記している。塑造のレベルはスキル構成の数値を変え、ページはその変化を1つずつ載せている。',
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
			'중국 본토 서비스(re.bluepoch.com)는 글로벌 서비스(re1999.bluepoch.com)보다 약 두 버전 앞서 있다. 2026-11-22 기준 중국 본토 클라이언트는 113.0.1422(4.1 버전), 글로벌 클라이언트는 111.0.1077(3.9 버전)이다. 중국 본토에 출시된 마도학자는 글로벌 클라이언트에 추가되기 전까지 글로벌 게임에 없다. 홈페이지에 그 목록이 있다.',
			'스킬 설명과 수치는 디코딩된 클라이언트 테이블(중국 본토 클라이언트는 github.com/St-Pavlov-Foundation/re1999-data, 글로벌 클라이언트는 re1999-data-global)에서 읽어 다시 쓴 것이다. 각 페이지에 클라이언트 빌드를 적는다. 출시일은 Fandom 위키와 공식 사이트에서 가져왔다.',
			'이름은 각 서비스를 따른다. 간체 중국어는 중국 본토 클라이언트, 영어, 일본어, 한국어, 번체 중국어는 글로벌 클라이언트에서 가져온다. 중국 본토에만 출시된 마도학자는 이들 언어의 공식 이름이 아직 없다. 그 페이지는 비공식 번역을 쓰며 그 사실을 밝힌다.',
			'주문에는 세 단계(1~3성)가 있으며, 페이지의 계수는 단계별로 적는다. 형상 레벨은 스킬 구성의 수치를 바꾸며, 페이지는 각 변화를 나열한다.',
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
