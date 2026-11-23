---
title: "Perchta"
description: "Perchta is a 6-star Star healer and Pursuit support, out on the mainland China service since 4.1."
appliesTo: "Reverse: 1999, mainland China client 113.0.1422 (version 4.1); global client 111.0.1077 (version 3.9)"
caveat: "Perchta is out only on the mainland China service: the global client 111.0.1077 does not contain her. Her English skill and status names are community translations, not official ones."
lastVerified: 2026-11-22
aliases:
  - "佩施塔"
  - "ペルヒタ"
  - "페르히타"
art:
  - title: "Reverse: 1999 Wiki (Fandom), File:Perchta.png"
    url: https://reverse1999.fandom.com/wiki/File:Perchta.png
  - title: "Image file, uploaded 2026-11-17"
    url: https://static.wikia.nocookie.net/reverse1999/images/6/6c/Perchta.png/revision/latest?cb=20261117201105
sources:
  - title: "re1999-data, mainland client 113.0.1422: character.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/blob/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json/character.json
  - title: "re1999-data, mainland client 113.0.1422: skill.json and skill_effect.json"
    url: https://github.com/St-Pavlov-Foundation/re1999-data/tree/ab87bfc0e9855eca7075599a1adb667584afdd99/data/json
  - title: "re1999-data-global, global client 111.0.1077 (no entry for Perchta)"
    url: https://github.com/St-Pavlov-Foundation/re1999-data-global/blob/7308a19ec644c60fd539034c9815cfaa23237dda/data/json/character.json
  - title: "Reverse: 1999 Wiki (Fandom), Perchta, revision 108771"
    url: https://reverse1999.fandom.com/wiki/Perchta?oldid=108771
  - title: "Mainland official site: version 4.1, updated 2026-11-05"
    url: https://re.bluepoch.com/
---

![Perchta, full-length art](/art/characters/perchta.webp)

| Field | Value |
| --- | --- |
| Rarity | 6 stars |
| Afflatus | Star |
| Damage | Reality |
| Tags | Heal, 洞知, Support, Remove Debuffs |
| Resonance Patterns | [U-shaped set](/systems/resonance/): Hyper, Overindulgence, Quiescence, Prudentiality, Equanimity |
| Mainland release | 2026-11-05 |
| Global release | not yet |

Perchta keeps a summoned guardian, the Seven Friends, in front of the team. It takes most of the damage aimed at allies, while her incantations heal the whole team, cleanse it and mark one enemy with a wound that ticks every round. She belongs to the Pursuit group of arcanists, whose shared Pursuit Points open a phase in which their Pursuit incantations can be cast.

## Incantations

| Incantation | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| Her Requital (single-target attack) | 200% Reality DMG; Cleaved multiplier +6% | 300%; +9% | 500%; +15% |
| Sweet Sustenance (mass heal) | heals 20% of Perchta's Max HP | 25% | 30% |

- **Her Requital** puts [Cleaved] on a target that does not have it. On a target that already has it, the hit raises Cleaved's damage multiplier instead.
- **Sweet Sustenance** first evens out the HP of all allies, then removes one kind of Stats Down, Neg Status or Control effect from each of them, then heals each ally and the Seven Friends by the share of Perchta's Max HP in the table. The heal cannot crit; the Seven Friends' heal also ignores Healing Done bonuses.

## Ultimate: From Death I Wake

Deals 750% Reality DMG to all enemies. On a target with [Cleaved], it raises Cleaved's multiplier by 30% and settles Cleaved once at once, for Genesis DMG equal to 200% of the current multiplier. Then all allies gain [Happily Ever After] for 3 rounds. If the Seven Friends are gone, Perchta summons them again with their guard; if they are present, they recover HP equal to 60% of Perchta's Max HP.

## Statuses

| Status | Effect |
| --- | --- |
| Seven Friends | HP equal to 130% of Perchta's Max HP. Takes 70% of the damage any ally takes. When 2, 3, or 4 or more allies are hit at once, each point of its HP absorbs 1.2, 1.5 or 1.8 damage. Gone when its HP runs out or Perchta leaves the field. |
| Seven Friends' Bond | While it lasts, the Seven Friends cannot drop below 1 HP. When an enemy attack leaves them at 1 HP, Perchta spends the Bond and 50% of her current HP to heal them by 200% of the HP she spent. It returns at the start of the round 3 rounds after it was used. |
| Cleaved | At the end of each round, deals Genesis DMG equal to 20% of Perchta's Max HP to the holder and adds one Star Pursuit Point. Only one target has it at a time. Being applied again resets the multiplier, which rises to at most 200%. Removed when Perchta leaves the field. |
| Happily Ever After | Critical DMG +20%, DMG Bonus +20%. Gaining it again adds to its duration; it cannot be dispelled. |

## Pursuit: Schwarzwald

Perchta enters battle with the Pursuit Scope. Before an incantation, a team holding at least 6 Pursuit Points (15 at most) can enter Full Pursuit, taking up to 10 points into it, and spend them on Pursuit incantations of the same Afflatus.

- **"Schwarzwald"**, her Pursuit incantation: 500% Reality DMG to all enemies. If it removed 8 stacks of [Vengeful Thread], Perchta gains 8 stacks of [Fairest Hatred].
- **Vengeful Thread**: each stack cuts the Pursuit Point cost of a Pursuit incantation by 1; at most 8 stacks, all removed when used. Perchta gains 1 stack whenever an ally casts a Pursuit incantation, and 8 stacks on entering Full Pursuit.
- **Fairest Hatred**: when an ally casts a Pursuit incantation, that attack gains DMG Bonus +10% and Penetration Rate +7.5%; one stack is used each time, at most 8 stacks.
- Inside Full Pursuit, after the team has acted 5 and 7 times in total, all allies gain Pursuit DMG Bonus +15% and +30%. The bonus clears when Full Pursuit ends.

## Inheritance

| Insight | Effect |
| --- | --- |
| 0 (Precognition) | On entering battle, gains the Pursuit Scope and summons the Seven Friends with Seven Friends' Bond. |
| 1 | If the Seven Friends are present at the start of a round, all allies ignore up to 4 Control effects that round, and Perchta's first incantation that round costs no action point and gives her 1 extra Moxie. While Perchta is on the field, all allies gain DMG Taken Reduction +30%, and Moxie that any ally gains beyond the cap is stored, up to 3, and refills Moxie at the end of the round where there is room. |
| 2 | Max HP +5% on entering battle. |
| 3 | On entering battle, Perchta gains 1 Moxie and gives all allies Happily Ever After for 3 rounds. |

| Insight | Max level | Materials |
| --- | --- | --- |
| 1 | 40 | Sharpodonty 18,000; Page of Starlit Ascent ×6; Trembling Tooth ×5; Luminite Ore ×5 |
| 2 | 50 | Sharpodonty 40,000; Scroll of Starlit Ascent ×10; Cicada Wings ×6; Biting Box ×5 |
| 3 | 60 | Sharpodonty 200,000; Tome of Starlit Ascent ×16; Bogeyman ×5; Mistilteinn ×3 |

## Portrait

Each Portrait level costs one copy of Perchta.

| Portrait | Change |
| --- | --- |
| 1 | "Schwarzwald" costs 6 Pursuit Points; Vengeful Thread caps at 6 stacks and she gains 6 on entering Full Pursuit; Fairest Hatred gives DMG Bonus +20% and Penetration Rate +15%; the Full Pursuit team bonus rises to +20% and +40%. |
| 2 | Happily Ever After gives Critical DMG +35% and DMG Bonus +35%; the Full Pursuit team bonus needs 4 and 6 actions. |
| 3 | The Seven Friends have 180% of Perchta's Max HP; Sweet Sustenance heals 30, 35 or 40% by rank; the Ultimate heals the Seven Friends by 100% of her Max HP. |
| 4 | Her Requital raises the Cleaved multiplier by 10, 15 or 25% by rank; Cleaved deals 30% of her Max HP per round and its multiplier rises to 250%; the Ultimate raises the multiplier by 45% and settles it at 300%. |
| 5 | The Full Pursuit team bonus needs 3 and 5 actions and rises to +25% and +50%; Happily Ever After gives Critical DMG +50% and DMG Bonus +50%. |

## Names

| English | Simplified Chinese | Traditional Chinese | Japanese | Korean |
| --- | --- | --- | --- | --- |
| Perchta | 佩施塔 | 佩施塔 (not yet official) | not yet official | not yet official |
