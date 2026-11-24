---
title: "状態効果"
description: "リバース：1999 の状態効果：プラスとマイナスの種類、行動阻害、複数の神秘学家が共有する状態。"
appliesTo: "リバース：1999、中国本土版クライアント 113.0.1422（バージョン 4.1）。グローバル版クライアント 111.0.1077（バージョン 3.9）"
caveat: "石化はリアルダメージの攻撃を、氷結はメンタルダメージの攻撃を受けると解けるため、その種類の攻撃で行動阻害中の敵が動けるようになる。"
lastVerified: 2026-11-23
aliases:
  - "Statuses"
  - "狀態效果"
  - "状态效果"
  - "상태 효과"
  - "Status effects"
  - "Buffs and debuffs"
  - "Control"
  - "控制"
sources:
  - title: "re1999-data、中国本土版クライアント 113.0.1422：skill_eff_desc.json（状態）と全神秘学家のスキルテキスト"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/skill_eff_desc.json
  - title: "re1999-data-global、グローバル版クライアント 111.0.1077：skill_eff_desc.json と各言語のテキスト"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/skill_eff_desc.json
  - title: "re1999-data-global、グローバル版クライアント 111.0.1077：loading_text.json（作戦マニュアルのヒント）"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/loading_text.json
---
## 状態の種類

状態はすべてプラスかマイナスのどちらかに分かれる。プラスの種類はステータス上昇、状態強化、カウンターで、バフ解除で取り除かれる。マイナスの種類はステータス低下、状態異常、行動阻害で、デバフ解除で取り除かれる。ゲームが解除されないと定めた状態は残る。

同名の状態を重ねて受けると、効果量と持続ターンに応じて前の状態が上書きされる。スペルの特殊効果は対象に抵抗されることがあり、弱体無効はマイナスの種類をすべて防ぐ。

## 行動阻害

行動阻害の状態は、キャラクターの行動を止めるか、使えるスペルを制限する。3つの状態は2スタックたまると、そのうちの1つに変わる。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| 気絶 | 行動不能 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[カサンドラ](/ja/arcanists/kassandra/)、[メディスンポケット](/ja/arcanists/medicine-pocket/)、[スイートハート](/ja/arcanists/sweetheart/)、[ホワイトラム](/ja/arcanists/white-rum/) |
| 石化 | 行動不能。リアルダメージを受けると解除される。 | [ドルーヴィスⅢ](/ja/arcanists/druvis-iii/)、[ジェシカ](/ja/arcanists/jessica/)、[五色月](/ja/arcanists/satsuki/) |
| 氷結 | 行動不能。メンタルダメージを受けると解除される。 | [J](/ja/arcanists/j/)、[ミス・モアッサン](/ja/arcanists/ms-moissan/) |
| 悪夢 | 行動不能。いずれかのダメージを受けると解除される。 | [ベビーブルー](/ja/arcanists/baby-blue/)、[ディガー](/ja/arcanists/diggers/)、[リサ＆ルイス](/ja/arcanists/twins-sleep/) |
| 武装解除 | アタック系スペルが使用できない。 | [ギベオンズアイ](/ja/arcanists/alien-t/)、[エリック](/ja/arcanists/erick/)、[ソネット](/ja/arcanists/sonetto/)、[スプートニク](/ja/arcanists/sputnik/) |
| 沈黙 | バフ・デバフ・ヒール・カウンター系スペルが使用できない。 | [ギベオンズアイ](/ja/arcanists/alien-t/)、[エリック](/ja/arcanists/erick/)、[スプートニク](/ja/arcanists/sputnik/)、[ボイジャー](/ja/arcanists/voyager/)、[X](/ja/arcanists/x/)、[ズィマー](/ja/arcanists/zima/) |
| 封印 | アルティメットが使用不能。 | [コーンブルメ](/ja/arcanists/bkornblume/)、[ララ・ファウンテン](/ja/arcanists/la-source/)、[ボイジャー](/ja/arcanists/voyager/)、[ズィマー](/ja/arcanists/zima/) |
| 硬直 | 2回までスタックすると、石化効果に変わる。石化がすでに存在する場合はその効果の持続ターン+1。 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[サーベス](/ja/arcanists/hissabeth/)、[五色月](/ja/arcanists/satsuki/) |
| コールド | 2回までスタックすると、氷結効果に変わる。氷結がすでに存在する場合はその効果の持続ターン+1。 | [J](/ja/arcanists/j/) |
| めまい | 2回までスタックすると、気絶効果に変わる。気絶がすでに存在する場合はその効果の持続ターン+1。 | [メスメル・Jr.](/ja/arcanists/mesmer-jr/) |

## 継続ダメージとその他のデバフ

これらの状態が与えるダメージはジェネシスダメージである。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| 燃焼 | 被回復効果が15%ダウンする（この効果は累積不可）。ターン終了時、所持者の攻撃力×4%分のジェネシスダメージを受ける。（最大30スタック。複数の燃焼は1つの【状態異常】と見なされ、効果発生後、スタック数が半分差し引かれる） | [6](/ja/arcanists/6/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[ベリル](/ja/arcanists/beryl/)、[グレイッシュブルー](/ja/arcanists/brume/)、[ドレイク](/ja/arcanists/drake/)、[イゾルデ](/ja/arcanists/isolde/)、[J](/ja/arcanists/j/)、[梁月](/ja/arcanists/liang-yue/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マルシャ](/ja/arcanists/marsha/)、[マチルダ](/ja/arcanists/matilda/)、[カエンボク](/ja/arcanists/spathodea/)、[ウル](/ja/arcanists/ulu/) |
| 光輪 | 被回復効果が25%ダウンする（この効果は累積不可）。ターン終了時、初期発動者の攻撃力×4%分のジェネシスダメージを受ける。（最大30スタック。複数の光輪は1つの【状態異常】と見なされ、効果発生後、スタック数が半分差し引かれる） | [ドレイク](/ja/arcanists/drake/)、[イゾルデ](/ja/arcanists/isolde/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マルシャ](/ja/arcanists/marsha/)、[マチルダ](/ja/arcanists/matilda/)、[カエンボク](/ja/arcanists/spathodea/) |
| 中毒 | ターン終了時、発動者の攻撃力に基づいたジェネシスダメージを受ける。（スタック可） | [6](/ja/arcanists/6/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[エターニティ](/ja/arcanists/eternity/)、[エツィオ](/ja/arcanists/ezio-auditore/)、[ジェシカ](/ja/arcanists/jessica/)、[カンジーラ](/ja/arcanists/kanjira/)、[梁月](/ja/arcanists/liang-yue/)、[レイビーズ](/ja/arcanists/rabies/)、[ラモナ](/ja/arcanists/ramona/)、[サザビー](/ja/arcanists/sotheby/)、[チューズデー](/ja/arcanists/tuesday/)、[ヴィロー](/ja/arcanists/willow/) |
| 流血 | 行動終了後、発動者の攻撃力×100%のジェネシスダメージを受ける。 | [エターニティ](/ja/arcanists/eternity/)、[ノーティカ](/ja/arcanists/nautika/)、[ホワイトラム](/ja/arcanists/white-rum/) |
| 腐蝕 | ターン終了時、所有者の残りHPに基づいたジェネシスダメージを受ける。 | [エターニティ](/ja/arcanists/eternity/)、[ジェスター](/ja/arcanists/the-fool/) |
| 重傷 | 被回復効果-50%。 | [バニーバニー](/ja/arcanists/bunny-bunny/)、[クリスタッロ](/ja/arcanists/cristallo/)、[エターニティ](/ja/arcanists/eternity/)、[イーグル](/ja/arcanists/silverwing-eagle/) |
| 虚弱 | 攻撃する時、ダメージボーナス-25%。（発動すると1スタック減少） | [コーンブルメ](/ja/arcanists/bkornblume/)、[ケントゥリオン](/ja/arcanists/centurion/)、[ディガー](/ja/arcanists/diggers/)、[ララ・ファウンテン](/ja/arcanists/la-source/)、[ローレライ](/ja/arcanists/lorelei/)、[マーカス](/ja/arcanists/marcus/)、[リサ＆ルイス](/ja/arcanists/twins-sleep/) |
| 盲目 | 単体攻撃時、ダメージボーナス-30%。 | [6](/ja/arcanists/6/)、[カシャパシャ](/ja/arcanists/click/) |
| ミスエイム | 範囲攻撃時、ダメージボーナス-30%。 | [6](/ja/arcanists/6/) |
| 朦朧 | クリティカル耐性率-25%。（スタック可。各スタックの持続時間は単独で計算される） | [ジェイミー](/ja/arcanists/blonney/)、[カンジーラ](/ja/arcanists/kanjira/)、[マチルダ](/ja/arcanists/matilda/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/)、[ボイジャー](/ja/arcanists/voyager/)、[スヴィスティ](/ja/arcanists/windsong/) |
| 危惧 | 受けるメンタルダメージが25%アップする。（発動すると1スタック減少） | [メェプル](/ja/arcanists/barbara/)、[ホラーペディア](/ja/arcanists/horropedia/)、[ノーティカ](/ja/arcanists/nautika/) |
| 動揺 | MPが得られない。 | [ミス・ラジオ](/ja/arcanists/ms-radio/)、[TTT](/ja/arcanists/ttt/)、[X](/ja/arcanists/x/) |
| MPドレイン | 攻撃を受けると、攻撃者のMP+1。（効果発生後、1スタック減少） | [メラニア](/ja/arcanists/melania/)、[モルダー](/ja/arcanists/moldir/)、[ナルキッソス](/ja/arcanists/narcissus/)、[レコレータ](/ja/arcanists/recoleta/) |

## バフ

複数の神秘学家が付与するプラスの状態。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| シールド | 効果が持続している間、一定ダメージを防ぐ。 | [メェプル](/ja/arcanists/barbara/)、[ベティ](/ja/arcanists/bette/)、[ドア](/ja/arcanists/door/)、[エズラ](/ja/arcanists/ezra/)、[J](/ja/arcanists/j/)、[曲娘](/ja/arcanists/jiu-niangzi/)、[ジョン・タイター](/ja/arcanists/john-titor/)、[カイパリーナ](/ja/arcanists/kiperina/)、[マルシャ](/ja/arcanists/marsha/)、[ミス・モアッサン](/ja/arcanists/ms-moissan/)、[ニューバベル](/ja/arcanists/ms-newbabel/)、[ニック・ボトム](/ja/arcanists/nick-bottom/)、[オリバー・フォッグ](/ja/arcanists/oliver-fog/)、[テナント](/ja/arcanists/tennant/)、[エニセイ](/ja/arcanists/yenisei/) |
| カウンター | 持続的なカウンター状態。攻撃を受けると効果が発動する。 | [6](/ja/arcanists/6/)、[チャーリー](/ja/arcanists/charlie/)、[サンド・フランネル](/ja/arcanists/desert-flannel/)、[エリック](/ja/arcanists/erick/)、[ホラーペディア](/ja/arcanists/horropedia/)、[曲娘](/ja/arcanists/jiu-niangzi/)、[ジョン・タイター](/ja/arcanists/john-titor/)、[ミス・モアッサン](/ja/arcanists/ms-moissan/)、[ネイムデー](/ja/arcanists/name-day/)、[ピクルス](/ja/arcanists/pickles/)、[スプートニク](/ja/arcanists/sputnik/)、[TTT](/ja/arcanists/ttt/)、[X](/ja/arcanists/x/) |
| 挑発 | 敵の注意を引きつける。一部の攻撃を受けた際に、優先的に攻撃の対象に選ばれる。 | [ギベオンズアイ](/ja/arcanists/alien-t/)、[ニューバベル](/ja/arcanists/ms-newbabel/)、[ノーティカ](/ja/arcanists/nautika/)、[オニオン](/ja/arcanists/onion/)、[パイオニア](/ja/arcanists/pioneer/)、[ポルターガイスト](/ja/arcanists/poltergeist/)、[ジェスター](/ja/arcanists/the-fool/) |
| 強固 | 攻撃を受けた時、ダメージ軽減+25%。（発動すると1スタック減少） | [37](/ja/arcanists/37/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[アヴグスト](/ja/arcanists/avgust/)、[クリスタッロ](/ja/arcanists/cristallo/)、[メディスンポケット](/ja/arcanists/medicine-pocket/)、[オリバー・フォッグ](/ja/arcanists/oliver-fog/)、[オニオン](/ja/arcanists/onion/)、[レグルス](/ja/arcanists/regulus/)、[ヴィラ](/ja/arcanists/vila/)、[ボイジャー](/ja/arcanists/voyager/)、[ホワイトラム](/ja/arcanists/white-rum/)、[エニセイ](/ja/arcanists/yenisei/) |
| 激昂 | 攻撃する時、ダメージボーナス+50%。（発動すると1スタック減少） | [ナイト](/ja/arcanists/a-knight/)、[アヴグスト](/ja/arcanists/avgust/)、[イゾルデ](/ja/arcanists/isolde/)、[ピクルス](/ja/arcanists/pickles/)、[ホワイトラム](/ja/arcanists/white-rum/) |
| 瞬発力 | 攻撃時、ダメージボーナス+25%。（発動すると1スタック減少） | [サンド・フランネル](/ja/arcanists/desert-flannel/)、[イゾルデ](/ja/arcanists/isolde/)、[ヴィラ](/ja/arcanists/vila/) |
| 弱体無効 | 【ステータス低下】【状態異常】【行動阻害】にかからなくなる。 | [パミエ](/ja/arcanists/dikke/)、[梁月](/ja/arcanists/liang-yue/)、[ノーティカ](/ja/arcanists/nautika/)、[エニセイ](/ja/arcanists/yenisei/) |
| 継続回復 | ターン開始時、発動者の攻撃力に基づいてHPを回復する。 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[アヴグスト](/ja/arcanists/avgust/)、[サザビー](/ja/arcanists/sotheby/) |
| 隠匿 | アルティメット以外のリアルダメージを回避する。 | [ノーティカ](/ja/arcanists/nautika/)、[ポルターガイスト](/ja/arcanists/poltergeist/)、[TTT](/ja/arcanists/ttt/) |
| スペル強化Ⅰ | ターン開始時、ランダムでスペル1枚のランク+1。 | [6](/ja/arcanists/6/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[アルゴス](/ja/arcanists/argus/)、[エニセイ](/ja/arcanists/yenisei/) |
| スペル強化Ⅱ | ターン開始時、ランダムでスペル2枚のランク+1。 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[アルゴス](/ja/arcanists/argus/)、[ベティ](/ja/arcanists/bette/)、[カーラ・ボナー](/ja/arcanists/kaalaa-baunaa/) |
| 連続行動Ⅰ | 行動回数+1。 | [37](/ja/arcanists/37/)、[エル・アレフ](/ja/arcanists/aleph/)、[程和光](/ja/arcanists/cheng-heguang/)、[パタパタペーパー](/ja/arcanists/flutterpage/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マーカス](/ja/arcanists/marcus/)、[モルダー](/ja/arcanists/moldir/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/) |

## チームの仕組み

複数の神秘学家が一緒にためるリソースと効果。中国本土版クライアントでは、血の薪、残光、看破の眼は同時に存在できない。グローバル版クライアントの血の薪と残光のテキストにはこの一文がなく、看破は中国本土版にのみ実装されている。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| 血の薪 | 味方キャラが合計で失った3000HPにつき、血の薪+1。（ただし、攻撃で受けたダメージは、30%分のみが換算される） | [エターニティ](/ja/arcanists/eternity/)、[エズラ](/ja/arcanists/ezra/)、[ノーティカ](/ja/arcanists/nautika/)、[ルブシカ](/ja/arcanists/rubuska/)、[センメルワイス](/ja/arcanists/semmelweis/)、[センティネル](/ja/arcanists/sentinel/) |
| 残光 | 任意の敵が【燃焼】【光輪】を付与されると、【残光】を獲得する。敵の数が少ないほど、獲得する【残光】が多くなる。 | [ベリル](/ja/arcanists/beryl/)、[ドレイク](/ja/arcanists/drake/)、[イゾルデ](/ja/arcanists/isolde/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マルシャ](/ja/arcanists/marsha/)、[マチルダ](/ja/arcanists/matilda/)、[カエンボク](/ja/arcanists/spathodea/) |
| 看破の眼（非公式） | グローバル版には未実装 | [37](/ja/arcanists/37/)、[狩勲の魔女リーリャ](/ja/arcanists/huntsworn-lilya/)、[ペルヒタ](/ja/arcanists/perchta/) |
| 啓示 | 消費した1ひらめきにつき、啓示を1点獲得する。毎ターン開始時、ランダムで通常スペルに配分される（各通常スペルは最大5点まで。ターン終了時、使用されなかったスペルの啓示が失われる）。【啓示】付きのスペルを自ら使用すると、スペル行列の最後に【即興スペル】が追加される。さらに、使用した啓示はこのターンの【即興スペル】に蓄積される。 | [エル・アレフ](/ja/arcanists/aleph/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[バルカローラ](/ja/arcanists/barcarola/)、[カイパリーナ](/ja/arcanists/kiperina/)、[マチルダ](/ja/arcanists/matilda/)、[鷺切](/ja/arcanists/paper-heron/)、[レグルス](/ja/arcanists/regulus/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/)、[ボイジャー](/ja/arcanists/voyager/) |
| 即興スペル | 単体攻撃。ランダムな敵1体に200%のメンタルダメージを与える。この攻撃時、追加で蓄積された啓示数×15%分のメンタルダメージを与える。蓄積された啓示が3/6/12/20点以上の場合、攻撃回数がそれぞれ+1/2/3/5。（即興スペルの与ダメージは、味方全員の平均ステータスによって算出される） | [エル・アレフ](/ja/arcanists/aleph/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[バルカローラ](/ja/arcanists/barcarola/)、[カイパリーナ](/ja/arcanists/kiperina/)、[マチルダ](/ja/arcanists/matilda/)、[鷺切](/ja/arcanists/paper-heron/)、[レグルス](/ja/arcanists/regulus/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/)、[ボイジャー](/ja/arcanists/voyager/) |
| 電力 | 科学技術の産物で、精密機器の使用に使う。（最大30回までスタック可能、解除不可） | [グレイッシュブルー](/ja/arcanists/brume/)、[カローン](/ja/arcanists/charon/)、[コルヴス](/ja/arcanists/corvus/)、[エニグマ](/ja/arcanists/enigma/)、[エズラ](/ja/arcanists/ezra/)、[ルーシー](/ja/arcanists/lucy/)、[ウルリッヒ](/ja/arcanists/ulrich/) |
| 泳動電場 | ターン開始時、泳動電場は注入された【電力】のスタック数に応じてレベルアップする。注入された【電力】が50点以上の場合、【泳動電場Lv.2】にレベルアップする。注入された【電力】が120点以上の場合、【泳動電場Lv.3】にレベルアップする。（泳動電場が終了した場合、注入された【電力】もなくなる） | [グレイッシュブルー](/ja/arcanists/brume/)、[カローン](/ja/arcanists/charon/)、[コルヴス](/ja/arcanists/corvus/)、[エニグマ](/ja/arcanists/enigma/)、[エズラ](/ja/arcanists/ezra/)、[ルーシー](/ja/arcanists/lucy/)、[ウルリッヒ](/ja/arcanists/ulrich/) |
| 術具 | 術具にエネルギーをチャージする。行動エリアの最後に術具が稼働し、エネルギーを消費してスペルを発動する。 | [コッペリア](/ja/arcanists/coppelia/)、[エバーエコー](/ja/arcanists/everecho/)、[ヘドネ](/ja/arcanists/hedone/)、[レグルス](/ja/arcanists/regulus/)、[双子](/ja/arcanists/the-twins/) |
| 礼儀 | アルティメット威力+3%。（最大100回までスタック可能、解除不可。アルティメット発動後に解除） | [ララ・ファウンテン](/ja/arcanists/la-source/)、[リーリャ](/ja/arcanists/lilya/)、[ダンカン](/ja/arcanists/mr-duncan/)、[ネイムデー](/ja/arcanists/name-day/)、[シャーマィン](/ja/arcanists/shamane/) |
| 能動特殊スペル | このスペルを発動すると、自らによる行動とみなされる。 | [ベリル](/ja/arcanists/beryl/)、[サーベス](/ja/arcanists/hissabeth/)、[カサンドラ](/ja/arcanists/kassandra/)、[ストレンジャー](/ja/arcanists/ms-stranger/) |
| 固定ジェネシスダメージ | このタイプのジェネシスダメージはステータスに影響されない。 | [ヘドネ](/ja/arcanists/hedone/)、[カカニア](/ja/arcanists/kakania/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/) |
