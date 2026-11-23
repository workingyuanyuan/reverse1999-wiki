---
title: "Hissabeth"
description: "Hissabeth is a 6-star Plant DPS who stacks Serpentine Scales with Hiss! cards for Mental DMG and has Euphoria."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Hissabeth's Ultimate raises each Serpentine Scales stack's damage from 20% to 70% only for the end of the round it is cast, then turns every stack into a Hiss! card."
lastVerified: 2026-11-22
aliases:
  - "冷週六"
  - "冷周六"
  - "サーベス"
  - "히사베스"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Hissabeth.png"
    url: https://reverse1999.fandom.com/wiki/File:Hissabeth.png
  - title: "Image file, uploaded 2025-04-10"
    url: https://static.wikia.nocookie.net/reverse1999/images/f/f1/Hissabeth.png/revision/latest?cb=20250410191028
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Hissabeth, revision 94459"
    url: https://reverse1999.fandom.com/wiki/Hissabeth?oldid=94459
---

![Hissabeth, full-length art](/art/characters/hissabeth.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Plant |
| Damage | Mental |
| Tags | DPS, Ritual, Control |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Mainland release | 2025-04-10 |
| Global release | 2025-07-03 |

Hissabeth works with a fixed pool of eight snakes. Snake's Den stacks on her become Hiss! cards, Hiss! puts Serpentine Scales on an enemy, and each Scales stack returns to her as Snake's Den after it deals its end-of-round Genesis DMG. Hiss! cards count as Ultimates and cost no action point, so Ultimate Might raises most of her damage.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Ouroboros (attack on 2 enemies) | 120% Mental DMG; +60% against Serpentine Scales | 180%; +100% | 300%; +150% |
| Infinite Recursion (self buff) | spends 2 Snake's Den for 2 Hiss! | 3 for 3 | 4 for 4 |

- **Infinite Recursion** hands out its rank 1 Hiss! cards at the end of the round. With too few Snake's Den, Hissabeth gains 1, 2 or 3 Moxie by rank.
- **Hiss!**: a single-target attack of 50, 100 or 250% Mental DMG by its rank that inflicts 1, 2 or 4 stacks of [Serpentine Scales] and gives Hissabeth 0, 1 or 2 Moxie. Casting it counts as her own action (a Sovereign Incantation).

## Ultimate: Experimental Rocketry

Deals 500% Mental DMG to all enemies. On the targets hit, each Serpentine Scales stack deals 70% instead of 20% at the end of that round; then all Serpentine Scales are taken back as the same number of rank 1 Hiss! cards.

## Statuses

| Status | Effect |
| --- | --- |
| Serpentine Scales | At the end of the round, the holder takes Genesis DMG equal to (50% + 20% per stack) of Hissabeth's ATK; it can crit and gains from Ultimate Might. Each trigger removes 1 stack, which returns to Hissabeth as 1 Snake's Den. If the holder leaves the field, the stacks move to the holder's ally with the highest ATK. Up to 8 stacks; cannot be dispelled. |
| Snake's Den | Up to 8 stacks; cannot be dispelled. At the start of each round, her stacks are set so that Snake's Den, Serpentine Scales and Hiss! cards on the field add up to 8. |
| Rigidity | At 2 stacks it becomes Petrify, or adds 1 round to an existing Petrify. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Hissabeth starts the battle with 8 Snake's Den. At the start of a round, if she has any, she spends 1 for a rank 1 Hiss!, once per round. Hiss! and her Ultimate do not count toward the team's incantation limit. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | Attacking an enemy with Serpentine Scales inflicts [Rigidity] and gives her 1 more Moxie, once per round. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×6; Magnesia Crystal ×6; Liquefied Terror ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×10; Esoteric Bones ×6; Goose Neck ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×16; Goldbell Spirit Bottle ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | The Insight 1 Hiss! can come twice per round; Hiss! deals 75, 150 or 375% by rank. |
| 2 | The Insight 3 effect can trigger twice per round. |
| 3 | After the Ultimate, each Serpentine Scales stack deals 100% that round. |
| 4 | The Ultimate deals 750%. |
| 5 | After the Ultimate, each Serpentine Scales stack deals 130% that round. |

## Euphoria

Euphoria opens at Insight III level 30. Hissabeth has one Epiphany of four levels.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | The Insight 1 Hiss! at the start of a round also gives her 1 Moxie. |
| 1 | 2 | Ouroboros then inflicts 1 random effect from [Collection of Debuffs] on all enemies; Infinite Recursion gives all allies [Stream of Consciousness] for 3 rounds; the Insight 3 effect also inflicts 2 random effects from Collection of Debuffs for 2 rounds. |
| 1 | 3 | Hiss! deals 100% more of its base Mental DMG and draws on an extra 30, 60 or 100% of Ultimate Might by rank. |
| 1 | 4 | The Ultimate deals 20% more of its base Mental DMG for each type of Neg Status on the target, counting up to 10; with 5 or more types it gains Penetration Rate +20% and draws on an extra 60% of Ultimate Might. |

- [Collection of Debuffs]: Blind, Mis-aim, Fracture I, Confusion, Gash and Pollution; an effect the target lacks comes first.
- [Stream of Consciousness]: Ultimate Might +30%, and +3% more for each type of Neg Status on the target, up to 30%.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Hissabeth | 冷周六 | 冷週六 | サーベス | 히사베스 |
