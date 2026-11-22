---
title: "Jiu Niangzi"
description: "Jiu Niangzi is a 6-star Mineral arcanist who deals Reality DMG, stacks Liquor and casts follow-up attacks."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Her Ultimate spends 6 Liquor for Penetration Rate +100% only when she holds 6 or more; with fewer, she gains 6 Liquor and 2 Cheers instead."
lastVerified: 2026-11-22
aliases:
  - "曲娘"
  - "곡랑"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Jiu Niangzi.png"
    url: https://reverse1999.fandom.com/wiki/File:Jiu_Niangzi.png
  - title: "Image file, uploaded 2024-01-11"
    url: https://static.wikia.nocookie.net/reverse1999/images/0/07/Jiu_Niangzi.png/revision/latest?cb=20240111180919
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Jiu Niangzi, revision 96733"
    url: https://reverse1999.fandom.com/wiki/Jiu_Niangzi?oldid=96733
---

![Jiu Niangzi, full-length art](/art/characters/jiu-niangzi.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Mineral |
| Damage | Reality |
| Tags | DPS, Extra Action, Channel |
| Mainland release | 2024-01-11 |
| Global release | 2024-05-30 |

Jiu Niangzi builds [Liquor], which powers her next damage incantation. Bottoms Up spends Liquor on a follow-up hit; Baijiu Ladle stocks Liquor and puts her in the [Tipsy] channel, which casts Bottoms Up by itself at the start of the next round. Her Insight passives refill Liquor from the buffs, counters, shields and channels on the team.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Bottoms Up (single-target attack) | 160% Reality DMG | 240% | 400% |
| Baijiu Ladle (self channel) | 3 [Liquor], 1 [Cheers]; [Tipsy] for 1 round | 6 Liquor, 1 Cheers | 9 Liquor, 2 Cheers |

- **Bottoms Up**: while she holds Liquor, it spends 1 to 3 stacks at random (chances 20%, 40% and 40% for 1, 2 and 3) on a follow-up hit, which gains Reality DMG +60% for each stack spent.
- **Tipsy**: if she is still channeling at the start of the next round, she casts Bottoms Up of the same rank as the Baijiu Ladle on the enemy with the lowest HP percentage. She cannot act while channeling, and an Ultimate attack on her ends it.

[Liquor]: powers up her next damage incantation; stacks, and cannot be dispelled.

[Cheers]: raises both the least and the most Liquor that Bottoms Up spends by 1, spending all she has if there is not enough; one stack is used each time.

## Ultimate: Baijiu and Mayhem

A mass attack for 350% Reality DMG, with Reality DMG +100% for each enemy fewer than 3, up to +200%. If she holds 6 or more Liquor before casting, she spends 6 to give the attack Penetration Rate +100%; with fewer, she gains 6 Liquor and 2 Cheers.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Gains 3 Liquor on entering battle. At the end of each round, gains 1 Liquor for every 4 different statuses of the kinds Stats Up, Pos Status, Counter, Shield and Channel on all allies, at most 3, rounded down. |
| 2 | ATK +5% on entering battle. |
| 3 | At the start of each round, while she holds Liquor, gains 1 random effect of the [Collection of Buffs] for 2 rounds. |

[Collection of Buffs]: one of four effects: DMG Taken Reduction +20%, DMG Heal +20%, Incantation Might +20% or Ultimate Might +20%; effects she does not have come first.

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×6; Spell of Banishing ×6; Milled Magnesia ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×10; Perpetual Cog ×5; Biting Box ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×16; Wyrmling Skeleton ×6; Mistilteinn ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | The Ultimate deals 400%, with +150% for each enemy fewer than 3, up to +300%. |
| 2 | Bottoms Up's follow-up gains Reality DMG +90% for each Liquor spent. |
| 3 | Insight III gives 2 effects of the Collection of Buffs. |
| 4 | Bottoms Up can spend up to 4 Liquor, with chances of 5%, 15%, 40% and 40% for 1, 2, 3 and 4. |
| 5 | The Collection of Buffs effects become +25% each; at the end of the round she gains 1 Liquor for every 3 different statuses, at most 5. |

## Euphoria

Euphoria opens at Insight III level 30. Jiu Niangzi has one Epiphany of four levels, built on [Sublime Flow].

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | An Ultimate attack no longer ends Tipsy. Each time another ally takes an extra action, she gains 1 Liquor and 1 Sublime Flow. With Sublime Flow at its cap, Baijiu Ladle first casts a Bottoms Up of the same rank, then enters Tipsy. |
| 1 | 2 | Her Ultimate gains Ultimate Might +4% for each Sublime Flow stack, up to +48%, and afterwards she gains 1 Liquor for each Sublime Flow stack. |
| 1 | 3 | When she gains Liquor at the end of the round, she gains as many stacks of Sublime Flow. |
| 1 | 4 | Baijiu Ladle at rank 1, 2 or 3 gives 2, 3 or 5 Sublime Flow. After another ally acts of its own accord, she spends a random amount of Liquor on a follow-up Bottoms Up, at most 3 times a round. |

[Sublime Flow]: Incantation Might +3% per stack, up to 12 stacks; lasts 3 rounds and cannot be dispelled.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Jiu Niangzi | 曲娘 | 曲娘 | 曲娘 | 곡랑 |
