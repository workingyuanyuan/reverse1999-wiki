// The Arcanists group of the sidebar: one collapsed group per Afflatus, its index page first,
// then its arcanists by rarity and English name, as pipeline/write_indexes.py lists them.
// Only pages that exist in English are listed; Starlight takes each label from the page title.

import { readFileSync, existsSync } from 'node:fs';

const AFFLATUS = [
	['Star', { 'zh-TW': '星', 'zh-CN': '星', ja: '星', ko: '천체' }],
	['Mineral', { 'zh-TW': '岩', 'zh-CN': '岩', ja: '岩', ko: '암석' }],
	['Beast', { 'zh-TW': '獸', 'zh-CN': '兽', ja: '獣', ko: '야수' }],
	['Plant', { 'zh-TW': '木', 'zh-CN': '木', ja: '木', ko: '나무' }],
	['Spirit', { 'zh-TW': '靈', 'zh-CN': '灵', ja: '霊', ko: '영혼' }],
	['Intellect', { 'zh-TW': '智', 'zh-CN': '智', ja: '知', ko: '지능' }],
];
const TWO = { 101: ['Mineral', 'Star'] };
const DOCS = new URL('../content/docs/', import.meta.url);

export function arcanistSidebar() {
	const { arcanists } = JSON.parse(readFileSync(new URL('../../records/arcanists.json', import.meta.url), 'utf8'));
	return AFFLATUS.map(([name, translations]) => {
		const members = arcanists
			.filter((a) => (TWO[a.afflatus] ?? [a.afflatus]).includes(name))
			.filter((a) => existsSync(new URL(`arcanists/${a.slug}.md`, DOCS)))
			.sort((a, b) => b.stars - a.stars || a.names.en.toLowerCase().localeCompare(b.names.en.toLowerCase()));
		return {
			label: name,
			translations,
			collapsed: true,
			items: [{ slug: `afflatus/${name.toLowerCase()}` }, ...members.map((a) => ({ slug: `arcanists/${a.slug}` }))],
		};
	});
}
