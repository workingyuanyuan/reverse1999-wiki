---
title: "Isolde"
description: "Isolde is a 6-star Spirit arcanist who deals Reality DMG by stacking Burn and setting off follow-up attacks."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Isolde casts Intermezzo by herself only in Interlude or Finale, when the enemy with the most Burn has 6 or more stacks; in Prelude, before 15 Heat, it comes only from her Ultimate."
lastVerified: 2026-11-22
aliases:
  - "伊索爾德"
  - "伊索尔德"
  - "イゾルデ"
  - "이졸데"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Isolde.png"
    url: https://reverse1999.fandom.com/wiki/File:Isolde.png
  - title: "Image file, uploaded 2024-03-03"
    url: https://static.wikia.nocookie.net/reverse1999/images/1/15/Isolde.png/revision/latest?cb=20240303195744
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Isolde, revision 85004"
    url: https://reverse1999.fandom.com/wiki/Isolde?oldid=85004
---

![Isolde, full-length art](/art/characters/isolde.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Spirit |
| Damage | Reality |
| Tags | DPS, Burn, Support |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Mainland release | 2024-02-22 |
| Global release | in the global client |

Isolde spreads [Burn] across the enemy team and turns it into [Heat]: Burn that runs out on the most-burned enemy each round becomes Heat, and Heat moves her through three stages, [Prelude], [Interlude] and [Finale]. From Interlude on, she casts [Intermezzo] at all enemies whenever one of them carries 6 or more stacks of Burn, and it deals more for every stack.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Twirling Melody (attack on 2 enemies) | 150% Reality DMG; Burn 2 stacks | 225%; Burn 2 stacks | 300%; Burn 2 stacks |
| Desired Freedom (mass debuff) | Critical DEF −25%, Reality DEF −15%; 2 rounds | −35%, −15%; 2 rounds | −50%, −15%; 2 rounds |

- **Twirling Melody** gains Penetration Rate +30% in Interlude and +50% in Finale.
- **Desired Freedom** lowers Reality DEF by 20% instead of 15% on a target that has Burn.
- [Burn]: Healing Taken −15%, which does not stack. At the end of the round, Genesis DMG of 4% of the holder's ATK per stack, up to 30 stacks; any number of stacks counts as one Neg Status, and half the stacks are removed each time it deals damage.

## Ultimate: Choking on Blood

Puts 5 stacks of Burn on all enemies and 5 more on the main target, and gives all allies 1 stack of [Rousing Morale]. Then she casts Intermezzo at the targets as a follow-up; each stack of Burn the Ultimate puts on the main target beyond its limit gives this Intermezzo Incantation Might +15%.

## Statuses

| Status | Effect |
| --- | --- |
| Heat | Gained from Burn stacks that resolve. 15 Heat move Isolde from Prelude to Interlude, 40 from Interlude to Finale. |
| Prelude | At the start of each round, all allies gain 3 stacks of [Preignition]. Cannot be dispelled. |
| Interlude | As Prelude; also, when the enemy with the most Burn has 6 or more stacks, Isolde casts Intermezzo. Cannot be dispelled. |
| Finale | As Interlude, and all allies also gain 1 stack of [Power Burst] each round; its Intermezzo has Incantation Might +15%. Cannot be dispelled. |
| Intermezzo | 50% Reality DMG to all enemies, plus 10% Reality DMG for each stack of Burn on the target. |
| Preignition | Before its holder attacks, puts 1 stack of Burn on the target for each stack; then all stacks are removed. |
| Rousing Morale | DMG Bonus +50% on an attack; 1 stack is used each time. |
| Power Burst | DMG Bonus +25% on an attack; 1 stack is used each time. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | On entering battle, Isolde enters Prelude and puts 3 stacks of Burn on all enemies. At the end of each round, she gains as much Heat as the Burn stacks the most-burned enemy loses. At 15 Heat, Prelude becomes Interlude. |
| 2 | ATK +5% on entering battle. |
| 3 | At 40 Heat, Interlude becomes Finale. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×3; Page of Beastly Thirst ×3; Silver Ore ×6; Milled Magnesia ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×5; Scroll of Beastly Thirst ×5; Esoteric Bones ×6; Golden Beetle ×3 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×8; Tome of Beastly Thirst ×8; Murmur of Insanity ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Intermezzo deals 13% more Reality DMG for each stack of Burn. |
| 2 | Interlude needs 10 Heat and Finale 30. |
| 3 | Intermezzo deals 16% more for each stack of Burn. |
| 4 | Twirling Melody deals 200, 300 or 400% by rank. |
| 5 | Intermezzo deals 20% more for each stack of Burn. |

## Euphoria

Euphoria opens at Insight III level 30. Isolde has one Epiphany of four levels, built on a gauge of [Lingering Glow].

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Lingering Glow builds whenever any enemy receives Burn or [Halo]. Desired Freedom lowers both Reality DEF and Mental DEF. |
| 1 | 2 | The Ultimate no longer gives Rousing Morale, and Finale no longer gives Power Burst. Instead, at the start of each round, Interlude gives all allies [Acciaccatura] for 1 round, and Finale gives them [Appoggiatura] for 1 round. |
| 1 | 3 | Intermezzo gains Incantation Might +1.5% for each stack of Burn on the target, counting up to 30 stacks. With at least 100, 200 or 300 Lingering Glow it gains Incantation Might +10, 20 or 30% more, and at 300 or more also Penetration Rate +30%. |
| 1 | 4 | Intermezzo deals 2% more Reality DMG for each point of Lingering Glow, and with at least 150 points it gives Isolde 1 Moxie. In Prelude, Interlude and Finale, 5, 10 and 15% of the Lingering Glow lost at the start of a round comes back after the next Intermezzo. |

- **Lingering Glow**: builds when any enemy receives Burn or Halo; the fewer enemies there are, the more it builds. It cannot be held together with Bloodtithe or the Pursuit Scope; the global client's text names Bloodtithe only.
- **Halo**: Healing Taken −25%, which does not stack. At the end of the round, Genesis DMG of 4% of the ATK of the arcanist who applied it per stack, up to 30 stacks; any number of stacks counts as one Neg Status, and half the stacks are removed each time it deals damage.
- **Acciaccatura**: DMG Dealt +18%.
- **Appoggiatura**: DMG Dealt +18%, plus 0.3% for each point of Lingering Glow, counting up to 300 points.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Isolde | 伊索尔德 | 伊索爾德 | イゾルデ | 이졸데 |
