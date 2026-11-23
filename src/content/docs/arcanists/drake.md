---
title: "Drake"
description: "Drake is a 6-star Beast Lingering Glow arcanist who deals Mental DMG with Burn; out only on the mainland."
appliesTo: "Reverse: 1999, mainland China client 113.0.1422 (version 4.1); global client 111.0.1077 (version 3.9)"
caveat: "Drake is out only on the mainland China service: the global client 111.0.1077 does not contain him. His English skill and status names are community translations, not official ones."
lastVerified: 2026-11-22
aliases:
  - "德雷克"
  - "ドレイク"
  - "드레이크"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Drake.png"
    url: https://reverse1999.fandom.com/wiki/File:Drake.png
  - title: "Image file, uploaded 2026-10-17"
    url: https://static.wikia.nocookie.net/reverse1999/images/d/da/Drake.png/revision/latest?cb=20261017235736
sources:
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "re1999-data, mainland client 113.0.1422: skill.json and skill_effect.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/tree/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json
  - title: "re1999-data-global, global client 111.0.1077 (no entry for Drake)"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Drake, revision 101381"
    url: https://reverse1999.fandom.com/wiki/Drake?oldid=101381
  - title: "Mainland official site: version 4.1, updated 2026-11-05"
    url: https://re.bluepoch.com/
---

![Drake, full-length art](/art/characters/drake.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Mental |
| Tags | Support, Lingering Glow, DPS, Channel |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Mainland release | version 4.0 |
| Global release | not yet |

Drake stacks [Burn] on one enemy and on himself, and the team's Burn and Halo fill the shared [Lingering Glow] gauge. His Ultimate is a channel that fills Progress; at 100 Progress he enters [Rebellious Act] for a round, cashes in his own Burn for Lingering Glow and casts [Inner Flame Unleashed] each time the gauge passes a mark. His team buff [True Will] gives allies Critical DMG and a share of his DMG Bonus.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| A Flash of Wildfire (single-target attack) | 200% Mental DMG; 8 Burn stacks | 300%; 10 stacks | 500%; 12 stacks |
| The Sole Pursuit (team buff) | True Will to all allies for 2 rounds; 12 Burn stacks on Drake | 14 stacks | 16 stacks |

- **A Flash of Wildfire** also puts [Adder's Fire] on the target for 3 rounds at every rank.
- **The Sole Pursuit** burns Drake himself; his Precognition makes him immune to Burn DMG.

## Ultimate: Whither My Heart?

Drake channels, enters [Rebellious Heart] and gains Progress +20.

## Statuses

| Status | Effect |
| --- | --- |
| Lingering Glow | A team resource: it builds whenever an enemy receives Burn or Halo, faster when fewer enemies remain. A team cannot hold it together with Bloodtithe or the Pursuit Scope. |
| Burn | Healing Taken −15%, not stacking; at the end of the round, Genesis DMG of 4% of the holder's ATK. Up to 30 stacks that count as one Neg Status; half the stacks are removed each time it triggers. |
| Adder's Fire | DMG Taken Reduction −20%; each attack on the holder adds 1 more Burn stack; the holder's Burn cap rises by 15. Only one enemy has it at a time. |
| True Will | Critical DMG +48%, and DMG Bonus equal to 140% of Drake's DMG Bonus, at most 78%. Gaining it again adds to its duration. |
| Rebellious Heart | Progress starts at 0, and Drake gains no Moxie while channelling. At 100 Progress he enters Rebellious Act for 1 round at the start of the next round and sheds all Control effects. |
| Rebellious Act | Drake is immune to Control, and the team's Lingering Glow cap rises by 250. Each time the gauge passes another 200, he casts Inner Flame Unleashed after any ally's action. He cannot gain Rebellious Heart while it lasts. |
| Inner Flame Unleashed | 600% Mental DMG to all enemies, with Incantation Might +1% for each Burn stack on the target and 20% more Mental DMG for every 10 Lingering Glow. On a target with Adder's Fire, it adds 3 Burn stacks to the target and to Drake. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | The team builds Lingering Glow. At the end of each round Drake gains as many Burn stacks as the most-burned enemy lost. He takes no Burn DMG, his own Burn does not drop when it triggers and is not removed by cleansing Neg Status. If he starts a round in Rebellious Act, each of his Burn stacks turns into 4 Lingering Glow and his Burn clears. |
| 1 | At the end of the round, Progress +20 in Rebellious Heart, or one Inner Flame Unleashed in Rebellious Act. Whenever a Lingering Glow ally takes an action, Progress +15 in Rebellious Heart, otherwise Moxie +1. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | With 3 or more Lingering Glow allies on entering battle, the Ultimate costs no AP. Drake's Burn cap rises by 5 more. When a Lingering Glow ally's attack breaks a target's Afflatus Guard, the team gains 100 Lingering Glow, at most once a round. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Spell of Banishing ×6; Sharp Needle ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Liquefied Terror ×5; Jeweled Egg ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Glowing Mothwing ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Rebellious Act raises the Lingering Glow cap by 450 and casts Inner Flame Unleashed every 150; Drake's extra Burn cap becomes 30; breaking Afflatus Guard gives 185 Lingering Glow. |
| 2 | True Will gives Critical DMG +60% and 160% of his DMG Bonus, at most 90%. |
| 3 | Adder's Fire gives DMG Taken Reduction −25%, adds 2 Burn stacks per attack and raises the Burn cap by 20. |
| 4 | A Flash of Wildfire deals 240, 360 or 600% by rank; Inner Flame Unleashed deals 1000% with Incantation Might +1.2% per Burn stack. |
| 5 | Rebellious Act raises the Lingering Glow cap by 750; each Burn stack turns into 6 Lingering Glow; breaking Afflatus Guard gives 325; Inner Flame Unleashed adds 35% per 10 Lingering Glow. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Drake | 德雷克 | 德雷克 (not yet official) | not yet official | not yet official |
