---
description: Quick situation report - current status, rank, and objectives
allowed-tools: [Read, Bash]
---

# SITREP - Situation Report

Quick status report. Read state.md and display current position.

## Execution

1. Read `state.md` in current directory (if exists)
2. Run `python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" profile` for current stats
3. Display combined report

## Response Format

```
╔═══════════════════════════════════════╗
║           📋 SITREP 📋                 ║
╚═══════════════════════════════════════╝

🎖️  RANK: [Current Rank]
⚡ XP: [Current XP] / [Next Rank XP]
🔥 STREAK: [Days] days
💥 COMBO: [Current]x

MISSION STATUS: [From state.md]

ACTIVE OBJECTIVES:
- [ ] [From state.md]

NEXT ACTION:
[From state.md or "Awaiting orders, Private."]
```

If no state.md exists:
"No active operation detected. Run /init-op to establish command structure."
