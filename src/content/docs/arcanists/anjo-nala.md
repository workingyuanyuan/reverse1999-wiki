---
title: "Anjo Nala"
description: "Anjo Nala is a 6-star Beast arcanist who deals Mental DMG and binds an ally to cast its Ultimate."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "The ally Anjo Nala binds cannot gain Moxie or cast its Ultimate on its own; it casts one only inside her Ultimate, which costs it 50% of its current HP (15% from Euphoria level 2)."
lastVerified: 2026-11-22
aliases:
  - "天使娜娜"
  - "アンジョナナ"
  - "안조 날라"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Anjo Nala.png"
    url: https://reverse1999.fandom.com/wiki/File:Anjo_Nala.png
  - title: "Image file, uploaded 2024-10-06"
    url: https://static.wikia.nocookie.net/reverse1999/images/f/f1/Anjo_Nala.png/revision/latest?cb=20241006214830
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Anjo Nala, revision 84950"
    url: https://reverse1999.fandom.com/wiki/Anjo_Nala?oldid=84950
---

![Anjo Nala, full-length art](/art/characters/anjo-nala.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Mental |
| Tags | DPS, Extra Action, Ritual, Control, Channel |
| Mainland release | 2024-09-19 |
| Global release | 2025-01-09 |

At the start of battle Anjo Nala binds one other ally; the kind of bond follows that ally's Afflatus, and the two share part of each other's stats. The bound ally's Moxie goes to her, and her Ultimate makes it cast its own Ultimate before hers. Twin Phantoms starts the 7-round [Hymn] channel, which her other incantations and the bound ally's casts shorten; when it ends, she casts [Angel's Temptation] and leaves all enemies unable to act.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Feast of Lust (single-target attack) | 180% Mental DMG; +40% per Neg Status type on the target | 270%; +60% | 450%; +100% |
| Twin Phantoms (self channel) | enters Hymn for 7 rounds; cast during Hymn, shortens it by 1 round | 7 rounds; by 2 | 7 rounds; by 3 |

**Feast of Lust** puts [Titillated] on the target for 2 rounds at every rank, and shortens Hymn by 1 round while Anjo Nala is in it.

[Hymn]: a 7-round channel; when it ends, Anjo Nala casts Angel's Temptation.

[Angel's Temptation]: an attack on all enemies that puts Titillated on them and deals 150% Mental DMG. Cast at the end of a completed Hymn channel, it puts [Captivated] on them instead and deals 250% Mental DMG more.

[Titillated]: DMG Bonus −10%; at 3 stacks it turns into Captivated for 1 round.

[Captivated]: the target cannot act and loses 10% ATK, which Anjo Nala gains.

## Ultimate: Interwoven Dreams

Anjo Nala and the bound ally both channel for 1 round and cannot act. At the start of the next round the bound ally loses 50% of its current HP and casts its own Ultimate; then Anjo Nala attacks all enemies, puts 2 random effects of [Collection of Debuffs] on them, and deals 500% Mental DMG, plus 60% for each type of Neg Status among all enemies.

[Collection of Debuffs]: seven effects, those the enemies lack chosen first:

| Status | Effect |
| --- | --- |
| Blind | DMG Bonus −30% on single-target attacks. |
| Nasty Wound | Healing Taken −50%. |
| Mis-aim | DMG Bonus −30% on attacks on several targets. |
| Weakness | DMG Bonus −25% when attacking; one stack is used each time. |
| Scared | Mental DMG taken +25%; one stack is used each time. |
| Confusion | Critical Resist −25%; stacks, each with its own duration. |
| Fracture I | When hit, the holder takes Genesis DMG equal to 20% of the ATK of the arcanist who applied it. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | On entering battle, Anjo Nala binds another ally, and the two gain a share of each other's stats by that ally's Afflatus: Spirit or Intellect, [Mind and Flesh], 4% of ATK and Max HP; Beast or Plant, [Bone and Blood], 8% of Critical DMG and Reality DEF; Mineral or Star, [Form and Phantom], 8% of Critical Rate and Mental DEF. Her Moxie cap becomes 12 and her Ultimate needs 8 Moxie. The bound ally cannot gain or cast its Ultimate, and Moxie it gains goes to Anjo Nala. |
| 2 | Critical DMG +15% on entering battle. |
| 3 | When the bound ally casts an incantation itself while Anjo Nala is in Hymn, Hymn shortens by 1 round and the bond adds an effect: Mind and Flesh, she follows up with a rank 1 Feast of Lust on the enemy with the lowest HP share; Bone and Blood, she gains 1 more Moxie; Form and Phantom, she casts Angel's Temptation, at most 2 times a round. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Spell of Banishing ×6; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Liquefied Terror ×5; Golden Grass Incense ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Watch Core ×6; Rheingold ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Form and Phantom's Angel's Temptation can come up to 3 times a round; Angel's Temptation deals 250%. |
| 2 | Angel's Temptation at the end of Hymn deals 375% more; Captivated lowers ATK by 15%. |
| 3 | The Ultimate deals 600%, plus 100% per Neg Status type; Bone and Blood gives 2 Moxie. |
| 4 | Mind and Flesh shares 8%, Bone and Blood and Form and Phantom 18%; Titillated turns into Captivated at 2 stacks. |
| 5 | The Ultimate puts 4 effects of Collection of Debuffs and adds 140% per Neg Status type. |

## Euphoria

Euphoria opens at Insight III level 30. Anjo Nala has one Epiphany of four levels; it builds on the bond.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | After the bound ally takes an extra action, the bond grows stronger and both gain 1 stack of [Harmonic Tapestry], at most 8. By bond it gives ATK +2% (Mind and Flesh), Ultimate Might +6% (Bone and Blood) or Extra Action DMG +10% (Form and Phantom). |
| 1 | 2 | The Ultimate takes 15% of the bound ally's current HP instead of 50%. Each time the bond grows stronger, Anjo Nala gains 1 Moxie and 2 stacks of [Ceremonious: Critical DMG], 4 more with Bone and Blood. |
| 1 | 3 | After the Ultimate attacks, Anjo Nala gains [The Final Sustain] for 2 rounds: Feast of Lust and Angel's Temptation deal extra Mental DMG equal to 300% of their base Mental DMG. |
| 1 | 4 | At 8 stacks of Harmonic Tapestry, the Ultimate costs no AP, does not count toward the Incantation Draw Limit, and gives 2 Moxie after it is cast. By bond: Mind and Flesh, Feast of Lust deals 400% more Mental DMG and shortens Hymn by 1 more round; Bone and Blood, the Ultimate deals extra Mental DMG equal to 140% of its base, and Ultimate Might counts double for it; Form and Phantom, Angel's Temptation turns excess Critical Rate into Critical DMG and deals extra Mental DMG equal to 200% of its base. |

[Ceremonious: Critical DMG]: Ultimate Critical DMG +3% per stack, up to 100 stacks; cannot be dispelled; used up when an Ultimate attacks.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Anjo Nala | 天使娜娜 | 天使娜娜 | アンジョナナ | 안조 날라 |
