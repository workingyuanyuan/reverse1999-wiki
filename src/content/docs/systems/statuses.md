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
Every status is positive or negative. The positive kinds are Stats Up, Pos Status and Counter, and a dispel removes them; the negative kinds are Stats Down, Neg Status and Control, and Purify removes them. A status the game marks as undispellable stays.

Whether a second status of the same name replaces the first depends on their strength and duration. The special effect of an incantation can be resisted by the target, and Immunity blocks every negative kind.

## Control

Control statuses stop a character acting or limit what it can cast. Three statuses build up into one of them at 2 stacks.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Daze | cannot act | [An-an Lee](/arcanists/an-an-lee/), [Kassandra](/arcanists/kassandra/), [Medicine Pocket](/arcanists/medicine-pocket/), [Sweetheart](/arcanists/sweetheart/), [White Rum](/arcanists/white-rum/) |
| Petrify | cannot act; ends when the holder takes a Reality DMG attack | [Druvis III](/arcanists/druvis-iii/), [Jessica](/arcanists/jessica/), [Satsuki](/arcanists/satsuki/) |
| Freeze | cannot act; ends when the holder takes a Mental DMG attack | [J](/arcanists/j/), [Ms. Moissan](/arcanists/ms-moissan/) |
| Nightmare | cannot act; ends when the holder takes any attack | [Baby Blue](/arcanists/baby-blue/), [Diggers](/arcanists/diggers/), [Twins Sleep](/arcanists/twins-sleep/) |
| Disarm | cannot cast Attack incantations | [aliEn T](/arcanists/alien-t/), [Erick](/arcanists/erick/), [Sonetto](/arcanists/sonetto/), [Sputnik](/arcanists/sputnik/) |
| Silence | cannot cast Buff, Debuff, Heal or Counter incantations | [aliEn T](/arcanists/alien-t/), [Erick](/arcanists/erick/), [Sputnik](/arcanists/sputnik/), [Voyager](/arcanists/voyager/), [X](/arcanists/x/), [Зима](/arcanists/zima/) |
| Seal | cannot cast the Ultimate | [Bkornblume](/arcanists/bkornblume/), [La Source](/arcanists/la-source/), [Voyager](/arcanists/voyager/), [Зима](/arcanists/zima/) |
| Rigidity | at 2 stacks turns into Petrify, or adds 1 round to a Petrify already there | [An-an Lee](/arcanists/an-an-lee/), [Hissabeth](/arcanists/hissabeth/), [Satsuki](/arcanists/satsuki/) |
| Cold | at 2 stacks turns into Freeze, or adds 1 round to a Freeze already there | [J](/arcanists/j/) |
| Paralyze | at 2 stacks turns into Daze, or adds 1 round to a Daze already there | [Mesmer Jr.](/arcanists/mesmer-jr/) |

## Damage over time and other debuffs

The damage these statuses deal is Genesis DMG.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Burn | Healing Taken -15% (does not stack); at the end of each round, Genesis DMG equal to 4% of the holder's ATK per stack; up to 30 stacks, which count as one Neg Status; half the stacks go each time it deals damage | [6](/arcanists/6/), [An-an Lee](/arcanists/an-an-lee/), [Beryl](/arcanists/beryl/), [Brume](/arcanists/brume/), [Drake](/arcanists/drake/), [Isolde](/arcanists/isolde/), [J](/arcanists/j/), [Liang Yue](/arcanists/liang-yue/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marsha](/arcanists/marsha/), [Matilda](/arcanists/matilda/), [Spathodea](/arcanists/spathodea/), [Ulu](/arcanists/ulu/) |
| Halo | like Burn, with Healing Taken -25% and the damage based on the ATK of whoever first applied it | [Drake](/arcanists/drake/), [Isolde](/arcanists/isolde/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marsha](/arcanists/marsha/), [Matilda](/arcanists/matilda/), [Spathodea](/arcanists/spathodea/) |
| Poison | at the end of each round, Genesis DMG based on the ATK of whoever applied it; stacks | [6](/arcanists/6/), [An-an Lee](/arcanists/an-an-lee/), [Eternity](/arcanists/eternity/), [Ezio Auditore](/arcanists/ezio-auditore/), [Jessica](/arcanists/jessica/), [Kanjira](/arcanists/kanjira/), [Liang Yue](/arcanists/liang-yue/), [Rabies](/arcanists/rabies/), [Ramona](/arcanists/ramona/), [Sotheby](/arcanists/sotheby/), [Tuesday](/arcanists/tuesday/), [Willow](/arcanists/willow/) |
| Bleed | after the holder acts, Genesis DMG equal to 100% of the applier's ATK | [Eternity](/arcanists/eternity/), [Nautika](/arcanists/nautika/), [White Rum](/arcanists/white-rum/) |
| Corrode | at the end of each round, Genesis DMG based on the holder's current HP | [Eternity](/arcanists/eternity/), [The Fool](/arcanists/the-fool/) |
| Nasty Wound | Healing Taken -50% | [Bunny Bunny](/arcanists/bunny-bunny/), [Cristallo](/arcanists/cristallo/), [Eternity](/arcanists/eternity/), [Silverwing Eagle](/arcanists/silverwing-eagle/) |
| Weakness | DMG Bonus -25% on an attack; one stack is used each time | [Bkornblume](/arcanists/bkornblume/), [Centurion](/arcanists/centurion/), [Diggers](/arcanists/diggers/), [La Source](/arcanists/la-source/), [Lorelei](/arcanists/lorelei/), [Marcus](/arcanists/marcus/), [Twins Sleep](/arcanists/twins-sleep/) |
| Blind | DMG Bonus -30% on 1-target attacks | [6](/arcanists/6/), [Click](/arcanists/click/) |
| Mis-aim | DMG Bonus -30% on mass attacks | [6](/arcanists/6/) |
| Confusion | Critical Resist Rate -25%; stacks, each stack with its own duration | [Blonney](/arcanists/blonney/), [Kanjira](/arcanists/kanjira/), [Matilda](/arcanists/matilda/), [Tooth Fairy](/arcanists/tooth-fairy/), [Voyager](/arcanists/voyager/), [Windsong](/arcanists/windsong/) |
| Scared | Mental DMG taken +25%; one stack is used each time | [Barbara](/arcanists/barbara/), [Horropedia](/arcanists/horropedia/), [Nautika](/arcanists/nautika/) |
| Disconcert | cannot gain Moxie | [Ms. Radio](/arcanists/ms-radio/), [TTT](/arcanists/ttt/), [X](/arcanists/x/) |
| Passion Drain | when the holder is attacked, the attacker gains 1 Moxie; one stack is used each time | [Melania](/arcanists/melania/), [Moldir](/arcanists/moldir/), [Narcissus](/arcanists/narcissus/), [Recoleta](/arcanists/recoleta/) |

## Buffs

Positive statuses that several arcanists grant.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Shield | absorbs damage while it lasts | [Barbara](/arcanists/barbara/), [Bette](/arcanists/bette/), [Door](/arcanists/door/), [Ezra](/arcanists/ezra/), [J](/arcanists/j/), [Jiu Niangzi](/arcanists/jiu-niangzi/), [John Titor](/arcanists/john-titor/), [Kiperina](/arcanists/kiperina/), [Marsha](/arcanists/marsha/), [Ms. Moissan](/arcanists/ms-moissan/), [Ms. NewBabel](/arcanists/ms-newbabel/), [Nick Bottom](/arcanists/nick-bottom/), [Oliver Fog](/arcanists/oliver-fog/), [Tennant](/arcanists/tennant/), [Yenisei](/arcanists/yenisei/) |
| Counter | a lasting status whose effect triggers when the holder is attacked | [6](/arcanists/6/), [Charlie](/arcanists/charlie/), [Desert Flannel](/arcanists/desert-flannel/), [Erick](/arcanists/erick/), [Horropedia](/arcanists/horropedia/), [Jiu Niangzi](/arcanists/jiu-niangzi/), [John Titor](/arcanists/john-titor/), [Ms. Moissan](/arcanists/ms-moissan/), [Name Day](/arcanists/name-day/), [Pickles](/arcanists/pickles/), [Sputnik](/arcanists/sputnik/), [TTT](/arcanists/ttt/), [X](/arcanists/x/) |
| Taunt | draws some attacks to the holder first | [aliEn T](/arcanists/alien-t/), [Ms. NewBabel](/arcanists/ms-newbabel/), [Nautika](/arcanists/nautika/), [ONiON](/arcanists/onion/), [Pioneer](/arcanists/pioneer/), [Poltergeist](/arcanists/poltergeist/), [The Fool](/arcanists/the-fool/) |
| Sturdiness | DMG Taken Reduction +25% when attacked; one stack is used each time | [37](/arcanists/37/), [An-an Lee](/arcanists/an-an-lee/), [Avgust](/arcanists/avgust/), [Cristallo](/arcanists/cristallo/), [Medicine Pocket](/arcanists/medicine-pocket/), [Oliver Fog](/arcanists/oliver-fog/), [ONiON](/arcanists/onion/), [Regulus](/arcanists/regulus/), [Vila](/arcanists/vila/), [Voyager](/arcanists/voyager/), [White Rum](/arcanists/white-rum/), [Yenisei](/arcanists/yenisei/) |
| Rousing Morale | DMG Bonus +50% on an attack; one stack is used each time | [A Knight](/arcanists/a-knight/), [Avgust](/arcanists/avgust/), [Isolde](/arcanists/isolde/), [Pickles](/arcanists/pickles/), [White Rum](/arcanists/white-rum/) |
| Power Burst | DMG Bonus +25% on an attack; one stack is used each time | [Desert Flannel](/arcanists/desert-flannel/), [Isolde](/arcanists/isolde/), [Vila](/arcanists/vila/) |
| Immunity | unaffected by Stats Down, Neg Status and Control | [Dikke](/arcanists/dikke/), [Liang Yue](/arcanists/liang-yue/), [Nautika](/arcanists/nautika/), [Yenisei](/arcanists/yenisei/) |
| Cure | at the start of each round, heals based on the ATK of whoever granted it | [An-an Lee](/arcanists/an-an-lee/), [Avgust](/arcanists/avgust/), [Sotheby](/arcanists/sotheby/) |
| Concealment | dodges Reality DMG attacks other than Ultimates | [Nautika](/arcanists/nautika/), [Poltergeist](/arcanists/poltergeist/), [TTT](/arcanists/ttt/) |
| Empower Incantation I | at the start of each round, one random incantation goes up one rank | [6](/arcanists/6/), [An-an Lee](/arcanists/an-an-lee/), [Argus](/arcanists/argus/), [Yenisei](/arcanists/yenisei/) |
| Empower Incantation II | at the start of each round, two random incantations go up one rank | [An-an Lee](/arcanists/an-an-lee/), [Argus](/arcanists/argus/), [Bette](/arcanists/bette/), [Kaalaa Baunaa](/arcanists/kaalaa-baunaa/) |
| Continuous Action I | AP +1 | [37](/arcanists/37/), [Aleph](/arcanists/aleph/), [Cheng Heguang](/arcanists/cheng-heguang/), [Flutterpage](/arcanists/flutterpage/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marcus](/arcanists/marcus/), [Moldir](/arcanists/moldir/), [Tooth Fairy](/arcanists/tooth-fairy/) |

## Team mechanics

Resources and effects that a group of arcanists builds together. Bloodtithe, Lingering Glow and Pursuit Scope cannot be active at the same time in the mainland client; the global client's text of Bloodtithe and Lingering Glow lacks that clause, and Pursuit is out only on the mainland service.

| Status | Effect | Arcanists whose kit names it |
| --- | --- | --- |
| Bloodtithe | 1 point each time the team has lost 3,000 HP in total; HP lost to attacks counts at 30% | [Eternity](/arcanists/eternity/), [Ezra](/arcanists/ezra/), [Nautika](/arcanists/nautika/), [Rubuska](/arcanists/rubuska/), [Semmelweis](/arcanists/semmelweis/), [Sentinel](/arcanists/sentinel/) |
| Lingering Glow | builds whenever an enemy is given Burn or Halo, more of it the fewer enemies there are | [Beryl](/arcanists/beryl/), [Drake](/arcanists/drake/), [Isolde](/arcanists/isolde/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/), [Marsha](/arcanists/marsha/), [Matilda](/arcanists/matilda/), [Spathodea](/arcanists/spathodea/) |
| Pursuit Scope (not yet official) | before an incantation, a team with at least 6 Pursuit Points (15 at most) can enter Full Pursuit, take up to 10 points into it, and spend them on Pursuit incantations of the same Afflatus | [37](/arcanists/37/), [Huntsworn Lilya](/arcanists/huntsworn-lilya/), [Perchta](/arcanists/perchta/) |
| Inspiration | each Eureka spent adds 1 point; at the start of a round the points go to random incantations, at most 5 each, and points on cards not cast are lost at the end of the round; casting a card that holds points adds an Impromptu Incantation at the end of the sequence | [Aleph](/arcanists/aleph/), [An-an Lee](/arcanists/an-an-lee/), [Barcarola](/arcanists/barcarola/), [Kiperina](/arcanists/kiperina/), [Matilda](/arcanists/matilda/), [Paper Heron](/arcanists/paper-heron/), [Regulus](/arcanists/regulus/), [Tooth Fairy](/arcanists/tooth-fairy/), [Voyager](/arcanists/voyager/) |
| Impromptu Incantation | 200% Mental DMG to a random enemy plus 15% per Inspiration point it carries; at 3, 6, 12 and 20 points it attacks 1, 2, 3 and 5 more times; uses the average stats of the whole team | [Aleph](/arcanists/aleph/), [An-an Lee](/arcanists/an-an-lee/), [Barcarola](/arcanists/barcarola/), [Kiperina](/arcanists/kiperina/), [Matilda](/arcanists/matilda/), [Paper Heron](/arcanists/paper-heron/), [Regulus](/arcanists/regulus/), [Tooth Fairy](/arcanists/tooth-fairy/), [Voyager](/arcanists/voyager/) |
| Dynamo | powers devices; up to 30 stacks, undispellable | [Brume](/arcanists/brume/), [Charon](/arcanists/charon/), [Corvus](/arcanists/corvus/), [Enigma](/arcanists/enigma/), [Ezra](/arcanists/ezra/), [Lucy](/arcanists/lucy/), [Ulrich](/arcanists/ulrich/) |
| Pulsing Field | an Array that grows at the start of a round with the Dynamo poured into it: Lv.1 DMG Bonus +15% for 3 rounds; Lv.2 from 50 Dynamo, Incantation Might +25% as well; Lv.3 from 120, Ultimate Might +35% as well, for 2 rounds; the Dynamo is lost when it ends | [Brume](/arcanists/brume/), [Charon](/arcanists/charon/), [Corvus](/arcanists/corvus/), [Enigma](/arcanists/enigma/), [Ezra](/arcanists/ezra/), [Lucy](/arcanists/lucy/), [Ulrich](/arcanists/ulrich/) |
| Conduit | charged with Energy; at the end of the action sequence it casts incantations again and again, spending Energy | [Coppélia](/arcanists/coppelia/), [Everecho](/arcanists/everecho/), [Hedone](/arcanists/hedone/), [Regulus](/arcanists/regulus/), [The Twins](/arcanists/the-twins/) |
| Ceremonious | Ultimate Might +3% per stack, up to 100 stacks, undispellable; gone after the Ultimate | [La Source](/arcanists/la-source/), [Lilya](/arcanists/lilya/), [Mr. Duncan](/arcanists/mr-duncan/), [Name Day](/arcanists/name-day/), [Shamane](/arcanists/shamane/) |
| Sovereign Incantation | casting it counts as the arcanist's own action | [Beryl](/arcanists/beryl/), [Hissabeth](/arcanists/hissabeth/), [Kassandra](/arcanists/kassandra/), [Ms. Stranger](/arcanists/ms-stranger/) |
| Static Genesis DMG | a kind of Genesis DMG that stat bonuses do not change | [Hedone](/arcanists/hedone/), [Kakania](/arcanists/kakania/), [Lorentz Butterfly](/arcanists/lorentz-butterfly/) |
