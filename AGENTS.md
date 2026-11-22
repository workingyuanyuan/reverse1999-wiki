# Rules for agents maintaining this site

This site is an unofficial wiki for the game Reverse: 1999 (重返未來：1999 / 重返未来：1999; developer and global publisher Bluepoch 深藍互動). Its first readers are AI agents; humans come second. The rules in `../AGENTS.md` apply; this file holds what is specific to this site.

State on 2026-11-23: a page for every released arcanist (138; Evelyn not yet), six Afflatus index pages, Summoning and pity and the home page, in English and translated; the look and the content are approved (2026-11-23). Not published yet.

## Decisions by the owner (2026-11-22)

- Service: the mainland China service is the main source. It runs about two versions ahead of the other services (mainland 4.1, global and Taiwan 3.9 on 2026-11-22). Readers on the global, Taiwan, Japanese and Korean services look up which arcanists the coming versions bring, to plan their pulls, so arcanists that are out only on the mainland service are in scope. Every arcanist record carries the mainland release version and date and, where it exists, the release on the other services; a page states that an arcanist is not yet out on the global service as a fact of the record, never a predicted date. This replaces, for this site only, the rule of the other game wikis that the next version stays out.
- Languages: English at the root, Traditional Chinese (`/zh-tw/`), Simplified Chinese (`/zh-cn/`), Japanese (`/ja/`) and Korean (`/ko/`). Names in each language follow that language's official strings: Simplified Chinese from the mainland service, Traditional Chinese from the Taiwan service, English from the global service, Japanese and Korean from the global client's Japanese and Korean text. A name that has no official string in a language yet (an arcanist, skill or status out only on the mainland service) is translated (owner, 2026-11-22): English takes the community translation of the Fandom wiki, Japanese and Korean are translated by us, Traditional Chinese converts the Simplified name. The page's caveat says these names are not yet official, and they are replaced by the official strings when the global client has them.
- Arcanists in the mainland data but not yet released there (Evelyn, mainland release 2026-11-26) are included when an official announcement gives the date (owner, 2026-11-22): the Afflatus index lists them with that date. Their page waits until the client data holds their kit (2026-11-23: Evelyn's skills are placeholders).
- Schneider is in the tables but was never released as a playable arcanist: no page, not listed (`SKIP` in `pipeline/write_indexes.py`).
- Release cells give dates only, no version numbers (2026-11-22): the version an arcanist came with is not in the client data, and a guessed version would be wrong for one service or the other. Drake and Glyndŵr have no date in the records yet and carry the mainland version 4.0 instead.
- Art (revised 2026-11-22): the full-length art of each arcanist from the Reverse: 1999 Wiki (Fandom), file `<English name>.png`, a transparent figure shown whole and unaltered. The official sites carry full-length art for the ten launch arcanists only (Taiwan site), so a link to an official original is not required. The page notes credit Bluepoch, the Fandom file page and the image file at the revision used (`pipeline/fetch_art.py` records it in `records/art.json`). Arcanists with no file on Fandom (in 2026-11: Evelyn, not yet released) have no art. Facts are never taken from `github.com/myssal/Reverse-1999-CN-Asset` alone: its `mappings/ArcanistMap.json` (ids, names, birthdays, skins) may serve only when a second source agrees.
- Scope of the first release: every released arcanist, after three sample pages of different rarities were approved (2026-11-22).
- Sources: look for wikis in every language of the site, Simplified Chinese first. Survey below.
- Game data (owner, 2026-11-22): the decoded client tables in `github.com/St-Pavlov-Foundation/re1999-data` (mainland client) and `github.com/St-Pavlov-Foundation/re1999-data-global` (global client) are the sources of in-game text and numbers: names, rarity, afflatus, damage type, skill names, effects and multipliers, Psychubes, materials. The mainland repository gives the Simplified Chinese text and every arcanist; the global repository gives the official English, Japanese, Korean and Traditional Chinese strings of what is out on the global service. Facts are restated in our own words and tables; no copy of the tables is committed (they carry no licence). Each page cites the file at a fixed commit and records the client build from `data/meta.json` in `appliesTo`. Wikis (Fandom, Huiji, BWIKI) are second witnesses, read for samples.
- Huiji (`res1999.huijiwiki.com`) may be read in the owner's own Chrome (the `claude-in-chrome` tools), one named page at a time at a human pace, for a bounded list of pages; facts only, restated, and no copy of its text committed. Not with the headless Playwright browser, and never by working around its Cloudflare challenge with a script: the challenge is the site's refusal of automated reading.

## Defaults taken from the advisors (2026-11-22; the owner may change them)

Fable, Astra and Neon were asked (`~/.local/state/delegation-log/docs-sites/20261122-r1999-plan*`). All three proposed the global service; the owner chose the mainland service for the reason above.

- Arcanist index split into six pages by afflatus: one index of about 140 links exceeds 5,000 characters.
- Answers across entries come first: summoning carry-over by banner type (counter, featured guarantee, destination banner as separate columns), Psychube to arcanist and back by trigger condition, Euphoria, a five-language name table, and what differs between services.
- No tier lists, no story chapter list.
- Wikis that refuse automated reading (a Cloudflare challenge) are not read by script.
- Who lets a change go live: the owner confirms every time. Look: taken from an official site, with continuous ambient motion behind the content (root rules). Address: `https://yuanaruru.com/reverse1999-wiki/`.

## Sources surveyed (2026-11-22)

| Source | Language | Access | Terms | Notes |
| --- | --- | --- | --- | --- |
| `re.bluepoch.com` | zh-CN | plain fetch; JS-loaded content | `robots.txt` 404 | mainland official site, 4.1 |
| `re1999.bluepoch.com/en/`, `/jp/` | en, ja | plain fetch; JS-loaded content | `robots.txt` 404; user agreement §10 on rights | global official site, 3.9 |
| `re1999.movergames.com` | zh-TW | plain fetch, server-rendered notices and a character section | `robots.txt` 404 | Taiwan service (separate client), 3.9; notices give times in UTC+8 |
| `res1999.huijiwiki.com` (灰機) | zh-CN | Cloudflare challenge on every page and on `api.php` | CC BY-NC-SA 3.0 for contributor text; game assets reserved to Bluepoch; `Content-Signal: search=yes,ai-train=no,use=reference`; disallows ClaudeBot | the active mainland wiki |
| `wiki.biligame.com/reverse1999` (BWIKI) | zh-CN | MediaWiki API; Tencent EdgeOne WAF (HTTP 567) when requests come fast | licence field empty | few edits since 2026-09; no page for the 4.0 and 4.1 arcanists (伊芙琳, 佩施塔, 格林杜尔, 德雷克) |
| `reverse1999.fandom.com` | en | MediaWiki API works with a plain fetch; HTML pages return a Cloudflare challenge | CC BY-SA | edited daily; infobox gives mainland and global release dates and names in Chinese, Japanese and Korean; arcanists out only on the mainland service have pages marked `{{CN}}` with translated skill text |
| `prydwen.gg/re1999` | en | plain fetch | `robots.txt` allows, `Crawl-delay: 10` | guide site for the global service |
| `wikiwiki.jp/reverse1999`, `gamerch.com/reverse1999`, `appmedia.jp/re1999` | ja | plain fetch | wikiwiki `robots.txt` disallows query URLs | wikiwiki home page does not name the newest arcanists |
| `namu.wiki`, `thewiki.kr` | ko | Cloudflare challenge | unknown | |
| `github.com/windbow27/kornblume` | five languages | GitHub | no licence file | arcanist names in en, ja, ko, zh-CN, zh-TW; its arcanist data credits Huiji, so it is not a second witness for Huiji's facts |
| `github.com/myssal/Reverse-1999-CN-Asset` | zh-CN, en names | GitHub | no licence file, no release | mainland client images and `ArcanistMap.json` (142 entries, last commit 2026-11-08 for 4.1) |
| `store.steampowered.com/app/3092660` | | | | global client languages: English, Japanese, Simplified Chinese, Traditional Chinese, Korean |
| `github.com/St-Pavlov-Foundation/re1999-data` | zh-CN | GitHub, raw files by plain fetch | no licence file | mainland client config tables decoded to JSON (`data/json/`) and Lua; `data/meta.json` names the client build (`113.0.1422`, `server: cn` on 2026-11-18); a workflow updates it twice a day. `character.json` has 142 arcanists with Chinese name, `nameEng`, rarity, damage type and skill ids; `skill.json` and `skill_effect.json` hold skill names and the full Chinese effect text with multipliers (4.x arcanists included) |
| `github.com/St-Pavlov-Foundation/re1999-data-global` | en, ja, ko, zh-TW, zh-CN | as above | no licence file | global client tables, build `111.0.1077` (`server: gl`, 2026-11-11); text sits in `data/configs/language/language_{en,jp,kr,tw,zh}.json`, keyed from the tables (`language_10003434`). 136 arcanists: those out only on the mainland service are absent |
| `uttu.merui.net` | five languages | JavaScript app | `Content-Signal: search=yes,ai-train=no,use=reference`; disallows ClaudeBot | archive site with mainland-only content |
| `reverse1999.wikiru.jp` | ja | plain fetch | `robots.txt` allows all | volunteer wiki |
| `github.com/UnderLotus/r1999-roster` | | GitHub | MIT | roster tool; its README names its data sources (the two data repositories above, Huiji, Fandom, wikiru, UTTU) |

Not found yet: the NGA board for the game; a fan-content guideline of Bluepoch in English or Chinese (a Japanese one is linked from the global `/jp/` news, JavaScript-only).

## Questions

The questions people ask, in each language, and the agent test set: `tests/agent-eval/questions.md`.

## Commands

```
python3 -I pipeline/fetch_data.py [--update]     # game tables at the commits pinned in records/sources.json -> cache/
python3 -I pipeline/build_records.py             # cache -> records/arcanists.json; game text per kit -> cache/source/<slug>.json
python3 -I pipeline/fetch_releases.py            # release dates from the Fandom infobox -> records/releases.json
python3 -I pipeline/glossary.py <slug> ... [--out F]  # official strings in five languages for translators -> cache/glossary.json
python3 -I pipeline/kit.py <slug> [lang ...]     # an arcanist's kit text side by side (default zh-CN en), for writers
python3 -I pipeline/scaffold.py write <lang> <slug> ...   # page skeleton: generated blocks plus WRITE marks for the text
python3 -I pipeline/scaffold.py check <page.md> ...       # generated blocks unchanged, no mark left, every number from the game text
python3 -I pipeline/lint_page.py <page.md> ...   # one-page check: frontmatter, prose patterns, headings, links, images
python3 -I pipeline/write_indexes.py             # the six Afflatus index pages and the home page's generated parts, every language but zh-cn
python3 -I pipeline/fetch_art.py [slug ...]      # full-length art from Fandom -> public/art/characters/<slug>.webp, records/art.json
uv run --with opencc-python-reimplemented python3 -I pipeline/names_voc.py   # mainland names that differ from converted Taiwan names -> records/names-voc.json
uv run --with opencc-python-reimplemented python3 -I scripts/to-zh-cn.py     # zh-tw pages -> zh-cn pages
pnpm verify      # prose check, build, acceptance checks
pnpm upstream    # compare the pinned game data with the current data; changes no page (upstream/README.md)
pnpm preview     # serve dist/ with charset=utf-8
```

## Content rules

- Arcanist pages: profile table (rarity, Afflatus, damage type, tags, mainland and global release), a short paragraph on how the kit works, then Incantations (per rank), Ultimate, statuses the kit uses, Inheritance by Insight with materials, Portrait, Euphoria where the arcanist has it, and a five-language names table. Numbers come from the tables of the client named in `appliesTo`; the text is our own words.
- Data codes, checked against Fandom on 2026-11-22: `rare` + 1 = stars; `career` 1 Mineral, 2 Star, 3 Plant, 4 Beast, 5 Spirit, 6 Intellect; `dmgType` 1 Reality, 2 Mental. Insight level caps in `character_rank` are cumulative (30, 70, 120, 180): the in-game cap of Insight n is the difference. In `skill_ex_level` descriptions, `▩n%s` names the skill a Portrait level changes: 0 the Insight passive set, 1 and 2 the incantations, 3 the Ultimate.
- Official terms per language: `cache/glossary.json`. Insight 洞悉 / 洞察 / 통찰, Portrait 塑造 / 塑造 / 형상, Euphoria 狂想 / 狂想 / 광상, Inheritance 傳承 / 伝承 / 계승, Incantation 咒語 / スペル / 주문, Ultimate 至終的儀式 / アルティメット / 최종 술식, Moxie 激情 / モキシー / 열정, Genesis DMG 本源創傷 / ジェネシスダメージ / 고정 피해, Precognition 先覺 / 予察 / 선각, Epiphany 閃念 / 瞬想 / 발상 (the global client's Euphoria screen; in Traditional Chinese 啟示 is Eureka, a team mechanic).
- Never edit `src/content/docs/zh-cn/` by hand.
- Summon rules: the rule text of each banner type is in `const.json`, row id = `info` of `summon_pool_detail.json` (`value2` holds the Chinese text in the mainland data and a language key in the global data); rates and pity are `initWeight` and `awardTime` of `summon_pool.json`. The global English text also keeps older rule texts under other keys (`language_10000347` to `language_10000363`) whose wording differs: read the key that `const.json` names. A banner's type is the one its rule text names in brackets (【限时角色征集】), not its title: some banners titled 限时活动征集 are of the Time-limited type.
- Euphoria opens at Insight III level 30 for a 6-star arcanist and at Insight III level 1 for a 5-star (Fandom, page Euphoria, revision 91875); the client data does not hold the condition.
- Where the two clients disagree on a value or a target, the page gives the mainland reading and says in one clause what the global client has.
- Section headings carry no quotation marks: Starlight curls them in the HTML and the heading check against the twin fails.

## Look (approved 2026-11-22)

Taken from the mainland and Taiwan official sites: parchment text `#eee4d5`, tan `#bba893`, one orange-brown accent family (`#a95d35` rules and table head rule, `#b55829` marks, `#db6f39` hover only); serif headings (the sites use Source Han Serif; the site serves Noto Serif TC, SC, JP and KR at weight 600 from the `@fontsource` packages, the same design under SIL OFL, split by Unicode range so a page loads only the slices it shows; each language's cut draws its Latin letters too, so a heading never mixes two serifs); a copper rhombus before section headings and the site name. Body text stays sans-serif: the serif fallbacks of Windows read poorly at body size.

The site opens in the dark theme (2026-11-22): with nothing stored it is dark; a reader's choice of light, dark or auto is kept (`src/components/ThemeProvider.astro`, `ThemeSelect.astro`). Dark theme (revised 2026-11-22; follows in part a dark, analogue, editorial design language in the game's manner): black painted ground; warm light leaking in from outside the window (right edge, low; bottom left corner), fixed to the window, so the middle where the text column sits stays darkest; a static grey grain tile over everything (`src/assets/grain.png`, alpha 0.10 baked in, normal blending, never animated); bars that cover scrolled content (header, phone menu, table of contents bar) carry the same grain; wide-window sidebars are clear. Square corners (1 px), including the phone menu button and the table of contents toggle; no shadows; weights 400 and 600 only; tables have no frame, rules across only and a copper rule over the head row, tabular figures; links and current items stay parchment with a copper line, because copper small text falls short of contrast on black; the chosen theme button is underlined, not filled; prose keeps about 42em a line in Chinese and Japanese, 46em in Korean and 75ch in English, while tables use the whole column. Not adopted, as too heavy for a reference site: narrative decoration (floating photos, background big type, catalogue micro text, mirrored titles), paper surfaces, serif body text. Checks on background-only screenshots at 390, 1440, 1920 and 2560 px: centre darker than edges, maximum luma under 40, grain mean 13 and spread 7.6 with equal channels, the text column's 16 px blocks at most 20 luma with a range under 8.

Light theme: parchment paper `#f4ede2` with brown ink, same tables and marks. Motion (`src/styles/reverse.css`, end): entrances measured from the official site's CSS (fade in while rising 2rem, 0.5 s, default ease; 0.3 s pointer responses), and rain in the margins that keeps rising (2026-11-22): the key visual of the official site is rain on a window, and in the game's story the Storm makes the rain go up from the ground to the sky, so short streaks drift straight up one tile in 4 s and drops creep up the glass in 90 s; a mask keeps it to the margins between the text column and the two sidebars. Favicon: a copper rhombus with rain lines, drawn for this site. Character art: the full-length figure, without frame or shadow, floats right of the profile table (two columns: field and value) and the opening paragraph on a wide window, at most 26rem high; on a phone it stands above the table, at most 20rem high; the first section starts below it.
