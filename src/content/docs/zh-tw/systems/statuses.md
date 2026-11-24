---
title: "狀態效果"
description: "重返未來：1999 的狀態效果：正面與負面類型、控制效果，以及多位神秘學家共用的狀態。"
appliesTo: "重返未來：1999，中國大陸版用戶端 113.0.1422（4.1 版）；國際版用戶端 111.0.1077（3.9 版）"
caveat: "石化在持有者受到現實創傷攻擊時解除，冰凍則在受到精神創傷攻擊時解除，因此對應類型的攻擊會讓受控制的敵人脫離控制。"
lastVerified: 2026-11-23
aliases:
  - "Statuses"
  - "状态效果"
  - "状態効果"
  - "상태 효과"
  - "Status effects"
  - "Buffs and debuffs"
  - "Control"
  - "控制"
sources:
  - title: "re1999-data，中國大陸版用戶端 113.0.1422：skill_eff_desc.json（狀態）與每位神秘學家的技能文字"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/skill_eff_desc.json
  - title: "re1999-data-global，國際版用戶端 111.0.1077：skill_eff_desc.json 與各語言文字"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/skill_eff_desc.json
  - title: "re1999-data-global，國際版用戶端 111.0.1077：loading_text.json（作戰手冊提示）"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/loading_text.json
---
## 狀態的種類

每個狀態都屬於正面或負面。正面類型為屬性提升、狀態增益與反制，驅散可以移除；負面類型為屬性削弱、狀態異常與控制，淨化可以移除。遊戲標示為無法驅散的狀態不會被移除。

同名狀態再次施加時，依兩者的強度與持續時間覆蓋前一個。咒語的特殊效果可能被目標抵抗；免疫擋下所有負面類型。

## 控制

控制狀態讓角色無法行動，或限制它能施放的咒語。有三種狀態在疊加到 2 層時會轉為其中一種控制。

| 狀態 | 效果 | 技能中提到它的神秘學家 |
| --- | --- | --- |
| 眩暈 | 無法行動 | [泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[卡珊卓](/zh-tw/arcanists/kassandra/)、[兔毛手袋](/zh-tw/arcanists/medicine-pocket/)、[瑪麗蓮](/zh-tw/arcanists/sweetheart/)、[白朗姆](/zh-tw/arcanists/white-rum/) |
| 石化 | 無法行動，受到現實創傷攻擊後解除 | [槲寄生](/zh-tw/arcanists/druvis-iii/)、[潔西卡](/zh-tw/arcanists/jessica/)、[五色月](/zh-tw/arcanists/satsuki/) |
| 冰凍 | 無法行動，受到精神創傷攻擊後解除 | [J](/zh-tw/arcanists/j/)、[莫桑女士](/zh-tw/arcanists/ms-moissan/) |
| 噩夢 | 無法行動，受到任意攻擊後解除 | [嬰兒藍](/zh-tw/arcanists/baby-blue/)、[挖掘藝術](/zh-tw/arcanists/diggers/)、[麗莎&路易斯](/zh-tw/arcanists/twins-sleep/) |
| 繳械 | 無法使用攻擊類普通咒語 | [星之眼](/zh-tw/arcanists/alien-t/)、[埃里克](/zh-tw/arcanists/erick/)、[十四行詩](/zh-tw/arcanists/sonetto/)、[斯普特尼克](/zh-tw/arcanists/sputnik/) |
| 緘默 | 無法使用增益、減益、治療、反制類普通咒語 | [星之眼](/zh-tw/arcanists/alien-t/)、[埃里克](/zh-tw/arcanists/erick/)、[斯普特尼克](/zh-tw/arcanists/sputnik/)、[遠旅](/zh-tw/arcanists/voyager/)、[X](/zh-tw/arcanists/x/)、[冬](/zh-tw/arcanists/zima/) |
| 封印 | 無法使用至終的儀式 | [柏林以東](/zh-tw/arcanists/bkornblume/)、[拉拉泉](/zh-tw/arcanists/la-source/)、[遠旅](/zh-tw/arcanists/voyager/)、[冬](/zh-tw/arcanists/zima/) |
| 僵硬 | 疊加到2層時，變為石化或使已存在的石化持續時間+1 | [泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[冷週六](/zh-tw/arcanists/hissabeth/)、[五色月](/zh-tw/arcanists/satsuki/) |
| 寒冷 | 疊加到2層時，變為冰凍或使已存在的冰凍持續時間+1 | [J](/zh-tw/arcanists/j/) |
| 麻痹 | 疊加到2層時，變為眩暈或使已存在的眩暈持續時間+1 | [小梅斯梅爾](/zh-tw/arcanists/mesmer-jr/) |

## 持續傷害與其他減益

這些狀態造成的傷害為本源創傷。

| 狀態 | 效果 | 技能中提到它的神秘學家 |
| --- | --- | --- |
| 燃燒 | 受到治療效果降低15%（效果不疊加)；回合結束時受到基於攜帶者攻擊\*4%的本源創傷（效果可疊加，最多可疊加30層，多層燃燒僅視為1個【狀態異常】，生效後扣除一半層數) | [6](/zh-tw/arcanists/6/)、[泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[貝麗爾](/zh-tw/arcanists/beryl/)、[灰調藍](/zh-tw/arcanists/brume/)、[德雷克](/zh-tw/arcanists/drake/)、[伊索爾德](/zh-tw/arcanists/isolde/)、[J](/zh-tw/arcanists/j/)、[梁月](/zh-tw/arcanists/liang-yue/)、[洛倫茲蝴蝶](/zh-tw/arcanists/lorentz-butterfly/)、[瑪爾紗](/zh-tw/arcanists/marsha/)、[瑪蒂爾達](/zh-tw/arcanists/matilda/)、[可燃點](/zh-tw/arcanists/spathodea/)、[和平烏魯](/zh-tw/arcanists/ulu/) |
| 光暈 | 受到治療效果降低25%（效果不疊加)；回合結束時受到基於初始來源攻擊\*4%的本源創傷（效果可疊加，最多可疊加30層，多層光暈僅視為1個【狀態異常】，生效後扣除一半層數) | [德雷克](/zh-tw/arcanists/drake/)、[伊索爾德](/zh-tw/arcanists/isolde/)、[洛倫茲蝴蝶](/zh-tw/arcanists/lorentz-butterfly/)、[瑪爾紗](/zh-tw/arcanists/marsha/)、[瑪蒂爾達](/zh-tw/arcanists/matilda/)、[可燃點](/zh-tw/arcanists/spathodea/) |
| 中毒 | 回合結束時，受到基於釋放者攻擊的本源創傷（可以疊加） | [6](/zh-tw/arcanists/6/)、[泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[溫妮弗雷德](/zh-tw/arcanists/eternity/)、[埃齊歐·奧迪托雷](/zh-tw/arcanists/ezio-auditore/)、[潔西卡](/zh-tw/arcanists/jessica/)、[坎吉拉](/zh-tw/arcanists/kanjira/)、[梁月](/zh-tw/arcanists/liang-yue/)、[愛寵](/zh-tw/arcanists/rabies/)、[拉莫納](/zh-tw/arcanists/ramona/)、[蘇芙比](/zh-tw/arcanists/sotheby/)、[藍手帕](/zh-tw/arcanists/tuesday/)、[篤篤骨](/zh-tw/arcanists/willow/) |
| 流血 | 行動後，受到使用者攻擊\*100%的本源創傷 | [溫妮弗雷德](/zh-tw/arcanists/eternity/)、[諾諦卡](/zh-tw/arcanists/nautika/)、[白朗姆](/zh-tw/arcanists/white-rum/) |
| 腐蝕 | 回合結束時，受到基於持有者當前生命的本源創傷 | [溫妮弗雷德](/zh-tw/arcanists/eternity/)、[弄臣](/zh-tw/arcanists/the-fool/) |
| 重傷 | 受到的治療效果-50% | [芭妮芭妮](/zh-tw/arcanists/bunny-bunny/)、[鉛玻璃](/zh-tw/arcanists/cristallo/)、[溫妮弗雷德](/zh-tw/arcanists/eternity/)、[銀裝小春雀兒](/zh-tw/arcanists/silverwing-eagle/) |
| 虛弱 | 攻擊時，創傷加成-25%（生效後減少1層） | [柏林以東](/zh-tw/arcanists/bkornblume/)、[百夫長](/zh-tw/arcanists/centurion/)、[挖掘藝術](/zh-tw/arcanists/diggers/)、[拉拉泉](/zh-tw/arcanists/la-source/)、[羅蕾萊](/zh-tw/arcanists/lorelei/)、[馬庫斯](/zh-tw/arcanists/marcus/)、[麗莎&路易斯](/zh-tw/arcanists/twins-sleep/) |
| 致盲 | 單體攻擊時，創傷加成-30% | [6](/zh-tw/arcanists/6/)、[喀嚓喀嚓](/zh-tw/arcanists/click/) |
| 失準 | 群體攻擊時，創傷加成-30% | [6](/zh-tw/arcanists/6/) |
| 明昧 | 抗暴率-25%（效果可疊加，每層時間獨立計算） | [金蜜兒](/zh-tw/arcanists/blonney/)、[坎吉拉](/zh-tw/arcanists/kanjira/)、[瑪蒂爾達](/zh-tw/arcanists/matilda/)、[牙仙](/zh-tw/arcanists/tooth-fairy/)、[遠旅](/zh-tw/arcanists/voyager/)、[北方哨歌](/zh-tw/arcanists/windsong/) |
| 憂懼 | 受到的精神創傷提升25%（生效後減少1層） | [數羊羔](/zh-tw/arcanists/barbara/)、[恐怖通](/zh-tw/arcanists/horropedia/)、[諾諦卡](/zh-tw/arcanists/nautika/) |
| 心神不寧 | 無法提升激情 | [無線電小姐](/zh-tw/arcanists/ms-radio/)、[TTT](/zh-tw/arcanists/ttt/)、[X](/zh-tw/arcanists/x/) |
| 激情萃取 | 受到攻擊後，攻擊者獲得1點激情（生效後減少1層） | [梅蘭妮](/zh-tw/arcanists/melania/)、[莫莉德爾](/zh-tw/arcanists/moldir/)、[納西瑟斯](/zh-tw/arcanists/narcissus/)、[虛構集](/zh-tw/arcanists/recoleta/) |

## 增益

多位神秘學家能賦予的正面狀態。

| 狀態 | 效果 | 技能中提到它的神秘學家 |
| --- | --- | --- |
| 護盾 | 持續時間內，抵擋一定創傷 | [數羊羔](/zh-tw/arcanists/barbara/)、[貝蒂](/zh-tw/arcanists/bette/)、[門](/zh-tw/arcanists/door/)、[愛茲拉](/zh-tw/arcanists/ezra/)、[J](/zh-tw/arcanists/j/)、[曲娘](/zh-tw/arcanists/jiu-niangzi/)、[約翰·提托](/zh-tw/arcanists/john-titor/)、[庫珀花環](/zh-tw/arcanists/kiperina/)、[瑪爾紗](/zh-tw/arcanists/marsha/)、[莫桑女士](/zh-tw/arcanists/ms-moissan/)、[新巴別塔](/zh-tw/arcanists/ms-newbabel/)、[尼克·波頓](/zh-tw/arcanists/nick-bottom/)、[霧行者](/zh-tw/arcanists/oliver-fog/)、[坦南特](/zh-tw/arcanists/tennant/)、[小葉尼塞](/zh-tw/arcanists/yenisei/) |
| 反制 | 賦予持續的反制狀態，被攻擊時觸發效果 | [6](/zh-tw/arcanists/6/)、[夏利](/zh-tw/arcanists/charlie/)、[沙絲絨](/zh-tw/arcanists/desert-flannel/)、[埃里克](/zh-tw/arcanists/erick/)、[恐怖通](/zh-tw/arcanists/horropedia/)、[曲娘](/zh-tw/arcanists/jiu-niangzi/)、[約翰·提托](/zh-tw/arcanists/john-titor/)、[莫桑女士](/zh-tw/arcanists/ms-moissan/)、[命名日](/zh-tw/arcanists/name-day/)、[皮克勒斯](/zh-tw/arcanists/pickles/)、[斯普特尼克](/zh-tw/arcanists/sputnik/)、[TTT](/zh-tw/arcanists/ttt/)、[X](/zh-tw/arcanists/x/) |
| 嘲諷 | 吸引敵人注意。受到部分攻擊時，會優先成為攻擊目標 | [星之眼](/zh-tw/arcanists/alien-t/)、[新巴別塔](/zh-tw/arcanists/ms-newbabel/)、[諾諦卡](/zh-tw/arcanists/nautika/)、[洋蔥頭](/zh-tw/arcanists/onion/)、[先驅者](/zh-tw/arcanists/pioneer/)、[吵鬧鬼](/zh-tw/arcanists/poltergeist/)、[弄臣](/zh-tw/arcanists/the-fool/) |
| 堅固 | 被攻擊時，受創減免+25%（生效後減少1層） | [37](/zh-tw/arcanists/37/)、[泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[阿夫西維](/zh-tw/arcanists/avgust/)、[鉛玻璃](/zh-tw/arcanists/cristallo/)、[兔毛手袋](/zh-tw/arcanists/medicine-pocket/)、[霧行者](/zh-tw/arcanists/oliver-fog/)、[洋蔥頭](/zh-tw/arcanists/onion/)、[星銻](/zh-tw/arcanists/regulus/)、[維拉](/zh-tw/arcanists/vila/)、[遠旅](/zh-tw/arcanists/voyager/)、[白朗姆](/zh-tw/arcanists/white-rum/)、[小葉尼塞](/zh-tw/arcanists/yenisei/) |
| 激昂 | 攻擊時，創傷加成+50%（生效後減少1層） | [未鏽鎧](/zh-tw/arcanists/a-knight/)、[阿夫西維](/zh-tw/arcanists/avgust/)、[伊索爾德](/zh-tw/arcanists/isolde/)、[皮克勒斯](/zh-tw/arcanists/pickles/)、[白朗姆](/zh-tw/arcanists/white-rum/) |
| 爆發力 | 攻擊時，創傷加成+25%(生效後減少1層） | [沙絲絨](/zh-tw/arcanists/desert-flannel/)、[伊索爾德](/zh-tw/arcanists/isolde/)、[維拉](/zh-tw/arcanists/vila/) |
| 免疫 | 不會受到【屬性削弱】【狀態異常】【控制】影響 | [帕米埃](/zh-tw/arcanists/dikke/)、[梁月](/zh-tw/arcanists/liang-yue/)、[諾諦卡](/zh-tw/arcanists/nautika/)、[小葉尼塞](/zh-tw/arcanists/yenisei/) |
| 癒合 | 回合開始時，基於使用者的攻擊回復生命 | [泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[阿夫西維](/zh-tw/arcanists/avgust/)、[蘇芙比](/zh-tw/arcanists/sotheby/) |
| 隱蔽 | 閃避非至終的儀式的現實創傷攻擊 | [諾諦卡](/zh-tw/arcanists/nautika/)、[吵鬧鬼](/zh-tw/arcanists/poltergeist/)、[TTT](/zh-tw/arcanists/ttt/) |
| 咒語強化Ⅰ | 回合開始時，隨機1張咒語階級+1 | [6](/zh-tw/arcanists/6/)、[泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[阿爾古斯](/zh-tw/arcanists/argus/)、[小葉尼塞](/zh-tw/arcanists/yenisei/) |
| 咒語強化Ⅱ | 回合開始時，隨機2張咒語階級+1 | [泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[阿爾古斯](/zh-tw/arcanists/argus/)、[貝蒂](/zh-tw/arcanists/bette/)、[伽菈波那](/zh-tw/arcanists/kaalaa-baunaa/) |
| 連續行動Ⅰ | 行動點+1 | [37](/zh-tw/arcanists/37/)、[阿萊夫](/zh-tw/arcanists/aleph/)、[程和光](/zh-tw/arcanists/cheng-heguang/)、[紙信圈兒](/zh-tw/arcanists/flutterpage/)、[洛倫茲蝴蝶](/zh-tw/arcanists/lorentz-butterfly/)、[馬庫斯](/zh-tw/arcanists/marcus/)、[莫莉德爾](/zh-tw/arcanists/moldir/)、[牙仙](/zh-tw/arcanists/tooth-fairy/) |

## 隊伍機制

由一群神秘學家共同累積的資源與效果。在中國大陸版用戶端中，薪血、餘輝與洞知眼無法同時存在；國際版用戶端的薪血與餘輝文字沒有這一條，洞知則只在中國大陸版上線。

| 狀態 | 效果 | 技能中提到它的神秘學家 |
| --- | --- | --- |
| 薪血 | 己方隊伍每累計損失3000生命，薪血+1（受到攻擊損失的生命僅記錄30%） | [溫妮弗雷德](/zh-tw/arcanists/eternity/)、[愛茲拉](/zh-tw/arcanists/ezra/)、[諾諦卡](/zh-tw/arcanists/nautika/)、[野樹莓](/zh-tw/arcanists/rubuska/)、[塞梅爾維斯](/zh-tw/arcanists/semmelweis/)、[瑪麗安娜](/zh-tw/arcanists/sentinel/) |
| 餘輝 | 任意敵方被賦予【燃燒】【光暈】將積累【餘輝】，怪物數量越少，積累的【餘輝】越多 | [貝麗爾](/zh-tw/arcanists/beryl/)、[德雷克](/zh-tw/arcanists/drake/)、[伊索爾德](/zh-tw/arcanists/isolde/)、[洛倫茲蝴蝶](/zh-tw/arcanists/lorentz-butterfly/)、[瑪爾紗](/zh-tw/arcanists/marsha/)、[瑪蒂爾達](/zh-tw/arcanists/matilda/)、[可燃點](/zh-tw/arcanists/spathodea/) |
| 洞知眼（非官方） | 國際版尚無此狀態 | [37](/zh-tw/arcanists/37/)、[狩勳女巫紅弩箭](/zh-tw/arcanists/huntsworn-lilya/)、[佩施塔](/zh-tw/arcanists/perchta/) |
| 啟示 | 每消耗1點靈光會累計1點啟示；每回合開始時隨機分配給普通咒語（每張普通咒語最多分配5點，回合結束時未使用的咒語所攜帶的啟示將被清除）；主動使用攜帶【啟示】的咒語，將在咒語序列最後追加【即興咒語】，且咒語會將其攜帶的啟示計入本次【即興咒語】 | [阿萊夫](/zh-tw/arcanists/aleph/)、[泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[芭卡洛兒](/zh-tw/arcanists/barcarola/)、[庫珀花環](/zh-tw/arcanists/kiperina/)、[瑪蒂爾達](/zh-tw/arcanists/matilda/)、[鷺鷥剪](/zh-tw/arcanists/paper-heron/)、[星銻](/zh-tw/arcanists/regulus/)、[牙仙](/zh-tw/arcanists/tooth-fairy/)、[遠旅](/zh-tw/arcanists/voyager/) |
| 即興咒語 | 單體攻擊，對隨機1名敵方目標造成200%精神創傷，本次攻擊額外造成15%\*計入啟示數量的精神創傷，當計入的啟示大於等於3/6/12/20時，攻擊次數+1/2/3/5（即興咒語造成傷害時使用己方全體的平均屬性進行計算） | [阿萊夫](/zh-tw/arcanists/aleph/)、[泥鯭的士](/zh-tw/arcanists/an-an-lee/)、[芭卡洛兒](/zh-tw/arcanists/barcarola/)、[庫珀花環](/zh-tw/arcanists/kiperina/)、[瑪蒂爾達](/zh-tw/arcanists/matilda/)、[鷺鷥剪](/zh-tw/arcanists/paper-heron/)、[星銻](/zh-tw/arcanists/regulus/)、[牙仙](/zh-tw/arcanists/tooth-fairy/)、[遠旅](/zh-tw/arcanists/voyager/) |
| 電能 | 科技的產物，用來使用精密器械（可以疊加，最多疊加30層，不可驅散） | [灰調藍](/zh-tw/arcanists/brume/)、[卡戎](/zh-tw/arcanists/charon/)、[告死鳥](/zh-tw/arcanists/corvus/)、[啞謎](/zh-tw/arcanists/enigma/)、[愛茲拉](/zh-tw/arcanists/ezra/)、[露西](/zh-tw/arcanists/lucy/)、[烏爾里希](/zh-tw/arcanists/ulrich/) |
| 湧動電場 | 回合開始時，湧動電場根據注入【電能】層數升級：注入【電能】值大於等於50時，術陣升級成【湧動電場lv2】，注入【電能】值大於等於120時，術陣升級成【湧動電場lv3】（當湧動電場消失時，注入的【電能】值將一同清空） | [灰調藍](/zh-tw/arcanists/brume/)、[卡戎](/zh-tw/arcanists/charon/)、[告死鳥](/zh-tw/arcanists/corvus/)、[啞謎](/zh-tw/arcanists/enigma/)、[愛茲拉](/zh-tw/arcanists/ezra/)、[露西](/zh-tw/arcanists/lucy/)、[烏爾里希](/zh-tw/arcanists/ulrich/) |
| 術具 | 通過使用交感能量為術具充能，在行動序列末尾，術具循環運轉，消耗交感能量釋放咒語 | [琺瑯眼](/zh-tw/arcanists/coppelia/)、[回聲謠](/zh-tw/arcanists/everecho/)、[赫多涅](/zh-tw/arcanists/hedone/)、[星銻](/zh-tw/arcanists/regulus/)、[雙生舞伶](/zh-tw/arcanists/the-twins/) |
| 禮儀 | 儀式威力提升3%（效果可疊加，最多疊加100層，不可驅散，釋放至終的儀式後消失） | [拉拉泉](/zh-tw/arcanists/la-source/)、[紅弩箭](/zh-tw/arcanists/lilya/)、[鄧肯先生](/zh-tw/arcanists/mr-duncan/)、[命名日](/zh-tw/arcanists/name-day/)、[鬃毛沙礫](/zh-tw/arcanists/shamane/) |
| 主格特殊咒語 | 釋放該咒語視為角色主動行動 | [貝麗爾](/zh-tw/arcanists/beryl/)、[冷週六](/zh-tw/arcanists/hissabeth/)、[卡珊卓](/zh-tw/arcanists/kassandra/)、[無名者](/zh-tw/arcanists/ms-stranger/) |
| 穩態本源創傷 | 該類型的本源創傷不會受到屬性加成影響 | [赫多涅](/zh-tw/arcanists/hedone/)、[卡卡尼亞](/zh-tw/arcanists/kakania/)、[洛倫茲蝴蝶](/zh-tw/arcanists/lorentz-butterfly/) |
