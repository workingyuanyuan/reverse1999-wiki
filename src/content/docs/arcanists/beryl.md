---
title: "Beryl"
description: "Beryl is a 6-star Intellect arcanist who deals Mental DMG, spreads Halo and casts the follow-up Destined Doom."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Beryl's Euphoria is out only on the mainland China service; the global client 111.0.1077 does not have it, and the name Foresight in it is a translation, not an official one."
lastVerified: 2026-11-22
aliases:
  - "貝麗爾"
  - "贝丽尔"
  - "ベリル"
  - "베릴"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Beryl.png"
    url: https://reverse1999.fandom.com/wiki/File:Beryl.png
  - title: "Image file, uploaded 2026-01-29"
    url: https://static.wikia.nocookie.net/reverse1999/images/9/98/Beryl.png/revision/latest?cb=20260129135005
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Beryl, revision 97396"
    url: https://reverse1999.fandom.com/wiki/Beryl?oldid=97396
---

![Beryl, full-length art](/art/characters/beryl.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Intellect |
| Damage | Mental |
| Tags | DPS, Lingering Glow, Extra Action, Rank Up |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Mainland release | 2025-10-30 |
| Global release | 2026-01-20 |

Beryl spreads [Halo] over the enemy team, and every stack of Halo or Burn that lands adds to the team's [Lingering Glow]. Each time Lingering Glow grows by 150, she casts the follow-up attack [Destined Doom] after the next allied action. At the start of battle she picks Emanation crystals of three colours, which decide what her passive aura, her generated cards and Destined Doom add.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Blaze Through the Lens (single-target attack) | 200% Mental DMG; 4 stacks of Halo | 300%; 6 stacks | 500%; 10 stacks |
| Nothing Unexpected (self buff) | 3 stacks of Vision | 5 stacks | 8 stacks |

Blaze Through the Lens puts the Halo in the table on its target when the target has fewer than 20 stacks or is the only enemy. Otherwise it gives each other enemy Halo equal to 50% of the target's stacks.

## Ultimate: A Shimmering Night

Before the hit, the Halo stacks on all enemies are redistributed by their current HP, up to Halo's stack limit. Then it deals 600% Mental DMG to all enemies.

## Statuses

| Status | Effect |
| --- | --- |
| Halo | Healing Taken −25%. At the end of the round, Genesis DMG based on 4% of the original inflicter's ATK. Stacks up to 30 and counts as one Neg Status; half the stacks are removed each time it deals damage. |
| Lingering Glow | A team count that grows whenever an enemy receives Burn or Halo, faster when fewer enemies remain. It cannot coexist with Bloodtithe or the Pursuit Scope. |
| Vision | While Beryl has it, Destined Doom needs 50 less Lingering Glow; each Destined Doom removes one stack. The reduction does not stack, and it cannot be dispelled. |
| Destined Doom | A follow-up attack: 500% Mental DMG to all enemies and 500% more to the enemy with the most Halo. Each Vision stack gives it Incantation Might +1%, counting up to 20 stacks. |
| Destined Doom · Emanation of Blue | A follow-up attack: 100% Mental DMG to all enemies and 100% more to the enemy with the most Halo, plus 120% to both for each Blue crystal; Vision adds Incantation Might as above. Only Blue crystals affect it. |
| Mirrored from Above | A Force Field: an effect its holder grants, which ends when the holder leaves the field. |
| Clairvoyant Prism | A generated card of rank 1, 2 or 3 at 40%, 50% and 10%. Each crystal picked lowers the rank 1 chance by 10% and raises the rank 3 chance by 10%; its colour follows the share of each colour picked. It is a Sovereign Incantation: casting it counts as Beryl's own action. |

## Emanation crystals

On entering battle, while the team has Lingering Glow, Beryl picks 2 crystals, at most 2 of one colour. Each crystal adds its effect again.

| Crystal | Mirrored from Above | Clairvoyant Prism card | Destined Doom |
| --- | --- | --- | --- |
| Blue | an extra-action attack puts 1 stack of Halo on the target | adds 30, 45 or 75 to the count toward Destined Doom, by rank | +33% chance of one extra Destined Doom · Emanation of Blue |
| Purple | an active attack puts 2 stacks of Halo on the target | Beryl gains 2, 3 or 5 stacks of Vision, by rank | 2 more stacks of Halo; +0.4% Mental DMG per point of Lingering Glow, also on the enemy with the most Halo |
| Green | a rank 2 or rank 3 incantation puts 1 or 2 stacks of Halo on the target | before the AP area resolves, raises the 1, 2 or 3 cards behind it by one rank | the attack has a rank, raised by 1; +80, 120 or 150% Mental DMG at rank 1, 2 or 3, also on the enemy with the most Halo |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Enemies receiving Burn or Halo build Lingering Glow. On entering battle, Beryl picks her Emanation crystals. For every 150 Lingering Glow gained, she casts Destined Doom once after any allied action. |
| 1 | Gains Mirrored from Above on entering battle. From round 2, at the start of each round, she creates one Precast Clairvoyant Prism. |
| 2 | Critical Rate +10% on entering battle. |
| 3 | On entering battle, gains 1 Moxie and adds 20 to Lingering Glow. At the end of each round with 60 or more Lingering Glow, gains 1 Moxie. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×3; Page of Starlit Ascent ×3; Silver Ore ×6; Liquefied Terror ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×5; Scroll of Starlit Ascent ×5; Esoteric Bones ×6; Prophetic Bird ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×8; Tome of Starlit Ascent ×8; Watch Core ×6; Golden Fleece ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Destined Doom needs 125 Lingering Glow. |
| 2 | Beryl picks 3 crystals; Halo stacks up to 35. |
| 3 | Gains 3 Moxie on entering battle. Destined Doom · Emanation of Blue deals 125%, plus 150% per Blue crystal; the Purple bonus becomes 0.5% per point of Lingering Glow; the Green bonus becomes 100, 150 or 187.5% by rank. |
| 4 | Blaze Through the Lens deals 300, 450 or 750% and puts 6, 9 or 15 stacks of Halo by rank; Nothing Unexpected gives 4, 6 or 10 stacks of Vision. |
| 5 | Beryl picks 4 crystals, at most 3 of one colour; Halo stacks up to 40. |

## Euphoria

Euphoria opens at Insight III level 30 and is out only on the mainland China service. Beryl has one Epiphany of four levels; it adds the status [Foresight]: at the end of each round, Beryl gains as many stacks of Vision as rank 1 Nothing Unexpected gives (3 stacks).

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Nothing Unexpected gives twice its Vision and Foresight for 2 rounds. |
| 1 | 2 | Each Clairvoyant Prism card can also spend 3 stacks of Vision, once, twice or three times by its rank 1, 2 or 3, for a bonus to Destined Doom that round; each use gives Beryl 1 Moxie at the end of the round. Blue: Destined Doom deals 35% of its base more (175%; 35% for the Blue version). Purple: Foresight lasts 1, 1 or 2 rounds longer by rank, and Destined Doom deals the per-point Lingering Glow bonus once more (0.4% per point). Green: Destined Doom deals 150% of its rank bonus more (120, 180 or 225% by rank). |
| 1 | 3 | The Ultimate deals 100% of its base damage more, scales with 100% of Incantation Might, deals 2% more Mental DMG per point of Lingering Glow and gives Beryl 10 stacks of Vision after the hit. She also gains 10 stacks of Vision on entering battle. |
| 1 | 4 | Destined Doom deals 20% of its base damage more (600%), and each Vision stack raises the attack's ATK by 0.2%, counting up to 20 stacks. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Beryl | 贝丽尔 | 貝麗爾 | ベリル | 베릴 |
