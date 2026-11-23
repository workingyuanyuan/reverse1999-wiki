---
title: "Ramona"
description: "Ramona is a 6-star Plant arcanist who deals Mental DMG through Poison and rewrites allied incantations."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Marigold Method fires only when an ally actively casts an incantation rewritten with Possessed, and each rewrite lasts 1 round."
lastVerified: 2026-11-22
aliases:
  - "拉莫納"
  - "拉莫纳"
  - "ラモナ"
  - "라모나"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Ramona.png"
    url: https://reverse1999.fandom.com/wiki/File:Ramona.png
  - title: "Image file, uploaded 2026-04-10"
    url: https://static.wikia.nocookie.net/reverse1999/images/3/3a/Ramona.png/revision/latest?cb=20260410015002
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Ramona, revision 93271"
    url: https://reverse1999.fandom.com/wiki/Ramona?oldid=93271
---

![Ramona, full-length art](/art/characters/ramona.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Plant |
| Damage | Mental |
| Tags | DPS, Poison, Rewrite |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Psychubes recommended in game | [Drown Out the Hustle](/psychubes/drown-out-the-hustle/) |
| Mainland release | 2026-03-26 |
| Global release | 2026-06-18 |

Ramona gathers Exorcist-for-Hire stacks. At the start of each round she spends them to rewrite that many allied incantations with Possessed, and each rewritten card an ally casts makes her fire Marigold Method, a follow-up attack on all enemies that adds Poison and Spirit Repellent. Spirit Repellent makes Poison settle extra times, and her Ultimate turns the Poison on each enemy into Expellant, which grows every round and bursts when it ends.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Purifying Incense (attack on 2 enemies) | 180% Mental DMG | 270% | 450% |
| Ghost-Be-Gone (single-target attack) | 200% Mental DMG; Poison settles once at 100% | 300%; 125% | 500%; 160% |

- Both incantations put 1 instance of [Poison] on each target for 2 rounds, dealing Genesis DMG equal to 40% of Ramona's ATK at the end of each round.
- **Purifying Incense** gives Ramona 1 stack of [Exorcist-for-Hire] after the attack.
- **Ghost-Be-Gone** settles 1 round of the target's Poison at once, at the share of its normal damage in the table; this does not shorten the Poison.

## Ultimate: For the Peace of Both Worlds

Deals 500% Mental DMG to all enemies and turns up to 6 instances of Poison on each target into 1 instance of [Expellant] for 2 rounds. Afterwards Ramona gains [Efficient Exorcist] for 2 rounds.

## Statuses

| Status | Effect |
| --- | --- |
| Poison | At the end of the round, the holder takes Genesis DMG based on the caster's ATK; instances stack. |
| Exorcist-for-Hire | Removed at the start of the round to set off Ramona's Precognition; at most 6 stacks. |
| Possessed | Rewrites an incantation for 1 round. When an ally actively casts it, Ramona casts [Marigold Method] once. It does not combine with other rewrites. |
| Marigold Method | A follow-up attack: 250% Mental DMG to all enemies, 1 instance of Poison (40% of ATK, 2 rounds), then 1 stack of [Spirit Repellent] on each target hit for 2 rounds. |
| Spirit Repellent | At the end of the round, each stack makes the holder's Poison settle once more without shortening it; at most 6 stacks, each timed on its own. |
| Expellant | Counts as Poison. At the end of the round, deals Genesis DMG equal to the number of Poison instances it absorbed × 50% of ATK, and 25% more for each round it has lasted. When its duration ends, it adds Genesis DMG equal to the rounds it lasted × 350% of ATK, counted as Poison DMG. |
| Efficient Exorcist | At the start of each round, Ramona gains a rank 3 Ghost-Be-Gone as a precast incantation, rewritten with Possessed. Cannot be dispelled; gaining it again adds to its duration. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | At the start of the round, Ramona removes her Exorcist-for-Hire stacks and rewrites one allied incantation with Possessed for each stack removed, her own incantations first. Each actively cast Possessed incantation makes her cast Marigold Method once. |
| 1 | At the start of each round, Ramona gains 1 stack of Exorcist-for-Hire. On entering battle, and whenever an enemy enters, she puts 2 instances of Poison (40% of ATK, 2 rounds) on the enemies. |
| 2 | ATK +5% on entering battle. |
| 3 | On entering battle, Ramona gains Moxie +2, and the first Marigold Method of each round gives her Moxie +1. For each enemy that leaves the field in a round, all enemies receive 1 stack of Spirit Repellent for 2 rounds at the start of the next round. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×6; Silver Ore ×6; Liquefied Terror ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×10; Esoteric Bones ×6; Jeweled Egg ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×16; Goldbell Spirit Bottle ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Insight 3 gives Moxie +3 on entering battle; Marigold Method deals 400% and adds 2 instances of Poison and 2 stacks of Spirit Repellent. |
| 2 | Expellant deals the absorbed Poison count × 75% of ATK, grows 35% per round and ends with the rounds lasted × 550% of ATK; Efficient Exorcist lasts 3 rounds. |
| 3 | Purifying Incense and Ghost-Be-Gone put 2 instances of Poison; every Poison Ramona applies deals 50% of her ATK. |
| 4 | Ghost-Be-Gone settles Poison at 140, 165 or 200% by rank; Expellant ends with the rounds lasted × 750% of ATK. |
| 5 | Expellant deals the absorbed Poison count × 100% of ATK and grows 45% per round; Ramona gains 2 stacks of Exorcist-for-Hire each round; Spirit Repellent from Marigold Method stacks up to 8. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Ramona | 拉莫纳 | 拉莫納 | ラモナ | 라모나 |
