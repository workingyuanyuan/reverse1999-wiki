# Rules for agents maintaining this site

An unofficial wiki for the game Reverse: 1999 (重返未來：1999 / 重返未来：1999; developer and global publisher Bluepoch 深藍互動), at `https://yuanaruru.com/reverse1999-wiki/`. The rules in `../AGENTS.md` apply; this file holds what is specific to this site.

Read before the work: `SOURCES.md` before fetching a source or reading the game tables (what each allows, the data codes, where each kind of fact is read and how it was checked); `pipeline/README.md` before running a pipeline script (commands, and the official terms per language for writers); `upstream/README.md` when `pnpm upstream` reports a difference; `../COMMUNITY.md` when a version lands. The state of the work goes in `reviews/work-log.md`; the questions people ask and the agent test set in `tests/agent-eval/questions.md`.

## Decisions

By the owner unless marked `agent`; the owner may change an agent's default.

- Service (2026-11-22): the mainland China service is the main source. It runs about two versions ahead, and readers on the other services look up which arcanists the coming versions bring, so arcanists out only on the mainland service are in scope. This replaces, for this site, the rule of the other game wikis that the next version stays out.
- Every arcanist record carries the mainland release version and date and, where it exists, the release on the other services; a page states that an arcanist is not yet out on the global service as a fact of the record, never a predicted date. Release cells give dates only, no version numbers (2026-11-22): the version is not in the client data. An arcanist with no date in the records carries the mainland version instead.
- Languages (2026-11-22): English at the root, Traditional Chinese (`/zh-tw/`), Simplified Chinese (`/zh-cn/`), Japanese (`/ja/`) and Korean (`/ko/`). Names follow each language's official strings: Simplified from the mainland service, Traditional from the Taiwan service, English, Japanese and Korean from the global client.
- A name with no official string in a language yet is translated (2026-11-22): English takes the Fandom wiki's community translation, Japanese and Korean are translated by us, Traditional Chinese converts the Simplified name. The page's caveat says these names are not yet official; the official strings replace them when the global client has them.
- Game data (2026-11-22): the decoded client tables of `St-Pavlov-Foundation/re1999-data` (mainland) and `re1999-data-global` (global) are the sources of in-game text and numbers. Each page cites the file at a fixed commit and records the client build from `data/meta.json` in `appliesTo`. Wikis (Fandom, Huiji, BWIKI) are second witnesses, read for samples; when looking for sources, look for wikis in every language of the site, Simplified Chinese first. No copy of the decoded tables is committed.
- The game's own text (2026-11-24) is shown as the game gives it, in each language's edition (English, Japanese, Korean and Traditional Chinese from the global client, Simplified Chinese from the mainland client): incantations, Ultimates, Insight passives, Portray levels, Euphoria, status terms, Psychube effects, and the arcanist profiles (cover, items, culture, skins, voice lines; one profile page per arcanist out on the global service, with only the entries the global client has, so every language holds the same set). Tables of numbers compiled from the game stay as our facts.
- An arcanist or Psychube out on the mainland service only has its kit or effect text in Simplified Chinese alone, so only the zh-cn page shows it (2026-11-24); the other languages keep the facts (profile table, Insight materials, names).
- Story text (2026-11-23): the full text of every chapter, in the language of each page, from the Reverse: 1999 Story Compendium, pinned in `records/story.json`; the page notes cite it at its commit and name Bluepoch as the owner of the text. An index page per kind of story, a page per chapter, a page per stage. Chapters out on the mainland service only are listed by their Simplified name, without a page.
- An arcanist in the mainland data but not yet released there is listed on its Afflatus index with the release date that an official announcement gives (2026-11-22); its page waits until the client data holds its kit.
- Schneider (2026-11-24) has an arcanist page and a profile page although she was never playable (`unplayable` in `scaffold.py`); she stays out of the counts (`SKIP` in `write_indexes.py`). Her art fades and returns every 14 s: an exception to the rule that images do not move, approved for this one image (2026-11-24). What her page holds, and that the rain on it is the Storm, are the agent's default.
- Art: from the Fandom wiki, the full-length art of each arcanist, a transparent figure shown whole and unaltered (2026-11-22), and the illustration of each Psychube's own screen, with its lettering (2026-11-23); credited to Bluepoch, the Fandom file page and the file at the revision used (`records/art.json`, `art-psychubes.json`). No file on Fandom, no art.
- Facts are never taken from `myssal/Reverse-1999-CN-Asset` alone; its `ArcanistMap.json` may serve only when a second source agrees.
- Huiji (`res1999.huijiwiki.com`) may be read in the owner's own Chrome, one named page at a time at a human pace, for a bounded list of pages; facts only, no copy committed. Never with a headless browser, and never by working around its Cloudflare challenge: the challenge is the site's refusal of automated reading. No wiki behind such a challenge is read by script (agent).
- Recommended Psychubes (2026-11-23): each arcanist's profile table lists, in the game's order, the Psychubes that `character_recommend.json` recommends (no recommendation, no row), the same record as the Recommended row of the Psychube pages; `check_pairs.py` fails when either side lacks the link back.
- Agent's defaults (2026-11-22): the arcanist index is split by Afflatus and the Psychube index by the stat it adds, because one index passes 5,000 characters; answers across entries come first (summoning carry-over by banner type, with counter, featured guarantee and destination banner as separate columns; Psychube to arcanist and back by trigger condition; Euphoria; a five-language name table; what differs between services); no tier lists on fact pages.
- Edition differences (agent, 2026-11-24): each page shows one edition of the game's text, so where the editions differ on a value or condition, the last section (`## Edition differences`, from `records/edition-notes.json`) says so in our own words, and lists Epiphanies out on the mainland only. Where the two clients disagree on a value or a target, the page gives the mainland reading and says in one clause what the global client has.
- No answer line on profile pages and story stages (`hidesAnswer` in `src/lib/site.mjs`).
- Home page key visual: "The Storm Is Coming", the rain scene of the Taiwan official site; the other official sites show only the current version's art.
- The owner confirms every change before it goes live.

## Commands

```
pnpm verify      # prose check, build, acceptance checks in eight processes, the prose ledger
pnpm upstream    # compare the pinned game data with the current data; changes no page (upstream/README.md)
pnpm preview     # serve dist/ with charset=utf-8
node scripts/prose-review.mjs status | run [--jobs N] | accept <hash> <reason>   # the prose ledger, after pnpm build
python3 -I pipeline/scaffold.py check <page.md> ...       # generated blocks unchanged, no mark left, every number from the game text
python3 -I pipeline/lint_page.py <page.md> ...            # one-page check: frontmatter, prose patterns, headings, links, images
uv run --with opencc-python-reimplemented python3 -I scripts/to-zh-cn.py     # zh-tw pages -> zh-cn pages (calls kit_text and psychube effects for zh-cn)
```

The other pipeline scripts (fetch, records, page writers, art) are in `pipeline/README.md`.

## Content rules

- Never edit `src/content/docs/zh-cn/`, the story pages or the profile pages by hand.
- Arcanist pages: profile table (rarity, Afflatus, damage type, tags, Resonance set and patterns, recommended Psychubes, mainland and global release), then the kit in the game's own text (Incantations by rank, Ultimate, Inheritance by Insight with the materials table, Portrait, Euphoria, the statuses the kit names), a five-language names table, and the edition differences. Only labels and headings are ours. zh-cn pages take the mainland client's text, cut to the entries the global client has.
- Psychube pages and the statuses page are written by `psychube.py` and `write_systems.py`; what each holds is in `pipeline/README.md`. On the statuses page the column of arcanists does not claim they apply the status.
- A fact that neither the tables nor a second source states is left off the page: level costs, the values of Resonance Ideas, which arcanists show Reasoning instead of Resonance, that Spirit and Intellect each have the advantage over the other. `SOURCES.md` lists these with what was read.
- A banner's type is the one its rule text names in brackets (【限时角色征集】), not its title. Read the rule text under the key that `const.json` names.
- Official terms per language come from `cache/glossary.json` (`glossary.py`); the list of core terms is in `pipeline/README.md`. In Traditional Chinese 啟示 is Eureka, a team mechanic; Epiphany is 閃念.
- Story pages are written by `pipeline/story.py` and never by hand; `check_prose.py` and `to-zh-cn.py` skip `story/`. How names are taken, what the sidebar shows on profile, chapter and stage pages and why stage pages are left out of `llms.txt`: `pipeline/README.md`.
- Section headings carry no quotation marks: Starlight curls them in the HTML and the heading check against the twin fails.

## Look (approved 2026-11-22)

The header comment of `src/styles/reverse.css` describes the look and holds its values.

- Taken from the mainland and Taiwan official sites: parchment text, tan secondary text, one orange-brown accent family, serif headings (Noto Serif TC, SC, JP and KR from `@fontsource`, weight 600, each language's cut drawing its Latin letters too), a copper rhombus before section headings and the site name. Body text stays sans-serif. Favicon: a copper rhombus with rain lines.
- The site opens in the dark theme; a reader's choice of light, dark or auto is kept (`ThemeProvider.astro`, `ThemeSelect.astro`).
- The dark theme keeps the text column darkest and its links parchment with a copper line (copper small text falls short of contrast on black); the values, the size of character art and the screenshot check for a change of ground are in `pipeline/README.md` (Look).
- Not adopted, as too heavy for a reference site: narrative decoration (floating photos, background big type, catalogue micro text, mirrored titles), paper surfaces, serif body text.
- Motion: entrances measured from the official site, and rain that keeps rising, as the Storm does in the game's story. A mask keeps it out of the text column only, so it runs behind the sidebar, the table of contents, the margins and the bands outside the centred frame (owner, 2026-11-26).
