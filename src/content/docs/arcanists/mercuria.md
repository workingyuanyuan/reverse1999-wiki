---
title: "Mercuria"
description: "Mercuria is a 6-star Spirit arcanist who deals Mental DMG and stacks Cosmic Energy, a team damage buff."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Each stack of Cosmic Energy expires on its own after 2 rounds (3 from Portrait 5); her Insight 3 team buffs need 9 and 16 stacks at the start of the round."
lastVerified: 2026-11-22
aliases:
  - "環狀水星"
  - "环状水星"
  - "マーキュリア"
  - "머큐리아"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Mercuria.png"
    url: https://reverse1999.fandom.com/wiki/File:Mercuria.png
  - title: "Image file, uploaded 2024-07-05"
    url: https://static.wikia.nocookie.net/reverse1999/images/f/fa/Mercuria.png/revision/latest?cb=20240705093508
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Mercuria, revision 85023"
    url: https://reverse1999.fandom.com/wiki/Mercuria?oldid=85023
---

![Mercuria, full-length art](/art/characters/mercuria.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Spirit |
| Damage | Mental |
| Tags | Support, Rank Up, DPS |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Psychubes recommended in game | [One with the Flow](/psychubes/one-with-the-flow/), [Starlight Wellspring](/psychubes/starlight-wellspring/) |
| Mainland release | 2024-07-18 |
| Global release | 2024-10-31 |

Mercuria gains stacks of Cosmic Energy whenever an ally casts an incantation, more for higher ranks, and every stack raises the damage of the whole team. At 9 and 16 stacks her Insight 3 passive adds Critical DMG and Incantation Might for all allies. Her Ultimate makes every ally's incantations count one rank higher in rank-based effects.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Restless Souls (single-target attack) | 160% Mental DMG | 240% | 400% |
| Self-Focusing (team buff) | allies Critical Rate +20%; Cosmic Energy +4 stacks | +25%; +5 | +30%; +6 |

- **Restless Souls** heals the ally with the lowest HP by 50% of Mercuria's ATK. It deals 30% more Mental DMG for each rank 2 incantation in the AP area and 50% more for each rank 3 one, up to 250% more.
- **Self-Focusing** lasts 2 rounds, for the Critical Rate and for the stacks.

## Ultimate: Morning Star for the Night

Removes 2 random Stats Up or Pos Status effects from every enemy, then deals 400% Mental DMG to all enemies. All allies gain [Rank Up] for 2 rounds.

[Rank Up]: an incantation counts as 1 rank higher wherever its rank is part of a calculation; its own effects do not change.

[Cosmic Energy]: a [Force Field]. Each stack gives all allies DMG Dealt +2%; up to 25 stacks, each with its own duration; cannot be dispelled.

[Force Field]: an effect the holder grants to characters on the field; it ends when the holder leaves the field.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Mercuria enters battle with 8 stacks of Cosmic Energy for 2 rounds. After any ally casts a rank 1, 2 or 3 incantation, she gains 2, 3 or 4 stacks, up to 25. On entering battle she gains 1 Moxie for each ally of the Natural Afflatus, up to 3. |
| 2 | ATK +5% on entering battle. |
| 3 | At the start of a round with 9 or more stacks, all allies gain Critical DMG +30% for 1 round; with 16 or more, also Incantation Might +20% for 2 rounds. At the end of a round in which allies cast 2 or more rank 3 incantations, she gains 1 Moxie. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×3; Page of Beastly Thirst ×3; Silver Ore ×6; Cicada Wings ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×5; Scroll of Beastly Thirst ×5; Liquefied Terror ×5; Golden Grass Incense ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×8; Tome of Beastly Thirst ×8; Wyrmling Skeleton ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | The Insight 3 Moxie needs 2 or more rank 2 incantations in the round instead. |
| 2 | The Insight 3 buffs become Critical DMG +50% and Incantation Might +30%. |
| 3 | Cosmic Energy holds up to 30 stacks, and each gives DMG Dealt +2.5%. |
| 4 | The Ultimate deals 475%, and Rank Up lasts 1 round longer. |
| 5 | Cosmic Energy lasts 1 round longer, and each stack gives DMG Dealt +3%. |

## Euphoria

Euphoria opens at Insight III level 30. Mercuria has one Epiphany of four levels.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Restless Souls deals 100% more per rank 2 and 200% more per rank 3 incantation in the AP area, up to 1000% more. At rank 3 it also gives Mercuria [Preparation · Mercuria] and [Simplified Ritual] after the attack. |
| 1 | 2 | The Critical Rate of Self-Focusing lasts 3 rounds. At the start of each round, one random incantation of Mercuria's gains 1 rank. |
| 1 | 3 | For each stack of Cosmic Energy, the Ultimate deals extra Mental DMG equal to 20% of its base and gains Ultimate Might +3%. |
| 1 | 4 | Rank Up also acts when its holder attacks with a rank 3 incantation: DMG Dealt rises by 40% of the bonus from Mercuria's current Cosmic Energy; a holder with Incantation Might Up gains 40% of Mercuria's Incantation Might Up, and one with Critical DMG Up gains 40% of her Critical DMG Up. The global text ties both of these to her Cosmic Energy instead. |

[Preparation · Mercuria]: at the start of the next round, a rank 2 Precast Incantation of Restless Souls is created.

[Simplified Ritual]: the next Ultimate costs no AP; removed once Mercuria casts an Ultimate herself.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Mercuria | 环状水星 | 環狀水星 | マーキュリア | 머큐리아 |
