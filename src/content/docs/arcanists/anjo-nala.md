---
title: "Anjo Nala"
description: "Anjo Nala is a 6-star Beast arcanist who deals Mental DMG and binds an ally to cast its Ultimate."
appliesTo: "Reverse: 1999, global client 111.0.1077 (version 3.9) and mainland China client 113.0.1422 (version 4.1)"
caveat: "The ally Anjo Nala binds cannot gain Moxie or cast its Ultimate on its own; it casts one only inside her Ultimate, which costs it 50% of its current HP (15% from Euphoria level 2)."
lastVerified: 2026-11-22
aliases:
  - "天使娜娜"
  - "アンジョナナ"
  - "안조 날라"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Anjo Nala.png"
    url: https://reverse1999.fandom.com/wiki/File:Anjo_Nala.png
  - title: "Image file, uploaded 2024-10-06"
    url: https://static.wikia.nocookie.net/reverse1999/images/f/f1/Anjo_Nala.png/revision/latest?cb=20241006214830
sources:
  - title: "re1999-data-global, global client 111.0.1077: character, skill and Euphoria tables"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/tree/7308a19ec644c60fd539034c9815cfaa23237dda/data/json
  - title: "re1999-data-global, global client 111.0.1077: English text"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/configs/language/language_en.json
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Anjo Nala, revision 84950"
    url: https://reverse1999.fandom.com/wiki/Anjo_Nala?oldid=84950
---

![Anjo Nala, full-length art](/art/characters/anjo-nala.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Beast |
| Damage | Mental |
| Tags | DPS, Extra Action, Ritual, Control, Channel |
| Resonance Patterns | [Z-shaped set](/systems/resonance/): Elucidation, Genuinity, Mercy, Equanimity, Equibalance |
| Psychubes recommended in game | [Transcendent Love](/psychubes/transcendent-love/), [Outside the City](/psychubes/outside-the-city/), [Blasphemer of Night](/psychubes/blasphemer-of-night/) |
| Mainland release | 2024-09-19 |
| Global release | 2025-01-09 |
| Profile | [Cover, items, stories, skins and voice lines](/arcanists/anjo-nala/profile/) |

## Incantations

### Feast of Lust

**Rank 1**: 1-target attack. Deals 180% Mental DMG, inflicts \[Titillated\] for 2 rounds on the target hit; if Anjo Nala is in the \[Hymn\] status, reduce \[Hymn\]'s remaining duration by 1 round; when attacking, for every type of \[Neg Status\] the target has, this attack deals an additional 40% Mental DMG.

**Rank 2**: 1-target attack. Deals 270% Mental DMG, inflicts \[Titillated\] for 2 rounds on the target hit; if Anjo Nala is in the \[Hymn\] status, reduce \[Hymn\]'s remaining duration by 1 round; when attacking, for every type of \[Neg Status\] the target has, this attack deals an additional 60% Mental DMG.

**Rank 3**: 1-target attack. Deals 450% Mental DMG, inflicts \[Titillated\] for 2 rounds on the target hit; if Anjo Nala is in the \[Hymn\] status, reduce \[Hymn\]'s remaining duration by 1 round; when attacking, for every type of \[Neg Status\] the target has, this attack deals an additional 100% Mental DMG.

### Twin Phantoms

**Rank 1**: Self channel. Enters the \[Hymn\] status for 7 rounds; when the channel ends, casts \[Angel's Temptation\]. When casting this incantation, if Anjo Nala is already in the \[Hymn\] status, then reduce the duration of \[Hymn\] by 1 round.

**Rank 2**: Self channel. Enters the \[Hymn\] status for 7 rounds; when the channel ends, casts \[Angel's Temptation\]. When casting this incantation, if Anjo Nala is already in the \[Hymn\] status, then reduce the duration of \[Hymn\] by 2 rounds.

**Rank 3**: Self channel. Enters the \[Hymn\] status for 7 rounds; when the channel ends, casts \[Angel's Temptation\]. When casting this incantation, if Anjo Nala is already in the \[Hymn\] status, then reduce the duration of \[Hymn\] by 3 rounds.

## Ultimate: Interwoven Dreams

Self channel. Both Anjo Nala and her bound ally enter a channeling status and cannot act for 1 round; at the start of the next round, the bound ally loses (Current HP x50%) HP and casts their ultimate, then Anjo Nala casts her own ultimate:

Mass attack. Inflicts 2 random effects from \[Collection of Debuffs\] on all enemies, then deals 500% Mental DMG to all enemies; for every type of \[Neg Status\] held among all enemies, this attack deals an additional 60% Mental DMG.

## Inheritance

**Insight 1 · Oath Bound**: When entering battle, Anjo Nala chooses another ally to bind with. The type of binding is determined by the Afflatus of the bound character, and provides enhancements to both characters:

Spirit/Intellect \[Mind and Flesh\]: 4% of each other's ATK and Max HP.

Beast/Plant \[Bone and Blood\]: 8% of each other's Critical DMG and Reality DEF.

Mineral/Star \[Form and Phantom\]: 8% of each other's Critical Rate and Mental DEF.

Anjo Nala's Max Moxie is changed to 12 while Ultimate Moxie Cost or Consumption is changed to 8.

The bound ally cannot gain or cast ultimates.

All Moxie gained by the bound ally will be transferred to Anjo Nala instead.

**Insight 2 · Oath Bound II**: Critical DMG +15% when entering battle.

**Insight 3 · Oath Bound III**: After the bound ally actively casts an incantation, if Anjo Nala is in the \[Hymn\] status, reduce the duration of the \[Hymn\] status by 1 round, and trigger additional effects based on the binding's type:

\[Mind and Flesh\]: Anjo Nala casts a rank 1 \[Feast of Lust\] as a follow-up attack on the enemy with the lowest HP percentage.

\[Bone and Blood\]: Anjo Nala gains 1 additional Moxie.

\[Form and Phantom\]: Anjo Nala casts 1 \[Angel's Temptation\], up to 2 times per round.

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Beastly Thirst ×6; Spell of Banishing ×6; Rough Silver Ingot ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Beastly Thirst ×10; Liquefied Terror ×5; Golden Grass Incense ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Beastly Thirst ×16; Watch Core ×6; Rheingold ×3 |

## Portrait

**Portrait 1**: **Oath Bound**: \[Form and Phantom\]'s follow-up attack can now be casted up to 3 times per round, and \[Angel's Temptation\]'s Mental DMG dealt is increased to 250%.

**Portrait 2**: **Twin Phantoms**: When \[Angel's Temptation\] is casted from a completed channel, the Mental DMG dealt is increased to 375%, and the ATK reduction from \[Captivated\] is boosted to 15%.

**Portrait 3**: **Interwoven Dreams**: The Mental DMG dealt is increased to 600%; and for every type of \[Neg Status\], the additional Mental DMG dealt is increased to 100%.

\[Bone and Blood\]'s additional Moxie gained is increased to 2.

**Portrait 4**: **Oath Bound**: \[Mind and Flesh\]'s stat bonus is increased to 8%;

\[Bone and Blood\]'s stat bonus is increased to 18%;

\[Form and Phantom\]'s stat bonus is increased to 18%;

The stack requirement for \[Titillated\] to become Captivated is reduced to 2.

**Portrait 5**: **Interwoven Dreams**: The number of random debuffs inflicted by \[Collection of Debuffs\] is increased to 4; and for every type of \[Neg Status\], the additional Mental DMG dealt is increased to 140%.

## Euphoria

**Epiphany 1, level 1**: New Effects Added: After the \[Bound\] ally performs an extra action, the binding between them and Anjo Nala is enhanced, and both gain 1 stack of \[Harmonic Tapestry\]. \[Harmonic Tapestry\] is stackable up to 8 times. Additional effects based on binding type:

Spirit/Intellect \[Mind and Flesh\]: ATK +2%.

Beast/Plant \[Bone and Blood\]: Ultimate Might +6%.

Star/Mineral \[Form and Phantom\]: Extra Action DMG +10%.

**Epiphany 1, level 2**: New Effects Added: When casting **Interwoven Dreams**, the Current HP consumed is reduced from 50% to 15%. When the binding is enhanced, Anjo Nala gains Moxie +1 and 2 stacks of \[Ceremonious: Critical DMG\] (4 extra stacks of \[Ceremonious: Critical DMG\] for \[Bone and Blood\]).

**Epiphany 1, level 3**: **Interwoven Dreams** New Effects Added: After attacking, gains \[The Final Sustain\] for 2 rounds: **Feast of Lust** and \[Angel's Temptation\] deal an additional (base Mental DMG x300%) Mental DMG.

**Epiphany 1, level 4**: New Effects Added: At 8 stacks of \[Harmonic Tapestry\], **Interwoven Dreams** no longer consumes AP nor takes up the allied Incantation Draw Limit, and it also grants Moxie +2 after casting. Additional effects for Anjo Nala based on binding type:

Spirit/Intellect \[Mind and Flesh\]: **Feast of Lust** deals an additional 400% Mental DMG and accelerates \[Hymn\] channeling by 1 round.

Beast/Plant \[Bone and Blood\]: **Interwoven Dreams** deals an additional (base Mental DMG x140%) Mental DMG. **Interwoven Dreams**'s Ultimate Might enhancement is doubled.

Star/Mineral \[Form and Phantom\]:When attacking with \[Angel's Temptation\], deals an additional (base Mental DMG x200%) Mental DMG and excess Critical Rate is converted to Critical DMG.

## Statuses

- **Titillated**: DMG Bonus -10%; after 3 stacks, changes to \[Captivated\] for 1 round.
- **Hymn**: Channels for 7 rounds; when the channel ends, casts \[Angel's Temptation\].
- **Angel's Temptation**: Mass attack. Inflicts \[Titillated\] on all enemies, then deals 150% Mental DMG; if this incantation is casted after \[Hymn\] has completed its channeling, the inflicted \[Titillated\] changes to \[Captivated\] instead; deals an additional 250% Mental DMG.
- **Collection of Debuffs**: There are 7 effects: \[Blind\], \[Nasty Wound\], \[Mis-aim\], \[Weakness\], \[Scared\], \[Confusion\] and \[Fracture I\]. Prioritizes effects not yet applied.
- **Mind and Flesh**: The binder and the bound ally gain 4% of each other's ATK and Max HP.
- **Bone and Blood**: The binder and the bound ally gain 8% of each other's Critical DMG and Reality DEF.
- **Form and Phantom**: The binder and the bound ally gain 8% of each other's Critical Rate and Mental DEF.
- **Captivated**: Cannot act. ATK -10%; grants an equal amount of ATK to Anjo Nala.
- **Ceremonious: Critical DMG**: Ultimate Critical DMG +3%, up to 100 stacks. Removes upon trigger. Undispellable.
- **The Final Sustain**: \[Feast of Lust\] and \[Angel's Temptation\] deal (base Mental DMG x300%) additional Mental DMG.
- **Blind**: DMG Bonus -30% when attacking 1 target.
- **Nasty Wound**: Healing Taken -50%.
- **Mis-aim**: DMG Bonus -30% when attacking multiple targets.
- **Weakness**: DMG Bonus -25% when attacking (reduced by 1 stack on trigger).
- **Scared**: Increases Mental DMG taken by 25% (-1 stack after triggering).
- **Confusion**: Critical Resist -25% (stackable, each stack timed independently).
- **Fracture I**: When attacked, takes additional (the user's ATK x20%) Genesis DMG.

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Anjo Nala | 天使娜娜 | 天使娜娜 | アンジョナナ | 안조 날라 |
