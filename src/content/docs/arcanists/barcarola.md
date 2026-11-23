---
title: "Barcarola"
description: "Barcarola is a 6-star Star arcanist who deals Mental DMG and turns the Eureka her team spends into attacks."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Barcarola's Impromptu Incantation computes its damage from the average stats of all allies, not from her own stats."
lastVerified: 2026-11-22
aliases:
  - "芭卡洛兒"
  - "芭卡洛儿"
  - "バルカローラ"
  - "바르카롤라"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Barcarola.png"
    url: https://reverse1999.fandom.com/wiki/File:Barcarola.png
  - title: "Image file, uploaded 2025-01-17"
    url: https://static.wikia.nocookie.net/reverse1999/images/b/bb/Barcarola.png/revision/latest?cb=20250117082147
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Barcarola, revision 84957"
    url: https://reverse1999.fandom.com/wiki/Barcarola?oldid=84957
---

![Barcarola, full-length art](/art/characters/barcarola.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Star |
| Damage | Mental |
| Tags | DPS, Inspiration, Support, Eureka |
| Resonance Patterns | [T-shaped set](/systems/resonance/): Elucidation, Genuinity, Hyper, Inspire, Delirament |
| Psychubes recommended in game | [Addio Coda](/psychubes/addio-coda/), [Belt It Out](/psychubes/belt-it-out/) |
| Mainland release | 2024-12-12 |
| Global release | 2025-03-27 |

Barcarola works with Eureka, a resource her team spends, and [Inspiration], points built from every Eureka spent. Inspiration lands on the team's incantations each round, and casting one that carries it adds an [Impromptu Incantation] to the end of the queue, which hits harder and more often the more points it collects. Her Ultimate puts allies in [Quartet], which raises ATK and feeds more Inspiration to every attack.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Cascading Arpeggios (single-target attack) | 200% Mental DMG | 300% | 500% |
| Music of the Heart (single-target attack) | 200% Mental DMG | 300% | 500% |

- Both spend 2 Eureka after the attack, at every rank.
- **Cascading Arpeggios** gives this round's Impromptu Incantation 1 more attack, and 1 more again when at least 3 allies are in Quartet.
- **Music of the Heart** gives this round's Impromptu Incantation DMG Dealt +20%, and +20% more when at least 3 allies are in Quartet.

## Ultimate: Sea Breeze Serenade

Targets one ally. Quartet on every ally lasts 1 round longer; the target and Barcarola enter Quartet for 5 rounds, or have it extended to 5 rounds if they already hold it. Then every ally in Quartet recovers 3 Eureka, Barcarola gains 1 Moxie, and this round's Impromptu Incantation counts 8 extra points of Inspiration.

- [Inspiration]: each Eureka spent adds 1 point. At the start of each round the points are spread at random over basic incantations, at most 5 on one card; points on cards not used by the end of the round are lost. Casting a card that carries points adds an Impromptu Incantation to the end of the incantation queue, and the card's points count toward it.
- [Impromptu Incantation]: attacks 1 random enemy for 200% Mental DMG plus 15% Mental DMG for each point of Inspiration counted toward it. With at least 3, 6, 12 or 20 points it gains 1, 2, 3 or 5 more attacks.
- [Quartet]: ATK +300, plus 5 ATK for each point of accumulated Inspiration, recalculated at the start of each round; each ally in Quartet makes Barcarola's ATK increase from it 15% larger. After the holder casts an attack incantation, the Impromptu Incantation counts 1 more point of Inspiration and every arcanist in Quartet spends 1 Eureka. It cannot be dispelled.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Eureka that any ally spends builds Inspiration, and Barcarola makes the points more likely to land on attack incantations. On entering battle she starts with 3 points of Inspiration and Max Eureka +1. She gains 4 Eureka at the start of each round and 1 Eureka after an ally casts an attack incantation. |
| 2 | ATK +5% on entering battle. |
| 3 | At the start of each round, DMG Dealt +(5% + 2.5% per point of accumulated Inspiration) for 1 round. The Impromptu Incantation becomes Star Afflatus, and each of its attacks in a round gives its next ones Critical Rate +7.5% and Critical DMG +7.5%. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Starlit Ascent ×6; Silver Ore ×6; Liquefied Terror ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Starlit Ascent ×10; Perpetual Cog ×5; Prophetic Bird ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Starlit Ascent ×16; Wyrmling Skeleton ×6; Mistilteinn ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Cascading Arpeggios gives the Impromptu Incantation 2 more attacks instead of 1. |
| 2 | The Insight 3 critical bonus per Impromptu attack becomes Critical Rate +15% and Critical DMG +15%. |
| 3 | With at least 3 allies in Quartet, Cascading Arpeggios adds 2 more attacks instead of 1. |
| 4 | Music of the Heart gives the Impromptu Incantation DMG Dealt +35%. |
| 5 | Quartet counts 2 points of Inspiration after each attack incantation instead of 1. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Barcarola | 芭卡洛儿 | 芭卡洛兒 | バルカローラ | 바르카롤라 |
