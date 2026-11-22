---
title: "Charon"
description: "Charon is a 6-star Spirit arcanist who deals Mental DMG through a channel and raises the team's crits."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "In his Ultimate's channel the first Day of Remorse costs no Shock Wave, each later one costs 50 stacks more, and the channel ends when he runs short."
lastVerified: 2026-11-22
aliases:
  - "卡戎"
  - "カローン"
  - "카론"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Charon.png"
    url: https://reverse1999.fandom.com/wiki/File:Charon.png
  - title: "Image file, uploaded 2025-06-27"
    url: https://static.wikia.nocookie.net/reverse1999/images/e/e2/Charon.png/revision/latest?cb=20250627013806
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Charon, revision 84968"
    url: https://reverse1999.fandom.com/wiki/Charon?oldid=84968
---

![Charon, full-length art](/art/characters/charon.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Spirit |
| Damage | Mental |
| Tags | Support, Dynamo, DPS, Channel, Array |
| Mainland release | 2025-07-17 |
| Global release | 2025-11-20 |

Charon gathers [Shock Wave] from both incantations, from the team's surplus Moxie and from units leaving the field, and every 40 stacks he gains add a stack of [Consternation]. His Ultimate turns his incantations waiting in the Spelldock into more Shock Wave and starts a channel that fires Day of Remorse at the end of each round, while his Insight 1 passive keeps a [Pulsing Field] up for the team. [Fear of Death] on enemies and [Peaceful Soul] on allies grow stronger with each stack of Consternation he holds.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| From the Void (attack on all enemies) | 200% Mental DMG; 20 Shock Wave | 300%; 30 | 500%; 50 |
| Advice from the Dead (team buff) | 20 Shock Wave | 30 | 50 |

At every rank, From the Void puts Fear of Death on the enemies it hits and Advice from the Dead gives all allies Peaceful Soul, each for 2 rounds.

## Ultimate: New Blooms of Life

Charon gains 1 Moxie, removes every From the Void and Advice from the Dead of his from the Spelldock, and gains 20, 30 or 50 stacks of Shock Wave for each card removed, by its rank. He then enters [Shadow of the Past]. Casting the Ultimate again while in Shadow of the Past resets the rising Shock Wave cost.

## Statuses

| Status | Effect |
| --- | --- |
| Shadow of the Past | At the end of each round, triggers Day of Remorse. The first trigger costs no Shock Wave; each trigger raises the cost of the next by 50 stacks. The channel ends when Charon lacks the Shock Wave. |
| Day of Remorse | 150% Mental DMG to all enemies, scaled by Ultimate Might at a 60% rate; each stack of Consternation adds 50% Mental DMG and 10% to that rate. Charon gains 1 Dynamo for every 5 stacks of Shock Wave he holds and 1 Moxie, and Fear of Death and Peaceful Soul last 1 round longer. |
| Shock Wave | Stacks spent by Charon's channel. |
| Consternation | Penetration Rate +5% per stack, at most 10 stacks, each with its own duration. |
| Fear of Death | Critical DEF −20%, and −5% more for each stack of Consternation on Charon (at most −20% more); at 4 or more stacks, DMG Taken +30%. When the holder is hit and its HP falls below 20% of the Max HP it had when the status was applied (a threshold capped at 4000% of Charon's ATK), Charon deals heavy [Static Genesis DMG]. |
| Static Genesis DMG | Genesis DMG that stat bonuses do not change. |
| Peaceful Soul | Critical Rate +30%, and +5% more for each stack of Consternation on Charon (at most +20% more); at 4 or more stacks, 80% of the holder's Critical Rate above the cap turns into Critical DMG. |
| Pulsing Field | Rises at the start of a round with the Dynamo put into it: Lv.2 at 50, Lv.3 at 120. The Dynamo inside is lost when the field ends. |
| Pulsing Field Lv.1 | All allies DMG Bonus +15% for 3 rounds. |
| Pulsing Field Lv.2 | All allies Incantation Might +25% and DMG Bonus +15% for 3 rounds. |
| Pulsing Field Lv.3 | All allies Ultimate Might +35%, Incantation Might +25% and DMG Bonus +15% for 2 rounds. |
| Amplified Surge | Pulsing Field Lv.1 rises straight to Lv.3, which needs 40 Dynamo. On reaching Lv.3, Charon and the adjacent ally in front gain [Simplified Ritual]; while Lv.3 stands, Charon has Penetration Rate +50%. |
| Simplified Ritual | The next Ultimate costs no AP; removed after an Ultimate is actively cast. |
| Dynamo | At most 30 stacks; cannot be dispelled. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Charon gains Amplified Surge, and at the start of a round with no Pulsing Field he sets up Pulsing Field Lv.1. At the end of each round he puts up to 20 Dynamo into the field. He gains 1 Shock Wave for each Dynamo beyond Lv.3, 20 for each point of Moxie the team gains beyond the cap (not while that Moxie is stored), and 20 or 40 whenever an enemy or an ally leaves the field. Every 40 stacks of Shock Wave he gains give him 1 stack of Consternation for 4 rounds. |
| 2 | ATK +5% on entering battle. |
| 3 | On entering battle and whenever an enemy enters, enemies gain Fear of Death for 2 rounds. On entering battle, Charon gains 20 Dynamo, 50 Shock Wave and 2 Moxie, plus 1 Moxie for each other Spirit or Intellect ally (at most 2). |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×3; Page of Beastly Thirst ×3; Magnesia Crystal ×6; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×5; Scroll of Beastly Thirst ×5; Fox Tail ×5; Goose Neck ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×8; Tome of Beastly Thirst ×8; Emerald Slate ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Peaceful Soul gains Critical Rate +7.5% per stack of Consternation (at most +30%), and converts 100% of the excess Critical Rate at 4 stacks. |
| 2 | On entering battle he gains 30 Dynamo, 90 Shock Wave and 3 Moxie. |
| 3 | Day of Remorse deals 400% and scales by Ultimate Might at a 70% rate. |
| 4 | Fear of Death lowers Critical DEF by 7.5% more per stack of Consternation (at most 30%), and raises DMG Taken by 40% at 4 stacks. |
| 5 | Each stack of Consternation adds 100% Mental DMG and 12% to the Ultimate Might rate of Day of Remorse. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Charon | 卡戎 | 卡戎 | カローン | 카론 |
