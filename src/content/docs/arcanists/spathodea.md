---
title: "Spathodea"
description: "Spathodea is a 6-star Beast arcanist who deals Reality DMG, stacks Burn and builds on critical hits."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Her Ultimate gains its second Critical DMG bonus only against a target with 15 or more stacks of Burn."
lastVerified: 2026-11-22
aliases:
  - "可燃點"
  - "可燃点"
  - "カエンボク"
  - "스파토데아"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Spathodea.png"
    url: https://reverse1999.fandom.com/wiki/File:Spathodea.png
  - title: "Image file, uploaded 2023-11-30"
    url: https://static.wikia.nocookie.net/reverse1999/images/2/22/Spathodea.png/revision/latest?cb=20231130233804
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Spathodea, revision 85060"
    url: https://reverse1999.fandom.com/wiki/Spathodea?oldid=85060
---

![Spathodea, full-length art](/art/characters/spathodea.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Reality |
| Tags | DPS, Burn |
| Mainland release | 2023-11-30 |
| Global release | 2024-04-18 |

Spathodea is a Burn arcanist. Ignition Point stocks her with [Preignition], which turns into Burn on the target before her next attack, and [Exhilaration], which adds Critical Rate to it, and queues a Precast Little Boxer for the next round. Her Insight passives turn Burn into Critical Rate and critical hits into more Burn, and her Ultimate gains Critical DMG against a heavily burning target.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Little Boxer (single-target attack) | 200% Reality DMG | 300% | 500% |
| Ignition Point (self buff) | 3 [Preignition], 2 [Exhilaration], 1 [Preparation - Spathodea I] | 6, 3, 1 Preparation - Spathodea II | 9, 5, 1 Preparation - Spathodea III |

- Little Boxer gains Critical DMG +40% while Spathodea has Preignition, at every rank.
- Preparation - Spathodea I, II or III makes a rank 1, 2 or 3 Little Boxer as a [Precast Incantation] at the start of the next round. She gains at most 1 Precast Incantation a round this way.

[Preignition]: before an attack, each stack puts 1 stack of [Burn] on the target; all stacks are then removed.

[Exhilaration]: each stack gives an attack Critical Rate +15%; all stacks are then removed.

[Precast Incantation]: counts as the incantation of the same name; unused ones are removed at the end of the round.

## Ultimate: Flame Within the Fire

Deals 700% Reality DMG to one enemy with Critical DMG +40%, and a further Critical DMG +40% if the target has 15 or more stacks of [Burn].

[Burn]: Healing Taken −15%, which does not stack. At the end of each round, Genesis DMG based on 4% of the holder's ATK. Up to 30 stacks, which count as one Neg Status; half the stacks are removed each time it deals damage.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | After one of her attacks applies Burn, her next attack gains Critical Rate +25%. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | When one of her single-target attacks crits, the target gets 4 stacks of Burn. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Trembling Tooth ×5; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Cicada Wings ×6; Bifurcated Skeleton ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Incorrupt Monkeypaw ×7; Golden Fleece ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Little Boxer's Critical DMG bonus becomes +70%. |
| 2 | The Insight I Critical Rate bonus becomes +50%. |
| 3 | Both Critical DMG bonuses of the Ultimate become +70%. |
| 4 | Little Boxer deals 220, 330 or 550% by rank. |
| 5 | The Ultimate deals 750%, and both its Critical DMG bonuses become +100%. |

## Euphoria

Euphoria opens at Insight III level 30. Spathodea has one Epiphany of four levels, built on Burn and [Lingering Glow].

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Lingering Glow builds whenever any enemy gets Burn or [Halo], 100% faster when an ally applies Burn. On entering battle, all enemies get 6 stacks of Burn, and their Burn stack limit rises by 15. |
| 1 | 2 | Exhilaration changes: on casting her Ultimate, each stack gives Critical Rate +5% and ATK +3%, up to 10 stacks, removed after the Ultimate. |
| 1 | 3 | Little Boxer deals extra Reality DMG equal to 100% of its base, gets its Critical DMG bonus without Preignition, and puts 2 stacks of Burn on the target after the hit. Insight III no longer needs a critical hit: she puts 6 stacks of Burn on the target before attacking. |
| 1 | 4 | The Ultimate gains Ultimate Might +2% for each Burn stack on the target, and extra Reality DMG equal to 5% of its base for every 10 points of Lingering Glow. She stores up to 2 Moxie beyond her cap and adds it back at the end of a round when she has room. |

[Lingering Glow]: a team resource that builds whenever an enemy gets Burn or Halo, faster when fewer enemies remain. It cannot be held together with Bloodtithe.

[Halo]: like Burn, but Healing Taken −25%, and the damage is based on 4% of the ATK of the unit that first applied it.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Spathodea | 可燃点 | 可燃點 | カエンボク | 스파토데아 |
