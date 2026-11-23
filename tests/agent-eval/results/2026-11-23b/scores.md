# Agent test, 2026-11-23 (second scope)

Nine questions on the pages added in the second scope (T23 to T31 in `../../questions.md`): Combat basics, Statuses, Insight and levels, Release dates, a Psychube page, and one question each from the Traditional Chinese, Japanese and Korean home pages. One reader model (Claude Sonnet, as a subagent), one run per side, 3 fetches per question, local serving of the site. Questions and expected answers written by the author of the site from the game data the pages cite. Fetches counted from the logs in this folder.

| # | This site | Original sources |
| --- | --- | --- |
| T23 Star advantage | pass | fail: no page on Afflatus, 5 fetches (1 error) |
| T24 Petrify and Freeze | pass | fail: not found, 6 fetches |
| T25 Insight III Sharpodonty | pass | pass |
| T26 Thunderous Applause | pass, 3 fetches: the name does not say which index page lists it | pass |
| T27 Mainland to global gap | pass | fail: not found |
| T28 Moxie of an Ultimate | pass | fail: no number |
| T29 燃燒 | pass | pass (read with T24's fetches) |
| T30 立于风暴脊 | pass | fail: not found |
| T31 4성 통찰 | partial: Insight II, level 50, without the reset to level 1 | partial: Insight II, no level cap |

| Run | Pass | Partial | Fail | Fetches (log) |
| --- | --- | --- | --- | --- |
| This site, start `/`, `/zh-tw/`, `/ja/`, `/ko/` | 8 | 1 | 0 | 15 |
| Original sources (Fandom through its API, official site, Prydwen) | 3 | 1 | 5 | 22, 1 of them an error (Prydwen 403) |

The site reader went straight to a page it guessed from the URL pattern on five questions instead of starting at the home page; the guessed pages exist and the count stays within the budget.

Causes and changes on the site:
- T26: the Psychube index pages split the Psychubes by the stat they add, which a reader with only the name cannot know. `llms.txt` now gives the URL pattern of a Psychube page. Not rerun.
- T31: the reset to level 1 is in the caveat; the reader left it out. No change.
