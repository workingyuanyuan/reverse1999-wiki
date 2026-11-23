// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';
import starlightLinksValidator from 'starlight-links-validator';
import { sitemapOptions } from './src/lib/sitemap.mjs';
import { ORIGIN, BASE, TITLE, DESCRIPTION } from './src/lib/site.mjs';
import { satteri } from '@astrojs/markdown-satteri';
import { hastBase } from './src/lib/hast-base.mjs';
import { arcanistSidebar, psychubeSidebar, storySidebar } from './src/lib/sidebar.mjs';

export default defineConfig({
	site: ORIGIN,
	base: BASE || undefined,
	trailingSlash: 'always',
	// Content links are written without the sub-path; this adds it in the HTML.
	markdown: { processor: satteri({ hastPlugins: [hastBase] }) },
	integrations: [
		// Added here so that it takes options; Starlight then leaves its own copy out.
		sitemap(sitemapOptions()),
		starlight({
			title: TITLE,
			description: DESCRIPTION,
			defaultLocale: 'root',
			locales: {
				root: { label: 'English', lang: 'en' },
				'zh-tw': { label: '繁體中文', lang: 'zh-TW' },
				'zh-cn': { label: '简体中文', lang: 'zh-CN' },
				ja: { label: '日本語', lang: 'ja' },
				ko: { label: '한국어', lang: 'ko' },
			},
			sidebar: [
				{
					label: 'Arcanists',
					translations: { 'zh-TW': '神秘學家', 'zh-CN': '神秘学家', ja: 'キャラクター', ko: '캐릭터' },
					items: arcanistSidebar(),
				},
				{
					label: 'Psychubes',
					translations: { 'zh-TW': '心相', 'zh-CN': '心相', ja: '心相', ko: '의지' },
					items: psychubeSidebar(),
				},
				{
					label: 'Systems',
					translations: { 'zh-TW': '系統', 'zh-CN': '系统', ja: 'システム', ko: '시스템' },
					items: ['summoning', 'combat', 'statuses', 'insight', 'resonance', 'releases'].map((p) => ({ slug: `systems/${p}` })),
				},
				{
					label: 'Story',
					translations: { 'zh-TW': '劇情', 'zh-CN': '剧情', ja: 'ストーリー', ko: '스토리' },
					items: storySidebar(),
				},
			],
			// The heading serif, self-hosted (SIL OFL 1.1): split by Unicode range, so a page
			// downloads only the slices of the characters it shows, at the one weight it uses.
			customCss: [
				'@fontsource/noto-serif-tc/600.css',
				'@fontsource/noto-serif-sc/600.css',
				'@fontsource/noto-serif-jp/600.css',
				'@fontsource/noto-serif-kr/600.css',
				'./src/styles/reverse.css',
			],
			components: {
				// Four overrides: the site name with its links, the answer above the body with the page notes after it, the theme buttons, and the script that opens the site in the dark theme.
				SiteTitle: './src/components/SiteTitle.astro',
				MarkdownContent: './src/components/MarkdownContent.astro',
				ThemeSelect: './src/components/ThemeSelect.astro',
				ThemeProvider: './src/components/ThemeProvider.astro',
			},
			routeMiddleware: './src/routeData.ts',
			credits: false,
			pagination: false,
			expressiveCode: {
				themes: ['night-owl', 'github-light'],
				// `patch` gets diff colours but keeps the literal +/- in the page text.
				// The `diff` language is not used: Expressive Code draws its +/- with CSS,
				// so an agent reading the HTML would not see which lines were added or removed.
				shiki: { langAlias: { patch: 'diff' } },
				styleOverrides: { borderRadius: '0', borderWidth: '1px', frames: { shadowColor: 'transparent' } },
			},
			plugins: [
				starlightLinksValidator({
					exclude: ['/**/*.md', '/*.md', '/llms.txt', '/**/llms.txt', '/index.json', '/**/index.json', '/**/art/**'],
				}),
			],
		}),
	],
});
