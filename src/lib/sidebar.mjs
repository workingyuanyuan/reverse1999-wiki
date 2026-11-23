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

// The Psychubes group: one collapsed group per index page (pipeline/psychube.py, by the stat a
// Psychube adds), its index page first, then its Psychubes by rarity and English name, from
// records/psychubes.json (written by pipeline/psychube.py indexes).
export function psychubeSidebar() {
	const { psychubes } = JSON.parse(readFileSync(new URL('../../records/psychubes.json', import.meta.url), 'utf8'));
	return [
		['critical', 'Critical', { 'zh-TW': '暴擊', 'zh-CN': '暴击', ja: 'クリティカル', ko: '치명타' }],
		['damage-6', '6-star damage', { 'zh-TW': '6 星輸出', 'zh-CN': '6 星输出', ja: '★6 攻撃', ko: '6성 공격' }],
		['damage-5', '5-star damage', { 'zh-TW': '5 星輸出', 'zh-CN': '5 星输出', ja: '★5 攻撃', ko: '5성 공격' }],
		['might', 'Might', { 'zh-TW': '威力', 'zh-CN': '威力', ja: '威力', ko: '위력' }],
		['survival', 'Survival and healing', { 'zh-TW': '生存與治療', 'zh-CN': '生存与治疗', ja: '生存と回復', ko: '생존과 치료' }],
	].map(([group, label, translations]) => ({
		label,
		translations,
		collapsed: true,
		items: [
			{ slug: `psychubes/${group}` },
			...psychubes
				.filter((p) => p.group === group && existsSync(new URL(`psychubes/${p.slug}.md`, DOCS)))
				.sort((a, b) => b.stars - a.stars || a.en.toLowerCase().localeCompare(b.en.toLowerCase()))
				.map((p) => ({ slug: `psychubes/${p.slug}` })),
		],
	}));
}
