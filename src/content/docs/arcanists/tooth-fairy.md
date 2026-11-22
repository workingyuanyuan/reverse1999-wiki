---
title: "Tooth Fairy"
description: "Tooth Fairy is a 6-star Star arcanist who deals Mental DMG, heals the team and lowers enemy Critical defences."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Song for the Bad Tooth removes Stats Down, Neg Status and Control effects from the team only when it lands a critical hit."
lastVerified: 2026-11-22
aliases:
  - "牙仙"
  - "トゥースフェアリー"
  - "투스 페어리"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Tooth Fairy.png"
    url: https://reverse1999.fandom.com/wiki/File:Tooth_Fairy.png
  - title: "Image file, uploaded 2023-11-18"
    url: https://static.wikia.nocookie.net/reverse1999/images/f/f8/Tooth_Fairy.png/revision/latest?cb=20231118205757
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Tooth Fairy, revision 85068"
    url: https://reverse1999.fandom.com/wiki/Tooth_Fairy?oldid=85068
---

![Tooth Fairy, full-length art](/art/characters/tooth-fairy.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Star |
| Damage | Mental |
| Tags | Heal, Support, Remove Debuffs |
| Mainland release | 2023-07-27 |
| Global release | 2023-12-07 |

Tooth Fairy pairs a mass heal with single-target Mental attacks that weaken enemies against critical hits. She collects [Baby Tooth] as the team casts incantations and spends 5 at the start of a round to lower all enemies' Critical Resist and Critical DEF. Her Euphoria moves the kit onto Eureka: Baby Teeth then come from Eureka the team spends and feed the [Impromptu Incantation].

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Empty Gums (single-target attack) | 150% Mental DMG | 250% | 450% |
| Lullaby (mass heal) | all allies heal 80% of her ATK | 120% | 200% |

- **Empty Gums** puts 1 stack of [Confusion] on the target for 1 round after the attack.
- **Lullaby** has Critical Rate +30% for the heal at every rank.

[Confusion]: Critical Resist −25%; stacks, each with its own duration.

## Ultimate: Song for the Bad Tooth

Deals 500% Mental DMG to one enemy with Critical Rate +30% for the attack. If it lands a critical hit, it removes Stats Down, Neg Status and [Control] effects from all allies.

[Control]: effects that stop a character from acting, such as Daze, Petrify, Nightmare, Freeze, Disarm, Silence and Seal.

[Baby Tooth]: at 5, the teeth are spent at the start of the round and set off the Insight 1 effect.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Tooth Fairy enters battle with 3 Baby Teeth and collects 1 each time any ally actively casts a character incantation. At the start of a round, with at least 5, she spends 5 to lower all enemies' Critical Resist and Critical DEF by 15% for 1 round. |
| 2 | Healing Done +10% on entering battle. |
| 3 | Each time the Baby Tooth Stats Down triggers, all allies recover 10% of their missing HP. She enters battle with 2 more Baby Teeth. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Starlit Ascent ×6; Spell of Banishing ×6; Solidus ×4 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Starlit Ascent ×10; Liquefied Terror ×5; Salted Mandrake ×4 |
| 3 | 60 | Sharpodonty 200,000; Tome of Starlit Ascent ×16; Wyrmling Skeleton ×6; Golden Fleece ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | The Ultimate deals 600%. |
| 2 | The Baby Tooth Critical Resist and Critical DEF reduction lasts 1 round longer. |
| 3 | Empty Gums deals 170, 280 or 500% by rank. |
| 4 | Lullaby heals 90, 135 or 225% of her ATK by rank. |
| 5 | The Baby Tooth reduction becomes 25%. |

## Euphoria

Euphoria opens at Insight III level 30. Tooth Fairy has one Epiphany of four levels; it turns her into a Eureka support for the Impromptu Incantation.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Max Eureka +5 and Eureka +2 at the start of each round; Eureka the team spends builds [Inspiration], and she enters battle with 5 Inspiration. Baby Teeth no longer come from incantations cast: she gains 1 for every 4 Eureka the team spends. At the start of the round she spends up to 5; each one gives the first 3 attacks of Impromptu Incantation that round DMG Dealt +4% and puts 1 stack of [Decayed Tooth] on all enemies. The Insight 3 heal becomes 5% of missing HP for each tooth spent, and each tooth also adds 2 Inspiration to that round's Impromptu Incantation. |
| 1 | 2 | Empty Gums no longer inflicts Confusion. It gives her [Continuous Action I] for 1 round and, after the attack, spends 2 Eureka to give Impromptu Incantation 1 more attack instance this round. |
| 1 | 3 | Lullaby also spends 2 Eureka to give Impromptu Incantation DMG Dealt +20% this round. |
| 1 | 4 | After the attack, the Ultimate adds 8 Inspiration to this round's Impromptu Incantation and puts [Neuralgia] on the target for 1 round, which triggers up to 3 times. |

- **Inspiration**: each Eureka spent adds 1 point. At the start of each round the points are spread at random over basic incantations, at most 5 on one card, and points on unused cards are cleared at the end of the round. Casting a card that carries points adds an Impromptu Incantation to the end of the queue with those points.
- **Impromptu Incantation**: hits a random enemy for 200% Mental DMG plus 15% Mental DMG for each Inspiration point it holds; with at least 3, 6, 12 or 20 points it gains 1, 2, 3 or 5 more attack instances. Its damage uses the average stats of all allies.
- **Decayed Tooth**: Critical Resist Rate −10% and Critical DEF −10%; up to 5 stacks, each with its own duration.
- **Neuralgia**: after each Impromptu Incantation attack on its holder, the holder takes [Static Genesis DMG] equal to 30% of that attack's total damage. A target holds only one Neuralgia at a time.
- **Static Genesis DMG**: Genesis DMG that stat bonuses do not change.
- **Continuous Action I**: AP +1.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Tooth Fairy | 牙仙 | 牙仙 | トゥースフェアリー | 투스 페어리 |
