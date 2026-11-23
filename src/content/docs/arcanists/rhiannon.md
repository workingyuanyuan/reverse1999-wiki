---
title: "Rhiannon"
description: "Rhiannon is a 6-star Beast support who deals Mental DMG, buffs the team and gives it an extra round."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Raptor Kinship starts at 0% charge and needs 100% before it gives the team an extra round; Insight III starts it at 70%."
lastVerified: 2026-11-22
aliases:
  - "小瑞安儂"
  - "小瑞安侬"
  - "リアンノン"
  - "리아논"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Rhiannon.png"
    url: https://reverse1999.fandom.com/wiki/File:Rhiannon.png
  - title: "Image file, uploaded 2026-05-20"
    url: https://static.wikia.nocookie.net/reverse1999/images/b/bf/Rhiannon.png/revision/latest?cb=20260520190022
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Rhiannon, revision 93343"
    url: https://reverse1999.fandom.com/wiki/Rhiannon?oldid=93343
---

![Rhiannon, full-length art](/art/characters/rhiannon.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Mental |
| Tags | Support, All-Rounder |
| Resonance Patterns | [U-shaped set](/systems/resonance/): Hyper, Overindulgence, Quiescence, Prudentiality, Equanimity |
| Psychubes recommended in game | [The Soft Rain of Yesterday](/psychubes/the-soft-rain-of-yesterday/) |
| Mainland release | 2026-04-30 |
| Global release | 2026-08-13 |

Rhiannon gains Attunement stacks each round and spends one with each incantation; every stack spent charges her Raptor Kinship and gives her Rapport, which raises the team's Stronger Afflatus damage. At 100% charge, Raptor Kinship gives the team an extra round in which enemies cannot act and ends it with Feast Call, a large attack on all enemies. Her Ultimate buffs the other allies and lets her cast reinforced incantations without spending AP. She counts as an All-Rounder.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Babble-Gabble (mass attack) | 200% Mental DMG; ATK +12% for 3 rounds | 300%; ATK +13% | 500%; ATK +14% |
| Sneaky-Peeky (mass buff) | all allies Flocksong 3 rounds; Max HP +12% for 3 rounds | Max HP +13% | Max HP +14% |

Both incantations spend 1 stack of [Attunement] for Rhiannon's own bonus in the table: ATK before Babble-Gabble hits, Max HP with Sneaky-Peeky.

- [Flocksong]: Incantation Might +30% and Ultimate Might +30%.
- [Attunement]: each stack spent charges Raptor Kinship by 8% and gives Rhiannon 2 stacks of [Rapport] for 3 rounds. At most 4 stacks.
- [Rapport]: a [Force Field] that raises the Stronger Afflatus DMG Multiplier of all allies by 4% per stack; at most 5 stacks, each with its own duration, and it cannot be dispelled. A Force Field ends when its holder leaves the field.

## Ultimate: Chirping Chorus

A team buff. All other allies gain [Adar Llwch Gwin] for 3 rounds, and Rhiannon gains [Bendith] for 4 rounds.

- [Adar Llwch Gwin]: ATK equal to 8% of Rhiannon's ATK, at most 250, and Max HP equal to 8% of her Max HP, at most 1250.
- [Bendith]: incantations Rhiannon casts herself cost no AP, and her basic incantations become their reinforced forms.

| Reinforced incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Babble-Gabble · Bendith (mass attack) | 400% Mental DMG; ATK +12% | 600%; ATK +13% | 1000%; ATK +14% |
| Sneaky-Peeky · Bendith (mass buff) | Flocksong; Max HP +12% | Max HP +13% | Max HP +14% |

- **Babble-Gabble · Bendith** also lowers the Critical DEF of all enemies by 15% for 3 rounds, and by 3% more for each stack of Rapport Rhiannon holds when the enemy is hit, up to 15% more.
- **Sneaky-Peeky · Bendith** also gives all allies DMG Bonus +15% for 3 rounds, and 3% more for each stack of Rapport she holds when the ally attacks, up to 15% more.

## Raptor Kinship

Rhiannon enters battle with Raptor Kinship at 0% charge; it holds up to 150%. Once it reaches 100%, she can activate it before incantations are cast: it spends 100% and puts her in [Sensory Bond].

- [Sensory Bond]: allies take an extra round of actions in which enemies cannot act. Right before the AP Area resolves, a rankless [Feast Call] joins the queue.
- [Feast Call]: deals 1500% Mental DMG to all enemies, plus 150% for each stack of Rapport Rhiannon holds; it always counts as Stronger Afflatus.
- [All-Rounder]: Rhiannon counts as a member of the Lingering Glow, Bloodtithe, Dynamo, Inspiration, Conduit, Burn, HP Sacrifice, Poison, Ritual, Rank Up, Extra Action and Shift teams.

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | Gives her Raptor Kinship, starting at 0% charge; she gains 2 stacks of Attunement at the start of each round. She is an All-Rounder. |
| 1 | She gains 1 stack of Rapport for 3 rounds at the start of each round. |
| 2 | ATK +5% on entering battle. |
| 3 | On entering battle, Moxie +3 and Raptor Kinship charged to 70%. At the end of each round, if she holds Attunement, she spends 1 stack for Moxie +1. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Trembling Tooth ×6; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Solidus ×6; Clawed Pendulum ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Platinum Ouija ×6; Mistilteinn ×3 |

## Portrait

| Portrait | Change |
| --- | --- |
| 1 | Moxie +5 on entering battle; Flocksong gives Incantation Might +45% and Ultimate Might +45%. |
| 2 | Raptor Kinship starts at 85%; each stack of Attunement spent charges 10% and gives 3 stacks of Rapport; Rapport stacks up to 7 and gives +5% per stack; Feast Call deals 3000%, plus 300% per stack of Rapport. |
| 3 | Babble-Gabble · Bendith lowers Critical DEF by 20%, and up to 21% more from Rapport; Sneaky-Peeky · Bendith gives DMG Bonus +20%, and up to 21% more from Rapport. |
| 4 | Adar Llwch Gwin gives 10% of her ATK, at most 310, and 10% of her Max HP, at most 1550. |
| 5 | She gains 2 stacks of Rapport at the start of each round; Raptor Kinship starts at 100%; each stack of Attunement spent charges 12.5% and gives 4 stacks of Rapport; Rapport stacks up to 10; Feast Call deals 5000%, plus 500% per stack of Rapport. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Rhiannon | 小瑞安侬 | 小瑞安儂 | リアンノン | 리아논 |
