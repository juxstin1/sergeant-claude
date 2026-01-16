---
description: Display full soldier profile with XP, rank, achievements, and stats
allowed-tools: [Bash]
---

# Soldier Profile

Display comprehensive soldier profile with all stats and progression.

## Execution

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" profile
```

## Response

Display the full profile output including:
- Current rank and title
- XP progress bar to next rank
- Combat stats (bugs fixed, tests written, objectives, missions)
- Streak and combo status
- Achievement progress
- Recent achievements

Add military commentary based on rank:
- **Recruit**: "Fresh meat. Everyone starts somewhere."
- **Private-Corporal**: "You're learning, soldier."
- **Sergeant-Staff Sgt**: "Now you're getting somewhere."
- **Master Sgt+**: "Outstanding performance. Keep it up."
