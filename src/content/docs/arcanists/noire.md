---
title: "Noire"
description: "Noire is a 6-star Plant arcanist who deals Mental DMG; her Ultimate grows with the Neg Status on enemies."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Noire's Euphoria takes away the random recast of her Ultimate: Genius Idea then becomes stacks of Endless Inspiration, gained at the start of a round only while she has 5 Moxie."
lastVerified: 2026-11-22
aliases:
  - "菲林士多"
  - "ノワール"
  - "누아르"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Noire.png"
    url: https://reverse1999.fandom.com/wiki/File:Noire.png
  - title: "Image file, uploaded 2025-01-17"
    url: https://static.wikia.nocookie.net/reverse1999/images/6/67/Noire.png/revision/latest?cb=20250117081953
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Noire, revision 85037"
    url: https://reverse1999.fandom.com/wiki/Noire?oldid=85037
---

![Noire, full-length art](/art/characters/noire.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Plant |
| Damage | Mental |
| Tags | DPS, Ritual, Control |
| Mainland release | 2025-02-06 |
| Global release | 2025-05-08 |

Noire marks one enemy with [Spotlight] each round; her attacks on it leave a random Neg Status, and each new Spotlight gives her Moxie and stacks of [Genius Idea]. Her Ultimate hits all enemies, gains damage and Penetration Rate from the Neg Status they carry, and may cast itself again for each stack of Genius Idea she holds.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Experimental Montage (single-target attack) | 200% Mental DMG | 300% | 500% |
| Stunt Take (attack on 2 enemies) | 120% Mental DMG; Genius Idea 4 stacks; Spotlight effect 1 extra time | 180%; 5 stacks; 2 extra times | 300%; 6 stacks; 3 extra times |

- **Experimental Montage** first moves every Neg Status effect of the other enemies onto its target, then attacks.
- **Stunt Take** gives Noire its Genius Idea stacks after the attack.
- [Spotlight]: after Noire attacks its holder, the holder gets one of these at random: 1 stack of [Rigidity], [Poison] for 2 rounds, or 5 stacks of [Burn].

## Ultimate: Climactic Moment

Deals 450% Mental DMG to all enemies. Against each target, every kind of Neg Status adds 100% Mental DMG and every stack adds Penetration Rate +3%, up to +500% and +30%. Each stack of Genius Idea gives a 6% chance that the Ultimate casts itself once more, and 8 stacks add 40% to the chance; each recast spends 5 stacks.

- [Genius Idea]: gives the Ultimate its chance to be cast again; the chance rises with the stacks.
- [Rigidity]: at 2 stacks it turns into Petrify, or adds 1 round to a Petrify already there.
- [Poison]: at the end of the round, Genesis DMG based on the ATK of the arcanist who applied it; it stacks.
- [Burn]: Healing Taken −15%, which does not stack. At the end of the round, Genesis DMG of 4% of the holder's ATK per stack, up to 30 stacks; any number of stacks counts as one Neg Status, and half the stacks are removed each time it deals damage.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | At the start of each round, puts Spotlight on the enemy with the highest share of its HP left, for 1 round. |
| 2 | ATK +5% on entering battle. |
| 3 | Whenever another unit gets Spotlight, Noire gains 1 Moxie and 2 stacks of Genius Idea, up to 10 stacks. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×6; Magnesia Crystal ×6; Spell of Fortune ×6 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×10; Rough Silver Ingot ×4; Winged Key ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×16; Goldbell Spirit Bottle ×6; Serpent Scepter ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Each stack of Genius Idea gives a 10% recast chance. |
| 2 | A recast spends 4 stacks of Genius Idea. |
| 3 | Genius Idea stacks up to 12. |
| 4 | Each kind of Neg Status adds 120% Mental DMG and each stack Penetration Rate +4%, up to +600% and +40%. |
| 5 | The Ultimate deals 550% Mental DMG. |

## Euphoria

Euphoria opens at Insight III level 30. Noire has one Epiphany of four levels, which reworks her Ultimate.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Genius Idea no longer gives a recast chance. At the start of a round, if Noire has 5 Moxie and at least as many Genius Idea stacks as a recast used to spend, she spends them and gains 1 stack of [Endless Inspiration], once a round; each Genius Idea stack she holds also gives the old base chance (6%, or 10% from Portrait 1) of 1 more stack. Endless Inspiration stacks up to 4; at the cap, no Genius Idea is spent. |
| 1 | 2 | Her passives gain: Moxie +3 on entering battle, and 1 stack of [Scene Direction] whenever another ally casts an Ultimate, up to the stack limit Genius Idea had before (10, or 12 from Portrait 3). |
| 1 | 3 | The Ultimate costs no action point and adds Mental DMG equal to 100% of its base Mental DMG. Its Penetration Rate bonus counts kinds of Neg Status instead of stacks, and the cap of its extra Mental DMG from Neg Status doubles. At base this is 900% Mental DMG, with +100% and Penetration Rate +3% per kind, up to +1000% and +30%. |
| 1 | 4 | If the Ultimate is recast once in a round, it adds 450% Mental DMG to all enemies; if twice, 450% plus 50% Mental DMG and Penetration Rate +1.5% per kind of Neg Status, up to +500% and +15%; if three or more times, 900% plus 100% and Penetration Rate +3% per kind, up to +1000% and +30%. |

- **Endless Inspiration**: each stack casts the Ultimate one more time when Noire casts it; up to 4 stacks, all removed after the Ultimate.
- **Scene Direction**: when Noire casts Climactic Moment, the attack gains Critical Rate +6% and benefits from Ultimate Might at a +12% rate. It cannot be dispelled and is removed at the end of the round in which she casts it.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Noire | 菲林士多 | 菲林士多 | ノワール | 누아르 |
