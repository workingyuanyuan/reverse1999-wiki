---
title: "Tuesday"
description: "Tuesday is a 6-star Spirit arcanist who deals Mental and Genesis DMG through Poison; she has Euphoria."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Horror Story Night is an array, and only one array can be on the field: when another array replaces it or it ends, all Poison on the enemies settles at once."
lastVerified: 2026-11-22
aliases:
  - "藍手帕"
  - "蓝手帕"
  - "チューズデー"
  - "튜즈데이"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Tuesday.png"
    url: https://reverse1999.fandom.com/wiki/File:Tuesday.png
  - title: "Image file, uploaded 2024-08-09"
    url: https://static.wikia.nocookie.net/reverse1999/images/1/16/Tuesday.png/revision/latest?cb=20240809040452
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Tuesday, revision 85069"
    url: https://reverse1999.fandom.com/wiki/Tuesday?oldid=85069
---

![Tuesday, full-length art](/art/characters/tuesday.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Spirit |
| Damage | Mental |
| Tags | DPS, Poison, Support, Array |
| Mainland release | 2024-08-08 |
| Global release | 2024-12-05 |

Tuesday spreads Poison and makes it hit harder. Her attack poisons one enemy and copies the Poison to others, her debuff raises the Genesis DMG enemies take and cuts their Critical Resist Rate, and her Ultimate deals Genesis DMG for every instance of Poison on a target, then sets up Horror Story Night, an array that settles enemy Poison an extra time each round without shortening it. Fear's Cradle from her first Insight lets the team's Poison crit.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| The Horror's Delight (single-target attack) | 130% Mental DMG; Poison spreads 2 times | 230%; 3 times | 455%; 4 times |
| In Mother's Arms (debuff on all enemies) | Genesis DMG Taken +15% | +25% | +35% |

- **The Horror's Delight** puts 2 instances of [Poison] on the target for 2 rounds, each dealing Genesis DMG equal to 20% of Tuesday's ATK at the end of the round. It then puts 1 instance of the same Poison on another random enemy, as many times as the table says, while a target is available.
- **In Mother's Arms** lasts 2 rounds and also lowers Critical Resist Rate by 15% at every rank, or by 20% on a poisoned enemy.

## Ultimate: Please, Come On In

Deals 225% Mental DMG to all enemies and puts 1 instance of Poison (20% of ATK, 2 rounds) on each. Then each target takes extra Genesis DMG equal to Tuesday's ATK × the instances of Poison on it × 30%; this damage can crit. The Ultimate also sets up the array [Horror Story Night] for 3 rounds.

## Statuses

| Status | Effect |
| --- | --- |
| Poison | At the end of the round, the holder takes Genesis DMG based on the caster's ATK; instances stack. |
| Horror Story Night | An array. Enemy Poison does not lose rounds when it settles; at the start of the enemy round, 1 round of their Poison settles. When the array ends or is replaced, all enemy Poison settles at once. Only one array can exist on the field, allied or enemy. |
| Fear's Cradle | A force field, gone when Tuesday leaves the field. The team's Poison can crit. Each Stats Down, Neg Status or Control effect an ally puts on an enemy has a 50% chance to add 1 instance of Poison (20% of ATK, 1 round). Cannot be dispelled. |
| Room Service | Moxie that an ally gains beyond the cap is stored, up to 5 per character, and refills that character's Moxie at the end of the round where there is room. Cannot be dispelled. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | On entering battle, Tuesday gains Fear's Cradle and Genesis DMG Dealt +15%. |
| 2 | ATK +5% on entering battle. |
| 3 | On entering battle, Tuesday gains Room Service and Moxie +2; the Moxie is given once. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×3; Page of Beastly Thirst ×3; Trembling Tooth ×5; Perpetual Cog ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×5; Scroll of Beastly Thirst ×5; Esoteric Bones ×6; Prophetic Bird ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×8; Tome of Beastly Thirst ×8; Silver Bullet ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | The Ultimate puts 2 instances of Poison; its extra Genesis DMG becomes 50% per instance. |
| 2 | In Mother's Arms raises Genesis DMG Taken by 30, 40 or 50% by rank and lowers Critical Resist Rate by 25%, or 30% on a poisoned enemy. |
| 3 | The Ultimate puts 3 instances of Poison; its extra Genesis DMG becomes 70% per instance. |
| 4 | Insight 1 gives Genesis DMG Dealt +35%. |
| 5 | The Horror's Delight deals 210, 310 or 535% by rank and spreads Poison 3, 4 or 5 times. |

## Euphoria

Euphoria opens at Insight III level 30. Tuesday has one Epiphany of four levels.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | The extra Genesis DMG of the Ultimate doubles (60% per instance of Poison, or 100% and 140% with Portraits 1 and 3), and the Ultimate gives Tuesday Moxie +1. |
| 1 | 2 | Insight 3 gives 2 more Moxie on entering battle, and her Ultimate no longer counts toward the team's incantation draw limit. |
| 1 | 3 | On a poisoned enemy, the Critical Resist Rate cut of In Mother's Arms doubles (to 40%, or 60% with Portrait 2), and the enemy takes Poison DMG +20%. |
| 1 | 4 | At the end of each round while Horror Story Night is active, Tuesday gains Moxie +1 and the debuffs of In Mother's Arms on all enemies last 1 round longer. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Tuesday | 蓝手帕 | 藍手帕 | チューズデー | 튜즈데이 |
