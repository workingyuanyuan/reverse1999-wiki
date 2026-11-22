---
title: "Hedone"
description: "Hedone is a 6-star Mineral arcanist who deals Reality DMG through a Conduit and recycles unused Energy cards."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Hedone draws no incantation cards and has no incantation ranks: her Conduit casts with Energy, and Flame Undying stays locked until it has smelted at least 1 Energy."
lastVerified: 2026-11-22
aliases:
  - "赫多涅"
  - "ヘドネ"
  - "헤도네"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Hedone.png"
    url: https://reverse1999.fandom.com/wiki/File:Hedone.png
  - title: "Image file, uploaded 2026-09-01"
    url: https://static.wikia.nocookie.net/reverse1999/images/c/c1/Hedone.png/revision/latest?cb=20260901184350
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Hedone, revision 108711"
    url: https://reverse1999.fandom.com/wiki/Hedone?oldid=108711
---

![Hedone, full-length art](/art/characters/hedone.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Mineral |
| Damage | Reality |
| Tags | Support, Conduit, DPS |
| Mainland release | 2026-08-13 |
| Global release | 2026-11-05 |

Hedone is a Conduit arcanist: instead of incantation cards she brings a Conduit and Energy cards, and Harmonization takes the place of Moxie. Her Flame Undying card turns Energy cards left unused at the end of a round into stored Energy, and each time it smelts, she gains Blazing Glory, which raises the Conduit Might and DMG Bonus of the whole team. Her Ultimate adds Genesis DMG based on the damage the team's incantations dealt over the last 4 rounds.

## Incantations

Hedone's Conduit holds one of two incantations at a time; they have no ranks, and both carry Interval.

| Incantation | Effect |
| --- | --- |
| Forged in Glory (single-target attack) | 500% Reality DMG; while Hedone has [Blazing Glory], 500% more Reality DMG and Mineral Energy +2 |
| At Full Draw (mass attack) | 350% Reality DMG to all enemies, then [Seared] for 4 rounds |

- [Conduit]: charged with Energy; at the end of the AP Area it runs and casts its incantation, spending Energy each time.
- [Interval]: after the Conduit casts this incantation, it cannot cast it again that round.
- [Seared]: an attack from a Conduit on the holder gains DMG Dealt +8%.
- [Blazing Glory]: a [Force Field] effect that gives all allies Conduit Might +10% and DMG Bonus equal to 100% of Hedone's Conduit Might, at most 65%. A Force Field ends when its holder leaves the field.

## Ultimate: The Thirteenth Labor

When Harmonization is full, the Conduit switches to the Ultimate. It deals 800% Reality DMG to all enemies, plus [Static Genesis DMG] equal to 100% of the [Absolute Prowess] record to the main target and 50% of it to every other target. If the Spelldock holds no [Flame Undying], the attack creates one there; if it holds one, the attack deals 800% more Reality DMG. Afterwards Hedone gains 1 stack of [Conduit Calibration II], the Absolute Prowess record is cleared, and the Conduit switches to At Full Draw.

- [Absolute Prowess]: records 10% of the damage that allied incantations dealt to enemies over the last 4 rounds, and 10% more for damage to a target with Seared.
- [Static Genesis DMG]: Genesis DMG that stat bonuses do not change.
- [Flame Undying]: at the end of each round, smelts up to 2 unused basic Energy cards in the Spelldock, those with the least Energy first, and stores 1 Energy for each Energy they held. It stops smelting after 4 Energy and stores at most 7. Played, it gives Mineral Energy equal to what it stores. It is locked until it has stored at least 1 Energy, does not count toward the Incantation Limit and costs no AP.
- [Conduit Calibration II]: the holder's Conduit needs 2 Energy less to activate; one stack is used each time.

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Hedone gets no basic incantations or Ultimate cards and casts through her Conduit; Harmonization replaces Moxie. On entering battle, she puts a Flame Undying in the Spelldock and gains Absolute Prowess. |
| 1 | Each time Flame Undying smelts Energy, Hedone gains Blazing Glory for 3 rounds. The Flame Undying from the start of battle begins with 2 stored Energy. |
| 2 | DMG Dealt +8% on entering battle. |
| 3 | Harmonization +75 on entering battle. Each time an ally's Conduit activates, Hedone gains Harmonization +1 for every Energy it spends. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×6; Spell of Banishing ×6; Solidus ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×10; Cicada Wings ×6; Winged Key ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×16; Silver Bullet ×6; Fruit of Good and Evil ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Flame Undying smelts up to 3 cards, stops after 6 Energy and stores at most 10; the one from the start of battle begins with 4. Forged in Glory and At Full Draw give Harmonization +30. One Mineral Energy I in the deck gives 2 Energy. |
| 2 | Harmonization +100 on entering battle; Blazing Glory gives Conduit Might +20% and DMG Bonus up to 75%. Two Mineral Energy I in the deck give 2 Energy. |
| 3 | Forged in Glory deals 800%, and gives Mineral Energy +3 while Hedone has Blazing Glory. |
| 4 | The Ultimate deals 1200%; Seared gives a Conduit attack DMG Dealt +16%. |
| 5 | Flame Undying stores 2 Energy for each Energy smelted, stops after 8 and stores at most 12; the one from the start of battle begins with 6. Absolute Prowess records 18%, and 18% more against Seared targets. Two Mineral Energy II in the deck give 3 Energy. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Hedone | 赫多涅 | 赫多涅 | ヘドネ | 헤도네 |
