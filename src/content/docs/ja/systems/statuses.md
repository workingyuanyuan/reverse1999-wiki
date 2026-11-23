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
状態はすべてプラスかマイナスのどちらかに分かれる。プラスの種類はステータス上昇、状態強化、カウンターで、バフ解除で取り除かれる。マイナスの種類はステータス低下、状態異常、行動阻害で、デバフ解除で取り除かれる。ゲームが解除されないと定めた状態は残る。

同名の状態を重ねて受けると、効果量と持続ターンに応じて前の状態が上書きされる。スペルの特殊効果は対象に抵抗されることがあり、弱体無効はマイナスの種類をすべて防ぐ。

## 行動阻害

行動阻害の状態は、キャラクターの行動を止めるか、使えるスペルを制限する。3つの状態は2スタックたまると、そのうちの1つに変わる。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| 気絶 | 行動できない。 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[カサンドラ](/ja/arcanists/kassandra/)、[メディスンポケット](/ja/arcanists/medicine-pocket/)、[スイートハート](/ja/arcanists/sweetheart/)、[ホワイトラム](/ja/arcanists/white-rum/) |
| 石化 | 行動できない。リアルダメージの攻撃を受けると解ける。 | [ドルーヴィスⅢ](/ja/arcanists/druvis-iii/)、[ジェシカ](/ja/arcanists/jessica/)、[五色月](/ja/arcanists/satsuki/) |
| 氷結 | 行動できない。メンタルダメージの攻撃を受けると解ける。 | [J](/ja/arcanists/j/)、[ミス・モアッサン](/ja/arcanists/ms-moissan/) |
| 悪夢 | 行動できない。どの攻撃を受けても解ける。 | [ベビーブルー](/ja/arcanists/baby-blue/)、[ディガー](/ja/arcanists/diggers/)、[リサ＆ルイス](/ja/arcanists/twins-sleep/) |
| 武装解除 | アタック系のスペルを使えない。 | [ギベオンズアイ](/ja/arcanists/alien-t/)、[エリック](/ja/arcanists/erick/)、[ソネット](/ja/arcanists/sonetto/)、[スプートニク](/ja/arcanists/sputnik/) |
| 沈黙 | バフ・デバフ・ヒール・カウンター系のスペルを使えない。 | [ギベオンズアイ](/ja/arcanists/alien-t/)、[エリック](/ja/arcanists/erick/)、[スプートニク](/ja/arcanists/sputnik/)、[ボイジャー](/ja/arcanists/voyager/)、[X](/ja/arcanists/x/)、[ズィマー](/ja/arcanists/zima/) |
| 封印 | アルティメットを使えない。 | [コーンブルメ](/ja/arcanists/bkornblume/)、[ララ・ファウンテン](/ja/arcanists/la-source/)、[ボイジャー](/ja/arcanists/voyager/)、[ズィマー](/ja/arcanists/zima/) |
| 硬直 | 2スタックで石化に変わる。すでに石化していれば、石化が1ターン延びる。 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[サーベス](/ja/arcanists/hissabeth/)、[五色月](/ja/arcanists/satsuki/) |
| コールド | 2スタックで氷結に変わる。すでに氷結していれば、氷結が1ターン延びる。 | [J](/ja/arcanists/j/) |
| めまい | 2スタックで気絶に変わる。すでに気絶していれば、気絶が1ターン延びる。 | [メスメル・Jr.](/ja/arcanists/mesmer-jr/) |

## 継続ダメージとその他のデバフ

これらの状態が与えるダメージはジェネシスダメージである。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| 燃焼 | 被回復効果 −15%（重複しない）。各ターン終了時、1スタックにつき持ち主の攻撃力の 4% に等しいジェネシスダメージを受ける。最大30スタックで、まとめて1つの状態異常と数える。ダメージを与えるたびにスタックが半分になる。 | [6](/ja/arcanists/6/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[ベリル](/ja/arcanists/beryl/)、[グレイッシュブルー](/ja/arcanists/brume/)、[ドレイク](/ja/arcanists/drake/)、[イゾルデ](/ja/arcanists/isolde/)、[J](/ja/arcanists/j/)、[梁月](/ja/arcanists/liang-yue/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マルシャ](/ja/arcanists/marsha/)、[マチルダ](/ja/arcanists/matilda/)、[カエンボク](/ja/arcanists/spathodea/)、[ウル](/ja/arcanists/ulu/) |
| 光輪 | 燃焼と同様だが、被回復効果は −25% で、ダメージは最初に付与した者の攻撃力に基づく。 | [ドレイク](/ja/arcanists/drake/)、[イゾルデ](/ja/arcanists/isolde/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マルシャ](/ja/arcanists/marsha/)、[マチルダ](/ja/arcanists/matilda/)、[カエンボク](/ja/arcanists/spathodea/) |
| 中毒 | 各ターン終了時、付与者の攻撃力に基づくジェネシスダメージを受ける。重複する。 | [6](/ja/arcanists/6/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[エターニティ](/ja/arcanists/eternity/)、[エツィオ](/ja/arcanists/ezio-auditore/)、[ジェシカ](/ja/arcanists/jessica/)、[カンジーラ](/ja/arcanists/kanjira/)、[梁月](/ja/arcanists/liang-yue/)、[レイビーズ](/ja/arcanists/rabies/)、[ラモナ](/ja/arcanists/ramona/)、[サザビー](/ja/arcanists/sotheby/)、[チューズデー](/ja/arcanists/tuesday/)、[ヴィロー](/ja/arcanists/willow/) |
| 流血 | 持ち主が行動した後、付与者の攻撃力の 100% に等しいジェネシスダメージを受ける。 | [エターニティ](/ja/arcanists/eternity/)、[ノーティカ](/ja/arcanists/nautika/)、[ホワイトラム](/ja/arcanists/white-rum/) |
| 腐蝕 | 各ターン終了時、持ち主の現在HPに基づくジェネシスダメージを受ける。 | [エターニティ](/ja/arcanists/eternity/)、[ジェスター](/ja/arcanists/the-fool/) |
| 重傷 | 被回復効果 −50%。 | [バニーバニー](/ja/arcanists/bunny-bunny/)、[クリスタッロ](/ja/arcanists/cristallo/)、[エターニティ](/ja/arcanists/eternity/)、[イーグル](/ja/arcanists/silverwing-eagle/) |
| 虚弱 | 攻撃時のダメージボーナス −25%。1回ごとに1スタック消費する。 | [コーンブルメ](/ja/arcanists/bkornblume/)、[ケントゥリオン](/ja/arcanists/centurion/)、[ディガー](/ja/arcanists/diggers/)、[ララ・ファウンテン](/ja/arcanists/la-source/)、[ローレライ](/ja/arcanists/lorelei/)、[マーカス](/ja/arcanists/marcus/)、[リサ＆ルイス](/ja/arcanists/twins-sleep/) |
| 盲目 | 単体攻撃のダメージボーナス −30%。 | [6](/ja/arcanists/6/)、[カシャパシャ](/ja/arcanists/click/) |
| ミスエイム | 範囲攻撃のダメージボーナス −30%。 | [6](/ja/arcanists/6/) |
| 朦朧 | クリティカル耐性率 −25%。重複し、スタックごとに持続ターンが別に数えられる。 | [ジェイミー](/ja/arcanists/blonney/)、[カンジーラ](/ja/arcanists/kanjira/)、[マチルダ](/ja/arcanists/matilda/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/)、[ボイジャー](/ja/arcanists/voyager/)、[スヴィスティ](/ja/arcanists/windsong/) |
| 危惧 | 受けるメンタルダメージ +25%。1回ごとに1スタック消費する。 | [メェプル](/ja/arcanists/barbara/)、[ホラーペディア](/ja/arcanists/horropedia/)、[ノーティカ](/ja/arcanists/nautika/) |
| 動揺 | モキシーを獲得できない。 | [ミス・ラジオ](/ja/arcanists/ms-radio/)、[TTT](/ja/arcanists/ttt/)、[X](/ja/arcanists/x/) |
| MPドレイン | 持ち主が攻撃を受けると、攻撃者がモキシーを1獲得する。1回ごとに1スタック消費する。 | [メラニア](/ja/arcanists/melania/)、[モルダー](/ja/arcanists/moldir/)、[ナルキッソス](/ja/arcanists/narcissus/)、[レコレータ](/ja/arcanists/recoleta/) |

## バフ

複数の神秘学家が付与するプラスの状態。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| シールド | 効果の間、ダメージを吸収する。 | [メェプル](/ja/arcanists/barbara/)、[ベティ](/ja/arcanists/bette/)、[ドア](/ja/arcanists/door/)、[エズラ](/ja/arcanists/ezra/)、[J](/ja/arcanists/j/)、[曲娘](/ja/arcanists/jiu-niangzi/)、[ジョン・タイター](/ja/arcanists/john-titor/)、[カイパリーナ](/ja/arcanists/kiperina/)、[マルシャ](/ja/arcanists/marsha/)、[ミス・モアッサン](/ja/arcanists/ms-moissan/)、[ニューバベル](/ja/arcanists/ms-newbabel/)、[ニック・ボトム](/ja/arcanists/nick-bottom/)、[オリバー・フォッグ](/ja/arcanists/oliver-fog/)、[テナント](/ja/arcanists/tennant/)、[エニセイ](/ja/arcanists/yenisei/) |
| カウンター | 持続する状態で、持ち主が攻撃を受けると効果が発動する。 | [6](/ja/arcanists/6/)、[チャーリー](/ja/arcanists/charlie/)、[サンド・フランネル](/ja/arcanists/desert-flannel/)、[エリック](/ja/arcanists/erick/)、[ホラーペディア](/ja/arcanists/horropedia/)、[曲娘](/ja/arcanists/jiu-niangzi/)、[ジョン・タイター](/ja/arcanists/john-titor/)、[ミス・モアッサン](/ja/arcanists/ms-moissan/)、[ネイムデー](/ja/arcanists/name-day/)、[ピクルス](/ja/arcanists/pickles/)、[スプートニク](/ja/arcanists/sputnik/)、[TTT](/ja/arcanists/ttt/)、[X](/ja/arcanists/x/) |
| 挑発 | 一部の攻撃を優先して持ち主に引きつける。 | [ギベオンズアイ](/ja/arcanists/alien-t/)、[ニューバベル](/ja/arcanists/ms-newbabel/)、[ノーティカ](/ja/arcanists/nautika/)、[オニオン](/ja/arcanists/onion/)、[パイオニア](/ja/arcanists/pioneer/)、[ポルターガイスト](/ja/arcanists/poltergeist/)、[ジェスター](/ja/arcanists/the-fool/) |
| 強固 | 攻撃を受けたとき、ダメージ軽減 +25%。1回ごとに1スタック消費する。 | [37](/ja/arcanists/37/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[アヴグスト](/ja/arcanists/avgust/)、[クリスタッロ](/ja/arcanists/cristallo/)、[メディスンポケット](/ja/arcanists/medicine-pocket/)、[オリバー・フォッグ](/ja/arcanists/oliver-fog/)、[オニオン](/ja/arcanists/onion/)、[レグルス](/ja/arcanists/regulus/)、[ヴィラ](/ja/arcanists/vila/)、[ボイジャー](/ja/arcanists/voyager/)、[ホワイトラム](/ja/arcanists/white-rum/)、[エニセイ](/ja/arcanists/yenisei/) |
| 激昂 | 攻撃時にダメージボーナス +50%。1回ごとに1スタック消費する。 | [ナイト](/ja/arcanists/a-knight/)、[アヴグスト](/ja/arcanists/avgust/)、[イゾルデ](/ja/arcanists/isolde/)、[ピクルス](/ja/arcanists/pickles/)、[ホワイトラム](/ja/arcanists/white-rum/) |
| 瞬発力 | 攻撃時にダメージボーナス +25%。1回ごとに1スタック消費する。 | [サンド・フランネル](/ja/arcanists/desert-flannel/)、[イゾルデ](/ja/arcanists/isolde/)、[ヴィラ](/ja/arcanists/vila/) |
| 弱体無効 | ステータス低下、状態異常、行動阻害を受けない。 | [パミエ](/ja/arcanists/dikke/)、[梁月](/ja/arcanists/liang-yue/)、[ノーティカ](/ja/arcanists/nautika/)、[エニセイ](/ja/arcanists/yenisei/) |
| 継続回復 | 各ターン開始時、付与した者の攻撃力に基づいて回復する。 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[アヴグスト](/ja/arcanists/avgust/)、[サザビー](/ja/arcanists/sotheby/) |
| 隠匿 | アルティメット以外のリアルダメージの攻撃を回避する。 | [ノーティカ](/ja/arcanists/nautika/)、[ポルターガイスト](/ja/arcanists/poltergeist/)、[TTT](/ja/arcanists/ttt/) |
| スペル強化Ⅰ | 各ターン開始時、ランダムなスペル1枚のランクが1上がる。 | [6](/ja/arcanists/6/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[アルゴス](/ja/arcanists/argus/)、[エニセイ](/ja/arcanists/yenisei/) |
| スペル強化Ⅱ | 各ターン開始時、ランダムなスペル2枚のランクが1上がる。 | [リー・アンアン](/ja/arcanists/an-an-lee/)、[アルゴス](/ja/arcanists/argus/)、[ベティ](/ja/arcanists/bette/)、[カーラ・ボナー](/ja/arcanists/kaalaa-baunaa/) |
| 連続行動Ⅰ | 行動回数 +1。 | [37](/ja/arcanists/37/)、[エル・アレフ](/ja/arcanists/aleph/)、[程和光](/ja/arcanists/cheng-heguang/)、[パタパタペーパー](/ja/arcanists/flutterpage/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マーカス](/ja/arcanists/marcus/)、[モルダー](/ja/arcanists/moldir/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/) |

## チームの仕組み

複数の神秘学家が一緒にためるリソースと効果。中国本土版クライアントでは、血の薪、残光、看破の眼は同時に存在できない。グローバル版クライアントの血の薪と残光のテキストにはこの一文がなく、看破は中国本土版にのみ実装されている。

| 状態 | 効果 | スキル説明に登場する神秘学家 |
| --- | --- | --- |
| 血の薪 | チームが合計 3,000 のHPを失うごとに1ポイント。攻撃によるHP減少は 30% 分のみ数える。 | [エターニティ](/ja/arcanists/eternity/)、[エズラ](/ja/arcanists/ezra/)、[ノーティカ](/ja/arcanists/nautika/)、[ルブシカ](/ja/arcanists/rubuska/)、[センメルワイス](/ja/arcanists/semmelweis/)、[センティネル](/ja/arcanists/sentinel/) |
| 残光 | 敵が燃焼か光輪を受けるたびにたまり、敵が少ないほど多くたまる。 | [ベリル](/ja/arcanists/beryl/)、[ドレイク](/ja/arcanists/drake/)、[イゾルデ](/ja/arcanists/isolde/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/)、[マルシャ](/ja/arcanists/marsha/)、[マチルダ](/ja/arcanists/matilda/)、[カエンボク](/ja/arcanists/spathodea/) |
| 看破の眼（非公式） | スペルを使う前、看破ポイントを6以上（上限15）持つチームは弱点看破に入れる。持ち込めるのは最大10ポイントで、そのポイントを同じ本源の看破スペルに使う。 | [37](/ja/arcanists/37/)、[狩勲の魔女リーリャ](/ja/arcanists/huntsworn-lilya/)、[ペルヒタ](/ja/arcanists/perchta/) |
| 啓示 | ひらめきを1消費するごとに1点増える。ターン開始時に点がランダムなスペルに配られ（1枚に最大5点）、使わなかったカードの点はターン終了時に消える。点を持つカードを使うと、スペル行列の最後に即興スペルが加わる。 | [エル・アレフ](/ja/arcanists/aleph/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[バルカローラ](/ja/arcanists/barcarola/)、[カイパリーナ](/ja/arcanists/kiperina/)、[マチルダ](/ja/arcanists/matilda/)、[鷺切](/ja/arcanists/paper-heron/)、[レグルス](/ja/arcanists/regulus/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/)、[ボイジャー](/ja/arcanists/voyager/) |
| 即興スペル | ランダムな敵1体にメンタルダメージ 200%、さらに持っている啓示1点につき 15%。3、6、12、20点で攻撃回数がそれぞれ1、2、3、5回増える。チーム全員の平均ステータスを使う。 | [エル・アレフ](/ja/arcanists/aleph/)、[リー・アンアン](/ja/arcanists/an-an-lee/)、[バルカローラ](/ja/arcanists/barcarola/)、[カイパリーナ](/ja/arcanists/kiperina/)、[マチルダ](/ja/arcanists/matilda/)、[鷺切](/ja/arcanists/paper-heron/)、[レグルス](/ja/arcanists/regulus/)、[トゥースフェアリー](/ja/arcanists/tooth-fairy/)、[ボイジャー](/ja/arcanists/voyager/) |
| 電力 | 装置を動かす。最大30スタックで、解除されない。 | [グレイッシュブルー](/ja/arcanists/brume/)、[カローン](/ja/arcanists/charon/)、[コルヴス](/ja/arcanists/corvus/)、[エニグマ](/ja/arcanists/enigma/)、[エズラ](/ja/arcanists/ezra/)、[ルーシー](/ja/arcanists/lucy/)、[ウルリッヒ](/ja/arcanists/ulrich/) |
| 泳動電場 | ターン開始時、注入された電力に応じて成長する陣法。Lv.1 はダメージボーナス +15% を3ターン。Lv.2 は電力50からで、さらにスペル威力 +25%。Lv.3 は120からで、さらにアルティメット威力 +35%、2ターン。終了すると電力は失われる。 | [グレイッシュブルー](/ja/arcanists/brume/)、[カローン](/ja/arcanists/charon/)、[コルヴス](/ja/arcanists/corvus/)、[エニグマ](/ja/arcanists/enigma/)、[エズラ](/ja/arcanists/ezra/)、[ルーシー](/ja/arcanists/lucy/)、[ウルリッヒ](/ja/arcanists/ulrich/) |
| 術具 | エネルギーをチャージする。行動エリアの最後に、エネルギーを消費しながらスペルを繰り返し発動する。 | [コッペリア](/ja/arcanists/coppelia/)、[エバーエコー](/ja/arcanists/everecho/)、[ヘドネ](/ja/arcanists/hedone/)、[レグルス](/ja/arcanists/regulus/)、[双子](/ja/arcanists/the-twins/) |
| 礼儀 | 1スタックごとにアルティメット威力 +3%。最大100スタックで、解除されない。アルティメットの後に消える。 | [ララ・ファウンテン](/ja/arcanists/la-source/)、[リーリャ](/ja/arcanists/lilya/)、[ダンカン](/ja/arcanists/mr-duncan/)、[ネイムデー](/ja/arcanists/name-day/)、[シャーマィン](/ja/arcanists/shamane/) |
| 能動特殊スペル | 使うと、その神秘学家自身の行動と数える。 | [ベリル](/ja/arcanists/beryl/)、[サーベス](/ja/arcanists/hissabeth/)、[カサンドラ](/ja/arcanists/kassandra/)、[ストレンジャー](/ja/arcanists/ms-stranger/) |
| 固定ジェネシスダメージ | ステータスボーナスの影響を受けないジェネシスダメージの一種。 | [ヘドネ](/ja/arcanists/hedone/)、[カカニア](/ja/arcanists/kakania/)、[ローレンツバタフライ](/ja/arcanists/lorentz-butterfly/) |
