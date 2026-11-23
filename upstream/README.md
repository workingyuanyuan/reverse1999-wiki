# Following the sources

`pnpm upstream` (`pipeline/upstream.py`) compares the game data the pages were written from with the current game data, and changes no page.

## What is watched

- The two repositories of decoded client tables pinned in `records/sources.json`: `St-Pavlov-Foundation/re1999-data` (mainland client) and `St-Pavlov-Foundation/re1999-data-global` (global client). The script reads the head of each with `git ls-remote`, fetches the tables this site reads at that head into `cache/`, and compares what each page rests on.
- The Fandom revisions that pages cite (`?oldid=`), through the Fandom API. Fandom is a second witness, so a newer revision is a note.
- The art files that pages show (`records/art.json`, `records/art-psychubes.json`), through the Fandom API. A newer upload is a note, and so is a Psychube file that was missing and now exists.

## The report

One line per difference, naming the page:

| Line | Meaning | What to do |
| --- | --- | --- |
| `arcanists/<slug>: changed in record` | rarity, Afflatus, damage type, Euphoria, Insight materials, a global name, or whether the global client has the arcanist | read the record in `records/arcanists.json` after the rebuild and correct the profile table, Inheritance or Names |
| `arcanists/<slug>: changed in zh-CN, en, …` | the game's text of the kit changed in those languages | compare `cache/source/<slug>.json` before and after the rebuild; restate the change |
| `index: <slug> now in the global client` | an arcanist out only on the mainland service reached the global client | remove it from the mainland-only table of every home page; its own page gets the official names and the global release |
| `index: <slug> new, mainland client only` | a new arcanist in the mainland client | add it to the mainland-only table; a page needs the owner's go-ahead |
| `systems/summoning: <client> banner type <id> changed` | the rule text of a banner type changed (markup and line breaks ignored) | read the text in `const.json` (id from `summon_pool_detail.json`) and correct the page |
| `systems/summoning: <client> rates and pity changed` | a pool has new base rates or pity counts | correct the rate and pity tables |
| `psychubes/<slug>: changed in …` | the Psychube's record changed: stats, extra stat, tags, recommendations, names or effect text (`text`) | run `python3 -I pipeline/psychube.py text <slug>` and compare; correct the effect, then regenerate the generated blocks by writing a new skeleton beside the page |
| `psychubes: new Psychube <slug>` | a new Psychube in the mainland client | `psychube.py write <lang> <slug>` in each language, write it, `psychube.py indexes` |
| `systems/statuses: <client> <id> changed` | the text of a status the Statuses page describes changed | correct its row in `records/statuses.json` and the translations, then `pipeline/write_systems.py` |
| `systems/insight: <rarity> changed` | a level cap or the Sharpodonty of an Insight changed | `pipeline/write_systems.py` rewrites the page |
| `systems/combat: … changed` | the Field Manual tips, a stat name or the Moxie cost of an Ultimate changed | read the change and correct Combat basics |
| `systems/resonance: … changed` | a Resonance level, grid size, material count, pattern cost, pattern stat or an arcanist's set changed | `pipeline/write_systems.py` rewrites the page; if it exits with an error, the values no longer agree within a rarity and the page needs a new table |
| `note …` | a new client build, a new arcanist in both clients, a newer Fandom revision | nothing fails; read when the pages are next checked |
| `note arcanists/<slug>: Fandom File:… has a newer upload` | the wiki replaced the art file | look at the new file; if it is still the full-length art, run `python3 -I pipeline/fetch_art.py <slug>` and copy the printed `art` lines into the page in every language |
| `note psychubes/<slug>: Fandom File:… has a newer upload` or `… now has File:…` | the wiki replaced or added a Psychube's illustration | look at the file; if it is the Psychube's own illustration, run `python3 -I pipeline/fetch_art.py --psychubes <slug>`, then `python3 -I pipeline/psychube.py art` and the zh-cn conversion |

Exit 0: no difference. 1: differences. 2: the comparison could not be made (network, a missing file).

## Updating the pages

1. `python3 -I pipeline/fetch_data.py --update` pins both repositories to their current head and fetches the tables.
2. `python3 -I pipeline/build_records.py` rebuilds `records/arcanists.json` and `cache/source/`.
3. Correct the English pages named in the report, then the zh-TW, ja and ko pages; write zh-CN with `scripts/to-zh-cn.py`.
4. Update `appliesTo` and the source links (commit and build) of every page that was read again, and its `lastVerified`.
5. `pnpm verify`, then the owner confirms before the change goes live.
