---
title: "Lucy"
description: "Lucy is a 6-star Intellect arcanist who deals Reality DMG, runs on Dynamo stacks and reinforces her own cards."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Lucy's cards are reinforced one at a time, each by an Advancement earned for every 20 Dynamo the team gains; her Ultimate is reinforced only after all three of her incantations are."
lastVerified: 2026-11-22
aliases:
  - "露西"
  - "ルーシー"
  - "루시"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Lucy.png"
    url: https://reverse1999.fandom.com/wiki/File:Lucy.png
  - title: "Image file, uploaded 2024-05-24"
    url: https://static.wikia.nocookie.net/reverse1999/images/0/05/Lucy.png/revision/latest?cb=20240524031404
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Lucy, revision 90493"
    url: https://reverse1999.fandom.com/wiki/Lucy?oldid=90493
---

![Lucy, full-length art](/art/characters/lucy.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Intellect |
| Damage | Reality |
| Tags | DPS, Dynamo |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Psychubes recommended in game | [Steps Forward](/psychubes/steps-forward/), [Blasphemer of Night](/psychubes/blasphemer-of-night/) |
| Mainland release | 2024-05-16 |
| Global release | 2024-09-19 |
| Profile | [Cover, items, stories, skins and voice lines](/arcanists/lucy/profile/) |

Lucy gathers [Dynamo] whenever she or an ally gains Moxie, and her attacks spend 10 stacks at a time for extra damage. Every 20 Dynamo the team gains gives her [Advancement], which reinforces one of her cards. Her Ultimate makes all her attacks count as the stronger Afflatus, and after it, and after each enemy falls, she casts [Conservation of Energy] at all enemies.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Power of Speed (single-target attack) | 200% Reality DMG; +60% with Dynamo | 300%; +90% | 500%; +150% |
| Electric Surge (attack on 2 enemies) | 150% Reality DMG; 1 more target, or +40% with Dynamo | 225%; +60% | 375%; +100% |

- Both spend 10 stacks of Dynamo for their extra effect.
- **Electric Surge** with Dynamo attacks 1 more enemy; if fewer than 3 enemies are present, it deals the extra Reality DMG in the table instead.
- [Conservation of Energy], cast by her Insight 3 passive and counted as a rank 2 incantation: 100% Reality DMG to all enemies; with 10 Dynamo spent, Penetration Rate +50%.

### Reinforced cards

| Card | Reinforced effect |
| --- | --- |
| Power of Speed | Hits 2 enemies: 220, 330 or 550% to the main target and 110, 165 or 275% to the second, by rank; the Dynamo bonus costs 5 stacks. |
| Electric Surge | Adds Genesis DMG equal to 80, 120 or 200% of Lucy's ATK, by rank; the Dynamo bonus costs 5 stacks. |
| Conservation of Energy | Adds 50% Reality DMG to targets below 50% HP, ignores Dodge and triggers no Reflect or Riposte. |
| A Step Forward | Loads 2 [Overcharged Ammunition] instead of Charged Ammunition and gives Lucy 1 Moxie. |

## Ultimate: A Step Forward

Lucy enters [Pragmatist] for 2 rounds, gains 1 stack of [Data Iteration] and loads 2 [Charged Ammunition].

- [Dynamo]: a resource for her machines; up to 30 stacks, cannot be dispelled.
- [Advancement]: at the start of the next round, Lucy picks one of her three incantations to reinforce; once all three are reinforced, the Ultimate is. It cannot be dispelled.
- [Pragmatist]: all her attacks count as the stronger Afflatus, with Stronger Afflatus Damage Multiplier +10%. It cannot be dispelled.
- [Data Iteration]: ATK +4%, up to 5 stacks; cannot be dispelled.
- [Charged Ammunition]: just before each attack, Lucy gains 5 stacks of Dynamo; one round of ammunition is used each time.
- [Overcharged Ammunition]: as Charged Ammunition, but 10 stacks of Dynamo.
- [Leadership]: a Force Field that gives the other allies Stronger Afflatus Damage Multiplier +10%; it cannot be dispelled and ends when Lucy leaves the field.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Lucy gains 2 stacks of Dynamo for each Moxie she gains, and 1 stack for each Moxie or Eureka another ally gains. Every 20 stacks of Dynamo the team gains in total give her Advancement. |
| 2 | Critical Rate +10% on entering battle. |
| 3 | After her Ultimate, Lucy gains Leadership for 2 rounds and casts Conservation of Energy. Whenever an enemy leaves the field, she gains 10 stacks of Dynamo and 1 stack of Data Iteration and casts Conservation of Energy, at most 2 times a round. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×3; Page of Starlit Ascent ×3; Silver Ore ×6; Esoteric Bones ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×5; Scroll of Starlit Ascent ×5; Solidus ×3; Salted Mandrake ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×8; Tome of Starlit Ascent ×8; Glowing Mothwing ×6; Golden Fleece ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Conservation of Energy deals 150%; reinforced, it adds 100% Reality DMG to targets below 75% HP. |
| 2 | Pragmatist and Leadership last 3 rounds and raise the Stronger Afflatus Damage Multiplier by 20%. |
| 3 | Data Iteration gives ATK +6%; an enemy leaving the field gives 2 stacks of it. |
| 4 | Conservation of Energy deals 200%; enemies leaving the field can trigger it up to 4 times a round. |
| 5 | Data Iteration gives ATK +8% and stacks up to 6; each Moxie or Eureka an ally gains gives Lucy 2 stacks of Dynamo. |

## Euphoria

Euphoria opens at Insight III level 30. Lucy has one Epiphany of four levels, built around a field of Dynamo.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | At the start of a round with no [Pulsing Field] of any level, Lucy deploys Pulsing Field Lv.1. After she casts a reinforced card, up to 10 stacks of her Dynamo go into the field. |
| 1 | 2 | Lucy enters battle with 20 stacks of Dynamo and gains 1 stack of Data Iteration after each reinforcement. |
| 1 | 3 | Lucy gains [Amplified Surge]. |
| 1 | 4 | Reinforced cards no longer spend Dynamo, and enemies leaving the field no longer give Dynamo. In a Pulsing Field of level 1, 2 or 3, reinforced cards add Reality DMG equal to 50, 70 or 120% of the base Reality DMG of Conservation of Energy; at level 3 they also add 8% Reality DMG for each stack of Dynamo she holds. Reinforced cards benefit from Ultimate Might at a 100% rate, 10% more for each stack of Data Iteration. |

- **Pulsing Field**: at the start of each round it levels up by the Dynamo put into it: level 2 at 50 or more, level 3 at 120 or more. The Dynamo in it is lost when the field ends.
- **Pulsing Field Lv.1**: all allies DMG Bonus +15% for 3 rounds.
- **Pulsing Field Lv.2**: all allies Incantation Might +25% and DMG Bonus +15% for 3 rounds.
- **Pulsing Field Lv.3**: all allies Ultimate Might +35%, Incantation Might +25% and DMG Bonus +15% for 2 rounds.
- **Amplified Surge**: when the field reaches level 3, Lucy gains 2 stacks of Overcharged Ammunition; while it stays at level 3, she gains 1 more after each critical hit.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Lucy | 露西 | 露西 | ルーシー | 루시 |
