---
title: "Ms. Stranger"
description: "Ms. Stranger is a 6-star Mineral arcanist who deals Mental DMG with a special card that counts as an Ultimate."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "A Moth to a Flame starts locked and unlocks only when it sits in the rightmost place of the Spelldock at the start of a round; it then costs no AP and counts as an Ultimate."
lastVerified: 2026-11-22
aliases:
  - "無名者"
  - "无名者"
  - "ストレンジャー"
  - "미스 스트레인저"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Ms. Stranger.png"
    url: https://reverse1999.fandom.com/wiki/File:Ms._Stranger.png
  - title: "Image file, uploaded 2026-08-09"
    url: https://static.wikia.nocookie.net/reverse1999/images/4/42/Ms._Stranger.png/revision/latest?cb=20260809213848
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Ms. Stranger, revision 89946"
    url: https://reverse1999.fandom.com/wiki/Ms._Stranger?oldid=89946
---

![Ms. Stranger, full-length art](/art/characters/ms-stranger.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Mineral |
| Damage | Mental |
| Tags | DPS, Ritual |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Psychubes recommended in game | [Until I Am Me](/psychubes/until-i-am-me/) |
| Mainland release | 2026-05-21 |
| Global release | 2026-09-03 |

Ms. Stranger's damage comes from A Moth to a Flame, a card that appears locked at the left of the Spelldock and grows stronger with every kind of incantation the team casts while it waits. It unlocks once it reaches the rightmost place, and her own incantations and Insight III move it there faster. Her Ultimate is a self buff that lets her follow each attack with an extra Moth to a Flame.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Cocoon Breaker (single-target attack) | 200% Mental DMG | 300% | 500% |
| Phototactic Instinct (mass attack) | 180% Mental DMG; Self-Deception 3 rounds | 270% | 450% |

- **Cocoon Breaker** checks where it sat in the Spelldock before it was cast. Right of A Moth to a Flame, it gives Ms. Stranger 2 stacks of [Last Piece of Herself] after the hit; left of it, the hit deals the same percentage again as extra Mental DMG.
- **Phototactic Instinct** hits all enemies and puts [Self-Deception] on every target hit at each rank.

[Self-Deception]: DMG Taken Reduction −20%; when A Moth to a Flame hits the holder, that attack gains Critical Rate +15% and Critical DMG +30%. Gaining it again renews its duration.

## Ultimate: Implanted Memories

A self buff. Ms. Stranger dispels her own Stats Down and Neg Status effects, gains [New Life] for 2 rounds and gains 1 stack of [Silent Flutter].

- [New Life]: DMG Taken Reduction +20%, DMG Bonus +40%, and Penetration Rate +20% for A Moth to a Flame. Gaining it again adds to its duration; it cannot be dispelled.
- [Silent Flutter]: after Ms. Stranger attacks with any incantation of her own, one stack is spent to cast A Moth to a Flame once more, with 2 stacks of each of the four enhancements. That cast does not count as an extra action. Up to 10 stacks; it cannot be dispelled.

## A Moth to a Flame

On entering battle, and at the start of the round after she loses the card, Ms. Stranger puts A Moth to a Flame in the leftmost place of the Spelldock, never further left than the 9th place from the right. It starts locked and cannot be used or moved. At the start of a round in which it is the rightmost card, it unlocks and dispels every [Control] effect on her.

Cast, it deals 440% Mental DMG to one enemy. It costs no AP, counts as an Ultimate and is a [Sovereign Incantation], so casting it counts as an action she takes herself.

While it waits, it gains enhancements of four types from the kinds of incantations and Ultimates that allies cast in the AP Area, at most 4 stacks of each type. Each stack adds to the cast:

| Type | Comes from | Each stack adds |
| --- | --- | --- |
| 1 | single-target attack or debuff | 110% Mental DMG, and 440% more to the main target |
| 2 | mass attack or debuff | 330% Mental DMG and 1 more target |
| 3 | buff or counter | Critical Rate +8%, Ultimate Might +12% |
| 4 | heal or channel | Critical DMG +12%, Incantation Might +12% |

- [Last Piece of Herself]: when she gains A Moth to a Flame, up to 4 stacks are spent; the card moves right by as many places as stacks spent and gains twice that number of enhancements, filling the types with the fewest stacks first. Up to 10 stacks; it cannot be dispelled.
- [Control]: effects that stop a character from acting, such as Daze, Petrify, Nightmare, Freeze, Disarm, Silence and Seal.
- [Sovereign Incantation]: casting it counts as the character taking an action herself.

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Puts a locked A Moth to a Flame in the Spelldock on entering battle and in the round after each use, and unlocks it when it is the rightmost card at the start of a round. |
| 1 | Her Ultimate does not count toward the team's Incantation Draw Limit. She gains Moxie +3 when A Moth to a Flame unlocks. Her incantations draw on both Incantation Might and Ultimate Might at 100%. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | On entering battle, her first A Moth to a Flame moves 8 places right at once and gains 16 enhancements, filling the types with the fewest stacks first. Each time an enemy's Afflatus Guard falls to 0, she gains 1 stack of Last Piece of Herself. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×6; Magnesia Crystal ×6; Esoteric Bones ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×10; Fox Tail ×6; Golden Beetle ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×16; Emerald Slate ×6; Rheingold ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | She gains 2 stacks of Last Piece of Herself when an enemy's Afflatus Guard falls to 0; a cast from Silent Flutter has 3 stacks of each enhancement. |
| 2 | New Life gives DMG Bonus +60% and A Moth to a Flame Penetration Rate +30%; a cast from Silent Flutter has 4 stacks of each enhancement. |
| 3 | Self-Deception gives DMG Taken Reduction −30%, and A Moth to a Flame gains Critical Rate +20% and Critical DMG +40% against its holder. |
| 4 | Her incantations draw on Incantation Might and Ultimate Might at 120%. |
| 5 | A Moth to a Flame deals 560%; each stack adds 140% and 560% to the main target (type 1), 420% (type 2), Critical Rate +10% and Ultimate Might +15% (type 3), Critical DMG +15% and Incantation Might +15% (type 4). |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Ms. Stranger | 无名者 | 無名者 | ストレンジャー | 미스 스트레인저 |
