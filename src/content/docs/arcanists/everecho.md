---
title: "Everecho"
description: "Everecho is a 6-star Mineral Conduit arcanist who heals the team and raises its damage with Past Shadows."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Tomorrow's Hope, her heal, can be cast only by spending a stack of Long-Lost Light from a Light's Might Energy card; without one, her Conduit falls back to Yesterday's Yearning."
lastVerified: 2026-11-22
aliases:
  - "回聲謠"
  - "回声谣"
  - "エバーエコー"
  - "에버에코"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Everecho.png"
    url: https://reverse1999.fandom.com/wiki/File:Everecho.png
  - title: "Image file, uploaded 2026-09-01"
    url: https://static.wikia.nocookie.net/reverse1999/images/0/0e/Everecho.png/revision/latest?cb=20260901220128
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Everecho, revision 102002"
    url: https://reverse1999.fandom.com/wiki/Everecho?oldid=102002
---

![Everecho, full-length art](/art/characters/everecho.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Mineral |
| Damage | Reality |
| Tags | Heal, Conduit, Support |
| Resonance Patterns | [U-shaped set](/systems/resonance/): Hyper, Overindulgence, Quiescence, Prudentiality, Equanimity |
| Mainland release | 2026-06-11 |
| Global release | 2026-09-24 |

Everecho has no incantation cards and no ordinary Ultimate: she casts through a [Conduit], which the team charges with Energy cards, and Harmonization takes the place of Moxie. Her Conduit switches between an attack that gives every ally [Past Shadows] and a mass heal that needs [Long-Lost Light], and she gives the whole team [Remembrance], a reserve that takes damage once HP reaches 1.

## Incantations

| Incantation | Effect |
| --- | --- |
| Yesterday's Yearning (mass attack, Interval) | 200% Reality DMG to all enemies; all allies gain 1 stack of [Past Shadows] for 2 rounds |
| Tomorrow's Hope (mass heal) | all allies recover HP equal to 180% of Everecho's ATK; removes 2 kinds of Stats Down, Neg Status or Control effects from each ally |

- **Tomorrow's Hope** spends 1 stack of Long-Lost Light each time it is cast. With none left, the Conduit switches to Yesterday's Yearning.
- [Interval]: once the Conduit casts the incantation, it stops for the rest of the round.

## Energy cards

| Card | Effect |
| --- | --- |
| Light's Might | Chaotic Energy +1; Everecho gains 1 stack of Long-Lost Light. Afterwards, unless the Conduit has Echoes' Embrace selected, it switches to Tomorrow's Hope. |
| Light's Might II | as Light's Might, with Chaotic Energy +2 |
| Chaotic Energy II | Chaotic Energy +2 |

## Ultimate: Echoes' Embrace

Deals 500% Reality DMG to all enemies, then puts [Hollow Shell] on all of them for 3 rounds, gives all allies 5 stacks of Past Shadows for 2 rounds and gives every Conduit ally [Rekindled Memory] for 3 rounds. Afterwards the Conduit switches to Tomorrow's Hope if Everecho holds Long-Lost Light, and to Yesterday's Yearning if she does not.

## Statuses

| Status | Effect |
| --- | --- |
| Conduit | Charged with Energy; at the end of the AP Area it runs in a loop, spending Energy to cast incantations. |
| Past Shadows | DMG Bonus equal to 0.6% of Everecho's ATK, plus DMG Bonus +1% for each stack. Up to 15 stacks; gaining it again refreshes its duration. |
| Long-Lost Light | Lets Everecho's Conduit cast Tomorrow's Hope. |
| Soothing Song | When its holder loses HP, it gains Remembrance in the same proportion of Remembrance's maximum as the share of HP lost. |
| Remembrance | Once HP falls to 1, Remembrance takes the rest of the damage. Its maximum equals 400% of Everecho's ATK. |
| Mend | At 4 stacks, lets its holder restart a Conduit that an Interval incantation stopped. Up to 4 stacks. |
| Hollow Shell | Reality DEF, Mental DEF and Critical DEF −10%. |
| Rekindled Memory | Critical DMG +2% for each stack of Past Shadows its holder has. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | No basic incantations or Ultimate; casts through the Conduit with Energy, and Harmonization replaces Moxie. On entering battle, all allies gain Soothing Song. Everecho gains 1 stack of Mend for each Energy the team spends. |
| 1 | At the start of each round, Everecho gains Harmonization +15, and all allies recover HP equal to 20% of Remembrance. |
| 2 | ATK +5% on entering battle. |
| 3 | On entering battle, all allies take 30% less DMG and Everecho gains Harmonization +30. Each Conduit ally stores up to 50 Harmonization beyond the cap and refills from it at the end of the round when there is room. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×6; Shattered Bones ×6; Luminite Ore ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×10; Spell of Fortune ×6; Biting Box ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×16; Goldbell Spirit Bottle ×6; Mistilteinn ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Echoes' Embrace gives 10 stacks of Past Shadows; Past Shadows caps at 20 stacks; 2 Light's Might cards in the deck give Chaotic Energy +2. |
| 2 | Past Shadows gives 0.8% of Everecho's ATK and +1.5% per stack; 1 more Light's Might card gives Chaotic Energy +2. |
| 3 | Hollow Shell lowers Reality DEF, Mental DEF and Critical DEF by 15%. |
| 4 | The Insight 1 heal becomes 35% of Remembrance; Tomorrow's Hope heals 240% of Everecho's ATK. |
| 5 | Past Shadows gives 1.2% of Everecho's ATK and +2% per stack; 2 Chaotic Energy II cards in the deck give Chaotic Energy +3. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Everecho | 回声谣 | 回聲謠 | エバーエコー | 에버에코 |
