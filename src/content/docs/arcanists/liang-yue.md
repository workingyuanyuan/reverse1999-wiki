---
title: "Liang Yue"
description: "Liang Yue is a 6-star Star arcanist who deals Reality DMG, grants the team Immunity and damage reduction."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Talons and Bane of All Evil work only while Arise, Qiangliang! from her Ultimate lasts; when it ends, all her talons are cleared."
lastVerified: 2026-11-22
aliases:
  - "梁月"
  - "양월"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Liang Yue.png"
    url: https://reverse1999.fandom.com/wiki/File:Liang_Yue.png
  - title: "Image file, uploaded 2025-01-17"
    url: https://static.wikia.nocookie.net/reverse1999/images/a/aa/Liang_Yue.png/revision/latest?cb=20250117081810
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Liang Yue, revision 85011"
    url: https://reverse1999.fandom.com/wiki/Liang_Yue?oldid=85011
---

![Liang Yue, full-length art](/art/characters/liang-yue.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Star |
| Damage | Reality |
| Tags | DPS, Extra Action, Immunity |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Mainland release | 2025-01-16 |
| Global release | 2025-04-24 |

Liang Yue's Ultimate puts her in [Arise, Qiangliang!], which splits the team's Spelldock into sections: cards on the right rise one rank, cards on the left make their buffs and debuffs last longer. While it lasts, each card played from those sections earns a Justice Talon or a Peace Talon, and every 6 talons she casts one of three [Bane of All Evil] attacks, chosen by which kind she holds more of. Along the way the team builds stacks of [Guardian's Resolve], a damage reduction.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Banish Evil (single-target attack) | 200% Reality DMG | 300%; Penetration Rate +30% | 500%; Penetration Rate +80% |
| Bless Life (single-ally buff) | Guardian's Blessing I, 1 round | Guardian's Blessing II | Guardian's Blessing III |

- **Banish Evil** adds 1 round to Guardian's Resolve on all allies at every rank. Played from the Spelldock during Arise, Qiangliang!, it also gives 1 extra Justice Talon.
- **Bless Life** adds 1 round to the blessing each time it is cast on the same ally. Played from the Spelldock during Arise, Qiangliang!, it also gives 1 extra Peace Talon.

## Ultimate: Call of Thunder: #0305

Deals 300% Reality DMG to all enemies. All allies gain [Immunity] for 1 round and 6 stacks of Guardian's Resolve for 2 rounds. Liang Yue gains Arise, Qiangliang! for 3 rounds; if she already has it, its duration resets to 3 rounds.

## Statuses

| Status | Effect |
| --- | --- |
| Guardian's Resolve | DMG Taken −0.8% per stack; each stack keeps its own duration; up to 30 stacks. |
| Arise, Qiangliang! | Splits the team's Spelldock. The 3 rightmost cards gain 1 rank before they take effect. The 3 leftmost cards make the Stats Up, Stats Down, Counter, Pos Status and Neg Status effects they apply last 1 round longer. Cards where the two sections overlap get both. |
| Guardian's Blessing I, II, III | DMG Dealt +25% and DMG Taken −25%. When the holder attacks, is attacked, or the round ends, Liang Yue casts Banish Evil at rank 1, 2 or 3 on the target, the attacker or the enemy with the lowest HP; each successful cast takes 1 round off the blessing. |
| Bane of All Evil · Justice | 400% Reality DMG to all enemies, counted as a rank 2 incantation; Critical Rate above the cap turns into Critical DMG. Each Justice Talon spent gives the attack Critical Rate +5%, Critical DMG +20% and DMG Dealt +10%. |
| Bane of All Evil · Peace | 400% Reality DMG to all enemies. For each Peace Talon spent, the target first receives 1 [Poison] for 1 round and 3 stacks of [Burn]. The attack gains DMG Dealt +10% for each Poison on the target and Penetration Rate +3% for each Burn stack. |
| Bane of All Evil · Balance | 200% Reality DMG to all enemies; Liang Yue gains 1 stack of Swift Resolve. |
| Swift Resolve | Bane of All Evil needs 1 talon fewer and deals 20% more Reality DMG, adding up per stack; up to 2 stacks, all used when it fires. Bane of All Evil · Balance deals a further 40% per stack on top and leaves the stacks in place. |
| Immunity | The holder is not affected by Stats Down, Neg Status or Control effects. |
| Poison | Genesis DMG at the end of the round, based on the caster's ATK; it stacks. |
| Burn | Healing Taken −15%, not stacking; at the end of the round, Genesis DMG of 4% of the holder's ATK per stack. Up to 30 stacks that count as one Neg Status; half the stacks are removed each time it triggers. |

Every Bane of All Evil gives all allies 1 stack of Guardian's Resolve for 2 rounds for each talon it spends.

## Inheritance

| Insight | Effect |
| --- | --- |
| 1 | During Arise, Qiangliang!, each card played from the right section gives 1 Justice Talon and each card from the left section 1 Peace Talon; a card from the overlap gives half of each. At 6 talons in total she spends 6 and casts Bane of All Evil: Justice if she holds more Justice Talons, Peace if more Peace Talons, Balance if they are equal. When Arise, Qiangliang! ends, her talons are cleared and each Swift Resolve stack turns into 3 stacks of Guardian's Resolve. |
| 2 | Critical Rate +10% on entering battle. |
| 3 | Moxie +3 on entering battle. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Starlit Ascent ×6; Trembling Tooth ×5; Esoteric Bones ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Starlit Ascent ×10; Cicada Wings ×6; Holy Silver ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Starlit Ascent ×16; Murmur of Insanity ×6; Fruit of Good and Evil ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Arise, Qiangliang! lasts 4 rounds, and each enhanced section covers 4 cards. |
| 2 | Liang Yue gains 5 Moxie on entering battle; Bane of All Evil needs 5 talons. |
| 3 | The Ultimate gives Immunity for 2 rounds and 12 stacks of Guardian's Resolve. |
| 4 | Banish Evil deals 240, 360 or 600% by rank, with Penetration Rate +40% at rank 2 and +100% at rank 3. Guardian's Resolve caps at 40 stacks of −1% each. |
| 5 | Bane of All Evil · Justice deals 600% and gives Critical DMG +30% per Justice Talon; Bane of All Evil · Peace deals 600% and gives DMG Dealt +20% per Poison; Bane of All Evil · Balance deals 300%, Swift Resolve caps at 3 stacks, and Balance's extra damage per stack becomes 80%. |

## Euphoria

Euphoria opens at Insight III level 30. Liang Yue has one Epiphany of four levels.

| Epiphany | Level | Change |
| --- | --- | --- |
| 1 | 1 | Each time another ally takes an extra action, Liang Yue gains 1 stack of [Ritual Dance] for 2 rounds, at most 5 times a round. Guardian's Resolve also gives DMG Dealt equal to its DMG Taken reduction, and attacks that use Incantation Might gain extra Incantation Might equal to 50% of that reduction. The effects that the left section of Arise, Qiangliang! extends now include [Force Field]. |
| 1 | 2 | Bane of All Evil · Justice counts Peace Talons as Justice Talons, and each one spent gives the attack ATK +0.5%. Bane of All Evil · Peace counts Justice Talons as Peace Talons, and each one spent first puts 1 stack of [Evil Expelled] on the targets for 1 round. Bane of All Evil · Balance gains Incantation Might +2% per talon spent. Every Bane of All Evil gains Incantation Might +5% per stack of Swift Resolve. |
| 1 | 3 | The Ultimate deals an extra 600% Reality DMG. During Arise, Qiangliang!, casting Banish Evil or Bless Life gives Liang Yue 1 stack of Ritual Dance for 2 rounds. |
| 1 | 4 | Liang Yue no longer receives the Ultimate card: at the start of a round with 5 Moxie she casts it automatically. Cast during Arise, Qiangliang!, it gives all allies 1 more round of Immunity and Guardian's Resolve, gives her 2 stacks of Swift Resolve and has Ultimate Might +100%. During Arise, Qiangliang!, Banish Evil and Bane of All Evil deal extra Reality DMG equal to the base duration of Arise, Qiangliang! times 15% of their base Reality DMG. At 4 stacks of Ritual Dance, Banish Evil played from the Spelldock counts as an extra action; at 8 stacks, the Ritual Dance bonus doubles and Banish Evil and Bane of All Evil take a further 40% of the effect of Incantation Might. |

- **Ritual Dance**: each stack makes Banish Evil and Bane of All Evil deal extra Reality DMG equal to 5% of their base Reality DMG; up to 8 stacks, each with its own duration.
- **Evil Expelled**: DMG Taken Reduction −2%; it stacks.
- **Force Field**: an effect that its holder grants to chosen characters on the field; it ends when the holder leaves.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Liang Yue | 梁月 | 梁月 | 梁月 | 양월 |
