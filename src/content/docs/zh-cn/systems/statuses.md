---
title: "状态效果"
description: "重返未来：1999 的状态效果：正面与负面类型、控制效果，以及多位神秘学家共用的状态。"
appliesTo: "重返未来：1999，中国大陆版客户端 113.0.1422（4.1 版）；国际版客户端 111.0.1077（3.9 版）"
caveat: "石化在持有者受到现实创伤攻击时解除，冰冻则在受到精神创伤攻击时解除，因此对应类型的攻击会让受控制的敌人脱离控制。"
lastVerified: 2026-11-23
aliases:
  - "Statuses"
  - "狀態效果"
  - "状態効果"
  - "상태 효과"
  - "Status effects"
  - "Buffs and debuffs"
  - "Control"
  - "控制"
sources:
  - title: "re1999-data，中国大陆版客户端 113.0.1422：skill_eff_desc.json（状态）与每位神秘学家的技能文字"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/skill_eff_desc.json
  - title: "re1999-data-global，国际版客户端 111.0.1077：skill_eff_desc.json 与各语言文字"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/skill_eff_desc.json
  - title: "re1999-data-global，国际版客户端 111.0.1077：loading_text.json（作战手册提示）"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/loading_text.json
---
## 状态的种类

每个状态都属于正面或负面。正面类型为属性提升、状态增益与反制，驱散可以移除；负面类型为属性削弱、状态异常与控制，净化可以移除。游戏标示为无法驱散的状态不会被移除。

同名状态再次施加时，依两者的强度与持续时间覆盖前一个。咒语的特殊效果可能被目标抵抗；免疫挡下所有负面类型。

## 控制

控制状态让角色无法行动，或限制它能施放的咒语。有三种状态在叠加到 2 层时会转为其中一种控制。

| 状态 | 效果 | 技能中提到它的神秘学家 |
| --- | --- | --- |
| 眩晕 | 无法行动 | [泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[卡珊德拉](/zh-cn/arcanists/kassandra/)、[兔毛手袋](/zh-cn/arcanists/medicine-pocket/)、[玛丽莲](/zh-cn/arcanists/sweetheart/)、[白朗姆](/zh-cn/arcanists/white-rum/) |
| 石化 | 无法行动，受到现实创伤攻击后解除 | [槲寄生](/zh-cn/arcanists/druvis-iii/)、[洁西卡](/zh-cn/arcanists/jessica/)、[五色月](/zh-cn/arcanists/satsuki/) |
| 冰冻 | 无法行动，受到精神创伤攻击后解除 | [J](/zh-cn/arcanists/j/)、[莫桑女士](/zh-cn/arcanists/ms-moissan/) |
| 噩梦 | 无法行动，受到任意攻击后解除 | [婴儿蓝](/zh-cn/arcanists/baby-blue/)、[挖掘艺术](/zh-cn/arcanists/diggers/)、[丽莎&路易斯](/zh-cn/arcanists/twins-sleep/) |
| 缴械 | 无法使用攻击类普通咒语 | [星之眼](/zh-cn/arcanists/alien-t/)、[埃里克](/zh-cn/arcanists/erick/)、[十四行诗](/zh-cn/arcanists/sonetto/)、[斯普特尼克](/zh-cn/arcanists/sputnik/) |
| 缄默 | 无法使用增益、减益、治疗、反制类普通咒语 | [星之眼](/zh-cn/arcanists/alien-t/)、[埃里克](/zh-cn/arcanists/erick/)、[斯普特尼克](/zh-cn/arcanists/sputnik/)、[远旅](/zh-cn/arcanists/voyager/)、[X](/zh-cn/arcanists/x/)、[冬](/zh-cn/arcanists/zima/) |
| 封印 | 无法使用至终的仪式 | [柏林以东](/zh-cn/arcanists/bkornblume/)、[拉拉泉](/zh-cn/arcanists/la-source/)、[远旅](/zh-cn/arcanists/voyager/)、[冬](/zh-cn/arcanists/zima/) |
| 僵硬 | 叠加到2层时，变为石化或使已存在的石化持续时间+1 | [泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[冷周六](/zh-cn/arcanists/hissabeth/)、[五色月](/zh-cn/arcanists/satsuki/) |
| 寒冷 | 叠加到2层时，变为冰冻或使已存在的冰冻持续时间+1 | [J](/zh-cn/arcanists/j/) |
| 麻痹 | 叠加到2层时，变为眩晕或使已存在的眩晕持续时间+1 | [小梅斯梅尔](/zh-cn/arcanists/mesmer-jr/) |

## 持续伤害与其他减益

这些状态造成的伤害为本源创伤。

| 状态 | 效果 | 技能中提到它的神秘学家 |
| --- | --- | --- |
| 燃烧 | 受到治疗效果降低15%（效果不叠加)；回合结束时受到基于携带者攻击\*4%的本源创伤（效果可叠加，最多可叠加30层，多层燃烧仅视为1个【状态异常】，生效后扣除一半层数) | [6](/zh-cn/arcanists/6/)、[泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[贝丽尔](/zh-cn/arcanists/beryl/)、[灰调蓝](/zh-cn/arcanists/brume/)、[德雷克](/zh-cn/arcanists/drake/)、[伊索尔德](/zh-cn/arcanists/isolde/)、[J](/zh-cn/arcanists/j/)、[梁月](/zh-cn/arcanists/liang-yue/)、[洛伦兹蝴蝶](/zh-cn/arcanists/lorentz-butterfly/)、[玛尔纱](/zh-cn/arcanists/marsha/)、[玛蒂尔达](/zh-cn/arcanists/matilda/)、[可燃点](/zh-cn/arcanists/spathodea/)、[和平乌鲁](/zh-cn/arcanists/ulu/) |
| 光晕 | 受到治疗效果降低25%（效果不叠加)；回合结束时受到基于初始来源攻击\*4%的本源创伤（效果可叠加，最多可叠加30层，多层光晕仅视为1个【状态异常】，生效后扣除一半层数) | [德雷克](/zh-cn/arcanists/drake/)、[伊索尔德](/zh-cn/arcanists/isolde/)、[洛伦兹蝴蝶](/zh-cn/arcanists/lorentz-butterfly/)、[玛尔纱](/zh-cn/arcanists/marsha/)、[玛蒂尔达](/zh-cn/arcanists/matilda/)、[可燃点](/zh-cn/arcanists/spathodea/) |
| 中毒 | 回合结束时，受到基于释放者攻击的本源创伤（可以叠加） | [6](/zh-cn/arcanists/6/)、[泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[温妮弗雷德](/zh-cn/arcanists/eternity/)、[艾吉奥·奥迪托雷](/zh-cn/arcanists/ezio-auditore/)、[洁西卡](/zh-cn/arcanists/jessica/)、[坎吉拉](/zh-cn/arcanists/kanjira/)、[梁月](/zh-cn/arcanists/liang-yue/)、[爱宠](/zh-cn/arcanists/rabies/)、[拉莫纳](/zh-cn/arcanists/ramona/)、[苏芙比](/zh-cn/arcanists/sotheby/)、[蓝手帕](/zh-cn/arcanists/tuesday/)、[笃笃骨](/zh-cn/arcanists/willow/) |
| 流血 | 行动后，受到使用者攻击\*100%的本源创伤 | [温妮弗雷德](/zh-cn/arcanists/eternity/)、[诺谛卡](/zh-cn/arcanists/nautika/)、[白朗姆](/zh-cn/arcanists/white-rum/) |
| 腐蚀 | 回合结束时，受到基于持有者当前生命的本源创伤 | [温妮弗雷德](/zh-cn/arcanists/eternity/)、[弄臣](/zh-cn/arcanists/the-fool/) |
| 重伤 | 受到的治疗效果-50% | [芭妮芭妮](/zh-cn/arcanists/bunny-bunny/)、[铅玻璃](/zh-cn/arcanists/cristallo/)、[温妮弗雷德](/zh-cn/arcanists/eternity/)、[银装小春雀儿](/zh-cn/arcanists/silverwing-eagle/) |
| 虚弱 | 攻击时，创伤加成-25%（生效后减少1层） | [柏林以东](/zh-cn/arcanists/bkornblume/)、[百夫长](/zh-cn/arcanists/centurion/)、[挖掘艺术](/zh-cn/arcanists/diggers/)、[拉拉泉](/zh-cn/arcanists/la-source/)、[罗蕾莱](/zh-cn/arcanists/lorelei/)、[马库斯](/zh-cn/arcanists/marcus/)、[丽莎&路易斯](/zh-cn/arcanists/twins-sleep/) |
| 致盲 | 单体攻击时，创伤加成-30% | [6](/zh-cn/arcanists/6/)、[喀嚓喀嚓](/zh-cn/arcanists/click/) |
| 失准 | 群体攻击时，创伤加成-30% | [6](/zh-cn/arcanists/6/) |
| 明昧 | 抗暴率-25%（效果可叠加，每层时间独立计算） | [金蜜儿](/zh-cn/arcanists/blonney/)、[坎吉拉](/zh-cn/arcanists/kanjira/)、[玛蒂尔达](/zh-cn/arcanists/matilda/)、[牙仙](/zh-cn/arcanists/tooth-fairy/)、[远旅](/zh-cn/arcanists/voyager/)、[北方哨歌](/zh-cn/arcanists/windsong/) |
| 忧惧 | 受到的精神创伤提升25%（生效后减少1层） | [数羊羔](/zh-cn/arcanists/barbara/)、[恐怖通](/zh-cn/arcanists/horropedia/)、[诺谛卡](/zh-cn/arcanists/nautika/) |
| 心神不宁 | 无法提升激情 | [无线电小姐](/zh-cn/arcanists/ms-radio/)、[TTT](/zh-cn/arcanists/ttt/)、[X](/zh-cn/arcanists/x/) |
| 激情萃取 | 受到攻击后，攻击者获得1点激情（生效后减少1层） | [梅兰妮](/zh-cn/arcanists/melania/)、[莫莉德尔](/zh-cn/arcanists/moldir/)、[纳西索斯](/zh-cn/arcanists/narcissus/)、[虚构集](/zh-cn/arcanists/recoleta/) |

## 增益

多位神秘学家能赋予的正面状态。

| 状态 | 效果 | 技能中提到它的神秘学家 |
| --- | --- | --- |
| 护盾 | 持续时间内，抵挡一定创伤 | [数羊羔](/zh-cn/arcanists/barbara/)、[贝蒂](/zh-cn/arcanists/bette/)、[门](/zh-cn/arcanists/door/)、[爱兹拉](/zh-cn/arcanists/ezra/)、[J](/zh-cn/arcanists/j/)、[曲娘](/zh-cn/arcanists/jiu-niangzi/)、[约翰·提托](/zh-cn/arcanists/john-titor/)、[库珀花环](/zh-cn/arcanists/kiperina/)、[玛尔纱](/zh-cn/arcanists/marsha/)、[莫桑女士](/zh-cn/arcanists/ms-moissan/)、[新巴别塔](/zh-cn/arcanists/ms-newbabel/)、[尼克·波顿](/zh-cn/arcanists/nick-bottom/)、[雾行者](/zh-cn/arcanists/oliver-fog/)、[坦南特](/zh-cn/arcanists/tennant/)、[小叶尼塞](/zh-cn/arcanists/yenisei/) |
| 反制 | 赋予持续的反制状态，被攻击时触发效果 | [6](/zh-cn/arcanists/6/)、[夏利](/zh-cn/arcanists/charlie/)、[沙丝绒](/zh-cn/arcanists/desert-flannel/)、[埃里克](/zh-cn/arcanists/erick/)、[恐怖通](/zh-cn/arcanists/horropedia/)、[曲娘](/zh-cn/arcanists/jiu-niangzi/)、[约翰·提托](/zh-cn/arcanists/john-titor/)、[莫桑女士](/zh-cn/arcanists/ms-moissan/)、[命名日](/zh-cn/arcanists/name-day/)、[皮克勒斯](/zh-cn/arcanists/pickles/)、[斯普特尼克](/zh-cn/arcanists/sputnik/)、[TTT](/zh-cn/arcanists/ttt/)、[X](/zh-cn/arcanists/x/) |
| 嘲讽 | 吸引敌人注意。受到部分攻击时，会优先成为攻击目标 | [星之眼](/zh-cn/arcanists/alien-t/)、[新巴别塔](/zh-cn/arcanists/ms-newbabel/)、[诺谛卡](/zh-cn/arcanists/nautika/)、[洋葱头](/zh-cn/arcanists/onion/)、[先驱者](/zh-cn/arcanists/pioneer/)、[吵闹鬼](/zh-cn/arcanists/poltergeist/)、[弄臣](/zh-cn/arcanists/the-fool/) |
| 坚固 | 被攻击时，受创减免+25%（生效后减少1层） | [37](/zh-cn/arcanists/37/)、[泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[阿夫西维](/zh-cn/arcanists/avgust/)、[铅玻璃](/zh-cn/arcanists/cristallo/)、[兔毛手袋](/zh-cn/arcanists/medicine-pocket/)、[雾行者](/zh-cn/arcanists/oliver-fog/)、[洋葱头](/zh-cn/arcanists/onion/)、[星锑](/zh-cn/arcanists/regulus/)、[维拉](/zh-cn/arcanists/vila/)、[远旅](/zh-cn/arcanists/voyager/)、[白朗姆](/zh-cn/arcanists/white-rum/)、[小叶尼塞](/zh-cn/arcanists/yenisei/) |
| 激昂 | 攻击时，创伤加成+50%（生效后减少1层） | [未锈铠](/zh-cn/arcanists/a-knight/)、[阿夫西维](/zh-cn/arcanists/avgust/)、[伊索尔德](/zh-cn/arcanists/isolde/)、[皮克勒斯](/zh-cn/arcanists/pickles/)、[白朗姆](/zh-cn/arcanists/white-rum/) |
| 爆发力 | 攻击时，创伤加成+25%(生效后减少1层） | [沙丝绒](/zh-cn/arcanists/desert-flannel/)、[伊索尔德](/zh-cn/arcanists/isolde/)、[维拉](/zh-cn/arcanists/vila/) |
| 免疫 | 不会受到【属性削弱】【状态异常】【控制】影响 | [帕米埃](/zh-cn/arcanists/dikke/)、[梁月](/zh-cn/arcanists/liang-yue/)、[诺谛卡](/zh-cn/arcanists/nautika/)、[小叶尼塞](/zh-cn/arcanists/yenisei/) |
| 愈合 | 回合开始时，基于使用者的攻击回复生命 | [泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[阿夫西维](/zh-cn/arcanists/avgust/)、[苏芙比](/zh-cn/arcanists/sotheby/) |
| 隐蔽 | 闪避非至终的仪式的现实创伤攻击 | [诺谛卡](/zh-cn/arcanists/nautika/)、[吵闹鬼](/zh-cn/arcanists/poltergeist/)、[TTT](/zh-cn/arcanists/ttt/) |
| 咒语强化Ⅰ | 回合开始时，随机1张咒语阶次+1 | [6](/zh-cn/arcanists/6/)、[泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[阿尔古斯](/zh-cn/arcanists/argus/)、[小叶尼塞](/zh-cn/arcanists/yenisei/) |
| 咒语强化Ⅱ | 回合开始时，随机2张咒语阶次+1 | [泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[阿尔古斯](/zh-cn/arcanists/argus/)、[贝蒂](/zh-cn/arcanists/bette/)、[伽菈波那](/zh-cn/arcanists/kaalaa-baunaa/) |
| 连续行动Ⅰ | 行动点+1 | [37](/zh-cn/arcanists/37/)、[阿莱夫](/zh-cn/arcanists/aleph/)、[程和光](/zh-cn/arcanists/cheng-heguang/)、[纸信圈儿](/zh-cn/arcanists/flutterpage/)、[洛伦兹蝴蝶](/zh-cn/arcanists/lorentz-butterfly/)、[马库斯](/zh-cn/arcanists/marcus/)、[莫莉德尔](/zh-cn/arcanists/moldir/)、[牙仙](/zh-cn/arcanists/tooth-fairy/) |

## 队伍机制

由一群神秘学家共同累积的资源与效果。在中国大陆版客户端中，薪血、余辉与洞知眼无法同时存在；国际版客户端的薪血与余辉文字没有这一条，洞知则只在中国大陆版上线。

| 状态 | 效果 | 技能中提到它的神秘学家 |
| --- | --- | --- |
| 薪血 | 己方队伍每累计损失3000生命，薪血+1（受到攻击损失的生命仅记录30%）；与【余辉】【洞知眼】无法同时存在 | [温妮弗雷德](/zh-cn/arcanists/eternity/)、[爱兹拉](/zh-cn/arcanists/ezra/)、[诺谛卡](/zh-cn/arcanists/nautika/)、[野树莓](/zh-cn/arcanists/rubuska/)、[塞梅尔维斯](/zh-cn/arcanists/semmelweis/)、[玛丽安娜](/zh-cn/arcanists/sentinel/) |
| 余辉 | 任意敌方被赋予【燃烧】【光晕】将积累【余辉】，怪物数量越少，积累的【余辉】越多；与【薪血】【洞知眼】无法同时存在 | [贝丽尔](/zh-cn/arcanists/beryl/)、[德雷克](/zh-cn/arcanists/drake/)、[伊索尔德](/zh-cn/arcanists/isolde/)、[洛伦兹蝴蝶](/zh-cn/arcanists/lorentz-butterfly/)、[玛尔纱](/zh-cn/arcanists/marsha/)、[玛蒂尔达](/zh-cn/arcanists/matilda/)、[可燃点](/zh-cn/arcanists/spathodea/) |
| 洞知眼 | 在使用咒语前，若至少拥有6个【洞知点】，可进入【弱点洞穿】阶段；与【余辉】【薪血】无法同时存在 | [37](/zh-cn/arcanists/37/)、[狩勋女巫红弩箭](/zh-cn/arcanists/huntsworn-lilya/)、[佩施塔](/zh-cn/arcanists/perchta/) |
| 启示 | 每消耗1点灵光会累计1点启示；每回合开始时随机分配给普通咒语（每张普通咒语最多分配5点，回合结束时未使用的咒语所携带的启示将被清除）；主动使用携带【启示】的咒语，将在咒语序列最后追加【即兴咒语】，且咒语会将其携带的启示计入本次【即兴咒语】 | [阿莱夫](/zh-cn/arcanists/aleph/)、[泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[芭卡洛儿](/zh-cn/arcanists/barcarola/)、[库珀花环](/zh-cn/arcanists/kiperina/)、[玛蒂尔达](/zh-cn/arcanists/matilda/)、[鹭鸶剪](/zh-cn/arcanists/paper-heron/)、[星锑](/zh-cn/arcanists/regulus/)、[牙仙](/zh-cn/arcanists/tooth-fairy/)、[远旅](/zh-cn/arcanists/voyager/) |
| 即兴咒语 | 单体攻击，对随机1名敌方目标造成200%精神创伤，本次攻击额外造成15%\*计入启示数量的精神创伤，当计入的启示大于等于3/6/12/20时，攻击次数+1/2/3/5（即兴咒语造成伤害时使用己方全体的平均属性进行计算） | [阿莱夫](/zh-cn/arcanists/aleph/)、[泥鯭的士](/zh-cn/arcanists/an-an-lee/)、[芭卡洛儿](/zh-cn/arcanists/barcarola/)、[库珀花环](/zh-cn/arcanists/kiperina/)、[玛蒂尔达](/zh-cn/arcanists/matilda/)、[鹭鸶剪](/zh-cn/arcanists/paper-heron/)、[星锑](/zh-cn/arcanists/regulus/)、[牙仙](/zh-cn/arcanists/tooth-fairy/)、[远旅](/zh-cn/arcanists/voyager/) |
| 电能 | 科技的产物，用来使用精密器械（可以叠加，最多叠加30层，不可驱散） | [灰调蓝](/zh-cn/arcanists/brume/)、[卡戎](/zh-cn/arcanists/charon/)、[告死鸟](/zh-cn/arcanists/corvus/)、[哑谜](/zh-cn/arcanists/enigma/)、[爱兹拉](/zh-cn/arcanists/ezra/)、[露西](/zh-cn/arcanists/lucy/)、[乌尔里希](/zh-cn/arcanists/ulrich/) |
| 涌动电场 | 回合开始时，涌动电场根据注入【电能】层数升级：注入【电能】值大于等于50时，术阵升级成【涌动电场lv2】，注入【电能】值大于等于120时，术阵升级成【涌动电场lv3】（当涌动电场消失时，注入的【电能】值将一同清空） | [灰调蓝](/zh-cn/arcanists/brume/)、[卡戎](/zh-cn/arcanists/charon/)、[告死鸟](/zh-cn/arcanists/corvus/)、[哑谜](/zh-cn/arcanists/enigma/)、[爱兹拉](/zh-cn/arcanists/ezra/)、[露西](/zh-cn/arcanists/lucy/)、[乌尔里希](/zh-cn/arcanists/ulrich/) |
| 术具 | 通过使用交感能量为术具充能，在行动序列末尾，术具循环运转，消耗交感能量释放咒语 | [珐琅眼](/zh-cn/arcanists/coppelia/)、[回声谣](/zh-cn/arcanists/everecho/)、[赫多涅](/zh-cn/arcanists/hedone/)、[星锑](/zh-cn/arcanists/regulus/)、[双生舞伶](/zh-cn/arcanists/the-twins/) |
| 礼仪 | 仪式威力提升3%（效果可叠加，最多叠加100层，不可驱散，释放至终的仪式后消失） | [拉拉泉](/zh-cn/arcanists/la-source/)、[红弩箭](/zh-cn/arcanists/lilya/)、[邓肯先生](/zh-cn/arcanists/mr-duncan/)、[命名日](/zh-cn/arcanists/name-day/)、[鬃毛沙砾](/zh-cn/arcanists/shamane/) |
| 主格特殊咒语 | 释放该咒语视为角色主动行动 | [贝丽尔](/zh-cn/arcanists/beryl/)、[冷周六](/zh-cn/arcanists/hissabeth/)、[卡珊德拉](/zh-cn/arcanists/kassandra/)、[无名者](/zh-cn/arcanists/ms-stranger/) |
| 稳态本源创伤 | 该类型的本源创伤不会受到属性加成影响 | [赫多涅](/zh-cn/arcanists/hedone/)、[卡卡尼亚](/zh-cn/arcanists/kakania/)、[洛伦兹蝴蝶](/zh-cn/arcanists/lorentz-butterfly/) |
