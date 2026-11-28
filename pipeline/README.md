# The pipeline: scripts and writers' references

Read this before running a script in this folder. `../AGENTS.md` holds the rules and the commands every change needs; `../SOURCES.md` the sources and the data codes; each script's header says what it reads and writes.

## Commands

```
python3 -I pipeline/fetch_data.py [--update]     # game tables at the commits pinned in records/sources.json -> cache/
python3 -I pipeline/build_records.py             # cache -> records/arcanists.json; game text per kit -> cache/source/<slug>.json
python3 -I pipeline/fetch_releases.py            # release dates from the Fandom infobox -> records/releases.json
python3 -I pipeline/glossary.py <slug> ... [--out F]      # official strings in five languages -> cache/glossary.json
python3 -I pipeline/kit.py <slug> [lang ...]              # an arcanist's kit text side by side, for writers
python3 -I pipeline/scaffold.py write <lang> <slug> ...   # page skeleton: generated blocks plus WRITE marks
python3 -I pipeline/scaffold.py profile <page.md> ...     # rewrite the profile table of finished pages (then to-zh-cn)
python3 -I pipeline/write_indexes.py             # the Afflatus index pages and the home page's generated parts
python3 -I pipeline/write_systems.py [lang ...]  # systems/releases, insight, statuses and resonance
python3 -I pipeline/kit_text.py write <slug> ... # the kit of arcanist pages in the game's text
python3 -I pipeline/psychube.py text <slug> [lang ...] | write <lang> <slug|all> | check <page.md> ... | indexes | effects | art   # Psychube pages: text for writers, skeletons, check, index pages, effect sections, art lines
python3 -I pipeline/edition_notes.py write       # the edition differences at the end of arcanist and Psychube pages (then to-zh-cn)
python3 -I pipeline/profile.py write [slug ...]  # profile pages from character_data, skin and character_voice
python3 -I pipeline/check_profile.py [slug ...]  # profile pages, kits, Psychube and status effects hold the game's text only
python3 -I pipeline/check_pairs.py               # every Psychube-arcanist link has its link back, in every language
python3 -I pipeline/story.py fetch | write       # the Compendium at the pinned commit -> cache/story/repo; every story page in five languages
python3 -I pipeline/fetch_art.py [--psychubes] [slug ...]   # art from Fandom -> public/art/, records/art*.json
uv run --with opencc-python-reimplemented python3 -I pipeline/names_voc.py   # mainland names that differ from converted Taiwan names
```

The page scripts write every language but `zh-cn`; `to-zh-cn.py` writes that one. `story.py write` writes all five.

## Terms

- Official terms per language: `cache/glossary.json`. Insight 洞悉 / 洞察 / 통찰, Portrait 塑造 / 塑造 / 형상, Euphoria 狂想 / 狂想 / 광상, Inheritance 傳承 / 伝承 / 계승, Incantation 咒語 / スペル / 주문, Ultimate 至終的儀式 / アルティメット / 최종 술식, Moxie 激情 / モキシー / 열정, Genesis DMG 本源創傷 / ジェネシスダメージ / 고정 피해, Precognition 先覺 / 予察 / 선각, Epiphany 閃念 / 瞬想 / 발상 (in Traditional Chinese 啟示 is Eureka, a team mechanic).

## Look: values and checks

The decisions on the look are in `../AGENTS.md`; the header comment of `src/styles/reverse.css` describes it.

- Dark theme: black painted ground, warm light leaking in from the window's edges so the text column stays darkest, a static grain over everything, square corners, no shadows, weights 400 and 600 only, tables ruled only across. Links and current items stay parchment with a copper line: copper small text falls short of contrast on black. Light theme: parchment paper with brown ink.
- Character art: the full-length figure, without frame or shadow, floats right of the profile table on a wide window (at most 26rem high) and stands above it on a phone (at most 20rem).
- Check a change of ground on background-only screenshots at 390, 1440, 1920 and 2560 px: centre darker than edges, maximum luma under 40, the text column's 16 px blocks at most 20 luma.

## What the page scripts write

- Psychube pages: profile table (rarity, tags, effect name, max level, stats at max level, the extra stat, the game's recommendations, whether the global client has it), the effect in the game's own text for Amplification 1 to 5, names table.
- Statuses page: the shared statuses are those that at least three arcanists' own kit text names in brackets; the effect column is the game's text of each status id (`skill_eff_desc.json`), the lead and the section intros are facts in our own words; the column of arcanists does not claim they apply the status.

## Story pages and the short sidebar

- Story pages (`pipeline/story.py`): a chapter's body starts with its table of stages, and no description says the page holds the text. Names of chapters and stages are the Compendium's headings in each language; a stage title that another page also has gets its chapter in brackets. The Compendium's bold marks are made to parse without changing a word. Only the six index pages are in the sidebar. `check_prose.py` and `to-zh-cn.py` skip `story/`.
- Short sidebar (agent): profile, chapter and stage pages show their own group whole and only the first link of every other group (`src/routeData.ts`), which keeps the build under the 1 GB that GitHub Pages serves. Stage pages are left out of `llms.txt` and the bundles; `llms.txt` says where they are. A stage is three steps from the home page, which `check-dist.mjs` allows for story pages only.
