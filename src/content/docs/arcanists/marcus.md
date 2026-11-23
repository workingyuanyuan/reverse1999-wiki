---
title: "Marcus"
description: "Marcus is a 6-star Plant arcanist who deals Mental DMG and spends Eureka to rank up cards; she has Euphoria."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Perusal, which her Euphoria builds on, needs 3 or more Plant, Spirit or Intellect allies at the start of battle and is removed when the team no longer meets that."
lastVerified: 2026-11-22
aliases:
  - "馬庫斯"
  - "马库斯"
  - "マーカス"
  - "마커스"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Marcus.png"
    url: https://reverse1999.fandom.com/wiki/File:Marcus.png
  - title: "Image file, uploaded 2024-03-21"
    url: https://static.wikia.nocookie.net/reverse1999/images/a/a3/Marcus.png/revision/latest?cb=20240321192303
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Marcus, revision 85444"
    url: https://reverse1999.fandom.com/wiki/Marcus?oldid=85444
---

![Marcus, full-length art](/art/characters/marcus.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Plant |
| Damage | Mental |
| Tags | DPS, Rank Up, Eureka |
| Resonance Patterns | [T-shaped set](/systems/resonance/): Elucidation, Genuinity, Hyper, Inspire, Delirament |
| Psychubes recommended in game | [Another Story](/psychubes/another-story/), [Blasphemer of Night](/psychubes/blasphemer-of-night/) |
| Mainland release | 2024-03-21 |
| Global release | 2024-08-01 |

Marcus marks one enemy with [Annotate] and gathers Eureka from it each time it acts. At the start of each round she spends Eureka to raise her own incantations by a rank, and her attacks deal more damage to the marked enemy. Her Ultimate also gives her a Precast copy of her single-target attack for the next round.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Reading Class (single-target attack) | 200% Mental DMG | 330% | 450%; Penetration Rate +30% |
| From the Lantern (attack on 2 enemies) | 130% Mental DMG; +30% on an Annotated target | 200%; +40%; 1 stack of Weakness | 300%; +75%; 1 stack of Weakness |

From the Lantern deals the extra damage in the table only to a target that has Annotate. From rank 2 it also puts 1 stack of [Weakness] on each target hit.

[Weakness]: the holder's next attack has DMG Bonus −25%; each attack that it affects removes one stack.

## Ultimate: Next Chapter

Deals 250% Mental DMG to all enemies, plus 200% Mental DMG to a target that has Annotate. Marcus then gains 1 stack of [Preparation · Marcus] and 2 Eureka.

- [Annotate]: each time the holder acts, Marcus gains 1 Eureka, at most 3 times a round; it cannot be dispelled.
- [Preparation · Marcus]: at the start of the next round, creates one rank 1 Precast Reading Class. Marcus gets at most one Precast card a round this way.
- [Precast Incantation]: counts as the incantation of the same name; unused Precast cards are removed at the end of the round.
- [Perusal]: Marcus gains 1 Moxie when she casts a rank 2 or rank 3 incantation; it cannot be dispelled.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Max Eureka +1. At the start of each round, if no enemy has Annotate, one enemy gets it, bosses first. Then, with 2 or more Eureka, Marcus spends as much as she can to raise random incantations of hers, lowest rank first: 2 Eureka from rank 1 to 2, 3 Eureka from rank 2 to 3. |
| 2 | ATK +5% on entering battle. |
| 3 | Gains 1 Eureka on entering battle and 1 more at the start of each round. With 3 or more Plant, Spirit or Intellect allies on entering battle, she gains Perusal, which is removed when the team no longer meets that. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×6; Trembling Tooth ×5; Cicada Wings ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×10; Solidus ×3; Prophetic Bird ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×16; Golden Compass ×5; Fruit of Good and Evil ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Gains 3 Eureka on entering battle. |
| 2 | Raising an incantation from rank 2 to 3 costs 2 Eureka. |
| 3 | From the Lantern deals 160, 270 or 420% by rank. |
| 4 | Gains 2 Eureka at the start of each round. |
| 5 | Reading Class deals 230, 380 or 520% by rank. |

## Euphoria

Euphoria opens at Insight III level 30. Marcus has one Epiphany of four levels, built on Perusal and a new status, [Life Experience], which feeds Precast cards and stronger attacks.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Perusal also gives Marcus 1 stack of Life Experience after any ally casts a rank 2 incantation and 2 stacks after a rank 3 one. At the start of the round she spends 1 or 2 stacks to create a rank 1 or rank 2 Precast Reading Class, then 1 or 2 more for a Precast From the Lantern of that rank. |
| 1 | 2 | Preparation · Marcus from the Ultimate creates a rank 2 Reading Class. Each attack of hers spends 2 stacks of Life Experience to deal extra Mental DMG equal to 100% of its base damage; Reading Class at rank 3 also gains Penetration Rate +30% more, From the Lantern deals 90, 120 or 225% more by rank to an Annotated target, and the Ultimate deals 600% more to an Annotated target. |
| 1 | 3 | Annotate no longer gives Eureka when its holder acts. Instead, when Marcus attacks the Annotated enemy, her excess Critical Rate turns into Critical DMG and she regains 1 Eureka. |
| 1 | 4 | Each time she has gained 8 stacks of Life Experience, she gains [Continuous Action I] (AP +1) for 1 round at the end of the round. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Marcus | 马库斯 | 馬庫斯 | マーカス | 마커스 |
