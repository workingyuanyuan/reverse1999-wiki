---
title: "Shamane"
description: "Shamane is a 6-star Beast arcanist who deals Reality DMG, weakens all enemies and refills his own Moxie."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Shamane's second Epiphany is out only on the mainland China service, and its English status names are translations, not official ones."
lastVerified: 2026-11-22
aliases:
  - "鬃毛沙礫"
  - "鬃毛沙砾"
  - "シャーマィン"
  - "갈기 모래"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Shamane.png"
    url: https://reverse1999.fandom.com/wiki/File:Shamane.png
  - title: "Image file, uploaded 2023-11-18"
    url: https://static.wikia.nocookie.net/reverse1999/images/c/c9/Shamane.png/revision/latest?cb=20231118210145
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Shamane, revision 85056"
    url: https://reverse1999.fandom.com/wiki/Shamane?oldid=85056
---

![Shamane, full-length art](/art/characters/shamane.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Reality |
| Tags | DPS, Ritual, Support |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Mainland release | 2023-09-07 |
| Global release | in the global client |

Shamane is a damage dealer who also lowers the enemy's defences. Spirit Medium raises the damage all enemies take, his attacks deal more for each kind of Stats Down on the target, and stacks of [Nature's Blessing] give Moxie back after each Ultimate. His first Epiphany passes Moxie to allies; the second replaces Moxie with Vein Points that he collects by moving along the line.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Apprentice's Dance (single-target attack) | 200% Reality DMG | 250%; Nature's Blessing 1 stack | 450%; Nature's Blessing 1 stack |
| Spirit Medium (mass debuff) | DMG Taken +10%; 2 rounds | +20%; 2 rounds | +30%; 3 rounds |

Spirit Medium also lowers Reality DEF and Mental DEF of all enemies by 15% at every rank, for the same number of rounds.

[Nature's Blessing]: after Shamane casts his Ultimate, up to 5 stacks are spent (all of them if he has fewer) and he gains that much Moxie.

## Ultimate: Edict of Atman

Deals 250% Reality DMG to all enemies and 250% Reality DMG more to the main target. Against the main target the attack has Critical Rate +20%, and Critical Rate above the cap turns into Critical DMG.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | DMG Dealt +8% for each kind of Stats Down on the target, at most +24%. Gains 2 stacks of Nature's Blessing on entering battle. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | Gains 1 stack of Nature's Blessing at the start of every second round. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Shattered Bones ×6; Milled Magnesia ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Spell of Fortune ×6; Clawed Pendulum ×3 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Silver Bullet ×6; Mistilteinn ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | The Insight 1 passive gives 5 stacks of Nature's Blessing on entering battle. |
| 2 | The Ultimate's Critical Rate bonus on the main target becomes +60%. |
| 3 | Apprentice's Dance deals 220, 280 or 500% by rank. |
| 4 | The Ultimate deals 300% to all enemies. |
| 5 | The Ultimate's Critical Rate bonus on the main target becomes +100%. |

## Euphoria

Euphoria opens at Insight III level 30. Shamane has two Epiphanies of four levels each; the second is out only on the mainland China service.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | After another ally casts an Ultimate, Shamane gains 2 stacks of [Rippling Energy]. |
| 1 | 2 | After his own Ultimate he spends all his stacks of Rippling Energy; every 2 stacks spent give a random ally 1 Moxie. |
| 1 | 3 | An ally who gains Moxie from Rippling Energy also gains 5 stacks of [Ceremonious]. |
| 1 | 4 | He gains 1 more stack of Rippling Energy after another ally's Ultimate, and 2 stacks just before casting his own. |
| 2 | 1 | The Insight 1 passive gains: Moxie is replaced by [Vein Points]; he no longer gains the Ultimate, and casts it on his own at the end of a round in which he holds 6 or more Vein Points. At the start of each round, 1 point of [Vein: Clear Sight] appears at a random position other than his, at most 4 points per position. Nature's Blessing gives Vein Points instead of Moxie. The Ultimate spends all his Vein Points after the attack; Apprentice's Dance moves him 1 position forward after the attack, and Spirit Medium 1 position back after it is cast. |
| 2 | 2 | Apprentice's Dance adds Reality DMG equal to 100% of its base Reality DMG, and gives 1 stack of Nature's Blessing at rank 1 as well. Spirit Medium adds DMG Taken +80% for all enemies, and its effects last 3 rounds at ranks 1 and 2 too. |
| 2 | 3 | The Insight 3 passive gains: on entering battle, the ally in position 1 gets 2 more maximum Vein Points, all allies gain 2 Vein Points, and Shamane 3 more. The Ultimate adds Reality DMG equal to 700% of its base Reality DMG to all enemies and 1750% Reality DMG to the main target; after it, the ally in position 1 steps back one place at a time to the last position. |
| 2 | 4 | The Ultimate deals 800% Reality DMG more to the main target for each Vein Point Shamane holds, and no longer raises its own Critical Rate or turns the excess into Critical DMG; instead, before the attack, all allies gain [Fertile Soil] for 3 rounds. After the attack, every other ally gains 1 Vein Point. |

- **Rippling Energy**: Ultimate Might +5%, up to 10 stacks; it cannot be dispelled.
- **Ceremonious**: Ultimate Might +3%, up to 100 stacks; it cannot be dispelled and ends when its holder casts an Ultimate.
- **Vein: Clear Sight**: Shamane's own vein. When he stands on its position and his Vein Points are not full, he picks up as much as he can, 1 point per pickup.
- **Fertile Soil**: Critical Rate up by the bonus the Ultimate used to give the main target (+20%, +60% from Portrait 2, +100% from Portrait 5); Critical Rate above the cap turns into Critical DMG at 100% when its holder deals damage.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Shamane | 鬃毛沙砾 | 鬃毛沙礫 | シャーマィン | 갈기 모래 |
