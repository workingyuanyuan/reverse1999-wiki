---
title: "Corvus"
description: "Corvus is a 6-star Intellect arcanist who deals Mental DMG and builds a team-buffing array with Dynamo."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Her follow-up attack Sew It All Up deals its extra damage only at Pulsing Field Lv.2 and Lv.3, which need 50 and 120 Dynamo poured into the field."
lastVerified: 2026-11-22
aliases:
  - "告死鳥"
  - "告死鸟"
  - "コルヴス"
  - "코르부스"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Corvus.png"
    url: https://reverse1999.fandom.com/wiki/File:Corvus.png
  - title: "Image file, uploaded 2025-12-12"
    url: https://static.wikia.nocookie.net/reverse1999/images/f/f3/Corvus.png/revision/latest?cb=20251212035921
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Corvus, revision 84975"
    url: https://reverse1999.fandom.com/wiki/Corvus?oldid=84975
---

![Corvus, full-length art](/art/characters/corvus.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Intellect |
| Damage | Mental |
| Tags | DPS, Dynamo, Channel, Array |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Mainland release | 2025-10-09 |
| Global release | 2026-01-01 |

Corvus keeps an array, the Pulsing Field, under the team and sets up its first level herself. Each action she takes gives her Dynamo, and her follow-up attack, Sew It All Up, pours that Dynamo into the field, which rises to Lv.2 and Lv.3 and buffs every ally more at each level. Her incantations give her stacks of [Electric Arc], which raise her ATK, and put [Breaking Point] on an enemy, which Sew It All Up spends for its bonus effects.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Arc-Threaded Shot (single-target attack) | 200% Mental DMG; 2 stacks of Electric Arc | 300%; 4 stacks | 500%; 8 stacks |
| Rosy Cracks (self channel) | 2 stacks of Electric Arc if the target already has Welding | 4 stacks | 8 stacks |

- **Arc-Threaded Shot** gives the target it hits 1 stack of Breaking Point at every rank.
- **Rosy Cracks** puts Corvus in [Stitching] for 2 rounds and puts [Welding] on the target enemy. On a target that already has Welding, Corvus also gains the Electric Arc in the table and the target gains 1 stack of Breaking Point.

## Ultimate: Sewn into Forever

Deals 700% Mental DMG to one enemy, gives it 1 stack of Breaking Point and triggers Sew It All Up once. The Ultimate does not count against the team's limit of incantations drawn.

## Sew It All Up

A single-target attack that counts as an extra action. It deals 400% Mental DMG, draws on Ultimate Might at a 100% rate and pours up to 20 stacks of Dynamo into the Pulsing Field. What else it does depends on the level of the field; the bonus marked with Breaking Point needs 1 stack of Breaking Point on the target and spends it.

| Field level | Extra damage | With Breaking Point |
| --- | --- | --- |
| Lv.1 | none | Corvus gains 3 stacks of Electric Arc |
| Lv.2 | +200% Mental DMG | +5% Mental DMG for each stack of Electric Arc she has |
| Lv.3 | +600% Mental DMG | +5% Mental DMG and Ultimate Might rate +0.3% for each stack of Electric Arc or Flickering Arc she has |

## Statuses

| Status | Effect |
| --- | --- |
| Pulsing Field | An array. At the start of a round it rises with the Dynamo poured into it: Lv.2 at 50 or more, Lv.3 at 120 or more. When the field ends, the Dynamo in it is lost. |
| Pulsing Field Lv.1 | All allies DMG Bonus +15%, for 3 rounds. |
| Pulsing Field Lv.2 | All allies Incantation Might +25% and DMG Bonus +15%, for 3 rounds. |
| Pulsing Field Lv.3 | All allies Ultimate Might +35%, Incantation Might +25% and DMG Bonus +15%, for 2 rounds. |
| Dynamo | Up to 30 stacks; cannot be dispelled. |
| Electric Arc | ATK +0.3% per stack, up to 60 stacks. |
| Flickering Arc | ATK +0.3% per stack, up to 240 stacks; cannot be dispelled. |
| Breaking Point | Spent by Sew It All Up for its bonus effect. |
| Welding | When the holder is attacked, Corvus gains 1 stack of Electric Arc. A Mental DMG attack also lowers its Mental DEF by 1%, down to −50% in total, and gives her 1 more stack. Sew It All Up strikes the enemy with Welding first; only one enemy has it at a time. |
| Stitching | At the end of each round, Corvus casts Sew It All Up at the effect of the current field level. Gaining it again adds to its duration. |
| Amplified Surge | Moxie +3 when the field reaches Lv.3; while the field is at Lv.3, Max Moxie +5 and immunity to Control effects. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | On entering battle, Corvus gains Amplified Surge. After each action she takes, she gains 10 stacks of Dynamo. At the start of a round with no Pulsing Field of any level, she sets up Pulsing Field Lv.1. |
| 1 | When Pulsing Field Lv.3 ends, every 2 stacks of Electric Arc turn into 1 stack of Dynamo and 2 stacks of [Flickering Arc]. |
| 2 | Critical Rate +10% on entering battle. |
| 3 | When the enemy with Welding leaves the field, Welding passes to the enemy with the lowest HP percentage, a boss first, with the same number of Breaking Point stacks. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×3; Page of Starlit Ascent ×3; Spell of Banishing ×6; Cicada Wings ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×5; Scroll of Starlit Ascent ×5; Rough Silver Ingot ×4; Red Lacquer Slab ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×8; Tome of Starlit Ascent ×8; Wyrmling Skeleton ×6; Rheingold ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | The Ultimate deals 1200% and gives 2 stacks of Breaking Point; Welding lowers Mental DEF by 2% per attack, down to −100% in total. |
| 2 | The Ultimate triggers Sew It All Up twice. |
| 3 | Sew It All Up deals 500%; its extra damage becomes 300% at Lv.2 and 700% at Lv.3. |
| 4 | The bonus of Sew It All Up for each stack becomes 8% at Lv.2 and Lv.3. |
| 5 | Both incantations give 4, 8 or 16 stacks of Electric Arc by rank; Electric Arc caps at 80 stacks and Flickering Arc at 320. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Corvus | 告死鸟 | 告死鳥 | コルヴス | 코르부스 |
