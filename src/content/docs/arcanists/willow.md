---
title: "Willow"
description: "Willow is a 6-star Plant arcanist who deals Mental DMG through Poison and Hag's Bane; she has Euphoria."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Ancient Ritual costs more Moxie each round it lasts; when her Moxie falls short, Willow casts Ending Pose and the channel ends."
lastVerified: 2026-11-22
aliases:
  - "篤篤骨"
  - "笃笃骨"
  - "ヴィロー"
  - "윌로우"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Willow.png"
    url: https://reverse1999.fandom.com/wiki/File:Willow.png
  - title: "Image file, uploaded 2024-11-02"
    url: https://static.wikia.nocookie.net/reverse1999/images/b/b2/Willow.png/revision/latest?cb=20241102054710
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Willow, revision 85076"
    url: https://reverse1999.fandom.com/wiki/Willow?oldid=85076
---

![Willow, full-length art](/art/characters/willow.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Plant |
| Damage | Mental |
| Tags | DPS, Poison, Channel |
| Mainland release | 2024-10-31 |
| Global release | 2025-02-20 |

Willow spreads [Poison] every round through her Insight 1 passive and each time an ally attacks, then turns it into [Hag's Bane], a poison whose damage grows each time it resolves in the same round. Her second attack spends Poison to make Hag's Bane resolve again at once. Her Ultimate is a channel, [Ancient Ritual], that adds Hag's Bane to every enemy each round for Moxie and ends with the mass attack [Ending Pose].

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Hag's Advice (single-target attack) | 100% Mental DMG; turns up to 3 Poison into Hag's Bane | 125%; up to 4 | 175%; up to 5 |
| Hag's Gratitude (single-target attack) | 100% Mental DMG; spends up to 2 Poison | 125%; up to 3 | 175%; up to 4 |

- **Hag's Advice** works on a target that already has Poison: each Poison it turns becomes 1 stack of Hag's Bane lasting 2 rounds.
- **Hag's Gratitude** works on a target that has both Poison and Hag's Bane: each Poison it spends makes the target's Hag's Bane resolve once, without using up a round of it.

## Ultimate: In the Fire, In the Shadow

Willow channels and enters Ancient Ritual.

## Statuses

| Status | Effect |
| --- | --- |
| Poison | Genesis DMG at the end of the round based on the caster's ATK; stacks. The Poison of her Insight 1 deals 20% of her ATK. |
| Hag's Bane | Counts as Poison. Genesis DMG equal to 20% of the caster's ATK at the end of the round, for 2 rounds. Each time it resolves, the target takes 40% more from further Hag's Bane resolves that round, up to 4 times. Up to 10 stacks. |
| Ancient Ritual | While it lasts, enemies count as having had Hag's Bane resolve 1 + (rounds elapsed) extra times that round. In the first round it costs no Moxie and puts 1 stack of Hag's Bane on all enemies. In each later round it costs 2 + 2 × (rounds elapsed) Moxie at the round's end and puts half that many stacks of Hag's Bane on all enemies. If her Moxie falls short, she spends what is left, casts Ending Pose and the channel ends. |
| Ending Pose | 200% Mental DMG to all enemies, then Genesis DMG equal to 50% of Willow's ATK for each stack of Hag's Bane on each target. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | At the start of a round, 2 enemies receive 2 Poison for 2 rounds, those with the most Poison first. When another ally casts an attack incantation on an enemy, Willow adds 2 Poison for 2 rounds to its main target, up to 2 times a round. |
| 2 | ATK +5% on entering battle. |
| 3 | Ancient Ritual also raises her Max Moxie by 5 and gives 1 more Moxie for each incantation she casts or moves. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×6; Shattered Bones ×6; Fox Tail ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×10; Rough Silver Ingot ×4; Biting Box ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×16; Murmur of Insanity ×6; Golden Fleece ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Hag's Bane deals 24% of her ATK. |
| 2 | Insight 1 Poison deals 40% of her ATK; each Hag's Bane resolve raises further resolves by 45%. |
| 3 | Hag's Advice turns up to 4, 5 or 6 Poison by rank. |
| 4 | Insight 1 adds 3 Poison when another ally attacks. |
| 5 | Each Hag's Bane resolve raises further resolves by 50%. |

## Euphoria

Euphoria opens at Insight III level 30. Willow has one Epiphany of four levels; it strengthens Hag's Bane and feeds Moxie to Ancient Ritual.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Each stack of Hag's Bane also gives its holder Poison DMG Taken +5%. When the stack cap is passed, the stacks with the fewest rounds left are removed first. |
| 1 | 2 | At the end of each round in Ancient Ritual, Willow gains 1 Moxie for every 2 stacks of Hag's Bane on the enemy that has the most. |
| 1 | 3 | Hag's Bane deals extra Genesis DMG equal to 100% of its base Genesis DMG. |
| 1 | 4 | Ending Pose gives her 3 Moxie. At the end of a round in which she is not in Ancient Ritual, she gains 2 Moxie. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Willow | 笃笃骨 | 篤篤骨 | ヴィロー | 윌로우 |
