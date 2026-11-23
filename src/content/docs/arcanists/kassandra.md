---
title: "Kassandra"
description: "Kassandra is a 6-star Mineral arcanist who deals Reality DMG with Assassinations and buffs the team."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Her Ultimate, Rush Assassination, comes from Adrenaline instead of Moxie: she gets one each time Adrenaline reaches 10, and Adrenaline then drops back to 0."
lastVerified: 2026-11-22
aliases:
  - "卡珊卓"
  - "卡珊德拉"
  - "カサンドラ"
  - "카산드라"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Kassandra.png"
    url: https://reverse1999.fandom.com/wiki/File:Kassandra.png
  - title: "Image file, uploaded 2025-08-08"
    url: https://static.wikia.nocookie.net/reverse1999/images/4/4a/Kassandra.png/revision/latest?cb=20250808063137
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Kassandra, revision 85006"
    url: https://reverse1999.fandom.com/wiki/Kassandra?oldid=85006
---

![Kassandra, full-length art](/art/characters/kassandra.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Mineral |
| Damage | Reality |
| Tags | DPS, Extra Action, Ritual, Support, Assassination |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Mainland release | 2025-08-28 |
| Global release | 2025-08-28 |

Kassandra has Adrenaline in place of Moxie. As it climbs from 0 to 10 in a cycle, she gets a Precast Sparta Kick at 2, a Precast Rain of Destruction at 6 and her Ultimate at 10. Advent of Artemis marks enemies with [Lethal Injury], which turns the next attack on them into an [Assassination], and a skill tree decides which of three Ways she projects as a [Force Field] over the team, with a larger share for allies who perform Assassinations.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Fury of Ares (attack on 2 enemies) | 120% Reality DMG; Adrenaline +1 | 180%; +2 | 300%; +4 |
| Advent of Artemis (single-target attack) | 150% Reality DMG; 1 stack of Lethal Injury | 225%; 2 stacks | 375%; 4 stacks |

The Adrenaline cycle adds two Precast cards; each is a [Sovereign Incantation].

| Card | Adrenaline | Effect |
| --- | --- | --- |
| Sparta Kick (single-target attack) | 2 | 200% Reality DMG and [Daze] for 1 round; 100% more Reality DMG on a target that is already dazed |
| Rain of Destruction (mass attack) | 6 | 500% Reality DMG to all enemies |

## Ultimate: Rush Assassination

Deals 750% Reality DMG to one enemy; the attack is an Assassination.

## Statuses

| Status | Effect |
| --- | --- |
| Lethal Injury | When its holder is attacked, the attack triggers an Assassination and 1 stack is removed. An Assassination on the holder also gains Final DMG Dealt +1% for every 100 points of Critical Technique the attacker has over it; that part removes no stack. |
| Assassination | The attack gains Final DMG Dealt +5% for every 100 points of Critical Technique the attacker has over the target. |
| Guidance of Three Gods | Raises the bonuses of the Ways. Up to 5 stacks; cannot be dispelled. |
| Way of Artemis | Force Field: all allies gain Critical DMG +27% plus 5.4% per stack of Guidance of Three Gods, and Critical Rate +15%; Assassination allies gain another 5.4% per stack and Critical Rate +10%. |
| Way of Ares | Force Field: all allies gain DMG Bonus +14% plus 2.8% per stack, and Incantation Might +18%; Assassination allies gain another 2.8% per stack and Incantation Might +12%. |
| Way of Nyx | Force Field: all allies gain ATK +7% plus 1.4% per stack, and Penetration Rate +24%; Assassination allies gain another 1.4% per stack and Penetration Rate +16%. |
| Force Field | An effect its holder gives to the characters it names; it ends when the holder leaves the field. |
| Daze | The target cannot act. |
| Sovereign Incantation | Casting it counts as the character actively taking an action. |
| Precast Incantation | Counts as the incantation of the same name; unused ones are removed at the end of the round. |

## Skill tree

Kassandra's skill tree has three branches, one for each Way; the first branch unlocked decides which Way she brings into battle. The abilities change her cards as follows.

| Way of the branch | Abilities |
| --- | --- |
| Artemis | Advent of Artemis puts 1 more stack of Lethal Injury. [Sixth Sense]: Fury of Ares, Advent of Artemis and Rain of Destruction put 1 more stack of Lethal Injury, and her Force Field adds 50% DMG of the attacker's type whenever an ally triggers an Assassination. |
| Ares | [Weapons Master]: Sparta Kick, Rain of Destruction and Rush Assassination put [Kick Gash], [Arrow Gash] and [Assassination Gash] for 3 rounds. Fury of Ares casts Sparta Kick on its main target once more for each different kind of Gash the target has. |
| Nyx | [Shadow Assassin]: her Assassinations gain Final DMG Dealt +1% more for every 100 points of Critical Technique she has over the target. Fury of Ares and Advent of Artemis count as Assassinations, and the Adrenaline cycle then gives only Rush Assassination. Rush Assassination that lands a critical hit gives her [Preparation · Kassandra]. |

- **Kick Gash, Arrow Gash, Assassination Gash**: when attacked, the holder takes extra Genesis DMG equal to 10% of the user's ATK.
- **Preparation · Kassandra**: at the start of the next round she gets a Precast Rush Assassination - Combo, 750% Reality DMG to one enemy, which counts as an Assassination and as an Ultimate. It cannot be dispelled.

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Adrenaline replaces Moxie. Within each cycle from 0 to 10, reaching 2 Adrenaline for the first time gives a Precast Sparta Kick, 6 a Precast Rain of Destruction and 10 a Rush Assassination, after which Adrenaline resets to 0. |
| 1 | Adrenaline +1 on entering battle and at the start of each round. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | Each time any ally triggers an Assassination, Kassandra gains 1 stack of Guidance of Three Gods, and 1 more when another Assassination arcanist is on the team. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×6; Silver Ore ×6; Spell of Fortune ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×10; Liquefied Terror ×5; Golden Grass Incense ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×16; Wyrmling Skeleton ×6; Golden Fleece ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Adrenaline +2 at the start of each round; Fury of Ares deals 150, 225 or 375% and Advent of Artemis 240, 360 or 600% by rank. |
| 2 | Each stack of Guidance of Three Gods gives Critical DMG +9.3% in Way of Artemis, DMG Bonus +4.8% in Way of Ares and ATK +2.8% in Way of Nyx, and as much again to Assassination allies. |
| 3 | Sparta Kick deals 300%, Rain of Destruction 700%, Rush Assassination and Rush Assassination - Combo 1250%. |
| 4 | Way of Artemis gives Critical Rate +24% (Assassination allies +16% more), Way of Ares Incantation Might +30% (+20%), Way of Nyx Penetration Rate +42% (+28%). |
| 5 | Sixth Sense adds 125% DMG; the Gashes deal Genesis DMG equal to 20% of the user's ATK; Shadow Assassin gives Final DMG Dealt +4% per 100 points of Critical Technique. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Kassandra | 卡珊德拉 | 卡珊卓 | カサンドラ | 카산드라 |
