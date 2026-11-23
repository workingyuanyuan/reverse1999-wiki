# Agent test

Checks whether an agent with only a fetch tool answers questions about Reverse: 1999 better from this site than from the sources a reader would otherwise use.

## Files

| File | Role |
| --- | --- |
| `questions.md` | The questions people ask in each language, and the test set (T1 onward) with the expected answer, the qualifier that is easy to miss, and the page that holds them. The expected answers are written from the game data the pages cite |
| `fetch.mjs` | The fetch tool given to the agent. Modelled on the MCP reference Fetch server: main-article extraction, Markdown output, 5,000 characters per call, `start_index` to continue. Every call is logged to `runs/<run>.log` |
| `results/<date>/` | Answers, fetch logs and scores of each recorded run |

## How to run

1. Build the site with a local address and serve it:

```
SITE_URL=http://127.0.0.1:4473/reverse1999-wiki pnpm build
pnpm preview 4473
```

2. Give a fresh agent the questions (without the expected answers), the fetch command below as its only source, a start URL, and a budget of 3 fetches per question.

```
node tests/agent-eval/fetch.mjs --run <run-name> --q <question-id> <url> [start_index]
```

Start URL for this site: `http://127.0.0.1:4473/reverse1999-wiki/` (T12: `http://127.0.0.1:4473/reverse1999-wiki/zh-tw/`). Start URLs for the baseline: `https://reverse1999.fandom.com/wiki/Reverse:_1999_Wiki`, `https://re1999.bluepoch.com/en/` and `https://www.prydwen.gg/re1999/`.

3. Score each answer against `questions.md`: pass needs the answer and the qualifier; partial is one of the two or an unverified inference; fail is a wrong or missing answer. Before marking an answer wrong, check it against the game data: the expected answer can be the error.

4. Run `pnpm verify` afterwards so that `dist/` carries the public address again.

## Search test

Runs on the live site once its pages are indexed; a record, not a gate for publishing.

1. Give a fresh agent the questions (without the expected answers, and without this site's name or address), a web search tool, and the fetch command above as its only way to read a page. No start URL.
2. Record the search tool, the queries the agent made and its answers. The fetch log holds the URLs it read.
3. Score each question: pass needs a page of this site among the pages read, and the answer with its qualifier. Record "not found" when no page of this site was read.

## Results

### 2026-11-22

12 questions. This site: 10 pass, 2 partial, 0 fail, 6 fetches; T12 passed after a fix to the home page (rerun, 2 fetches). Original sources: 4 pass, 5 partial, 3 fail, 21 fetches, 4 of them refused with 403. One Claude Sonnet reader, one run per side, local serving; questions by the author of the site. Details in `results/2026-11-22/scores.md`.

### 2026-11-23, second scope

9 questions on Combat basics, Statuses, Insight and levels, Release dates and Psychubes. This site: 8 pass, 1 partial, 0 fail, 15 fetches. Original sources: 3 pass, 1 partial, 5 fail, 22 fetches, 1 refused with 403. One Claude Sonnet reader, one run per side, local serving; questions by the author of the site. Details in `results/2026-11-23b/scores.md`.

### 2026-11-23, Resonance

4 questions on the Resonance page. This site: 4 pass, 7 fetches; the list of arcanists by set needed a second fetch of the English page. Original sources: 0 of 4, 11 fetches, 4 refused with 403; Fandom has no Resonance page. One Claude Sonnet reader, one run per side, local serving; questions by the author of the site. Details in `results/2026-11-23c/scores.md`.
