// Acceptance checks on the built site in dist/. Run with `pnpm check` after `pnpm build`.
// Fails (exit 1) when an agent would get a worse page than a human does.
//
//  1. Pairing: every HTML page has a Markdown twin, an alternate link, a visible
//     link to the twin, and entries in llms.txt and index.json.
//  2. Clean Markdown: no JSX, no MDX imports, no `:::` directives.
//  3. First 5,000 characters: the answer, scope and caveat appear within the first
//     5,000 characters of the Markdown twin and of the text extracted from the HTML.
//  4. Equivalence: headings and code blocks extracted from the HTML match the twin.
//  5. No decoration leak: marks the skin draws with CSS must not appear in the
//     text extracted from the HTML.
//     Home page: it links every page, or an index page that links it.
//  6. Language parity: every language has the same pages, dates, sources, names, code
//     blocks and link targets. Japanese and Korean are partial: a page they lack must be
//     listed in records/pending.json, a listed page must not exist, links to listed pages
//     are absent from that language, and Starlight's English fallback at such an address
//     is noindex and listed nowhere.
//  7. Bundles: each language's llms-full.txt and llms-small.txt carry every page's
//     answer and caveat; a hidden pointer to the Markdown twin survives extraction.
//  8. llms.txt: notes, bundles and other languages within the first 5,000 characters.
//  9. The 404 page links each language's home page and page list.
// 10. robots.txt names the sitemap and carries a Content-Signal line.
// 11. The header links the first page of each sidebar section (none while the site has one); the page notes link the Markdown twin, llms.txt and index.json; no text in <main>
//     is about the site or the page; every footnote links a listed source (scripts/check-page-text.mjs).
// Being found: title, description, canonical, hreflang and sitemap (scripts/check-found.mjs).

import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { JSDOM } from 'jsdom';
import { Readability } from '@mozilla/readability';
import TurndownService from 'turndown';
import { SITE, LOCALES, LLMS_NOTES, localeOf, bareId, idInLocale, htmlPath, mdPath, llmsPath, withBase, isStage, isStoryText, isProfile, isGameText, hidesAnswer } from '../src/lib/site.mjs';
import { bundlePath } from '../src/lib/llms.mjs';
import { readPages, readPending } from '../src/lib/content-index.mjs';
import { checkFound } from './check-found.mjs';
import { checkHeaderAndOutputs, checkSelfReference, checkOpening, checkFootnotes } from './check-page-text.mjs';
import { checkProse } from './prose-review.mjs';

const DIST = fileURLToPath(new URL('../dist/', import.meta.url));
const LIMIT = 5000;
// The top-level sidebar groups, in order, by the id of their first page (astro.config.mjs).
const SECTIONS = ['afflatus/star', 'psychubes/critical', 'systems/summoning', 'story/main'];
const failures = [];
const fail = (page, message) => failures.push(`${page}: ${message}`);

const read = (path) => readFileSync(join(DIST, path), 'utf8');
// Arcanists out on the mainland service only: their kit is game text in Simplified Chinese alone, so
// the zh-cn page has kit headings the other languages lack. The same for Psychubes, below.
const MAINLAND_ONLY = new Set(JSON.parse(readFileSync(new URL('../records/arcanists.json', import.meta.url), 'utf8'))
	.arcanists.filter((a) => !a.inGlobal).map((a) => `arcanists/${a.slug}`));
// Psychubes out on the mainland service only: their effect is game text in Simplified Chinese alone.
for (const p of JSON.parse(readFileSync(new URL('../records/psychubes.json', import.meta.url), 'utf8')).psychubes) {
	if (!p.inGlobal) MAINLAND_ONLY.add(`psychubes/${p.slug}`);
}
// Pages whose sections between the profile table and the names table are the game's text: the kit
// of an arcanist (pipeline/kit_text.py) and the effect of a Psychube (pipeline/psychube.py).
const KIT_PAGES = new Set([
	...JSON.parse(readFileSync(new URL('../records/arcanists.json', import.meta.url), 'utf8')).arcanists.map((a) => `arcanists/${a.slug}`),
	...JSON.parse(readFileSync(new URL('../records/psychubes.json', import.meta.url), 'utf8')).psychubes.map((p) => `psychubes/${p.slug}`),
]);
/** The page with the game's text of a kit or Psychube page taken out: every section but the last (names). */
function withoutGameText(doc, id) {
	if (!KIT_PAGES.has(bareId(id))) return doc;
	const copy = doc.cloneNode(true);
	const heads = [...copy.querySelectorAll('.sl-markdown-content > .sl-heading-wrapper.level-h2')];
	if (heads.length < 2) return copy;
	for (let el = heads[0]; el && el !== heads.at(-1); ) {
		const next = el.nextElementSibling;
		el.remove();
		el = next;
	}
	return copy;
}
const normalize = (text) => text.replace(/\s+/g, ' ').trim();

/** Fenced code blocks of a Markdown string, as trimmed strings. */
function codeBlocks(markdown) {
	return [...markdown.matchAll(/^```[^\n]*\n([\s\S]*?)^```/gm)].map((m) => m[1].trim());
}
/** ATX headings of a Markdown string outside code blocks, as `level text`. */
function headings(markdown) {
	const withoutCode = markdown.replace(/^```[^\n]*\n[\s\S]*?^```/gm, '');
	return [...withoutCode.matchAll(/^(#{1,6}) (.+)$/gm)].map((m) => `${m[1].length} ${m[2].trim()}`);
}

if (!existsSync(DIST)) {
	console.error('dist/ not found. Run `pnpm build` first.');
	process.exit(1);
}

const pages = readPages();
const byId = new Map(pages.map((p) => [p.id, p]));
const ids = new Set(pages.map((p) => p.id));
const english = pages.filter((p) => localeOf(p.id) === LOCALES[0]);

// Partial languages. records/pending.json lists, per content folder, the English pages that
// language does not have yet. Every other English page must exist in every language.
const pendingRaw = readPending();
/** Locale -> set of bare page ids that language lacks. */
const pending = new Map(LOCALES.map((l) => [l, new Set()]));
for (const [dir, list] of Object.entries(pendingRaw)) {
	const locale = LOCALES.find((l) => l.dir && l.dir === dir);
	if (!locale) {
		fail('records/pending.json', `"${dir}" is not a language folder of the site`);
		continue;
	}
	for (const bare of list) {
		if (!ids.has(bare)) fail('records/pending.json', `${dir}: ${bare} is not an English page`);
		if (ids.has(idInLocale(bare, locale))) fail('records/pending.json', `${dir}: ${bare} is listed as pending, but ${idInLocale(bare, locale)} exists`);
		pending.get(locale).add(bare);
	}
}
const isPending = (bare, locale) => pending.get(locale).has(bare);
for (const { id } of english) {
	for (const locale of LOCALES.slice(1)) {
		const otherId = idInLocale(id, locale);
		if (!ids.has(otherId) && !isPending(id, locale)) fail(otherId, `missing: no ${locale.label} version of ${id}, and records/pending.json does not list it`);
	}
}
for (const { id } of pages) {
	if (!ids.has(bareId(id))) fail(id, `no English page ${bareId(id)}`);
}

/** Prose of a Markdown body: code blocks removed. */
const prose = (body) => body.replace(/^```[^\n]*\n[\s\S]*?^```/gm, '');
/** Whether an internal link names a file (an image) rather than a page. */
const isFile = (path) => /\.[a-z0-9]+$/i.test(path);
/** Page id named by an internal link path: `/ja/operators/` -> `ja/operators`, `/` -> `index`. */
function idFromLink(path) {
	const trimmed = path.replace(/^\/+|\/+$/g, '');
	return trimmed === '' ? 'index' : trimmed;
}
/** Internal link paths of a body outside code, in order. */
const internalLinks = (body) => [...prose(body).matchAll(/\]\((\/[^)\s#]*)/g)].map((m) => m[1]);
/** Link targets of a body: pages without their language prefix, files as written. */
const linkTargets = (body) => new Set(internalLinks(body).map((path) => (isFile(path) ? path : bareId(idFromLink(path)))));

/** The first 5,000 characters a readability-style extractor returns for each page. jsdom frees a
 * closed window only once the event loop runs, so this yields after each page. */
async function extractHeads(list) {
	const heads = [];
	for (const p of list) {
		const file = (htmlPath(p.id) + 'index.html').slice(1);
		const w = new JSDOM(read(file), { url: SITE + htmlPath(p.id) }).window;
		const parsed = new Readability(w.document).parse();
		w.close();
		heads.push(turndown.turndown(parsed?.content ?? '').slice(0, LIMIT));
		await new Promise((resolve) => setImmediate(resolve));
	}
	return heads;
}

/** The bundles, read once: path -> normalized text. */
const bundles = new Map();
/** Each language's llms.txt, by locale. */
const llmsTxt = new Map(LOCALES.map((l) => [l, read(llmsPath(l).slice(1))]));
const indexJson = JSON.parse(read('index.json'));
const indexed = new Set(indexJson.pages.map((p) => p.markdown));
const turndown = new TurndownService({ headingStyle: 'atx', codeBlockStyle: 'fenced' });

// Every HTML file in dist must belong to a known page (or be the 404 page).
function htmlFiles(dir) {
	return readdirSync(dir, { withFileTypes: true }).flatMap((e) =>
		e.isDirectory()
			? e.name.startsWith('_') || e.name === 'pagefind'
				? []
				: htmlFiles(join(dir, e.name))
			: e.name.endsWith('.html')
				? [relative(DIST, join(dir, e.name)).replace(/\\/g, '/')]
				: []
	);
}
const expectedHtml = new Set(pages.map((p) => (htmlPath(p.id) + 'index.html').slice(1)));
/** Starlight's English fallbacks at the addresses of pending pages: file -> locale page id. */
const fallbackHtml = new Map(
	[...pending].flatMap(([locale, set]) => [...set].map((bare) => [(htmlPath(idInLocale(bare, locale)) + 'index.html').slice(1), idInLocale(bare, locale)]))
);
for (const file of htmlFiles(DIST)) {
	if (file === '404.html' || expectedHtml.has(file)) continue;
	if (!fallbackHtml.has(file)) {
		fail(file, 'HTML page without a content entry');
		continue;
	}
	// A fallback is not a page of its language: noindex, no hreflang, no JSON-LD, not searched.
	const head = new JSDOM(read(file)).window.document;
	if (head.querySelector('meta[name="robots"]')?.getAttribute('content') !== 'noindex') fail(file, 'fallback page without <meta name="robots" content="noindex">');
	if (head.querySelector('link[hreflang]')) fail(file, 'fallback page with hreflang links');
	if (head.querySelector('script[type="application/ld+json"]')) fail(file, 'fallback page with JSON-LD');
	if (head.querySelector('[data-pagefind-body]')) fail(file, 'fallback page in the site search');
}
// No output for agents names a fallback address or a twin of one.
const fallbackUrls = [...fallbackHtml.values()].flatMap((id) => [SITE + htmlPath(id), SITE + mdPath(id)]);
const outputs = [
	['index.json', read('index.json')],
	...LOCALES.flatMap((l) => [llmsPath(l), bundlePath(l, 'full'), bundlePath(l, 'small')].map((path) => [path, read(path.slice(1))])),
];
for (const [name, text] of outputs) {
	for (const url of fallbackUrls) if (text.includes(url + ')') || text.includes(url + '>') || text.includes(url + '"') || text.includes(url + '\n')) fail(name, `names ${url}, a page its language does not have`);
}
for (const id of fallbackHtml.values()) {
	if (existsSync(join(DIST, mdPath(id).slice(1)))) fail(mdPath(id), 'Markdown twin of a page its language does not have');
}

// Each page opens two DOMs. jsdom frees a closed window only once the event loop runs, so a
// loop that never yields kept every document and passed Node's 4 GB heap at 700 pages: close
// the previous page's windows and yield.
let openWindows = [];
// scripts/check-dist-parallel.mjs runs this script in several processes, each on every n-th page
// (CHECK_SHARD=i/n); the checks of the whole site run in the first.
const [SHARD, SHARDS] = (process.env.CHECK_SHARD ?? '0/1').split('/').map(Number);
for (const [k, { id, data }] of pages.entries()) {
	if (k % SHARDS !== SHARD) continue;
	if (openWindows.length) {
		for (const w of openWindows) w.close();
		openWindows = [];
		await new Promise((resolve) => setImmediate(resolve));
	}
	const mdFile = mdPath(id).slice(1);
	const htmlFile = (htmlPath(id) + 'index.html').slice(1);
	if (!existsSync(join(DIST, htmlFile))) {
		fail(id, `missing HTML page ${htmlFile}`);
		continue;
	}
	if (!existsSync(join(DIST, mdFile))) {
		fail(id, `missing Markdown twin ${mdFile}`);
		continue;
	}
	const md = read(mdFile);
	const html = read(htmlFile);
	const dom = new JSDOM(html, { url: SITE + htmlPath(id) });
	const doc = dom.window.document;
	openWindows.push(dom.window);

	// 1. Pairing
	const alternate = doc.querySelector('link[rel="alternate"][type="text/markdown"]');
	if (alternate?.getAttribute('href') !== SITE + mdPath(id)) fail(id, 'missing or wrong <link rel="alternate" type="text/markdown">');
	if (!doc.querySelector(`main a[href="${withBase(mdPath(id))}"]`)) fail(id, 'no visible link to the Markdown twin inside <main>');
	// A story stage is listed by its chapter page, not in llms.txt or the bundles (src/lib/llms.mjs).
	if (!isStage(id) && !llmsTxt.get(localeOf(id)).includes(SITE + mdPath(id))) fail(id, `Markdown twin not listed in ${llmsPath(localeOf(id))}`);
	if (!indexed.has(SITE + mdPath(id))) fail(id, 'page not listed in index.json');
	if (!doc.querySelector('script[type="application/ld+json"]')) fail(id, 'missing JSON-LD');

	// 7. Bundles and the pointer for agents
	for (const set of isStage(id) || isProfile(id) ? [] : ['full', 'small']) {
		const path = bundlePath(localeOf(id), set);
		if (!bundles.has(path)) bundles.set(path, normalize(read(path.slice(1))));
		const bundle = bundles.get(path);
		for (const text of [data.description, data.caveat]) {
			if (!bundle.includes(normalize(String(text)))) fail(id, `answer or caveat missing from ${bundlePath(localeOf(id), set)}`);
		}
			}
	const note = doc.querySelector('main .agent-note');
	if (!note?.textContent.includes(SITE + mdPath(id)) || !note.textContent.includes(SITE + llmsPath(localeOf(id)))) fail(id, 'missing hidden pointer to the Markdown twin and the page list');
	// A profile or stage page shows no answer line; its hidden note carries the description.
	if (hidesAnswer(id) ? doc.querySelector('main .answer') || !note?.textContent.includes(String(data.description)) : !doc.querySelector('main .answer')) {
		fail(id, hidesAnswer(id) ? 'the page shows the answer line, or its hidden note lacks the description' : 'no answer line under the title');
	}
	if (note && (note.hasAttribute('hidden') || note.getAttribute('aria-hidden') === 'true' || note.getAttribute('style'))) {
		fail(id, 'the pointer for agents must be hidden by CSS class only, or extractors drop it');
	}

	// 2. Clean Markdown
	const mdProse = md.replace(/^```[^\n]*\n[\s\S]*?^```/gm, '').replace(/`[^`\n]*`/g, '');
	if (/(?<!\\)<[A-Z][A-Za-z]*[\s/>]/.test(mdProse)) fail(id, 'JSX component tag in Markdown twin');
	if (/^import\s.+from\s/m.test(mdProse)) fail(id, 'MDX import in Markdown twin');
	if (/^:::/m.test(mdProse)) fail(id, '`:::` directive in Markdown twin');

	// The answer under the title is one short sentence: LOCALES gives each language's limit
	// (English 110, Chinese 70, Japanese 70, Korean 90 characters).
	const maxAnswer = localeOf(id).maxDescription;
	// On a page about one thing (a character, a chapter), the answer line does not repeat the game's
	// name: the reader is on that game's wiki (root AGENTS.md, Content contract).
	{
		const loc = localeOf(id);
		const bare = loc.dir && id.startsWith(loc.dir + '/') ? id.slice(loc.dir.length + 1) : id;
		const home = pages.find((p) => p.id === (loc.dir || 'index'))?.data;
		if (home && /^(arcanists|psychubes|story)\/(?!(main|events|characters|characters-2|anecdotes|other|critical|damage-6|damage-5|might|survival)$)./.test(bare)) {
			const names = [home.title, ...(home.aliases ?? [])].map((n) => String(n).replace(/\s*(wiki|위키)$/i, '')).filter((n) => n.length >= 3);
			const hit = names.find((n) => String(data.description).includes(n));
			if (hit) fail(id, `the answer line repeats the game's name (${hit}); the page is about one thing of the game`);
		}
	}
	if (String(data.description).length > maxAnswer) fail(id, `description is ${String(data.description).length} characters; the limit is ${maxAnswer}`);

	// 3. First 5,000 characters
	const required = [
		['answer', data.description],
		['scope', data.appliesTo],
		['caveat', data.caveat],
	];
	const mdHead = normalize(md.slice(0, LIMIT));
	for (const [name, text] of required) {
		if (!mdHead.includes(normalize(String(text)))) fail(id, `${name} not within the first ${LIMIT} characters of the Markdown twin`);
	}
	// Worst case for HTML: a fetch tool that keeps the whole body, navigation included.
	for (const el of doc.querySelectorAll('script, style, template, svg')) el.remove();
	const bodyHead = normalize(doc.body.textContent).slice(0, LIMIT);
	for (const [name, text] of required) {
		if (!bodyHead.includes(normalize(String(text)))) fail(id, `${name} not within the first ${LIMIT} characters of the full HTML text`);
	}

	// 4. Equivalence, on the article that a readability-style extractor keeps.
	const articleDom = new JSDOM(html, { url: SITE + htmlPath(id) });
	openWindows.push(articleDom.window);
	const article = new Readability(articleDom.window.document).parse();
	const mainEl = doc.querySelector('main');
	const extracted = turndown.turndown(mainEl.innerHTML);
	const mdBody = md.slice(md.indexOf('\n---\n') + 5);
	// Starlight curls apostrophes in the HTML (Echoes' Embrace); compare them straight.
	// The HTML renderer curls quotes and joins three dots.
	const straight = (h) => h.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"').replace(/\u2026/g, '...');
	// Emphasis marks are dropped on both sides: the twin writes *x* where the extractor writes _x_.
	// (A bare _ inside a word of the twin is a letter; the extractor escapes it.)
	const noMarks = (h) => h.replace(/(?<!\\)(\*+|~~)/g, '');
	const wantHeadings = headings(mdBody).map((h) => straight(normalize(noMarks(h.replace(/`/g, '')).replace(/\\([<>*_[\]~])/g, '$1'))));
	const gotHeadings = headings(extracted)
		.filter((h) => !h.startsWith('1 '))
		.map((h) => straight(normalize(noMarks(h).replace(/(?<!\\)_+/g, '').replace(/\\/g, '').replace(/`/g, ''))));
	if (JSON.stringify(wantHeadings) !== JSON.stringify(gotHeadings)) {
		fail(id, `headings differ between HTML and Markdown twin\n    md:   ${wantHeadings.join(' | ')}\n    html: ${gotHeadings.join(' | ')}`);
	}
	const wantCode = codeBlocks(mdBody).map(normalize);
	const gotCode = [...mainEl.querySelectorAll('pre')].map((pre) => {
		const lines = [...pre.querySelectorAll('.ec-line')];
		const text = lines.length ? lines.map((l) => l.textContent).join('\n') : pre.textContent;
		return normalize(text);
	});
	if (JSON.stringify(wantCode) !== JSON.stringify(gotCode)) {
		fail(id, `code blocks differ between HTML (${gotCode.length}) and Markdown twin (${wantCode.length})`);
		for (let i = 0; i < Math.max(wantCode.length, gotCode.length); i++) {
			if (wantCode[i] !== gotCode[i]) {
				failures.push(`    block ${i + 1}\n      md:   ${wantCode[i]}\n      html: ${gotCode[i]}`);
				break;
			}
		}
	}
	if (!article || !normalize(article.textContent).includes(normalize(String(data.description)))) {
		fail(id, 'a readability-style extractor does not keep the answer');
	}
	if (article && !article.textContent.includes(SITE + mdPath(id))) {
		fail(id, 'a readability-style extractor does not keep the pointer to the Markdown twin');
	}

	// The home page reaches every page of its language in at most two steps: it links the
	// page itself, or an index page that links it, each within the first 5,000 characters
	// an extractor returns. A page that neither lists is one an agent cannot find.
	if (id === 'index' || LOCALES.some((l) => l.dir === id)) {
		// A game wiki's home page shows an official key visual of the game (root AGENTS.md, Visible page).
		if (!/<img[^>]+src="[^"]*\/art\/key-visual\.webp"/.test(html)) fail(id, 'the home page shows no key visual (/art/key-visual.webp)');
		// A game wiki's home page says in its answer line what the game is: its name and when it came out,
		// not a list of what the site holds (root AGENTS.md, Content contract).
		{
			const game = String(data.title).replace(/\s*(wiki|위키)$/i, '');
			if (!String(data.description).includes(game) || !/\d{4}-\d{2}-\d{2}/.test(String(data.description)))
				fail(id, `the home page's description does not say what ${game} is (its name and its release date)`);
		}
		const head = turndown.turndown(article?.content ?? '').slice(0, LIMIT);
		const mine = pages.filter((p) => p.id !== id && localeOf(p.id) === localeOf(id));
		const direct = mine.filter((p) => head.includes(`(${withBase(htmlPath(p.id))})`) || head.includes(`(${SITE}${htmlPath(p.id)})`));
		const indexHeads = await extractHeads(direct);
		const linksTo = (heads, p) => [`(${withBase(htmlPath(p.id))})`, `(${SITE}${htmlPath(p.id)})`].some((l) => heads.some((h) => h.includes(l)));
		// The story takes one step more (site AGENTS.md): home page, story index, chapter page,
		// stage page. A chapter page that a story index lists is an index of its stages.
		const chapters = mine.filter((p) => /\/story\/[^/]+$/.test('/' + p.id) && !direct.includes(p) && linksTo(indexHeads, p));
		const chapterHeads = await extractHeads(chapters);
		// A profile page takes the same step: home page, Afflatus index, arcanist page, profile page.
		const arcanists = mine.filter((p) => /\/arcanists\/[^/]+$/.test('/' + p.id) && !direct.includes(p) && linksTo(indexHeads, p));
		const arcanistHeads = await extractHeads(arcanists.filter((p) => mine.some((o) => o.id === p.id + '/profile')));
		for (const other of mine) {
			if (direct.includes(other)) continue;
			const link = [`(${withBase(htmlPath(other.id))})`, `(${SITE}${htmlPath(other.id)})`];
			if (/\/story\/[^/]+\/[^/]+$/.test('/' + other.id) && linksTo(chapterHeads, other)) continue;
			if (isProfile(other.id) && linksTo(arcanistHeads, other)) continue;
			if (!indexHeads.some((h) => link.some((l) => h.includes(l)))) {
				fail(id, `${htmlPath(other.id)} is linked neither from the home page nor from an index page it links, within the first ${LIMIT} extracted characters`);
			}
		}
	}

	// Header, page notes and page text (scripts/check-page-text.mjs): the header links the
	// sections in the sidebar's order, the page notes link the twin, llms.txt and index.json,
	// and no text in <main> is about the site or the page.
	checkHeaderAndOutputs(doc, id, fail, {
		sections: SECTIONS.map((s) => withBase(htmlPath(idInLocale(s, localeOf(id))))),
		outputs: [withBase(mdPath(id)), withBase(llmsPath(localeOf(id))), withBase('/index.json')],
	});
	checkOpening(doc, id, fail);
	checkFootnotes(doc, id, fail, (data.sources || []).map((s) => s.url.replace(/\/$/, '')));
	// Chapter and stage pages of the story quote the game's text, in which characters speak of pages.
	// So do the kit of an arcanist page and the effect of a Psychube page (a passive named 翻閱此頁).
	if (!isGameText(id)) checkSelfReference(withoutGameText(doc, id), id, fail);
	// Profile pages turn the client's <i>, <b> and <s> into *, ** and ~~ (pipeline/profile.py). A
	// mark that CommonMark does not read shows as a literal character: the page shows exactly as
	// many asterisks and tildes as the twin escapes.
	// Story stages show the Compendium's bold marks, which pipeline/story.py (fix_marks) makes parse.
	if (isProfile(id) || isStage(id)) {
		const content = doc.querySelector('.sl-markdown-content')?.cloneNode(true);
		// The anchor link of each heading repeats the heading's text for screen readers.
		content?.querySelectorAll('script, style, .sl-anchor-link').forEach((e) => e.remove());
		const shown = content?.textContent ?? '';
		// A story's ~ is the Compendium's own character (꿔~), never written as a mark.
		for (const c of isStage(id) ? ['*'] : ['*', '~']) {
			const want = md.split('\\' + c).length - 1;
			const got = shown.split(c).length - 1;
			if (got !== want) fail(id, `${got - want} ${c} mark(s) of the game's rich text were not read as Markdown`);
		}
	}

	// 5. No decoration leak into extracted text.
	const visible = normalize(withoutGameText(doc, id).body.textContent);
	for (const [name, pattern] of [
		['footnote back-link glyph', /↩/],
		// Add a pattern here for every piece of text the skin draws with CSS `content`. The skin
		// draws its rhombus marks as shapes, with no text; a typed rhombus would copy them.
		['rhombus before a name', /(^|\s)[◆◇♦❖]\s?\S/],
	]) {
		// The game's own text may hold a rhombus.
		if (!isGameText(id) && pattern.test(visible)) fail(id, `decoration leaked into page text: ${name}`);
	}
	// The skin draws a rhombus before each section heading. It may not be typed into one.
	for (const h of doc.querySelectorAll('main h1, main h2, main h3')) {
		if (/^[◆◇♦❖]/.test(h.textContent.trim())) fail(id, `decoration typed into a heading: ${h.textContent.trim().slice(0, 40)}`);
	}

	// 6. Language parity
	const mine = localeOf(id);
	// Links stay inside the page's language and never lead to a page that language lacks.
	for (const path of internalLinks(byId.get(id).body).filter((path) => !isFile(path))) {
		if (localeOf(idFromLink(path)) !== mine) fail(id, `link ${path} leaves the page's language`);
		else if (isPending(bareId(idFromLink(path)), mine)) fail(id, `link ${path} leads to a page ${mine.label} does not have yet (records/pending.json)`);
		else if (!ids.has(idFromLink(path))) fail(id, `link ${path} leads to no page`);
	}
	for (const other of LOCALES) {
		if (other === mine) continue;
		const otherId = idInLocale(id, other);
		if (!ids.has(otherId)) {
			// Reported once, above, for each English page a language lacks.
			continue;
		}
		const twin = byId.get(otherId).data;
		const same = (a, b) => JSON.stringify(a ?? null) === JSON.stringify(b ?? null);
		if (!same(data.lastVerified, twin.lastVerified)) fail(id, `lastVerified differs from ${otherId}`);
		if (!same(data.effectiveDate, twin.effectiveDate)) fail(id, `effectiveDate differs from ${otherId}`);
		// The page title in one language is an alias in the other, so compare the whole set of names.
		const names = (d) => (d.aliases ? [d.title, ...d.aliases].map(String).sort() : null);
		if (Boolean(data.aliases) !== Boolean(twin.aliases)) fail(id, `aliases present in only one of ${id} and ${otherId}`);
		else if (data.aliases && !same(names(data), names(twin))) fail(id, `title and aliases do not name the same set as ${otherId}`);
		if (!same(data.sources?.map((s) => s.url), twin.sources?.map((s) => s.url))) fail(id, `source URLs differ from ${otherId}`);
		const otherMd = read(mdPath(otherId).slice(1));
		if (!same(codeBlocks(md), codeBlocks(otherMd))) fail(id, `code blocks differ from ${otherId}`);
		// A stage's Trails can differ between the mainland text (zh-cn) and the global text.
		const kitOnlyInZhCn = MAINLAND_ONLY.has(bareId(id)) && (mine.dir === 'zh-cn' || other.dir === 'zh-cn');
		if (!isStoryText(id) && !kitOnlyInZhCn && headings(md).length !== headings(otherMd).length) fail(id, `number of headings differs from ${otherId}`);
		// The same link targets, except links to pages that either language lacks.
		const lacking = (bare) => isPending(bare, mine) || isPending(bare, other);
		const targets = (pageId) => [...linkTargets(byId.get(pageId).body)].filter((t) => !lacking(t)).sort();
		const a = targets(id);
		const b = targets(otherId);
		if (!same(a, b)) {
			fail(id, `link targets differ from ${otherId}: only here ${a.filter((t) => !b.includes(t)).join(' ') || '-'}; only there ${b.filter((t) => !a.includes(t)).join(' ') || '-'}`);
		}
	}
}

if (SHARD === 0) {
// 8. llms.txt: what an agent must know before it answers, the bundles and the other
// languages all come within the first 5,000 characters, ahead of the page list.
for (const locale of LOCALES) {
	const name = llmsPath(locale);
	const head = llmsTxt.get(locale).slice(0, LIMIT);
	for (const note of LLMS_NOTES[locale.lang].notes) {
		if (!head.includes(note)) fail(name, `a note is not within the first ${LIMIT} characters`);
	}
	const links = [
		...['full', 'small'].map((set) => bundlePath(locale, set)),
		'/index.json',
		...LOCALES.filter((other) => other !== locale).map(llmsPath),
	];
	for (const link of links) {
		if (!head.includes(`${SITE}${link}`)) fail(name, `link to ${link} is not within the first ${LIMIT} characters`);
	}
	const listed = pages.filter((p) => localeOf(p.id) === locale);
	const beyond = listed.filter((p) => !head.includes(SITE + mdPath(p.id))).length;
	if (beyond) console.warn(`note: ${name} lists ${beyond} of ${listed.length} pages beyond its first ${LIMIT} characters`);
}

// 9. A wrong URL is not a dead end: the 404 page links each language's home and page list.
const notFound = new JSDOM(read('404.html')).window.document;
for (const locale of LOCALES) {
	for (const href of [locale.dir ? `/${locale.dir}/` : '/', llmsPath(locale)].map(withBase)) {
		if (!notFound.querySelector(`main a[href="${href}"]`)) fail('404.html', `no link to ${href}`);
	}
}

// 10. robots.txt names the sitemap and states how the content may be used.
const robots = existsSync(join(DIST, 'robots.txt')) ? read('robots.txt') : '';
if (!robots.includes(`Sitemap: ${SITE}/sitemap-index.xml`)) fail('robots.txt', 'missing or without the sitemap');
if (!/^Content-Signal: /m.test(robots)) fail('robots.txt', 'no Content-Signal line');


await checkFound(DIST, pages, fail);
// 11. Every unit of the site's own prose is in the prose ledger (scripts/prose-review.mjs).
await checkProse(fail, DIST);
}

if (failures.length) {
	console.error(`FAIL: ${failures.filter((f) => !f.startsWith('    ')).length} problem(s) in ${pages.length} pages\n`);
	for (const f of failures) console.error('- ' + f);
	process.exit(1);
}
console.log(`PASS: ${pages.length} pages, each with a Markdown twin; all checks passed.`);
