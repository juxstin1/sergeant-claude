---
description: Display earned medals and decorations with full military honors
allowed-tools: [Bash, Read]
---

# Medals - Hall of Honor

Display your earned medals and military decorations with full honors.

## Execution

Run `python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" medals`

## Display Format

```
╔═══════════════════════════════════════════════════════════╗
║                    🎖️ MEDAL CABINET 🎖️                     ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  🏅 COMBAT MEDALS                                         ║
║  ├── Purple Heart        - First bug fixed                ║
║  ├── Bronze Star         - 10 bugs eliminated             ║
║  ├── Silver Star         - 50 bugs eliminated             ║
║  └── Medal of Honor      - 100 bugs eliminated            ║
║                                                           ║
║  🎗️ SERVICE RIBBONS                                       ║
║  ├── Good Conduct        - 7 day streak                   ║
║  ├── Meritorious Service - 30 day streak                  ║
║  └── Distinguished       - 100 day streak                 ║
║                                                           ║
║  ⭐ CAMPAIGN STARS                                        ║
║  ├── First Campaign      - Complete first operation       ║
║  ├── Veteran             - Complete 10 operations         ║
║  └── War Hero            - Complete 50 operations         ║
║                                                           ║
║  🏆 SPECIAL DECORATIONS                                   ║
║  ├── Code Ninja          - 5 ambush strikes               ║
║  ├── Fortress Builder    - 10 fortifications              ║
║  └── Supreme Commander   - Reach max rank                 ║
║                                                           ║
║  TOTAL DECORATIONS: [X] / 15                              ║
╚═══════════════════════════════════════════════════════════╝
```

## Locked Medals

Show locked medals as:
```
║  └── [🔒] Medal of Honor - 100 bugs eliminated (67/100)  ║
```

## Post-Display

If any new medals earned since last check, display unlock notification:

```
🎖️ NEW MEDAL EARNED! 🎖️
Bronze Star - 10 bugs eliminated
"For valor in the face of spaghetti code"
```
