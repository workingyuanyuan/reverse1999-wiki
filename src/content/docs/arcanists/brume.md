---
title: "Brume"
description: "Brume is a 6-star Beast arcanist who deals Mental DMG with extra-action attacks, Burn and an electric field."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "End of the Ride, her extra-action attack on all enemies, comes only from the Insight 3 passive, and only when one Prismatic Power channel consumes at least 40 stacks of Thermoelectric Conversion."
lastVerified: 2026-11-22
aliases:
  - "灰調藍"
  - "灰调蓝"
  - "グレイッシュブルー"
  - "브룸"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Brume.png"
    url: https://reverse1999.fandom.com/wiki/File:Brume.png
  - title: "Image file, uploaded 2026-01-29"
    url: https://static.wikia.nocookie.net/reverse1999/images/2/24/Brume.png/revision/latest?cb=20260129135128
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Brume, revision 84967"
    url: https://reverse1999.fandom.com/wiki/Brume?oldid=84967
---

![Brume, full-length art](/art/characters/brume.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Mental |
| Tags | DPS, Dynamo, Support, Channel, Array |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Mainland release | 2025-11-20 |
| Global release | 2026-02-12 |

Brume builds stacks of Thermoelectric Conversion from her cards, her Ultimate and the Burn she spreads, then spends them in a one-round channel that ends in a volley of extra-action attacks. Her first incantation lets her choose between an attack and that channel; her second buffs the whole team. She also lays a Pulsing Field that the team fills with Dynamo, and that grows stronger in two steps.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Left-Hand Steering, Improvised Detour (single-target attack) | 200% Mental DMG | 300% | 500% |
| Left-Hand Steering, Calculated Path (self channel) | 10 stacks of Thermoelectric Conversion | 15 | 20 |
| Testing Flame (team buff) | 10 stacks of Thermoelectric Conversion | 15 | 20 |

- **Left-Hand Steering** is one card: when it is cast, Brume picks Improvised Detour or Calculated Path at the card's rank.
- **Improvised Detour** gives Brume [Crystalline Discharge] for 3 rounds after the hit.
- **Calculated Path** puts Brume into the channel [Prismatic Power] for 1 round.
- **Testing Flame** gives all allies [Truth Tempered] for 2 rounds.

## Ultimate: Thrown Into Heroics

Deals 750% Mental DMG to one enemy and gives Brume 10 stacks of Thermoelectric Conversion. Truth Tempered on every ally lasts 1 round longer. After the hit, the target receives 10 stacks of [Burn] and [Freeloader] for 1 round.

## Statuses

| Status | Effect |
| --- | --- |
| Thermoelectric Conversion | Spent by channelling; cannot be dispelled. |
| Prismatic Power | A channel. If Brume still holds it at the end of the round, she casts [Cost of the Roadside View] once and consumes as much Thermoelectric Conversion as she can: every 10 stacks add 100% Mental DMG to each Cost of the Roadside View, and every 20 stacks add one more cast. One channel consumes at most 60 stacks, for 2 extra casts and +200% on each. |
| Cost of the Roadside View | 200% Mental DMG to one enemy and 3 stacks of Burn. It counts as an extra action, and Ultimate Might applies to it at 100%. |
| End of the Ride | 600% Mental DMG to all enemies and 5 stacks of Burn. It counts as an extra action, and Ultimate Might applies to it at 100%. |
| Crystalline Discharge | Cost of the Roadside View deals 100% more Mental DMG and End of the Ride 200% more; cannot be dispelled. |
| Truth Tempered | DMG Bonus +20% and Incantation Might +10%; an ally who deals Mental DMG also gains Incantation Might +10% and Ultimate Might +40%. Each hit puts 2 stacks of [Disguise Dissolved] on the target for 2 rounds, 2 more when the hit is an extra action. |
| Disguise Dissolved | Critical Resist Rate -1% and Critical DEF -3% per stack; up to 20 stacks, each with its own duration. |
| Freeloader | Cost of the Roadside View targets the holder first. |
| Burn | Healing Taken -15%, which does not stack. At the end of each round, Genesis DMG equal to 4% of the holder's ATK per stack, then half the stacks are removed; up to 30 stacks, counted as one Neg Status. |
| Dynamo | Up to 30 stacks; cannot be dispelled. |
| Pulsing Field | At the start of a round, it rises with the Dynamo put into it: Lv.2 at 50 or more, Lv.3 at 120 or more. The Dynamo inside is lost when the field ends. |
| Pulsing Field Lv.1 | All allies gain DMG Bonus +15% for 3 rounds. |
| Pulsing Field Lv.2 | All allies gain Incantation Might +25% and DMG Bonus +15% for 3 rounds. |
| Pulsing Field Lv.3 | All allies gain Ultimate Might +35%, Incantation Might +25% and DMG Bonus +15% for 2 rounds. |
| Amplified Surge | When Pulsing Field Lv.3 starts, Brume gains 20 stacks of Thermoelectric Conversion and her Crystalline Discharge lasts 1 round longer. Under Lv.3, Cost of the Roadside View deals 400% more Mental DMG. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Brume gains Amplified Surge, and 10 stacks of Dynamo on entering battle. At the start of a round with no Pulsing Field of any level, she lays Pulsing Field Lv.1. At the end of each round she gains 5 stacks of Dynamo and puts up to 15 into the field. Her Ultimate does not count toward the team's incantation draw limit. |
| 1 | Brume gains 5 stacks of Thermoelectric Conversion at the start of each round, 5 for every 20 stacks of Dynamo the team puts into the field, and 2 for every 3 stacks of Burn put on enemies. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | Brume enters battle with Crystalline Discharge for 3 rounds. For every 15 stacks of Thermoelectric Conversion she gains, she also gains 5 stacks of Dynamo and 1 Moxie. When one Prismatic Power channel consumes at least 40 stacks, she casts End of the Ride once at its end; every 10 stacks beyond that add 200% Mental DMG, up to 400%. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Shattered Bones ×6; Spell of Fortune ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Perpetual Cog ×5; Holy Silver ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Bogeyman ×5; Mistilteinn ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Crystalline Discharge from Improvised Detour adds 120% and 250%. Calculated Path gives 15, 20 or 25 stacks by rank. Cost of the Roadside View deals 240%; Prismatic Power adds 120% per 10 stacks, consumes up to 80 stacks and allows up to 3 extra casts. Under Pulsing Field Lv.3, Amplified Surge makes Cost of the Roadside View deal 480% more. |
| 2 | Testing Flame gives 15, 20 or 25 stacks by rank; Truth Tempered gives DMG Bonus +30% and Ultimate Might +50% to allies who deal Mental DMG. |
| 3 | End of the Ride deals 800%, and the extra damage from consumed stacks rises to at most 800%. |
| 4 | End of the Ride deals 1200% and takes Ultimate Might at 125%; each further 10 stacks add 250%, up to 1000%. |
| 5 | Truth Tempered gives DMG Bonus +40% and Ultimate Might +60% to allies who deal Mental DMG. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Brume | 灰调蓝 | 灰調藍 | グレイッシュブルー | 브룸 |
