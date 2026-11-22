# Agent test, 2026-11-22

Twelve questions (T1 to T12 in `../../questions.md`). One reader model (Claude Sonnet, as a subagent), one run per side, 3 fetches per question, local serving of the site. Questions and expected answers written by the author of the site from the game data the pages cite. Fetches counted from the logs in this folder.

| # | This site | Original sources |
| --- | --- | --- |
| T1 pity carry-over | pass | fail: not found (4 fetches, over the budget) |
| T2 hard and soft pity | pass | partial: no "same banner type" for the reset |
| T3 after a lost 50/50 | partial: answer right, added that the guarantee does not carry to the next banner, which no source states | partial: answer right, carry-over not addressed |
| T4 7th duplicate 6-star | pass | partial: 28 Albums inferred, Pneuma Film Developers missing |
| T5 mainland-only arcanists | pass | partial: lists Narcissus, whom the global client 111.0.1077 already has (the Fandom CN tag is stale) |
| T6 Perchta | pass | pass |
| T7 Sonetto buff | pass | pass |
| T8 Druvis III Euphoria | pass | partial: unlock condition not found |
| T9 Evelyn | pass | pass |
| T10 6-star rate | pass | pass |
| T11 Druvis III Insight 3 | pass | fail: tiers not attributed, Sharpodonty and Tome missing |
| T12 zh-TW carry-over | partial (answered from the home page without the qualifier); after the fix, pass in a rerun with 2 fetches | fail: not found |

| Run | Pass | Partial | Fail | Fetches (log) |
| --- | --- | --- | --- | --- |
| This site, start `http://127.0.0.1:4473/reverse1999-wiki/` | 10 | 2 | 0 | 6 (T12 rerun: 2) |
| Original sources (Fandom, official site, Prydwen) | 4 | 5 | 3 | 21, 4 of them 403 (Fandom HTML pages and Prydwen); T1 over the budget |

Causes and changes on the site:
- T12: the zh-TW home page named only the carrying type. The home page now also says that limited, collaboration and most event banners clear the count, in every language.
- T3: the page states what the rule text says (the carry-over rule names the count and the raised rate; the guarantee names the current banner's rate-up). The reader's extra inference is not in the page; no change.
