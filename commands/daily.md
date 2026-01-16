---
description: Show today's combat log - XP earned, actions, streak status
allowed-tools: [Bash]
---

# Daily Combat Log

Display today's progress and activity.

## Execution

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" daily
```

## Response

```
╔═══════════════════════════════════════╗
║      📅 TODAY'S COMBAT LOG 📅          ║
╠═══════════════════════════════════════╣
║  ⚡ XP Earned: [amount]               ║
║  🎯 Actions: [count]                  ║
║  🔥 Streak: Day [N]                   ║
║  💥 Best Combo: [N]x                  ║
╚═══════════════════════════════════════╝
```

## Commentary

Based on activity:
- **No activity**: "No activity today yet. Get to work, soldier!"
- **Low activity**: "Slow day. Pick up the pace."
- **Medium activity**: "Solid progress. Keep pushing."
- **High activity**: "Outstanding combat operations today!"
