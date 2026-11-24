---
title: "상태 효과"
description: "리버스: 1999 상태 효과: 버프와 디버프의 종류, 제어 효과, 여러 마도학자가 함께 쓰는 상태."
appliesTo: "리버스: 1999, 중국 본토 클라이언트 113.0.1422(4.1 버전). 글로벌 클라이언트 111.0.1077(3.9 버전)"
caveat: "석화는 보유자가 현실 피해 공격을 받으면, 빙결은 정신 피해 공격을 받으면 끝나므로, 해당 유형의 공격이 제어된 적을 풀어 준다."
lastVerified: 2026-11-23
aliases:
  - "Statuses"
  - "狀態效果"
  - "状态效果"
  - "状態効果"
  - "Status effects"
  - "Buffs and debuffs"
  - "Control"
  - "控制"
sources:
  - title: "re1999-data, 중국 본토 클라이언트 113.0.1422: skill_eff_desc.json(상태)과 모든 마도학자의 스킬 텍스트"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/skill_eff_desc.json
  - title: "re1999-data-global, 글로벌 클라이언트 111.0.1077: skill_eff_desc.json과 언어별 텍스트"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/skill_eff_desc.json
  - title: "re1999-data-global, 글로벌 클라이언트 111.0.1077: loading_text.json(작전 매뉴얼 팁)"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/loading_text.json
---
## 상태의 종류

모든 상태는 긍정 효과 아니면 부정 효과다. 긍정 효과의 종류는 속성 증가, 버프 상태, 카운터이며 해제로 없어진다. 부정 효과의 종류는 속성 감소, 상태 이상, 제어이며 정화로 없어진다. 게임이 해제되지 않는다고 표시한 상태는 남는다.

같은 이름의 상태가 다시 걸리면 강도와 지속 시간에 따라 앞의 상태를 덮어쓴다. 주문의 특수 효과는 대상이 저항할 수 있으며, 면역은 모든 부정 효과를 막는다.

## 제어

제어 상태는 캐릭터가 행동하지 못하게 하거나 쓸 수 있는 것을 제한한다. 세 가지 상태는 2스택이 되면 그중 하나로 바뀐다.

| 상태 | 효과 | 스킬에 이 상태가 나오는 마도학자 |
| --- | --- | --- |
| 기절 | 행동 불가 | [안안 리](/ko/arcanists/an-an-lee/), [카산드라](/ko/arcanists/kassandra/), [메디슨 포켓](/ko/arcanists/medicine-pocket/), [마릴린](/ko/arcanists/sweetheart/), [화이트 럼](/ko/arcanists/white-rum/) |
| 석화 | 행동 불가, 현실 피해 공격을 받은 후 해제. | [드루비스](/ko/arcanists/druvis-iii/), [제시카](/ko/arcanists/jessica/), [사츠키](/ko/arcanists/satsuki/) |
| 빙결 | 행동 불가, 정신 피해 공격을 받은 후 해제. | [J](/ko/arcanists/j/), [무아상](/ko/arcanists/ms-moissan/) |
| 악몽 | 행동 불가, 임의 공격을 받은 후 해제. | [베이비 블루](/ko/arcanists/baby-blue/), [디거스](/ko/arcanists/diggers/), [리사&루이스](/ko/arcanists/twins-sleep/) |
| 무장 해제 | 공격 유형 일반 주문 사용 불가. | [에일리언 T](/ko/arcanists/alien-t/), [에릭](/ko/arcanists/erick/), [소네트](/ko/arcanists/sonetto/), [스푸트니크](/ko/arcanists/sputnik/) |
| 침묵 | 버프, 디버프, 치료, 카운터 유형 일반 주문 사용 불가. | [에일리언 T](/ko/arcanists/alien-t/), [에릭](/ko/arcanists/erick/), [스푸트니크](/ko/arcanists/sputnik/), [보이저](/ko/arcanists/voyager/), [X](/ko/arcanists/x/), [겨울](/ko/arcanists/zima/) |
| 봉인 | 최종 술식 사용 불가. | [콘블룸](/ko/arcanists/bkornblume/), [라 수르스](/ko/arcanists/la-source/), [보이저](/ko/arcanists/voyager/), [겨울](/ko/arcanists/zima/) |
| 경직 | 2스택 중첩 시 석화로 변경 또는 이미 존재하는 석화 1턴 연장. | [안안 리](/ko/arcanists/an-an-lee/), [히사베스](/ko/arcanists/hissabeth/), [사츠키](/ko/arcanists/satsuki/) |
| 추위 | 2스택 중첩 시 빙결로 변경 또는 이미 존재하는 빙결 1턴 연장. | [J](/ko/arcanists/j/) |
| 마비 | 2스택 중첩 시 기절로 변경 또는 이미 존재하는 기절 1턴 연장. | [메스머 주니어](/ko/arcanists/mesmer-jr/) |

## 지속 피해와 그 밖의 디버프

이 상태들이 주는 피해는 고정 피해다.

| 상태 | 효과 | 스킬에 이 상태가 나오는 마도학자 |
| --- | --- | --- |
| 연소 | 받는 치료 효과 15% 감소(효과 중첩 불가). 턴 종료 시 보유자의 공격×4%에 해당하는 고정 피해를 줌(효과 중첩 가능, 최대 30스택 중첩. 모든 연소는 \[상태 이상\] 1개로 간주. 적용 후 스택 절반 차감). | [6](/ko/arcanists/6/), [안안 리](/ko/arcanists/an-an-lee/), [베릴](/ko/arcanists/beryl/), [브룸](/ko/arcanists/brume/), [드레이크](/ko/arcanists/drake/), [이졸데](/ko/arcanists/isolde/), [J](/ko/arcanists/j/), [양월](/ko/arcanists/liang-yue/), [로렌츠 버터플라이](/ko/arcanists/lorentz-butterfly/), [마샤](/ko/arcanists/marsha/), [마틸다](/ko/arcanists/matilda/), [스파토데아](/ko/arcanists/spathodea/), [울루](/ko/arcanists/ulu/) |
| 빛무리 | 받는 치료 효과 25% 감소(효과 중첩 불가). 턴 종료 시 보유자의 공격×4%에 해당하는 고정 피해를 줌(효과 중첩 가능, 최대 30스택 중첩. 모든 빛무리는 \[상태 이상\] 1개로 간주. 적용 후 스택 절반 차감). | [드레이크](/ko/arcanists/drake/), [이졸데](/ko/arcanists/isolde/), [로렌츠 버터플라이](/ko/arcanists/lorentz-butterfly/), [마샤](/ko/arcanists/marsha/), [마틸다](/ko/arcanists/matilda/), [스파토데아](/ko/arcanists/spathodea/) |
| 중독 | 턴 종료 시 사용자 공격에 따른 고정 피해를 받음(중첩 가능) | [6](/ko/arcanists/6/), [안안 리](/ko/arcanists/an-an-lee/), [이터니티](/ko/arcanists/eternity/), [에지오 아디토레](/ko/arcanists/ezio-auditore/), [제시카](/ko/arcanists/jessica/), [칸지라](/ko/arcanists/kanjira/), [양월](/ko/arcanists/liang-yue/), [레이비스](/ko/arcanists/rabies/), [라모나](/ko/arcanists/ramona/), [소더비](/ko/arcanists/sotheby/), [튜즈데이](/ko/arcanists/tuesday/), [윌로우](/ko/arcanists/willow/) |
| 출혈 | 행동 후 사용자 공격×100%의 고정 피해를 받음. | [이터니티](/ko/arcanists/eternity/), [노티카](/ko/arcanists/nautika/), [화이트 럼](/ko/arcanists/white-rum/) |
| 부식 | 턴 종료 시 현재 HP에 따른 고정 피해를 받음. | [이터니티](/ko/arcanists/eternity/), [광대](/ko/arcanists/the-fool/) |
| 중상 | 받는 치료 효과 -50% | [바니바니](/ko/arcanists/bunny-bunny/), [크리스탈로](/ko/arcanists/cristallo/), [이터니티](/ko/arcanists/eternity/), [은빛 이글](/ko/arcanists/silverwing-eagle/) |
| 쇠약 | 공격 시 피해 보너스 -25%(적용 후 1스택 감소) | [콘블룸](/ko/arcanists/bkornblume/), [센츄리온](/ko/arcanists/centurion/), [디거스](/ko/arcanists/diggers/), [라 수르스](/ko/arcanists/la-source/), [로렐라이](/ko/arcanists/lorelei/), [마커스](/ko/arcanists/marcus/), [리사&루이스](/ko/arcanists/twins-sleep/) |
| 실명 | 단일 공격 시 피해 보너스 -30% | [6](/ko/arcanists/6/), [클릭](/ko/arcanists/click/) |
| 흐림 | 광역 공격 시 피해 보너스 -30% | [6](/ko/arcanists/6/) |
| 의식 혼란 | 치명타 저항률 -25%(효과 중첩 가능, 스택당 시간 개별 계산) | [블로니](/ko/arcanists/blonney/), [칸지라](/ko/arcanists/kanjira/), [마틸다](/ko/arcanists/matilda/), [투스 페어리](/ko/arcanists/tooth-fairy/), [보이저](/ko/arcanists/voyager/), [윈드송](/ko/arcanists/windsong/) |
| 불안 | 받는 정신 피해 25% 증가(적용 후 1스택 감소) | [바바라](/ko/arcanists/barbara/), [호러피디아](/ko/arcanists/horropedia/), [노티카](/ko/arcanists/nautika/) |
| 심란 | 열정 증가 불가 | [미스 라디오](/ko/arcanists/ms-radio/), [TTT](/ko/arcanists/ttt/), [X](/ko/arcanists/x/) |
| 열정 추출 | 공격받은 후 공격자는 열정 1 획득(적용 후 1스택 감소) | [멜라니아](/ko/arcanists/melania/), [몰디르](/ko/arcanists/moldir/), [나르키소스](/ko/arcanists/narcissus/), [레콜레타](/ko/arcanists/recoleta/) |

## 버프

여러 마도학자가 부여하는 긍정 상태.

| 상태 | 효과 | 스킬에 이 상태가 나오는 마도학자 |
| --- | --- | --- |
| 보호막 | 지속시간 동안 피해 1회 방어. | [바바라](/ko/arcanists/barbara/), [베티](/ko/arcanists/bette/), [문](/ko/arcanists/door/), [에즈라](/ko/arcanists/ezra/), [J](/ko/arcanists/j/), [곡랑](/ko/arcanists/jiu-niangzi/), [존 티토](/ko/arcanists/john-titor/), [키페리나](/ko/arcanists/kiperina/), [마샤](/ko/arcanists/marsha/), [무아상](/ko/arcanists/ms-moissan/), [뉴바벨](/ko/arcanists/ms-newbabel/), [닉 보텀](/ko/arcanists/nick-bottom/), [올리버 포그](/ko/arcanists/oliver-fog/), [테넌트](/ko/arcanists/tennant/), [예니세이](/ko/arcanists/yenisei/) |
| 카운터 | 지속적인 카운터 상태 부여, 공격받을 시 효과 발동. | [6](/ko/arcanists/6/), [찰리](/ko/arcanists/charlie/), [데저트 플란넬](/ko/arcanists/desert-flannel/), [에릭](/ko/arcanists/erick/), [호러피디아](/ko/arcanists/horropedia/), [곡랑](/ko/arcanists/jiu-niangzi/), [존 티토](/ko/arcanists/john-titor/), [무아상](/ko/arcanists/ms-moissan/), [네임데이](/ko/arcanists/name-day/), [피클즈](/ko/arcanists/pickles/), [스푸트니크](/ko/arcanists/sputnik/), [TTT](/ko/arcanists/ttt/), [X](/ko/arcanists/x/) |
| 도발 | 적의 주의를 끌어 일부 공격을 받을 시 우선 공격 목표가 됨 | [에일리언 T](/ko/arcanists/alien-t/), [뉴바벨](/ko/arcanists/ms-newbabel/), [노티카](/ko/arcanists/nautika/), [어니언](/ko/arcanists/onion/), [파이오니어](/ko/arcanists/pioneer/), [폴터가이스트](/ko/arcanists/poltergeist/), [광대](/ko/arcanists/the-fool/) |
| 견고 | 공격받을 시 피해 감면 +25%(적용 후 1스택 감소) | [37](/ko/arcanists/37/), [안안 리](/ko/arcanists/an-an-lee/), [아브구스트](/ko/arcanists/avgust/), [크리스탈로](/ko/arcanists/cristallo/), [메디슨 포켓](/ko/arcanists/medicine-pocket/), [올리버 포그](/ko/arcanists/oliver-fog/), [어니언](/ko/arcanists/onion/), [레굴루스](/ko/arcanists/regulus/), [빌라](/ko/arcanists/vila/), [보이저](/ko/arcanists/voyager/), [화이트 럼](/ko/arcanists/white-rum/), [예니세이](/ko/arcanists/yenisei/) |
| 격앙 | 공격 시 피해 보너스 +50%(적용 후 1스택 감소) | [A 나이트](/ko/arcanists/a-knight/), [아브구스트](/ko/arcanists/avgust/), [이졸데](/ko/arcanists/isolde/), [피클즈](/ko/arcanists/pickles/), [화이트 럼](/ko/arcanists/white-rum/) |
| 폭발력 | 공격 시 피해 보너스 +25%(적용 후 1스택 감소). | [데저트 플란넬](/ko/arcanists/desert-flannel/), [이졸데](/ko/arcanists/isolde/), [빌라](/ko/arcanists/vila/) |
| 면역 | \[속성 감소\] \[상태 이상\] \[제어\]의 영향을 받지 않음. | [디케](/ko/arcanists/dikke/), [양월](/ko/arcanists/liang-yue/), [노티카](/ko/arcanists/nautika/), [예니세이](/ko/arcanists/yenisei/) |
| 유합 | 턴 시작 시 사용자 공격에 따라 HP 회복. | [안안 리](/ko/arcanists/an-an-lee/), [아브구스트](/ko/arcanists/avgust/), [소더비](/ko/arcanists/sotheby/) |
| 은폐 | 최종 술식이 아닌 현실 피해 공격을 회피. | [노티카](/ko/arcanists/nautika/), [폴터가이스트](/ko/arcanists/poltergeist/), [TTT](/ko/arcanists/ttt/) |
| 주문 강화Ⅰ | 턴 시작 시 랜덤 1장의 주문 단계 +1 | [6](/ko/arcanists/6/), [안안 리](/ko/arcanists/an-an-lee/), [아르고스](/ko/arcanists/argus/), [예니세이](/ko/arcanists/yenisei/) |
| 주문 강화Ⅱ | 턴 시작 시 랜덤 2장의 주문 단계 +1 | [안안 리](/ko/arcanists/an-an-lee/), [아르고스](/ko/arcanists/argus/), [베티](/ko/arcanists/bette/), [갈라보나](/ko/arcanists/kaalaa-baunaa/) |
| 연속 행동Ⅰ | 행동 횟수 +1 | [37](/ko/arcanists/37/), [알레프](/ko/arcanists/aleph/), [정화광](/ko/arcanists/cheng-heguang/), [플러터 페이지](/ko/arcanists/flutterpage/), [로렌츠 버터플라이](/ko/arcanists/lorentz-butterfly/), [마커스](/ko/arcanists/marcus/), [몰디르](/ko/arcanists/moldir/), [투스 페어리](/ko/arcanists/tooth-fairy/) |

## 팀 메커니즘

여러 마도학자가 함께 쌓는 자원과 효과. 중국 본토 클라이언트에서 신혈, 여광, 간파의 눈은 동시에 활성화될 수 없다. 글로벌 클라이언트의 신혈과 여광 텍스트에는 이 조항이 없으며, 간파는 중국 본토 서비스에만 나와 있다.

| 상태 | 효과 | 스킬에 이 상태가 나오는 마도학자 |
| --- | --- | --- |
| 신혈 | 아군 부대가 HP 누적 3000 잃을 때마다 신혈 +1(공격받아 잃은 HP는 30%만 기록) | [이터니티](/ko/arcanists/eternity/), [에즈라](/ko/arcanists/ezra/), [노티카](/ko/arcanists/nautika/), [루부스카](/ko/arcanists/rubuska/), [제멜바이스](/ko/arcanists/semmelweis/), [센티널](/ko/arcanists/sentinel/) |
| 여광 | 임의 적에게 \[연소\] \[빛무리\] 부여 시 \[여광\] 누적, 몬스터 수량이 적을수록 \[여광\]이 더 많이 누적 | [베릴](/ko/arcanists/beryl/), [드레이크](/ko/arcanists/drake/), [이졸데](/ko/arcanists/isolde/), [로렌츠 버터플라이](/ko/arcanists/lorentz-butterfly/), [마샤](/ko/arcanists/marsha/), [마틸다](/ko/arcanists/matilda/), [스파토데아](/ko/arcanists/spathodea/) |
| 간파의 눈 (비공식) | 글로벌 클라이언트에는 아직 없음 | [37](/ko/arcanists/37/), [사냥 훈장의 마녀 릴리아](/ko/arcanists/huntsworn-lilya/), [페르히타](/ko/arcanists/perchta/) |
| 계시 | 신기한 빛 1포인트 소모할 때마다 계시가 1포인트씩 누적. 턴 시작 시마다 무작위로 일반 주문에 계시가 배분(각 일반 주문은 최대 5포인트까지 배분 가능하며, 턴 종료 시 사용하지 않은 주문이 보유한 계시는 초기화된다). \[계시\]를 보유한 주문을 직접 사용 시 주문 대기열 마지막에 \[즉흥 주문\] 추가되고, 해당 주문이 보유한 계시를 이번 \[즉흥 주문\]에 부여 | [알레프](/ko/arcanists/aleph/), [안안 리](/ko/arcanists/an-an-lee/), [바르카롤라](/ko/arcanists/barcarola/), [키페리나](/ko/arcanists/kiperina/), [마틸다](/ko/arcanists/matilda/), [노사전](/ko/arcanists/paper-heron/), [레굴루스](/ko/arcanists/regulus/), [투스 페어리](/ko/arcanists/tooth-fairy/), [보이저](/ko/arcanists/voyager/) |
| 즉흥 주문 | 단일 공격, 랜덤 적군 목표 1명에게 200%의 정신 피해를 줌, 해당 공격으로 15%×누적 계시 수의 정신 피해를 추가로 줌, 축적된 계시 수가 3/6/12/20 이상일 시, 공격 횟수 +1/2/3/5(즉흥 주문이 피해를 줄 때 모든 아군의 평균 속성으로 계산 진행) | [알레프](/ko/arcanists/aleph/), [안안 리](/ko/arcanists/an-an-lee/), [바르카롤라](/ko/arcanists/barcarola/), [키페리나](/ko/arcanists/kiperina/), [마틸다](/ko/arcanists/matilda/), [노사전](/ko/arcanists/paper-heron/), [레굴루스](/ko/arcanists/regulus/), [투스 페어리](/ko/arcanists/tooth-fairy/), [보이저](/ko/arcanists/voyager/) |
| 전력 | 과학 기술의 산물, 정밀 기계 사용에 활용(중첩 가능, 최대 30스택 중첩, 해제 불가). | [브룸](/ko/arcanists/brume/), [카론](/ko/arcanists/charon/), [코르부스](/ko/arcanists/corvus/), [이니그마](/ko/arcanists/enigma/), [에즈라](/ko/arcanists/ezra/), [루시](/ko/arcanists/lucy/), [울리히](/ko/arcanists/ulrich/) |
| 전기장 폭주 | 턴 시작 시 전기장 폭주는 주입한 \[전력\] 스택에 따라 레벨업: 주입한 \[전력\]이 50 이상일 시 술진은 \[전기장 폭주 Lv.2\]로 레벨업, 주입한 \[전력\]이 120 이상일 시 술진은 \[전기장 폭주 Lv.3\]으로 레벨업(전기장 폭주 소멸 시 주입한 \[전력\]도 함께 초기화) | [브룸](/ko/arcanists/brume/), [카론](/ko/arcanists/charon/), [코르부스](/ko/arcanists/corvus/), [이니그마](/ko/arcanists/enigma/), [에즈라](/ko/arcanists/ezra/), [루시](/ko/arcanists/lucy/), [울리히](/ko/arcanists/ulrich/) |
| 마도구 | 교감 에너지를 사용하면 마도구에 에너지가 충전됩니다. 행동 대기열 마지막에 마도구가 순환 작동하며 교감 에너지를 소모해 주문을 시전합니다. | [코펠리아](/ko/arcanists/coppelia/), [에버에코](/ko/arcanists/everecho/), [헤도네](/ko/arcanists/hedone/), [레굴루스](/ko/arcanists/regulus/), [쌍둥이](/ko/arcanists/the-twins/) |
| 예의 | 술식 위력 3% 증가(효과 중첩 가능, 최대 100스택 중첩, 해제 불가, 최종 술식 시전 후 소멸). | [라 수르스](/ko/arcanists/la-source/), [릴리아](/ko/arcanists/lilya/), [던컨](/ko/arcanists/mr-duncan/), [네임데이](/ko/arcanists/name-day/), [갈기 모래](/ko/arcanists/shamane/) |
| 메인 특수 주문 | 해당 주문 시전 시 캐릭터가 직접 행동한 것으로 간주 | [베릴](/ko/arcanists/beryl/), [히사베스](/ko/arcanists/hissabeth/), [카산드라](/ko/arcanists/kassandra/), [미스 스트레인저](/ko/arcanists/ms-stranger/) |
| 안정 고정 피해 | 해당 유형의 고정 피해는 속성 보너스의 영향을 받지 않음 | [헤도네](/ko/arcanists/hedone/), [카카니아](/ko/arcanists/kakania/), [로렌츠 버터플라이](/ko/arcanists/lorentz-butterfly/) |
