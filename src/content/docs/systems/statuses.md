---
title: "Statuses"
description: "Reverse: 1999 statuses: positive and negative kinds, Control effects and the statuses arcanists share."
appliesTo: "Reverse: 1999, mainland China client 113.0.1422 (version 4.1); global client 111.0.1077 (version 3.9)"
caveat: "Petrify ends when the holder takes a Reality DMG attack and Freeze when it takes a Mental DMG attack, so an attack of that type frees a controlled enemy."
lastVerified: 2026-11-23
aliases:
  - "狀態效果"
  - "状态效果"
  - "状態効果"
  - "상태 효과"
  - "Status effects"
  - "Buffs and debuffs"
  - "Control"
  - "控制"
sources:
  - title: "re1999-data, mainland client 113.0.1422: skill_eff_desc.json (statuses) and the skill text of every arcanist"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/skill_eff_desc.json
  - title: "re1999-data-global, global client 111.0.1077: skill_eff_desc.json and its text in each language"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/skill_eff_desc.json
  - title: "re1999-data-global, global client 111.0.1077: loading_text.json (Field Manual tips)"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/loading_text.json
---
## Kinds of status

Every status is positive or negative. The positive kinds are Stats Up, Pos Status and Counter, and a dispel removes them; the negative kinds are Stats Down, Neg Status and Control, and Purify removes them. A status the game marks as undispellable stays.

Whether a second status of the same name replaces the first depends on their strength and duration. The special effect of an incantation can be resisted by the target, and Immunity blocks every negative kind.

## Control

Control statuses stop a character acting or limit what it can cast. Three statuses build up into one of them at 2 stacks.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Daze | Cannot act. | [An-an Lee](/arcanists/an-an-lee/), [Kassandra](/arcanists/kassandra/), [Medicine Pocket](/arcanists/medicine-pocket/), [Sweetheart](/arcanists/sweetheart/), [White Rum](/arcanists/white-rum/) |
| Petrify | Cannot act. Dispels the effect after taking Reality DMG attack. | [Druvis III](/arcanists/druvis-iii/), [Jessica](/arcanists/jessica/), [Satsuki](/arcanists/satsuki/) |
| Freeze | Cannot act. Dispels the effect after taking Mental DMG attack. | [J](/arcanists/j/), [Ms. Moissan](/arcanists/ms-moissan/) |
| Nightmare | Cannot act. Dispels the effect after taking any attack. | [Baby Blue](/arcanists/baby-blue/), [Diggers](/arcanists/diggers/), [Twins Sleep](/arcanists/twins-sleep/) |
| Disarm | Cannot cast Attack-type incantations. | [aliEn T](/arcanists/alien-t/), [Erick](/arcanists/erick/), [Sonetto](/arcanists/sonetto/), [Sputnik](/arcanists/sputnik/) |
| Silence | Cannot cast Buff, Debuff, Heal, or Counter-type incantations. | [aliEn T](/arcanists/alien-t/), [Erick](/arcanists/erick/), [Sputnik](/arcanists/sputnik/), [Voyager](/arcanists/voyager/), [X](/arcanists/x/), [Зима](/arcanists/zima/) |
| Seal | Cannot use Ultimate. | [Bkornblume](/arcanists/bkornblume/), [La Source](/arcanists/la-source/), [Voyager](/arcanists/voyager/), [Зима](/arcanists/zima/) |
| Rigidity | When there are 2 stacks, turns into Petrify status or extends the duration of existing Petrify status for 1 round. | [An-an Lee](/arcanists/an-an-lee/), [Hissabeth](/arcanists/hissabeth/), [Satsuki](/arcanists/satsuki/) |
| Cold | When there are 2 stacks, turns into Freeze status or extends the duration of existing Freeze status for 1 round. | [J](/arcanists/j/) |
| Paralyze | When there are 2 stacks, turns into Daze status or extends the duration of existing Daze status for 1 round. | [Mesmer Jr.](/arcanists/mesmer-jr/) |

## Damage over time and other debuffs

The damage these statuses deal is Genesis DMG.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Burn | Healing Taken -15% (unstackable). At the end of the round, takes (the holder's ATK x4%) Genesis DMG (stackable up to 30 times, multiple stacks of Burn is regarded as 1 \[Neg Status\], removes 50% of the stacks when triggered). | [6](/arcanists/6/), [An-an Lee](/arcanists/an-an-lee/), [Beryl](/arcanists/beryl/), [Brume](/arcanists/brume/), [Drake](/arcanists/drake/), [Isolde](/arcanists/isolde/), [J](/arcanists/j/), [Liang Yue](/arcanists/liang-yue/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marsha](/arcanists/marsha/), [Matilda](/arcanists/matilda/), [Spathodea](/arcanists/spathodea/), [Ulu](/arcanists/ulu/) |
| Halo | Healing Taken -25% (unstackable). At the end of the round, takes (the inflicter's ATK x4%) Genesis DMG (stackable up to 30 times, multiple stacks of Halo are regarded as 1 \[Neg Status\], removes 50% of the stacks when triggered). | [Drake](/arcanists/drake/), [Isolde](/arcanists/isolde/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marsha](/arcanists/marsha/), [Matilda](/arcanists/matilda/), [Spathodea](/arcanists/spathodea/) |
| Poison | At the end of the round, takes Genesis DMG based on the user's ATK (stackable). | [6](/arcanists/6/), [An-an Lee](/arcanists/an-an-lee/), [Eternity](/arcanists/eternity/), [Ezio Auditore](/arcanists/ezio-auditore/), [Jessica](/arcanists/jessica/), [Kanjira](/arcanists/kanjira/), [Liang Yue](/arcanists/liang-yue/), [Rabies](/arcanists/rabies/), [Ramona](/arcanists/ramona/), [Sotheby](/arcanists/sotheby/), [Tuesday](/arcanists/tuesday/), [Willow](/arcanists/willow/) |
| Bleed | After action, takes (the caster's ATK ×100%) Genesis DMG. | [Eternity](/arcanists/eternity/), [Nautika](/arcanists/nautika/), [White Rum](/arcanists/white-rum/) |
| Corrode | When a round ends, takes Genesis DMG based on the carrier's current HP. | [Eternity](/arcanists/eternity/), [The Fool](/arcanists/the-fool/) |
| Nasty Wound | Healing Taken -50%. | [Bunny Bunny](/arcanists/bunny-bunny/), [Cristallo](/arcanists/cristallo/), [Eternity](/arcanists/eternity/), [Silverwing Eagle](/arcanists/silverwing-eagle/) |
| Weakness | DMG Bonus -25% when attacking (reduced by 1 stack on trigger). | [Bkornblume](/arcanists/bkornblume/), [Centurion](/arcanists/centurion/), [Diggers](/arcanists/diggers/), [La Source](/arcanists/la-source/), [Lorelei](/arcanists/lorelei/), [Marcus](/arcanists/marcus/), [Twins Sleep](/arcanists/twins-sleep/) |
| Blind | DMG Bonus -30% when attacking 1 target. | [6](/arcanists/6/), [Click](/arcanists/click/) |
| Mis-aim | DMG Bonus -30% when attacking multiple targets. | [6](/arcanists/6/) |
| Confusion | Critical Resist -25% (stackable, each stack timed independently). | [Blonney](/arcanists/blonney/), [Kanjira](/arcanists/kanjira/), [Matilda](/arcanists/matilda/), [Tooth Fairy](/arcanists/tooth-fairy/), [Voyager](/arcanists/voyager/), [Windsong](/arcanists/windsong/) |
| Scared | Increases Mental DMG taken by 25% (-1 stack after triggering). | [Barbara](/arcanists/barbara/), [Horropedia](/arcanists/horropedia/), [Nautika](/arcanists/nautika/) |
| Disconcert | Cannot gain Moxie. | [Ms. Radio](/arcanists/ms-radio/), [TTT](/arcanists/ttt/), [X](/arcanists/x/) |
| Passion Drain | After the holder is attacked, the attacker gains Moxie +1 (-1 stack after trigger). | [Melania](/arcanists/melania/), [Moldir](/arcanists/moldir/), [Narcissus](/arcanists/narcissus/), [Recoleta](/arcanists/recoleta/) |

## Buffs

Positive statuses that several arcanists grant.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Shield | Blocks certain DMG for a certain duration. | [Barbara](/arcanists/barbara/), [Bette](/arcanists/bette/), [Door](/arcanists/door/), [Ezra](/arcanists/ezra/), [J](/arcanists/j/), [Jiu Niangzi](/arcanists/jiu-niangzi/), [John Titor](/arcanists/john-titor/), [Kiperina](/arcanists/kiperina/), [Marsha](/arcanists/marsha/), [Ms. Moissan](/arcanists/ms-moissan/), [Ms. NewBabel](/arcanists/ms-newbabel/), [Nick Bottom](/arcanists/nick-bottom/), [Oliver Fog](/arcanists/oliver-fog/), [Tennant](/arcanists/tennant/), [Yenisei](/arcanists/yenisei/) |
| Counter | Grants continuous Counter. Effect is triggered When the caster is attacked. | [6](/arcanists/6/), [Charlie](/arcanists/charlie/), [Desert Flannel](/arcanists/desert-flannel/), [Erick](/arcanists/erick/), [Horropedia](/arcanists/horropedia/), [Jiu Niangzi](/arcanists/jiu-niangzi/), [John Titor](/arcanists/john-titor/), [Ms. Moissan](/arcanists/ms-moissan/), [Name Day](/arcanists/name-day/), [Pickles](/arcanists/pickles/), [Sputnik](/arcanists/sputnik/), [TTT](/arcanists/ttt/), [X](/arcanists/x/) |
| Taunt | Draws the enemy's attention. When taking certain attacks, becomes the priority of the attacks. | [aliEn T](/arcanists/alien-t/), [Ms. NewBabel](/arcanists/ms-newbabel/), [Nautika](/arcanists/nautika/), [ONiON](/arcanists/onion/), [Pioneer](/arcanists/pioneer/), [Poltergeist](/arcanists/poltergeist/), [The Fool](/arcanists/the-fool/) |
| Sturdiness | When attacked, DMG Taken Reduction +25% (-1 stack after trigger). | [37](/arcanists/37/), [An-an Lee](/arcanists/an-an-lee/), [Avgust](/arcanists/avgust/), [Cristallo](/arcanists/cristallo/), [Medicine Pocket](/arcanists/medicine-pocket/), [Oliver Fog](/arcanists/oliver-fog/), [ONiON](/arcanists/onion/), [Regulus](/arcanists/regulus/), [Vila](/arcanists/vila/), [Voyager](/arcanists/voyager/), [White Rum](/arcanists/white-rum/), [Yenisei](/arcanists/yenisei/) |
| Rousing Morale | DMG Bonus +50% when attacking (reduced by 1 stack on trigger). | [A Knight](/arcanists/a-knight/), [Avgust](/arcanists/avgust/), [Isolde](/arcanists/isolde/), [Pickles](/arcanists/pickles/), [White Rum](/arcanists/white-rum/) |
| Power Burst | DMG Bonus +25% when attacking (-1 stack after trigger). | [Desert Flannel](/arcanists/desert-flannel/), [Isolde](/arcanists/isolde/), [Vila](/arcanists/vila/) |
| Immunity | Immune to \[Stats Down\], \[Neg Status\], and \[Control\] statuses. | [Dikke](/arcanists/dikke/), [Liang Yue](/arcanists/liang-yue/), [Nautika](/arcanists/nautika/), [Yenisei](/arcanists/yenisei/) |
| Cure | At the start of the round, recovers HP based on the user's ATK. | [An-an Lee](/arcanists/an-an-lee/), [Avgust](/arcanists/avgust/), [Sotheby](/arcanists/sotheby/) |
| Concealment | Dodges Reality DMG dealt by non-Ultimate attacks. | [Nautika](/arcanists/nautika/), [Poltergeist](/arcanists/poltergeist/), [TTT](/arcanists/ttt/) |
| Empower Incantation I | At the start of the round, a random incantation gains rank +1. | [6](/arcanists/6/), [An-an Lee](/arcanists/an-an-lee/), [Argus](/arcanists/argus/), [Yenisei](/arcanists/yenisei/) |
| Empower Incantation II | At the start of the round, 2 random incantations gain rank +1. | [An-an Lee](/arcanists/an-an-lee/), [Argus](/arcanists/argus/), [Bette](/arcanists/bette/), [Kaalaa Baunaa](/arcanists/kaalaa-baunaa/) |
| Continuous Action I | AP +1. | [37](/arcanists/37/), [Aleph](/arcanists/aleph/), [Cheng Heguang](/arcanists/cheng-heguang/), [Flutterpage](/arcanists/flutterpage/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marcus](/arcanists/marcus/), [Moldir](/arcanists/moldir/), [Tooth Fairy](/arcanists/tooth-fairy/) |

## Team mechanics

Resources and effects that a group of arcanists builds together. Bloodtithe, Lingering Glow and Pursuit Scope cannot be active at the same time in the mainland client; the global client's text of Bloodtithe and Lingering Glow lacks that clause, and Pursuit is out only on the mainland service.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Bloodtithe | Whenever allies lose 3000 HP combined, accumulate 1 point of \[Bloodtithe\]; HP lost from being attacked accumulates \[Bloodtithe\] at only 30% efficiency. | [Eternity](/arcanists/eternity/), [Ezra](/arcanists/ezra/), [Nautika](/arcanists/nautika/), [Rubuska](/arcanists/rubuska/), [Semmelweis](/arcanists/semmelweis/), [Sentinel](/arcanists/sentinel/) |
| Lingering Glow | Accumulates \[Lingering Glow\] whenever an enemy is inflicted with \[Burn\] or \[Halo\]. The fewer enemies there are, the more \[Lingering Glow\] is accumulated. | [Beryl](/arcanists/beryl/), [Drake](/arcanists/drake/), [Isolde](/arcanists/isolde/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marsha](/arcanists/marsha/), [Matilda](/arcanists/matilda/), [Spathodea](/arcanists/spathodea/) |
| Pursuit Scope (not yet official) | Not in the global client yet | [37](/arcanists/37/), [Huntsworn Lilya](/arcanists/huntsworn-lilya/), [Perchta](/arcanists/perchta/) |
| Inspiration | For every 1 Eureka consumed, accumulate 1 point of \[Inspiration\].<br>At the start of each round, randomly distribute Inspiration points onto basic incantations (each incantation may receive up to 5 points of Inspiration, and at the end of the round, the points of Inspiration on unused incantations are cleared).<br>When actively casting an incantation with \[Inspiration\] points on it, add an \[Impromptu Incantation\] to the end of the spell queue, and all Inspiration points on these casted incantations will be granted to the \[Impromptu Incantation\]. | [Aleph](/arcanists/aleph/), [An-an Lee](/arcanists/an-an-lee/), [Barcarola](/arcanists/barcarola/), [Kiperina](/arcanists/kiperina/), [Matilda](/arcanists/matilda/), [Paper Heron](/arcanists/paper-heron/), [Regulus](/arcanists/regulus/), [Tooth Fairy](/arcanists/tooth-fairy/), [Voyager](/arcanists/voyager/) |
| Impromptu Incantation | 1-target attack. Deals 200% Mental DMG to a random enemy and an additional (the total points of Inspiration granted to Impromptu Incantation x15%) Mental DMG. If Impromptu Incantation has at least 3/6/12/20 points of Inspiration, it gains attack instances +1/2/3/5 (Impromptu Incantation's DMG calculation is based on the average stats of all allies). | [Aleph](/arcanists/aleph/), [An-an Lee](/arcanists/an-an-lee/), [Barcarola](/arcanists/barcarola/), [Kiperina](/arcanists/kiperina/), [Matilda](/arcanists/matilda/), [Paper Heron](/arcanists/paper-heron/), [Regulus](/arcanists/regulus/), [Tooth Fairy](/arcanists/tooth-fairy/), [Voyager](/arcanists/voyager/) |
| Dynamo | A product of technology used for meticulous machinery (up to 30 stacks, undispellable). | [Brume](/arcanists/brume/), [Charon](/arcanists/charon/), [Corvus](/arcanists/corvus/), [Enigma](/arcanists/enigma/), [Ezra](/arcanists/ezra/), [Lucy](/arcanists/lucy/), [Ulrich](/arcanists/ulrich/) |
| Pulsing Field | At the start of the round, Pulsing Field upgrades based on the \[Dynamo\] transferred into it. At 50+, upgrades into \[Pulsing Field Lv.2\]. At 120+, upgrades into \[Pulsing Field Lv.3\]. When Pulsing Field disappears, all \[Dynamo\] transferred into it are also cleared. | [Brume](/arcanists/brume/), [Charon](/arcanists/charon/), [Corvus](/arcanists/corvus/), [Enigma](/arcanists/enigma/), [Ezra](/arcanists/ezra/), [Lucy](/arcanists/lucy/), [Ulrich](/arcanists/ulrich/) |
| Conduit | Use Energy to power Conduits. Conduits activate at the end of the AP Area and repeatedly cast incantations by consuming Energy. | [Coppélia](/arcanists/coppelia/), [Everecho](/arcanists/everecho/), [Hedone](/arcanists/hedone/), [Regulus](/arcanists/regulus/), [The Twins](/arcanists/the-twins/) |
| Ceremonious | Ultimate Might +3% (up to 100 stacks, undispellable, disappears after casting an Ultimate). | [La Source](/arcanists/la-source/), [Lilya](/arcanists/lilya/), [Mr. Duncan](/arcanists/mr-duncan/), [Name Day](/arcanists/name-day/), [Shamane](/arcanists/shamane/) |
| Sovereign Incantation | Casting this incantation counts as the character actively taking an action. | [Beryl](/arcanists/beryl/), [Hissabeth](/arcanists/hissabeth/), [Kassandra](/arcanists/kassandra/), [Ms. Stranger](/arcanists/ms-stranger/) |
| Static Genesis DMG | This type of Genesis DMG is not affected by relevant stat bonuses. | [Hedone](/arcanists/hedone/), [Kakania](/arcanists/kakania/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/) |
