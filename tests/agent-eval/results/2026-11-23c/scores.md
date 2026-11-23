# Agent test, 2026-11-23 (Resonance)

Four questions on the Resonance page (T32 to T35 in `../../questions.md`), one of them from the Traditional Chinese home page. One reader model (Claude Sonnet, as a subagent), one run per side, 3 fetches per question, local serving of the site. Questions and expected answers written by the author of the site from the game data the page cites. Fetches counted from the logs in this folder.

| # | This site | Original sources |
| --- | --- | --- |
| T32 4-star Resonance cap | pass | fail: no Resonance page on Fandom, 3 fetches (1 error) |
| T33 Sharpodonty, 6-star | pass (read with T32's fetch) | fail: not found, 3 fetches (1 error) |
| T34 十四行詩的共鳴調頻 | pass | fail: not found, 3 fetches (2 errors) |
| T35 Lilya's patterns | pass, 3 fetches: the list of arcanists by set starts after the first 5,000 characters of the English page | fail: not found |

| Run | Pass | Partial | Fail | Fetches (log) |
| --- | --- | --- | --- | --- |
| This site, start `/`, `/zh-tw/` | 4 | 0 | 0 | 7 |
| Original sources (Fandom through its API, official site, Prydwen) | 0 | 0 | 4 | 11, 4 of them errors (Fandom HTML and Prydwen 403) |

Causes on the site:
- T35: the arcanist's own page does not name its Resonance set, and the English page reaches the list of arcanists by set only with a second fetch (`start_index` 5000). The reader also opened Huntsworn Lilya first. Not changed.
