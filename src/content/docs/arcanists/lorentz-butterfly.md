---
title: "Lorentz Butterfly"
description: "Lorentz Butterfly is a 6-star Intellect arcanist who deals Mental DMG and supports Lingering Glow teams."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Her team bonus to DMG Bonus and Incantation Might grows with the number of Lingering Glow allies (1, 2 or 3) and counts at most 600 Lingering Glow."
lastVerified: 2026-11-22
aliases:
  - "洛倫茲蝴蝶"
  - "洛伦兹蝴蝶"
  - "ローレンツバタフライ"
  - "로렌츠 버터플라이"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Lorentz Butterfly.png"
    url: https://reverse1999.fandom.com/wiki/File:Lorentz_Butterfly.png
  - title: "Image file, uploaded 2026-03-25"
    url: https://static.wikia.nocookie.net/reverse1999/images/5/51/Lorentz_Butterfly.png/revision/latest?cb=20260325210807
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Lorentz Butterfly, revision 100694"
    url: https://reverse1999.fandom.com/wiki/Lorentz_Butterfly?oldid=100694
---

![Lorentz Butterfly, full-length art](/art/characters/lorentz-butterfly.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Intellect |
| Damage | Mental |
| Tags | Support, Lingering Glow, DPS, Rewrite |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Mainland release | 2026-03-05 |
| Global release | 2026-05-28 |

Lorentz Butterfly belongs to the Lingering Glow group: Burn and Halo on enemies build up Lingering Glow, and her Insight 3 passive turns it into DMG Bonus and Incantation Might for the whole team each round, more with more Lingering Glow allies. She spreads [Burn], her first incantation adds damage based on what the team's incantations already dealt to the target that round, and her Ultimate prints copies of a chosen incantation that cost no AP the next round.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| The Primer's Flutter (single-target attack) | 200% Mental DMG; 2 Burn | 400%; 2 Burn; Static Genesis DMG 3% | 800%; 3 Burn; 6% |
| Chaos Criteria (buff) | The Igniting Wingbeat on herself, 2 rounds | on herself and the other Lingering Glow allies, 2 rounds | on herself and the other Lingering Glow allies, 3 rounds |

- **The Primer's Flutter** puts its Burn on the target before the hit. From rank 2, the hit adds [Static Genesis DMG] equal to 3% (rank 2) or 6% (rank 3) of the damage that allied incantations dealt to the target this round, raised by 0.5% (rank 2) or 1% (rank 3) for every 100 Lingering Glow, counting at most 600. This triggers at most 10 times a round.
- **Chaos Criteria** gives [The Igniting Wingbeat]: each attack of the holder adds 1 stack of Burn.

## Ultimate: The Unstable Dynamical System

Before casting, Lorentz Butterfly chooses 1 basic incantation in the Spelldock. She gains [Continuous Action I] for 1 round, and 3 [Precast Incantation] copies of the chosen card are printed; they come out at the start of the next round, rewritten with [Fractal Dimension].

## Statuses

| Status | Effect |
| --- | --- |
| Burn | Healing Taken −15% (does not stack). At the end of each round, the holder takes Genesis DMG equal to 4% of its own ATK. Stacks up to 30 times; all stacks count as one Neg Status; half the stacks are removed after it takes effect. |
| Halo | Healing Taken −25% (does not stack). At the end of each round, the holder takes Genesis DMG equal to 4% of the ATK of the one who applied it. Same stacking rules as Burn. |
| Lingering Glow | Builds up whenever an enemy gains Burn or Halo, more when fewer enemies are on the field. Cannot exist alongside Bloodtithe or the Pursuit Scope. |
| Static Genesis DMG | Genesis DMG that stat bonuses do not affect. |
| Continuous Action I | AP +1. |
| Precast Incantation | Counts as the incantation of the same name. Unused ones are removed at the end of the round. |
| Fractal Dimension | A rewrite of the card: it costs no AP when played, gives no Moxie and cannot be merged. It does not stack with other rewrites. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Burn or Halo on any enemy builds up Lingering Glow. |
| 1 | Before the AP Area resolves, each of Lorentz Butterfly's basic incantations gains one rank for every other basic incantation of the same kind in the AP Area. |
| 2 | Critical Rate +10% on entering battle. |
| 3 | On entering battle, she gains 2 Moxie. At the end of each round, every Lingering Glow ally who did not cast an Ultimate that round gains 1 Moxie, and Lorentz Butterfly 1 more. Ultimates of Lingering Glow allies do not count toward the Incantation Draw Limit. The Burn stack limit of all enemies rises by 5, and by 15 more with 3 Lingering Glow allies. At the start of each round, for every 100 Lingering Glow (counting at most 600), all allies gain DMG Bonus +2.5%, 5% or 15% and Incantation Might +1%, 2% or 6% for 1 round, with 1, 2 or 3 Lingering Glow allies. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×3; Page of Starlit Ascent ×3; Shattered Bones ×6; Sharp Needle ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×5; Scroll of Starlit Ascent ×5; Fox Tail ×5; Holy Silver ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×8; Tome of Starlit Ascent ×8; Bogeyman ×5; Golden Fleece ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Continuous Action I lasts 2 rounds; she gains 2 extra Moxie at round end if she cast no Ultimate; the Incantation Might bonus becomes 3%, 4% or 8%; the Lingering Glow raise of The Primer's Flutter becomes 0.6% (rank 2) or 1.2% (rank 3). |
| 2 | The Ultimate prints 4 copies; the DMG Bonus becomes 5.5%, 8% or 18%. |
| 3 | The Igniting Wingbeat from Chaos Criteria lasts 3, 3 or 4 rounds by rank; the Incantation Might bonus becomes 5%, 6% or 10%. |
| 4 | The DMG Bonus becomes 8.5%, 11% or 21%. |
| 5 | The Ultimate prints 5 copies; the Lingering Glow raise of The Primer's Flutter becomes 0.7% (rank 2) or 1.4% (rank 3). |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Lorentz Butterfly | 洛伦兹蝴蝶 | 洛倫茲蝴蝶 | ローレンツバタフライ | 로렌츠 버터플라이 |
