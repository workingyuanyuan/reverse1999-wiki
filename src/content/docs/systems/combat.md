---
title: "Combat basics"
description: "Reverse: 1999 combat: incantation cards each round, three damage types, a 5-Moxie Ultimate for most arcanists."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Afflatus advantage works in two separate groups: the cycle Beast, Plant, Star, Mineral, and the pair Spirit and Intellect; an attack with the advantage deals 30% more damage."
lastVerified: 2026-11-23
aliases:
  - "戰鬥基礎"
  - "战斗基础"
  - "バトルの基本"
  - "전투 기본"
  - "Afflatus advantage"
  - "靈感克制"
  - "灵感克制"
  - "Moxie"
  - "激情"
  - "Genesis DMG"
  - "本源創傷"
  - "本源创伤"
sources:
  - title: "re1999-data-global, global client 111.0.1077: loading_text.json (Field Manual tips)"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/loading_text.json
  - title: "re1999-data-global, global client 111.0.1077: English text (Afflatus relations, keys language_10030417 to language_10030420)"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json (Ultimate cost), character_attribute.json (stats), loading_text.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/tree/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json
  - title: "Reverse: 1999 Wiki (Fandom), Damage, revision 53347"
    url: https://reverse1999.fandom.com/wiki/Damage?oldid=53347
  - title: "Reverse: 1999 Wiki (Fandom), Moxie, revision 31417"
    url: https://reverse1999.fandom.com/wiki/Moxie?oldid=31417
---
## Rounds

A battle in Reverse: 1999 is fought in rounds. Each round the team gets a hand of incantation cards and a number of actions (AP) to spend on them; the enemies act on their own AP. Damage depends on the Afflatus of attacker and target, the damage type and the stats below.

## Afflatus advantage

| Group | Has the advantage over |
| --- | --- |
| Beast | Plant |
| Plant | Star |
| Star | Mineral |
| Mineral | Beast |
| Spirit and Intellect | a relation of their own (Spirit & Intellect Relation) |

The game calls the first group Natural Relations. An attack on an enemy whose Afflatus is weaker deals 30% more damage, in both groups. The bonus is separate from DMG Bonus.

## Damage types

| Type | What reduces it |
| --- | --- |
| Reality DMG | the target's Reality DEF |
| Mental DMG | the target's Mental DEF |
| Genesis DMG | nothing: fixed damage that ignores all DEF and damage reduction, and gains from almost no DMG Bonus |

Each arcanist deals Reality or Mental DMG; Genesis DMG comes from statuses such as Burn and Poison and from some skills. The damage type also matters for Control: a Reality DMG attack ends Petrify, and a Mental DMG attack ends Freeze (see [Statuses](/systems/statuses/)).

## Incantations and AP

- The hand holds up to 7 incantations with 4 characters on the field (support included); the limit depends on how many are alive and deployed.
- Casting an incantation or moving one in the hand spends an action. Moving a card onto an identical one raises its rank, up to rank 3; a higher rank is stronger.
- With fewer allies left, the team has fewer actions each round but gets higher-rank incantations more easily. Defeating an enemy likewise cuts the actions the enemies take.
- A card cast this round can be taken back by tapping the action area before the round plays out.

## Moxie and the Ultimate

Moxie is the resource the Ultimate spends. An arcanist gains it by casting and moving incantations, and through some skills.

- 131 of the 138 released arcanists need 5 Moxie for the Ultimate.
- Alexios, Ezio Auditore, Kassandra, Coppelia, Everecho, The Twins and Hedone fill another resource instead.
- Disconcert stops an arcanist gaining Moxie; some enemies and arcanists remove Moxie.

## Stats

| Stat | What it does |
| --- | --- |
| HP | the character leaves the battle at 0 |
| ATK | the base of the damage an attack deals |
| Reality DEF | lowers Reality DMG taken |
| Mental DEF | lowers Mental DMG taken |
| Critical Technique | adds Critical Rate and Critical DMG |
| Critical Rate | chance of a critical hit; also of a critical heal |
| Critical Resist Rate | lowers the chance of being hit critically |
| Critical DMG | damage of a critical hit; also the healing of a critical heal, with diminishing returns |
| Critical DEF | lowers the damage of critical hits taken |
| DMG Bonus | raises damage dealt |
| DMG Taken Reduction | lowers damage taken |
| Penetration Rate | ignores part of the target's Reality DEF and Mental DEF |
| Incantation Might | raises the damage of incantations |
| Ultimate Might | raises the damage of the Ultimate |
| Healing Done | raises healing given |
| DMG Heal | at the start of a round, heals part of the damage taken in the last round |
| Leech Rate | turns part of the damage dealt into the attacker's HP |
| Genesis DMG Bonus | raises Genesis DMG dealt |

## Terms in five languages

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Afflatus | 灵感 | 靈感 | 本源 | 영감 |
| Incantation | 咒语 | 咒語 | スペル | 주문 |
| Ultimate | 至终的仪式 | 至終的儀式 | アルティメット | 최종 술식 |
| Moxie | 激情 | 激情 | モキシー | 열정 |
| AP | 行动点 | 行動點 | 行動回数 | 행동 횟수 |
| Reality DMG | 现实创伤 | 現實創傷 | リアルダメージ | 현실 피해 |
| Mental DMG | 精神创伤 | 精神創傷 | メンタルダメージ | 정신 피해 |
| Genesis DMG | 本源创伤 | 本源創傷 | ジェネシスダメージ | 고정 피해 |
