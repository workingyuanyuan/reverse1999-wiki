---
title: "Aleph"
description: "Aleph is a 6-star Intellect arcanist who deals Mental DMG and supports the team with Eureka and Inspiration."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "His Ultimate is a channel: the memorized incantations and the Interpretation burst land only next round, just before the action point area resolves, and he cannot act until then."
lastVerified: 2026-11-22
aliases:
  - "阿萊夫"
  - "阿莱夫"
  - "エル・アレフ"
  - "알레프"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Aleph.png"
    url: https://reverse1999.fandom.com/wiki/File:Aleph.png
  - title: "Image file, uploaded 2025-03-15"
    url: https://static.wikia.nocookie.net/reverse1999/images/9/92/Aleph.png/revision/latest?cb=20250315142427
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Aleph, revision 84946"
    url: https://reverse1999.fandom.com/wiki/Aleph?oldid=84946
---

![Aleph, full-length art](/art/characters/aleph.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Intellect |
| Damage | Mental |
| Tags | Support, Inspiration, Channel, Eureka |
| Mainland release | 2025-03-20 |
| Global release | 2025-06-19 |

Aleph runs on Eureka, which his Insight 1 passive supplies at the start of every round. Each point of Eureka the team spends becomes a point of [Inspiration] on a basic incantation, and casting a card that carries Inspiration adds an [Impromptu Incantation] to the end of the queue. His Ultimate memorizes the cards cast in its round and recasts them in the next, then turns Impromptu Incantation into a burst against every enemy holding [Interpretation].

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Disciplinary Power (single-target attack) | 100% Mental DMG | 200% | 400% |
| Idealist's Declaration (mass buff) | 1 stack of [Clarification] to all allies | 2 stacks | 3 stacks |

- **Disciplinary Power** gives Aleph [Continuous Action I] for 1 round at every rank. After the attack it spends 2 Eureka to give Impromptu Incantation 1 more attack instance this round.
- **Idealist's Declaration** stacks last 3 rounds. The card also spends 2 Eureka to give all allies 1 more stack.

## Ultimate: Reflections of Omniscience

Aleph enters a self channel and [Memorize]s the first 2 basic incantations actively cast this round, then holds [Hyperthymesia] for 1 round.

## Statuses

| Status | Effect |
| --- | --- |
| Continuous Action I | AP +1. |
| Clarification | Incantation Might +10%. Up to 4 stacks, each with its own duration. |
| Inspiration | Each Eureka spent adds 1 point. At the start of each round the points are spread at random over basic incantations, at most 5 on one card; points on cards not used by the end of the round are cleared. Casting a card that carries points adds an Impromptu Incantation to the end of the queue, and its points go to that Impromptu Incantation. |
| Impromptu Incantation | Hits a random enemy for 200% Mental DMG plus 15% Mental DMG for each Inspiration point it holds. With at least 3, 6, 12 or 20 points it gains 1, 2, 3 or 5 more attack instances. Its damage uses the average stats of all allies. |
| Interpretation | Mental DEF and DMG Taken Reduction −10%, and −2% more of each for every stack after the first. Lasts 3 rounds; up to 8 stacks, each with its own duration. |
| Memorize | Keeps the rank, the Inspiration points and the Rewrite effects of a memorized card. |
| Hyperthymesia | Aleph channels into the next round and cannot act. The channel ends just before the action point area resolves: the memorized cards join the spell queue and are cast with the round's other cards, count as actively cast and give no Moxie. Then Impromptu Incantation gains 2 more attack instances this round; each attack but the last puts Interpretation on its target, and the last hits every enemy holding Interpretation for extra Mental DMG equal to its stacks × 80%, after which all Interpretation is removed. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Max Eureka +2, and Eureka +4 at the start of each round. Eureka spent by any ally builds Inspiration. When an ally with Clarification actively casts an attack incantation, Aleph spends 1 Eureka so that 1 attack instance of Impromptu Incantation this round puts Interpretation on the target it hits. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | Each time Aleph spends Eureka, he has a 25% chance to get 1 Eureka back. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×3; Page of Starlit Ascent ×3; Spell of Banishing ×6; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×5; Scroll of Starlit Ascent ×5; Cicada Wings ×6; Golden Grass Incense ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×8; Tome of Starlit Ascent ×8; Wyrmling Skeleton ×6; Rheingold ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Continuous Action I from Disciplinary Power lasts 2 rounds; the Insight 3 chance to get Eureka back becomes 50%. |
| 2 | The Ultimate memorizes 3 cards; each stack of Interpretation after the first lowers Mental DEF and DMG Taken Reduction by 3%. |
| 3 | The final attack of Impromptu Incantation deals stacks × 160%; when Hyperthymesia ends, Impromptu Incantation gains 4 more attack instances. |
| 4 | Clarification gives Incantation Might +15%. |
| 5 | The final attack deals stacks × 240%; each stack of Interpretation after the first lowers Mental DEF and DMG Taken Reduction by 5%. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Aleph | 阿莱夫 | 阿萊夫 | エル・アレフ | 알레프 |
