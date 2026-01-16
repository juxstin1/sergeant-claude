---
description: Open a loot box for random rewards
argument-hint: [rarity]
allowed-tools: [Bash]
---

# Loot Box

Open a loot box for random rewards!

## Execution

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" loot $ARGUMENTS
```

Optional rarity argument: common, uncommon, rare, epic, legendary
If not specified, rarity is randomly determined.

## Dramatic Opening

```
🎁 SUPPLY DROP INCOMING...

╔═══════════════════════════════════════╗
║         📦 LOOT BOX 📦                 ║
║         [RARITY]                       ║
╚═══════════════════════════════════════╝

*opening...*

🎉 YOU RECEIVED:
→ [Reward Name]
→ [Effect]
```

## Possible Rewards

- **XP Packs**: Direct XP injection
- **Multiplier Boosts**: Temporary XP multiplier (1.5x, 2x, 3x)
- **Titles**: New display titles

## Response Based on Rarity

- **Common**: "Standard issue. It's something."
- **Uncommon**: "Better than MREs."
- **Rare**: "Now we're talking, soldier."
- **Epic**: "Outstanding pull!"
- **Legendary**: "JACKPOT! The gods smile upon you today."
