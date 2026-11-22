# Agent test, 2026-11-23

Ten questions on the pages added since the first run (T13 to T22 in `../../questions.md`): an Afflatus index, arcanist pages of different kinds (5-star Euphoria, a kit the two clients word differently, mainland-only arcanists and Epiphanies), and one question each from the Japanese, Korean and Traditional Chinese home pages. One reader model (Claude Sonnet, as a subagent), one run per side, 3 fetches per question, local serving of the site. Questions and expected answers written by the author of the site from the game data the pages cite. Fetches counted from the logs in this folder; a question over the budget fails.

| # | This site | Original sources |
| --- | --- | --- |
| T13 6-star Beast Mental | pass | fail: list not found, 5 fetches (2 errors) |
| T14 Tennant Euphoria | pass | fail: right answer from the Euphoria page, 10 fetches (4 errors) |
| T15 Door's shield | pass | partial: the global reading only, no difference between the clients |
| T16 Drake | pass | partial: out only on the mainland inferred from a tag; names not marked unofficial |
| T17 Getian Old Bones | pass | fail: 300%; the game data of both clients gives 400% |
| T18 Centurion's second Epiphany | pass | fail: says she has one Epiphany |
| T19 An-An Lee Epiphany 2 level 3 | partial: formula and difference between the clients right; the page's totals (+35, 40, 50%) read as a mismatch | fail: global reading only, 5 fetches |
| T20 リーリャ Insight 3 | fail: answered for Huntsworn Lilya, linked from the home page's mainland-only table | partial: the Insight III row assumed from row order, Sharpodonty missing |
| T21 37 광상 | pass | partial: unlock level right; Euphoria out only on the mainland not found |
| T22 格林杜爾 | pass | partial: out only on the mainland inferred from a tag |

| Run | Pass | Partial | Fail | Fetches (log) |
| --- | --- | --- | --- | --- |
| This site, start `/`, `/ja/`, `/ko/`, `/zh-tw/` | 8 | 1 | 1 | 14 |
| Original sources (Fandom through its API, official site, Prydwen) | 0 | 5 | 5 | 31, 6 of them errors (Fandom HTML pages and Prydwen 403) |

Causes and changes on the site:
- T19: the page gave the totals for each rank without the step between them. It now says that at 400% the formula gives 20% more, so the totals are +35, 40 and 50%. Not rerun.
- T20: Huntsworn Lilya and Lilya share the name リーリャ, and only Huntsworn Lilya is on the home page. Her caveat now says she is a separate arcanist, and her opening paragraph links Lilya's page, in every language. Rerun twice: with the caveat alone, the reader noticed the second arcanist but did not open her page (`site-20261123-t20a.log`, 2 fetches); with the link, it gave both arcanists' materials, right (`site-20261123-t20b.log`), in 4 fetches, one of them a second fetch of the same page.
