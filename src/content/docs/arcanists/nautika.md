---
title: "Nautika"
description: "Nautika is a 6-star Spirit Bloodtithe arcanist who spends her own HP to deal Reality DMG based on Max HP."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Nautika's Ultimate does not use Moxie: it opens at 8 Faith, and she gains 1 Faith each time the team's Bloodtithe rises."
lastVerified: 2026-11-22
aliases:
  - "諾諦卡"
  - "诺谛卡"
  - "ノーティカ"
  - "노티카"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Nautika.png"
    url: https://reverse1999.fandom.com/wiki/File:Nautika.png
  - title: "Image file, uploaded 2025-05-16"
    url: https://static.wikia.nocookie.net/reverse1999/images/2/27/Nautika.png/revision/latest?cb=20250516021018
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Nautika, revision 101999"
    url: https://reverse1999.fandom.com/wiki/Nautika?oldid=101999
---

![Nautika, full-length art](/art/characters/nautika.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Spirit |
| Damage | Reality |
| Tags | DPS, Bloodtithe, Channel |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Mainland release | 2025-05-15 |
| Global release | 2025-09-19 |

Nautika turns lost HP into power. Every 3000 HP the team loses adds a point of [Bloodtithe], and her incantations cost her own HP, or every unit's, to add damage based on her Max HP. Her Ultimate spends the stored Bloodtithe at the end of the round on a channelled flurry of hits that also heals her.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Haunting Pain (attack on 2 enemies) | loses 20% of current HP; 100% Reality DMG plus 100% based on 10% of Max HP; 4 stacks of [Higge] | 30%; 150% plus 15% of Max HP; 6 stacks | 50%; 250% plus 25% of Max HP; 10 stacks |
| Gates of Horn and Ivory (choice) | casts rank 1 Weaver of Light or Martyr of the Abyss | rank 2 | rank 3 |
| Weaver of Light (self counter) | [Mother Spirit's Guidance] and DMG Taken −10% for 3 rounds | −15% | −25% |
| Martyr of the Abyss (single-target attack) | every unit on the field loses 20% of current HP; damage based on 10% of Max HP | 30%; 15% | 50%; 25% |

- **Gates of Horn and Ivory** lets her choose, when cast, which of its two cards to play at the same rank.
- **Martyr of the Abyss** never takes more than 20, 30 or 50% of Nautika's Max HP from any unit, by rank. It gives all allies [Adversity I] for 3 rounds, then deals Reality DMG equal to 50% for each unit on the field.

## Ultimate: Divine Yoik

Nautika channels and enters [Blood Sacrifice] for 1 round; the card does not count toward the team's Incantation Draw Limit.

## Statuses

| Status | Effect |
| --- | --- |
| Bloodtithe | A team resource: +1 for every 3000 HP the allies lose in total; HP lost to attacks counts at 30%. In the mainland client a team cannot hold it together with Lingering Glow or the Pursuit Scope; the global text has no such clause. |
| Blood Sacrifice | At the end of the round, spends as much Bloodtithe as it can: every 8 points give 3 Blood Sacrifice points, at most 24. With 3 or more points she casts [A Thousand Scars], otherwise [A Thousand Springs]. She cannot act while channelling. |
| A Thousand Scars | One hit on a random enemy per Blood Sacrifice point, each 100% Reality DMG based on 25% of her Max HP; then 100% based on 50% of her Max HP to all enemies. Heals her 5% of Max HP per point spent. |
| A Thousand Springs | 500% Reality DMG to all enemies, plus 100% based on 25% of her Max HP; heals her 15% of Max HP. |
| Mouth of the Mother | Nautika loses 20% of current HP to deal 150% Reality DMG to all enemies, plus 100% based on 15% of her Max HP. |
| Higge | Max HP +2% per stack, up to 15 stacks, for 3 rounds; each new stack renews the duration. |
| Mother Spirit's Guidance | Gains 1 stack of Higge whenever attacked; Healing Taken +10%, and +5% more for each 10% of HP missing, up to +40%. |
| Adversity I | DMG Taken Reduction and DMG Bonus +10%, and +2.5% more for each 10% of Max HP missing, up to +20%. |
| Reborn | Survives one lethal attack, removes all negative effects from her and heals 30% of Max HP; then it is gone. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | Gains 1 stack of Higge after each action. |
| 2 | The team gathers Bloodtithe. On entering battle Nautika loses 50% of current HP to raise Bloodtithe and its cap by 8; her own HP-loss effects cannot take her below 15% HP. Faith replaces her Moxie: +1 whenever Bloodtithe rises, and the Ultimate opens at 8. |
| 3 | During Mother Spirit's Guidance, casts Mouth of the Mother once for every 8 Bloodtithe gained. At the start of a round without Reborn, spends 4 Bloodtithe to gain it; each later time costs 4 more. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×3; Page of Beastly Thirst ×3; Silver Ore ×6; Esoteric Bones ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×5; Scroll of Beastly Thirst ×5; Spell of Fortune ×6; Winged Key ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×8; Tome of Beastly Thirst ×8; Bogeyman ×5; Fruit of Good and Evil ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Bloodtithe and its cap rise by 16 on entering battle; Higge gives Max HP +3%; Mouth of the Mother triggers every 6 Bloodtithe. |
| 2 | Blood Sacrifice gives 3 points for every 7 Bloodtithe, at most 27; A Thousand Scars hits for 27.5% of Max HP and heals 10% per point; A Thousand Springs uses 50% of Max HP and heals 30%. |
| 3 | Mother Spirit's Guidance gives Healing Taken +20%, and +7.5% for each 10% of HP missing, up to 60%; Mouth of the Mother costs 30% of current HP and its extra damage uses 25% of Max HP. |
| 4 | Martyr of the Abyss uses 20, 30 or 50% of Max HP by rank; Weaver of Light gives DMG Taken Reduction +20, +25 or +40% for 4 rounds, and Mother Spirit's Guidance lasts 4 rounds. |
| 5 | Blood Sacrifice gives 3 points for every 6 Bloodtithe, at most 30; A Thousand Scars hits for 35% of Max HP. |

## Euphoria

Euphoria opens at Insight III level 30. Nautika has one Epiphany of four levels.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | She gains 2 stacks of Higge after each action and when attacked during Mother Spirit's Guidance; each stack of Higge also gives DMG Bonus +1%. |
| 1 | 2 | The Max HP-based damage of Haunting Pain rises to 110%; Martyr of the Abyss deals 75% for each unit on the field. |
| 1 | 3 | The Ultimate's attacks gain Ultimate Might +15% while she has both Adversity I and Mother Spirit's Guidance; the Max HP-based damage of A Thousand Scars and A Thousand Springs rises to 115%. |
| 1 | 4 | HP-loss effects cannot take her below 16% HP, and on entering battle she gives the same floor to every other Bloodtithe ally; the Max HP-based damage of Mouth of the Mother rises to 115%. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Nautika | 诺谛卡 | 諾諦卡 | ノーティカ | 노티카 |
