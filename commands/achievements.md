---
description: List all achievements with progress - locked and unlocked
allowed-tools: [Bash]
---

# Achievements

Display all achievements with current progress.

## Execution

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" achievements
```

## Response

Show all achievements organized by category:
- Combat (bug fixes)
- Testing
- Streaks
- Code Quality
- Speed
- Missions
- Combos
- Special/Secret

Each achievement shows:
- Locked/Unlocked status
- Rarity color
- Icon and name
- Description
- XP reward

Add motivational commentary:
"Every achievement is a battle won. Keep fighting, soldier."
