---
title: "Enigma"
description: "Enigma is a 6-star Intellect Dynamo support who deals Reality DMG and guards the team with Bastion."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Enigma's Bastion, which guards the whole team, cannot coexist with a Shield."
lastVerified: 2026-11-22
aliases:
  - "啞謎"
  - "哑谜"
  - "エニグマ"
  - "이니그마"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Enigma.png"
    url: https://reverse1999.fandom.com/wiki/File:Enigma.png
  - title: "Image file, uploaded 2026-05-20"
    url: https://static.wikia.nocookie.net/reverse1999/images/8/8b/Enigma.png/revision/latest?cb=20260520183607
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Enigma, revision 92535"
    url: https://reverse1999.fandom.com/wiki/Enigma?oldid=92535
---

![Enigma, full-length art](/art/characters/enigma.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Intellect |
| Damage | Reality |
| Tags | Shield, Dynamo, Support, Array |
| Resonance Patterns | [U-shaped set](/systems/resonance/): Hyper, Overindulgence, Quiescence, Prudentiality, Equanimity |
| Mainland release | 2026-04-09 |
| Global release | 2026-07-02 |

Enigma is a Dynamo support who builds the Pulsing Field array. At the end of each round he transfers Dynamo into the field, Ciphertext adds to each transfer, and the field rises to Lv.2 at 50 and Lv.3 at 120 Dynamo transferred. His incantations and Loop Chain keep a team-wide Bastion up, and his Ultimate gives the team Critical DMG and a DMG Bonus that grows with the Ciphertext spent.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Infinite Translation (single-target attack) | 200% Reality DMG; 3 Ciphertext to all allies | 300%; 4 Ciphertext | 500%; 5 Ciphertext |
| Meshing Minds (self buff) | Bastion of 280% of his ATK | 420% | 700% |

- Both incantations give Enigma 10 stacks of Dynamo at every rank.
- **Meshing Minds** adds its Bastion to any Bastion he already holds, up to 1250% of his ATK. While he holds it, the first 4 Control effects inflicted on allies each round are prevented, shared by the whole team.

## Ultimate: The Riddle and the Answer

Gives Enigma [Cipher Machine] for 2 rounds, dispels all Stats Down, Neg Status and Control effects from every ally, and gives him 5 stacks of [Loop Chain], enough for one Closed-Loop Principle.

## Statuses

| Status | Effect |
| --- | --- |
| Dynamo | Stacks up to 30; cannot be dispelled. |
| Ciphertext | When Dynamo is transferred into the Pulsing Field, the field gains extra Dynamo equal to the holder's Ciphertext stacks, and the Ciphertext is removed. Up to 5 stacks before Insight 1 raises the cap. |
| Bastion | Absorbs damage aimed at any ally. When 1, 2, 3, or 4 or more allies are hit at once, each point absorbs 1, 1.2, 1.5 or 1.8 damage. Allies lose no HP to enemy damage until it runs out. Cannot coexist with a Shield. |
| Pulsing Field | Array. At the start of a round it levels up by the Dynamo transferred into it: Lv.2 at 50 or more, Lv.3 at 120 or more. The transferred Dynamo is lost when the field ends. |
| Pulsing Field Lv.1 | All allies DMG Bonus +15% for 3 rounds. |
| Pulsing Field Lv.2 | All allies Incantation Might +25% and DMG Bonus +15% for 3 rounds. |
| Pulsing Field Lv.3 | All allies Ultimate Might +35%, Incantation Might +25% and DMG Bonus +15% for 2 rounds. |
| Amplified Surge | On reaching Lv.3, Enigma gains 1 Moxie. Under Lv.3, all allies gain 3 Ciphertext at the start of each round, and each ally's attack gains Incantation Might +0.4% per Dynamo stack held; Reality DMG allies also deal an extra 6% Reality DMG per stack, Mental DMG allies gain a further 0.4% Incantation Might per stack. |
| Loop Chain | At 5 stacks, casts Closed-Loop Principle and removes 5 stacks; at most 9 stacks. |
| Closed-Loop Principle | 200% Reality DMG to all enemies; 5 Ciphertext to all allies; a Bastion of 280% of Enigma's ATK on the same terms as Meshing Minds; then Enigma gains 1 Moxie and 5 Dynamo. |
| Cipher Machine | All allies Critical DMG +20%, and DMG Bonus +2% for each Ciphertext stack the team has removed so far, counting up to 30; the count resets once applied. |

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Gains Amplified Surge. At the start of a round with no Pulsing Field of any level, deploys Pulsing Field Lv.1. On entering battle, gives all allies 10 Ciphertext and himself 10 Dynamo and a Bastion of 280% of his ATK. At the end of each round, transfers up to 10 Dynamo into the Pulsing Field. His Ultimate does not count against the team's incantation draw limit. |
| 1 | Gains 1 Loop Chain whenever an ally takes an action of their own, whenever an ally is attacked, and at the end of each round. With 1, 2, or 3 or more Dynamo arcanists on the team, every ally's Ciphertext cap rises by 1, 2 or 5. |
| 2 | ATK +5% on entering battle. |
| 3 | On entering battle, gains 3 Moxie and raises every ally's Dynamo cap by 20. At the start of each round in which he holds a Bastion, all allies gain DMG Taken Reduction +30% for 2 rounds. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Mineral Wealth ×3; Page of Starlit Ascent ×3; Spell of Banishing ×6; Perpetual Cog ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Mineral Wealth ×5; Scroll of Starlit Ascent ×5; Cicada Wings ×6; Bifurcated Skeleton ×6 |
| 3 | 60 | Sharpodonty 200,000; Tome of Mineral Wealth ×8; Tome of Starlit Ascent ×8; Watch Core ×6; Walking Terror ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Bastion prevents the first 6 Control effects each round; Insight 3 raises the Dynamo cap by 40; Cipher Machine lasts 3 rounds and counts up to 40 Ciphertext. |
| 2 | Cipher Machine gives Critical DMG +30% and DMG Bonus +2.4% per Ciphertext removed. |
| 3 | Infinite Translation deals 240, 360 or 600% by rank; Closed-Loop Principle deals 240%; Cipher Machine gives DMG Bonus +2.8% per Ciphertext removed. |
| 4 | The Bastion from entering battle and from Closed-Loop Principle becomes 340% of his ATK; Meshing Minds gives 340, 510 or 850% by rank. |
| 5 | Under Lv.3, Amplified Surge gives Incantation Might +0.6% per Dynamo stack; Reality DMG allies deal an extra 8% per stack, Mental DMG allies gain a further 0.6%. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Enigma | 哑谜 | 啞謎 | エニグマ | 이니그마 |
