---
title: "Marsha"
description: "Marsha is a 6-star Beast arcanist who deals Reality DMG, shields the team and burns enemies (Lingering Glow)."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "The Burden Unspoken that Frontline Care casts when an ally is hit is always rank 1 and gets no Critical Rate bonus; only her own cast adds it and removes debuffs."
lastVerified: 2026-11-22
aliases:
  - "瑪爾紗"
  - "玛尔纱"
  - "マルシャ"
  - "마샤"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Marsha.png"
    url: https://reverse1999.fandom.com/wiki/File:Marsha.png
  - title: "Image file, uploaded 2026-03-05"
    url: https://static.wikia.nocookie.net/reverse1999/images/c/cb/Marsha.png/revision/latest?cb=20260305202625
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Marsha, revision 89026"
    url: https://reverse1999.fandom.com/wiki/Marsha?oldid=89026
---

![Marsha, full-length art](/art/characters/marsha.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Reality |
| Tags | Shield, Lingering Glow, Support, Remove Debuffs |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Psychubes recommended in game | [Singleness of Heart](/psychubes/singleness-of-heart/) |
| Mainland release | 2025-12-11 |
| Global release | 2026-03-05 |

Marsha keeps a stacking shield on the whole team and burns every enemy. Her Insight 1 passive gives her 2 stacks of [Frontline Care] each round, and each time an ally is hit she spends one to cast Burden Unspoken without using an action. Her attacks and spent Frontline Care build [Pain's Recompense], which her Ultimate turns into [Discipline Forged] for all allies. She belongs to the Lingering Glow group of arcanists, which builds points whenever enemies receive Burn or Halo.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Virtue of Restraint (single-target attack) | 200% Reality DMG; 3 stacks of [Burn]; 100% more against 8 or more Burn | 300%; 5 stacks; 150% more | 500%; 8 stacks; 250% more |
| Burden Unspoken (mass shield) | all allies a Shield of 150% of her ATK; multiplier + Critical Rate ×40% on her own cast | 225%; ×60% | 375%; ×100% |

- **Virtue of Restraint** gives Marsha 1 stack of Pain's Recompense after the attack. The bonus damage applies when the target already has at least 8 stacks of Burn.
- **Burden Unspoken** shields last 3 rounds and give their holder DMG Taken Reduction +30%. On an ally who already has a shield, the new shield adds to it, up to 650% of Marsha's ATK, and the shield runs for 3 rounds again. When she casts it herself, it spends 1 Frontline Care, adds her Critical Rate times the share in the table to the shield multiplier, and removes one kind of Stats Down or Neg Status from all allies.

## Ultimate: Violence Begets Violence

Marsha gains 1 stack of Pain's Recompense, deals 750% Reality DMG to all enemies and puts 4 stacks of Burn on each. Then she spends up to 5 stacks of Pain's Recompense, and all allies gain as many stacks of Discipline Forged for 3 rounds.

## Statuses

| Status | Effect |
| --- | --- |
| Burn | Healing Taken −15% (does not stack). At the end of the round, Genesis DMG based on 4% of the holder's ATK. Up to 30 stacks, which count as one Neg Status; half the stacks are removed each time it deals damage. |
| Halo | Healing Taken −25% (does not stack). At the end of the round, Genesis DMG based on 4% of the inflicter's ATK. Up to 30 stacks, which count as one Neg Status; half the stacks are removed each time it deals damage. |
| Pain's Recompense | Critical Rate +2.5% and Critical DMG +2.5% per stack; up to 20 stacks; cannot be dispelled. |
| Frontline Care | Up to 2 stacks. When any ally is attacked, Marsha spends 1 stack to cast a rank 1 Burden Unspoken. |
| Discipline Forged | Critical Rate +20%; when the holder deals damage, 50% of the excess Critical Rate becomes Critical DMG. Each stack adds Incantation Might +1% and Critical DMG +2.5% and keeps its own duration; cannot be dispelled. |
| Lingering Glow | Points that build whenever an enemy receives Burn or Halo, faster the fewer enemies remain. It cannot exist together with Bloodtithe or the Pursuit Scope. |
| Morning Prayer | With 1, 2, or 3 or more Lingering Glow allies, Lingering Glow builds 3, 5 or 8% faster. With 3, all enemies' Burn stack cap rises by 5, and at the start of each round all allies gain Critical DMG +1% for that round for every 10 Lingering Glow points, counting up to 100 points. |
| Pardon | Blocks the first Control effect on the holder, then disappears; does not stack. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Lingering Glow builds whenever an enemy receives Burn or Halo. |
| 1 | On entering battle, all allies gain a Shield of 150% of Marsha's ATK for 3 rounds, with DMG Taken Reduction +30% while they hold it, and Marsha gains the Morning Prayer that matches the number of Lingering Glow allies on the field. At the start of each round, she gains 2 stacks of Frontline Care, removes one kind of Control from each ally under Control, and gives every other ally Pardon for 1 round. |
| 2 | Critical Rate +10% on entering battle. |
| 3 | Each Frontline Care stack spent gives her 1 stack of Pain's Recompense. At the start of each round she puts 3 stacks of Burn on all enemies. She gains 1 Moxie on entering battle, and 1 Moxie after a critical hit or after spending Frontline Care, at most 2 a round. Moxie beyond her cap is stored, up to 2, and refills her at the end of the round when there is room. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Magnesia Crystal ×6; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Perpetual Cog ×5; Biting Box ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Glowing Mothwing ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | She gains 3 Moxie on entering battle; Morning Prayer raises enemies' Burn stack cap by 10; Discipline Forged gives Critical Rate +30% and turns 75% of excess Critical Rate into Critical DMG. |
| 2 | The Ultimate spends up to 7 stacks of Pain's Recompense; Discipline Forged lasts 4 rounds. |
| 3 | The Ultimate deals 1000% and gives her 2 stacks of Pain's Recompense; each Discipline Forged stack gives Incantation Might +2%. |
| 4 | Burden Unspoken shields 180, 270 or 450% of her ATK by rank, and the multiplier added on her own cast is Critical Rate ×90, 130 or 220%; the entering-battle shield holds 180% of her ATK. |
| 5 | With 3 or more Lingering Glow allies, Morning Prayer makes Lingering Glow build 14% faster; Discipline Forged gives Critical Rate +40% and turns 100% of excess Critical Rate into Critical DMG. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Marsha | 玛尔纱 | 瑪爾紗 | マルシャ | 마샤 |
