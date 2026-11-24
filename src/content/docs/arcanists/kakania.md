---
title: "Kakania"
description: "Kakania is a 6-star Plant arcanist who takes damage for her allies and turns it into Genesis DMG and healing."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "Once her Empathy is full (20% of her Max HP), Kakania stops taking damage for allies; her Ultimate empties it."
lastVerified: 2026-11-22
aliases:
  - "卡卡尼亞"
  - "卡卡尼亚"
  - "カカニア"
  - "카카니아"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Kakania.png"
    url: https://reverse1999.fandom.com/wiki/File:Kakania.png
  - title: "Image file, uploaded 2024-06-03"
    url: https://static.wikia.nocookie.net/reverse1999/images/3/3f/Kakania.png/revision/latest?cb=20240603154318
sources:
  - title: "re1999-data-global, global client 111.0.1077: character and skill tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Kakania, revision 85003"
    url: https://reverse1999.fandom.com/wiki/Kakania?oldid=85003
---

![Kakania, full-length art](/art/characters/kakania.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Plant |
| Damage | Mental |
| Tags | Heal, Support |
| Resonance Patterns | [U-shaped set](/systems/resonance/): Hyper, Overindulgence, Quiescence, Prudentiality, Equanimity |
| Psychubes recommended in game | [The Fighter's Best Wishes](/psychubes/the-fighters-best-wishes/) |
| Mainland release | 2024-06-06 |
| Global release | 2024-10-10 |
| Profile | [Cover, items, stories, skins and voice lines](/arcanists/kakania/profile/) |

## Incantations

### Subconscious

**Rank 1**: 1-target attack. Deals 180% Mental DMG plus (Current \[Empathy\] x180%) Genesis DMG.

**Rank 2**: 1-target attack. Deals 270% Mental DMG plus (Current \[Empathy\] x220%) Genesis DMG.

**Rank 3**: 1-target attack. Deals 450% Mental DMG plus (Current \[Empathy\] x260%) Genesis DMG.

### Association

**Rank 1**: 1-target buff. When cast on self, recovers (the user's Max HP x20%) HP. When cast on other allies, loses own (Max HP x10%) HP and grants \[Solace\] to the target for 2 rounds.

**Rank 2**: 1-target buff. When cast on self, recovers (the user's Max HP x30%) HP. When cast on other allies, loses own (Max HP x15%) HP and grants \[Solace\] to the target for 2 rounds.

**Rank 3**: 1-target buff. When cast on self, recovers (the user's Max HP x40%) HP. When cast on other allies, loses own (Max HP x20%) HP and grants \[Solace\] to the target for 2 rounds.

## Ultimate: Id, Ego, and Superego

1-target attack. Deals 400% Mental DMG plus (Current \[Empathy\] x1000%) Genesis DMG to the target, resets \[Empathy\] to zero, and then starts recording the damage the target takes for the round. At the end of the round, deals (recorded damage taken x30%) \[Static Genesis DMG\] to the target.

## Inheritance

**Insight 1 · Psychoanalysis**: When attacked, directs 50% of the damage taken by other allies to Kakania instead.

Whenever Kakania takes damage, 10% of that damage is stored as \[Empathy\], which can store up to 20% of Kakania's Max HP. Once \[Empathy\] is full, Kakania can no longer take damage on behalf of other allies.

**Insight 2 · Psychoanalysis II**: When entering battle, Max HP +5%.

**Insight 3 · Psychoanalysis III**: Whenever \[Empathy\] stores (Kakania's Max HP x3%) damage, recovers own (Max HP x10%) HP for all allies.

When being healed, deals (Current \[Empathy\] x100%) Genesis DMG to all enemies.

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Plantal Vimen ×6; Spell of Banishing ×6; Perpetual Cog ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Plantal Vimen ×10; Rough Silver Ingot ×4; Biting Box ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Plantal Vimen ×16; Glowing Mothwing ×6; Rheingold ×3 |

## Portrait

**Portrait 1**: **Association**: \[Solace\]'s ATK bonus is increased to 400, and the additional ATK bonus based on \[Empathy\] value is increased to 13%.

**Portrait 2**: **Psychoanalysis**: The threshold for \[Empathy\] to trigger healing is decreased from 3% HP to 2% HP. When healed, the Genesis DMG dealt is increased to (current Empathy value x120%).

**Portrait 3**: **Psychoanalysis**: \[Empathy\]'s maximum value is increased to 30% of Max HP. The percentage of damage taken that's converted to \[Empathy\] is changed to 15%.

**Portrait 4**: **Subconscious**: At rank 1/2/3, the Genesis DMG dealt is increased to (current \[Empathy\] value x270/310/350%).

**Portrait 5**: **Id, Ego, and Superego**: The additional Genesis DMG dealt is increased to (current \[Empathy\] value x1300%); the \[Static Genesis DMG\] dealt at the end of the round is increased to (recorded value x45%).

## Statuses

- **Empathy**: Enhances Kakania's incantations. Records Kakania's damage taken.
- **Solace**: Grants the target ally 300 ATK plus (on-cast \[Empathy\] value x10%) ATK.
- **Static Genesis DMG**: This type of Genesis DMG is not affected by relevant stat bonuses.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Kakania | 卡卡尼亚 | 卡卡尼亞 | カカニア | 카카니아 |
