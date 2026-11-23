---
title: "Cornerstone"
description: "Cornerstone is a 6-star Mineral DPS who deals Reality DMG through ripostes fed by the damage her team avoids."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Cornerstone's Ultimate deals no damage when cast: it starts Delivery Process, and its attack, Delivery Feedback, comes at the end of the enemy round."
lastVerified: 2026-11-22
aliases:
  - "奠基石"
  - "コーナーストーン"
  - "코너스톤"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Cornerstone.png"
    url: https://reverse1999.fandom.com/wiki/File:Cornerstone.png
  - title: "Image file, uploaded 2026-09-25"
    url: https://static.wikia.nocookie.net/reverse1999/images/5/59/Cornerstone.png/revision/latest?cb=20260925082238
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Cornerstone, revision 101523"
    url: https://reverse1999.fandom.com/wiki/Cornerstone?oldid=101523
---

![Cornerstone, full-length art](/art/characters/cornerstone.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Mineral |
| Damage | Reality |
| Tags | DPS, Riposte |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Mainland release | 2026-07-02 |
| Global release | 2026-10-15 |

Cornerstone banks the damage her team avoids and spends it on ripostes. While she is on the field every ally carries Eligibility Assessment, which cuts each hit taken and stores the amount as Trial and Error points; other allies' ripostes draw extra Reality DMG from that bank, and her own Feedback attacks at the end of the enemy round empty it for bonus damage. Extra actions by the team build Progressive Iteration, which turns into the Design Revision stacks that strengthen her Ultimate.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Concrete Functionality (single-target attack) | 200% Reality DMG; in Inspection Process +200% and Critical DMG +40% | 300%; +300%, +60% | 500%; +500%, +100% |
| Figure-Ground Relationship (self counter) | [Inspection Process] for 2 rounds; 2 stacks of [Progressive Iteration] | 2 rounds; 3 stacks | 2 rounds; 5 stacks |

Concrete Functionality counts as a riposte at every rank. The Progressive Iteration stacks from Figure-Ground Relationship last 2 rounds.

## Ultimate: Today Builds Tomorrow

A self counter: Cornerstone enters [Delivery Process] for 1 round, and Delivery Feedback strikes at the end of the enemy round.

## Statuses

| Status | Effect |
| --- | --- |
| Eligibility Assessment | Held by every ally while Cornerstone is on the field. Each hit of non-Genesis damage from an enemy attack is cut by up to 80% of the ATK she entered battle with; the amount cut is stored as Trial and Error. |
| Trial and Error | Cornerstone's bank, up to 500% of the ATK she entered battle with. Whenever another ally ripostes, she adds Reality DMG equal to 100% of her ATK, raised by 100% times the share of the bank that is full. A full bank stores nothing more, while Eligibility Assessment keeps cutting damage. |
| Inspection Process | At the end of each enemy round, Cornerstone casts Inspection Feedback, even under Control. Gaining it again adds to its duration; it cannot be dispelled. |
| Inspection Feedback | 1000% Reality DMG to all enemies; Cornerstone gains 1 stack of Design Revision and 1 Moxie. It empties Trial and Error and deals 100% more Reality DMG for every 1000 points emptied. Counts as a riposte. |
| Delivery Process | Eligibility Assessment cuts up to 160% of her entry ATK per hit. At the end of the enemy round she casts Delivery Feedback, even under Control, and Inspection Process does not fire that round. Gaining it again adds to its duration; it cannot be dispelled. |
| Delivery Feedback | 2000% Reality DMG to all enemies; she gains 1 Moxie. It empties Trial and Error for 100% more Reality DMG per 1000 points. With at least 5 stacks of Design Revision, it spends 5 for 1000% more Reality DMG, Ultimate Might +75% and Penetration Rate +20%; with fewer, she gains 3 stacks. Counts as a riposte and extends Inspection Process by 1 round. |
| Progressive Iteration | Riposte DMG Bonus +4% and Incantation Might +4% per stack; up to 20 stacks, each timed on its own; cannot be dispelled. |
| Design Revision | Spent by Delivery Feedback; up to 10 stacks; cannot be dispelled. |
| Control | Effects that stop a unit acting: Daze, Petrify, Nightmare, Freeze, Disarm, Silence, Seal. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | While Cornerstone is on the field, all allies hold Eligibility Assessment and she holds Trial and Error. Her Moxie cap is 1 lower and her Ultimate costs 1 Moxie less. |
| 1 | Each extra action by an ally gives her 1 stack of Progressive Iteration for 2 rounds, and 1 more if the action is a riposte. Every 10 stacks gained give her 1 stack of Design Revision. |
| 2 | ATK +5% on entering battle. |
| 3 | Her Ultimate does not count toward the team's incantation limit. She gains 2 Moxie on entering battle and stores up to 4 Moxie beyond her cap, which refills her Moxie at the end of a round where there is room. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×6; Magnesia Crystal ×6; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×10; Fox Tail ×5; Goose Neck ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×16; Emerald Slate ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | A stack of Design Revision takes 8 stacks of Progressive Iteration; Delivery Feedback deals 4000% and needs 4 stacks of Design Revision; Inspection Feedback deals 2500%. |
| 2 | Spending Design Revision gives Delivery Feedback 2500% more Reality DMG, Ultimate Might +100% and Penetration Rate +30%; Inspection Feedback deals 250% more per 1000 Trial and Error points and gives 2 stacks of Design Revision; Progressive Iteration gives +5% per stack. |
| 3 | The damage added to allies' ripostes becomes 200% of her ATK, raised by 250% times the share of the bank that is full. |
| 4 | Eligibility Assessment cuts up to 120% of her entry ATK per hit, 240% during Delivery Process; Trial and Error holds up to 600%. |
| 5 | Delivery Feedback deals 5000% and 250% more per 1000 Trial and Error points; Progressive Iteration gives +6% per stack, up to 25 stacks. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Cornerstone | 奠基石 | 奠基石 | コーナーストーン | 코너스톤 |
