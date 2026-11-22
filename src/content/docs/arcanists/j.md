---
title: "J"
description: "J is a 6-star Beast arcanist who deals Reality DMG with Burn and ripostes and shields allies; he has Euphoria."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "J's own Burn hurts him each time he attacks: 50% less, never below 15% HP, and only from Euphoria level 1 is he immune to it."
lastVerified: 2026-11-22
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:J.png"
    url: https://reverse1999.fandom.com/wiki/File:J.png
  - title: "Image file, uploaded 2024-07-03"
    url: https://static.wikia.nocookie.net/reverse1999/images/5/51/J.png/revision/latest?cb=20240703012011
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), J, revision 94458"
    url: https://reverse1999.fandom.com/wiki/J?oldid=94458
---

![J, full-length art](/art/characters/j.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Reality |
| Tags | Shield, Burn, Support, Riposte |
| Mainland release | 2024-06-27 |
| Global release | 2024-11-21 |

J burns enemies and himself at once: every Burn stack his attacks inflict, he also gains, and his ATK rises with his own stacks. His mass counter shields the whole team and answers each hit on a shielded ally with [Tempering], and his Ultimate copies his Burn stacks onto every enemy.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Hardness Testing (single-target attack) | 180% Reality DMG | 270% | 450% |
| Heat Treating (mass counter) | all allies Shield of 100% of J's ATK, 2 rounds | 150% | 250% |

- **Hardness Testing** puts 2 stacks of [Burn] on the target at every rank and gives all allies DMG Dealt +1% for each Burn stack on J, for 2 rounds.
- **Heat Treating** adds 3% to the Shield multiplier for each Burn stack on J. While an ally holds this Shield, each attack on that ally makes J riposte with Tempering.

[Tempering]: a riposte on all enemies for 30% Reality DMG, plus 10% for every 10% of HP J has lost; each target hit gets 2 stacks of Burn.

## Ultimate: Over the Haight Street!

Before the hit, every enemy receives as many Burn stacks as J holds; then he deals 350% Reality DMG to all enemies. J gains no Burn from this attack. For each Burn stack beyond the main target's limit, the attack deals 10% more Reality DMG.

- [Burn]: Healing Taken −15%; at the end of the round, Genesis DMG based on 4% of the holder's ATK. Stacks up to 30 and counts as one Neg Status; half the stacks are removed each time it deals damage.
- [Shield]: absorbs damage while it lasts.
- [Freeze]: the target cannot act; a Mental DMG attack ends it. [Cold]: at 2 stacks it becomes Freeze or extends a Freeze by 1 round.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | When attacking, J gains ATK +0.5% per Burn stack on himself, and his own Burn deals its damage to him without losing stacks. Each time his attack inflicts Burn, he gains the same number of stacks. His own Burn deals 50% less damage to him and cannot take him below 15% HP. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | J's Burn limit rises to 35 stacks, and while he has Burn he is immune to Freeze and Cold. At the start of a round below 50% HP, he dispels his own Stats Down and Neg Status effects other than Burn and gains Critical Rate +20% for 1 round. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Magnesia Crystal ×6; Esoteric Bones ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Fox Tail ×5; Goose Neck ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Platinum Ouija ×5; Mistilteinn ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Tempering deals 40%, plus 15% for every 10% of HP lost. |
| 2 | The Insight I ATK bonus becomes 1% per Burn stack. |
| 3 | J's Burn limit rises to 45 stacks. |
| 4 | The Ultimate deals 450%, plus 15% for each excess Burn stack. |
| 5 | The Insight I ATK bonus becomes 1.5% per Burn stack. |

## Euphoria

Euphoria opens at Insight III level 30. J has one Epiphany of four levels.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | The Insight I ATK bonus is doubled. J still gains Burn equal to what he inflicts even beyond a target's limit, he is immune to Burn DMG, and his Burn no longer loses stacks when it deals damage. The Insight III passive now works by his Burn stacks at the start of each round, each step adding to the last: at 10 or more, all allies gain DMG Taken Reduction +1% per stack for 1 round; at 20 or more, J clears his Neg Status effects other than Burn and one kind of Stats Down or Control, and every other ally loses one kind of Neg Status, Stats Down or Control; at 30 or more, all allies gain Riposte DMG Bonus +1% per stack for 1 round. |
| 1 | 2 | Hardness Testing no longer buffs the team; it deals extra Reality DMG equal to 100% of its base, inflicts 6 stacks of Burn and counts as a riposte. |
| 1 | 3 | The Ultimate deals extra Reality DMG equal to 100% of its base, and its bonus per excess Burn stack becomes 500% of the original (50% instead of 10%). After the hit, all allies gain DMG Dealt +2.5% per Burn stack on J for 3 rounds (the global client's English text names DMG Bonus here). The Ultimate no longer counts toward the team's Incantation Limit. |
| 1 | 4 | Heat Treating's base Shield multiplier becomes 150% of the original and +5% per Burn stack; a Shield on an ally that already has one adds to it, up to 600% of J's ATK. Tempering deals 300% Reality DMG plus 5% per Burn stack on J instead of the HP-lost bonus. After Tempering, J gains 1 Moxie, all allies gain a Shield of 90% of his ATK (+2% per Burn stack; stacks on an existing Shield up to 600% of his ATK), and every ally's Shield lasts 3 rounds; the Shield and Moxie parts work at most twice a round. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| J | J | J | J | J |
