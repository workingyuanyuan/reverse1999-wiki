---
title: "Ezio Auditore"
description: "Ezio Auditore is a 6-star Star arcanist who deals Reality DMG with Assassination attacks and counters."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Ezio's Ultimate cannot be cast by hand: it fires by itself at the start of a round once his Synchronization, which replaces Moxie, reaches 100%."
lastVerified: 2026-11-22
aliases:
  - "埃齊歐·奧迪托雷"
  - "艾吉奥·奥迪托雷"
  - "エツィオ"
  - "에지오 아디토레"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Ezio Auditore.png"
    url: https://reverse1999.fandom.com/wiki/File:Ezio_Auditore.png
  - title: "Image file, uploaded 2025-08-08"
    url: https://static.wikia.nocookie.net/reverse1999/images/0/08/Ezio_Auditore.png/revision/latest?cb=20250808055453
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Ezio Auditore, revision 84988"
    url: https://reverse1999.fandom.com/wiki/Ezio_Auditore?oldid=84988
---

![Ezio Auditore, full-length art](/art/characters/ezio-auditore.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Star |
| Damage | Reality |
| Tags | DPS, Poison, Ritual, Extra Action, Assassination |
| Resonance Patterns | [Cross-shaped set](/systems/resonance/): Elucidation, Genuinity, Stupefaction, Aspirational, Hyperphrenia |
| Psychubes recommended in game | [As the Bell Tolls](/psychubes/as-the-bell-tolls/) |
| Mainland release | 2025-08-07 |
| Global release | 2025-08-07 |

Ezio's attacks count as [Assassination]: they gain Final DMG Dealt for every 100 points by which his Critical Technique exceeds the target's. He fills Synchronization by assassinating, by countering marked enemies and by defeating enemies, and his Ultimate then strikes one chosen enemy several times. He fights with one weapon and one small weapon, whose effects Portrait 2 and 5 strengthen.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Work in the Dark (single-target attack) | 400% Reality DMG | 600% | 1000% |
| Serve the Light (self counter) | [Eyes Caught] on one enemy and [Fighting Experience] on Ezio, 1 round | 2 rounds | 3 rounds |

- **Work in the Dark** counts as an Assassination at every rank.
- **Serve the Light** marks the enemy with the most attack incantations queued.

## Ultimate: Branding of Faith

Ezio picks one enemy and hits it 3 times, each time with [Arrow of Faith] or [Edge of Faith], then finishes with [Death Be Not Unkind]. Enemy effects cannot redirect these attacks.

## Statuses

| Status | Effect |
| --- | --- |
| Assassination | The attack gains Final DMG Dealt +5% for every 100 points of Critical Technique the attacker has above the target. |
| Eyes Caught | The enemy turns its attention to Ezio: some attacks on the team go to him first. |
| Fighting Experience | Whenever an ally is attacked, Ezio answers with [Counter Kill]. Gaining it again adds to its duration; it cannot be dispelled. |
| Counter Kill | 500% Reality DMG, with Critical DMG +50% when Ezio himself was attacked; 500% when only other allies were. Counts as an Assassination. |
| Arrow of Faith | Single-target attack: 100% Reality DMG, and 50% more if the target is below 50% HP. |
| Edge of Faith | Single-target attack: 100% Reality DMG, and 50% more if the target is at 50% HP or above. |
| Death Be Not Unkind | Single-target attack: 700% Reality DMG. |
| Shadowstalk | Critical DMG +30%, DMG Taken Reduction +40%. |
| Apprentice Assassin | At 8 stacks it turns into [Master Assassin]. Other allies also gain Master Assassin: Assassination arcanists at 70% of Ezio's effect, the rest at 50%. |
| Master Assassin | Assassinations gain a further Final DMG Dealt +6% for every 100 points of Critical Technique above the target. |
| Assassin Mark | When another ally actively casts an incantation on the holder, Ezio spends 1 stack to cast rank 1 Work in the Dark on it as a follow-up attack, which adds no mark. Up to 5 stacks. |
| Eagle's Guidance | Spent during the Ultimate: every 2 stacks add one more Arrow of Faith or Edge of Faith. Up to 6 stacks. |
| Poison | Genesis DMG at the end of each round, based on the inflicter's ATK; stacks. |

Arrow of Faith, Edge of Faith and Death Be Not Unkind all count as Assassinations, ignore Dodge and trigger neither DMG sharing nor additional DMG.

## Weapons

Ezio carries one weapon (Venetian Falchion, Condottiero War Hammer or Captain's Sword) and one small weapon (Channeled Cinquedea, Butcher Knife or Sultan's Knife). Portrait 2 strengthens each weapon:

| Weapon | Portrait 2 |
| --- | --- |
| Venetian Falchion | Puts 2 stacks of [Assassin Mark] on the target. |
| Condottiero War Hammer | Ezio gains 2 stacks of [Eagle's Guidance] after another ally's Ultimate; in his Ultimate, each Arrow of Faith, Edge of Faith or Death Be Not Unkind adds Final DMG Dealt +2.5%. |
| Captain's Sword | Incantation and Ultimate attacks add Genesis DMG of 80% of the base Reality DMG of rank 1 Work in the Dark or of Death Be Not Unkind, plus 1.5% of it for each Poison on the target, or 2.5% when the target has 10 or more. |

Portrait 5 strengthens each pairing:

| Weapon | Small weapon | Portrait 5 |
| --- | --- | --- |
| Venetian Falchion | Channeled Cinquedea | Extra actions gain DMG Bonus +100%; excess Critical Rate becomes Critical DMG at 150%. |
| Venetian Falchion | Butcher Knife | Extra actions gain DMG Bonus +100%; enemies leaving the field trigger Work in the Dark up to 4 times a round. |
| Venetian Falchion | Sultan's Knife | Extra actions gain DMG Bonus +100%; the duration bonus of Fighting Experience and Eyes Caught becomes 2 rounds (in the global client: they last 2 rounds). |
| Condottiero War Hammer | Channeled Cinquedea | Ultimate Might +40%; Synchronization +20% at the start of each round. |
| Condottiero War Hammer | Butcher Knife | Ultimate Might +40%; Synchronization +20% after the Ultimate. |
| Condottiero War Hammer | Sultan's Knife | Ultimate Might +40%; Synchronization +20% when an enemy leaves the field after an ally's action. |
| Captain's Sword | Channeled Cinquedea | Genesis DMG +20%; 2 more Poison. |
| Captain's Sword | Butcher Knife | Genesis DMG +20%; 3 more Poison. |
| Captain's Sword | Sultan's Knife | Genesis DMG +20%; when an enemy leaves the field, its allies take over up to 20 of its Poison. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Synchronization replaces Moxie; at 100% the Ultimate fires at the start of the round, and there is no other way to cast it. Synchronization +5% when an incantation triggers an Assassination, +5% when Counter Kill hits an enemy with Eyes Caught, +10% when he defeats the target of his attack. |
| 1 | DMG Taken −15% when attacked during Fighting Experience, and −30% more if the attacker has Eyes Caught. |
| 2 | Critical DMG +15% on entering battle. |
| 3 | When an attack leaves Ezio below 30% HP, Eyes Caught is removed from all enemies and he enters [Shadowstalk] for 1 round, at most once a round. Each Assassination by any ally gives him 1 stack of [Apprentice Assassin]. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Starlit Ascent ×6; Trembling Tooth ×5; Esoteric Bones ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Starlit Ascent ×10; Cicada Wings ×6; Prophetic Bird ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Starlit Ascent ×16; Silver Bullet ×6; Fruit of Good and Evil ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Master Assassin gives +10% per 100 Critical Technique; the Ultimate casts Arrow of Faith or Edge of Faith up to 4 times. |
| 2 | Each weapon's effect is strengthened (see Weapons). |
| 3 | Master Assassin gives +11%; Work in the Dark deals 460, 675 or 1125% by rank; Arrow of Faith and Edge of Faith deal 140%. |
| 4 | Master Assassin gives +12%; Counter Kill deals 600% in both cases; Death Be Not Unkind deals 900%. |
| 5 | Each pairing of weapon and small weapon is strengthened (see Weapons). |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Ezio Auditore | 艾吉奥·奥迪托雷 | 埃齊歐·奧迪托雷 | エツィオ | 에지오 아디토레 |
