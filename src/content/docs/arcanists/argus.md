---
title: "Argus"
description: "Argus is a 6-star Plant arcanist who deals Reality DMG, strips enemy buffs and lowers enemy defenses."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Her extra Grave Digger shot comes from the Insight III passive and is added only in a round whose incantations total 3 ranks or more."
lastVerified: 2026-11-22
aliases:
  - "阿爾古斯"
  - "阿尔古斯"
  - "アルゴス"
  - "아르고스"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Argus.png"
    url: https://reverse1999.fandom.com/wiki/File:Argus.png
  - title: "Image file, uploaded 2024-08-30"
    url: https://static.wikia.nocookie.net/reverse1999/images/2/26/Argus.png/revision/latest?cb=20240830025237
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Argus, revision 84951"
    url: https://reverse1999.fandom.com/wiki/Argus?oldid=84951
---

![Argus, full-length art](/art/characters/argus.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Plant |
| Damage | Reality |
| Tags | DPS, Rank Up, Support, Remove Buffs |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Psychubes recommended in game | [Stray Off the Path](/psychubes/stray-off-the-path/), [Outside the City](/psychubes/outside-the-city/), [Thunderous Applause](/psychubes/thunderous-applause/) |
| Mainland release | 2024-08-29 |
| Global release | 2024-12-26 |

Argus strips one enemy of its buffs and marks it with [Pinpointed], a debuff that lowers its DMG Taken Reduction and Critical DEF and gains stacks with every hit. Her first incantation raises the ranks of her cards, and from Insight III each round adds a Grave Digger shot whose rank follows the total ranks of the incantations played that round. She also has Euphoria.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Shotgun Shower (single-target attack) | 160% Reality DMG; Empower Incantation I 1 round | 280%; Empower Incantation II 1 round | 450%; Empower Incantation II 2 rounds |
| Penetrating Eye (single-target debuff) | Pinpointed 3 rounds | 5 stacks of Pinpointed, 3 rounds | 10 stacks of Pinpointed, 3 rounds |

- **Shotgun Shower** gives Argus herself the Empower Incantation status after the hit.
- **Penetrating Eye** first dispels every Stats Up and Pos Status effect on the target. Only one enemy on the field can hold Pinpointed at a time.

[Empower Incantation I]: at the start of the round, one random incantation goes up 1 rank. [Empower Incantation II] does the same for 2 random incantations.

## Ultimate: No Mark Unstruck

Deals 500% Reality DMG to one enemy. If the target has [Pinpointed], before the hit it gains 5 more stacks, the whole status lasts its full duration again, and the attack gains Penetration Rate +30% and Critical Rate +30%.

[Pinpointed]: DMG Taken Reduction −15% and Critical DEF −15%, and both fall by a further 2% for each stack beyond the first. Each attack the holder takes adds stacks: 2, 3 or 4 for a rank 1, 2 or 3 incantation, 1 for an attack with no rank. Stacks added this way do not renew the duration. At most 15 stacks.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | After Argus casts an incantation of rank 1, 2 or 3, all allies gain DMG Dealt +10%, +15% or +25% for 2 rounds. |
| 2 | Critical Rate +10% on entering battle. |
| 3 | Before the incantations in the AP Area resolve, adds a [Grave Digger] to the queue as an extra action, aimed first at an enemy with Pinpointed. Its rank follows the total ranks played that round: 3 to 4 ranks give a rank 1 shot of 100% Reality DMG; 5 to 6 a rank 2 shot of 150% and Moxie +1; 7 or more a rank 3 shot of 300%, Moxie +1 and a guaranteed critical hit. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×6; Shattered Bones ×6; Liquefied Terror ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×10; Perpetual Cog ×5; Winged Key ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×16; Goldbell Spirit Bottle ×6; Fruit of Good and Evil ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Grave Digger deals 150, 250 or 400% by rank. |
| 2 | Pinpointed starts at −20%, and each further stack lowers DMG Taken Reduction and Critical DEF by 2.5% more. |
| 3 | Grave Digger deals 200, 350 or 500% by rank. |
| 4 | Pinpointed starts at −25%, and each further stack lowers both by 3% more. |
| 5 | The Ultimate deals 700%. |

## Euphoria

Euphoria opens at Insight III level 30. Argus has one Epiphany of four levels; two of them strengthen Grave Digger.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | After each action she takes herself, Argus gains 5 stacks of [Incantation Bullet]: Incantation Might +25% when attacking. |
| 1 | 2 | Grave Digger raises a random incantation of hers by 1 rank after it hits; at rank 3 it raises one more. |
| 1 | 3 | The Ultimate deals extra Reality DMG equal to 80% of its base Reality DMG to a target with Pinpointed. |
| 1 | 4 | For each rank in the AP Area, up to 10, Grave Digger deals 50% more Reality DMG, gives Argus 1 stack of [Ceremonious: Ultimate Might] and has a 10% chance to fire once more. |

[Ceremonious: Ultimate Might]: Ultimate Might +3% per stack, up to 100 stacks; it cannot be dispelled and is removed after Argus casts her Ultimate.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Argus | 阿尔古斯 | 阿爾古斯 | アルゴス | 아르고스 |
