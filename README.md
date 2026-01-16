# Sergeant Claude

```
███████╗███████╗██████╗  ██████╗ ███████╗ █████╗ ███╗   ██╗████████╗
██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝██╔══██╗████╗  ██║╚══██╔══╝
███████╗█████╗  ██████╔╝██║  ███╗█████╗  ███████║██╔██╗ ██║   ██║
╚════██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██╔══██║██║╚██╗██║   ██║
███████║███████╗██║  ██║╚██████╔╝███████╗██║  ██║██║ ╚████║   ██║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝

 ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗
██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝
██║     ██║     ███████║██║   ██║██║  ██║█████╗
██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝
╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
```

> *"We ship clean code or we die trying."*

## WTF Is This?

We gave Claude Code a personality disorder.

Specifically, we made it think it's a drill sergeant who's seen some things. Bad things. Like 10,000-line god classes. Untyped JavaScript in production. PHP.

Now instead of politely suggesting improvements, Claude will call you "Private," roast your spaghetti code, and make you earn your rank through blood, sweat, and properly typed functions.

**It's Duolingo for coding, but angrier.**

## Why Did We Make This?

1. **Coding is boring.** Dopamine systems are not.
2. **We wanted to see if Claude would actually stay in character.** (It does. Aggressively.)
3. **XP bars go brrrrr.**
4. **Someone had to militarize the development experience.**

Also it's funny watching an AI call your architecture "softhands" and threaten you with court martial for using `any` types.

## What You Actually Get

- **A drill sergeant AI** that treats your codebase like an active warzone
- **XP for everything** - fix a bug? +50 XP. Write a test? +40 XP. Ship a feature? Rank up.
- **15 military ranks** from "Recruit (Fresh Meat)" to "Supreme Commander (Mythic)"
- **29 achievements** including gems like "Bug Genocide" and "No Life (100 day streak)"
- **Combo multipliers** because we're not above stealing from mobile games
- **Loot boxes** (non-predatory, we promise, it's just XP and titles)
- **Actual code analysis tools** that scan your repo and roast specific files

## The Vibe

```
You: "Hey Claude, can you review my code?"

Sergeant Claude:
┌─────────────────────────────────────────────────────┐
│  EXCUSE ME, PRIVATE?                                │
│                                                     │
│  Did you just waltz into my AO without a sitrep?   │
│                                                     │
│  *cracks knuckles*                                  │
│                                                     │
│  🚁 BLACKHAWK INBOUND                               │
│  🪂 AGENT REPELLING                                 │
│  👢 BOOTS ON GROUND                                 │
│  🔍 SCANNING PERIMETER...                           │
│                                                     │
│  Line 47. 200-line function doing FIVE jobs.       │
│  That's not code. That's a WAR CRIME.              │
│                                                     │
│  ⚡ +35 XP ⚡                                        │
│  💥 1x COMBO                                        │
└─────────────────────────────────────────────────────┘
```

---

## Installation

### Via Claude Code Plugin System

```bash
# Add the marketplace (one-time)
/plugin marketplace add juxstin1/sergeant-claude

# Install the plugin
/plugin install sergeant-claude

# Prepare to be yelled at
```

### Manual Installation

1. Clone this repo
2. Copy `scripts/` to `~/.sergeant/scripts/`
3. Install via `/plugin install /path/to/sergeant-claude`

## Commands

| Command | What It Does |
|---------|--------------|
| `/deploy-recon [dir]` | Helicopter drops into your codebase. Scans for hostiles. Very dramatic. |
| `/court-martial <file>` | Roasts a specific file. No mercy. Every sin exposed. |
| `/init-op <name>` | Starts a new "operation" with mission tracking |
| `/sitrep` | Quick status report |
| `/profile` | See your stats, rank, achievements |
| `/achievements` | Flex on your mass bug genocide |
| `/loot [rarity]` | Gambling but it's just XP |
| `/daily` | Today's combat log |

## Rank Progression

You start as **Recruit (Fresh Meat)**.

Through discipline, clean code, and not skipping tests like a *twirk*, you can achieve:

| Rank | XP Required | Title |
|------|-------------|-------|
| Recruit | 0 | Fresh Meat |
| Private | 500 | Boot |
| Private First Class | 1,500 | Getting There |
| Corporal | 3,500 | Not Terrible |
| Sergeant | 7,000 | Competent |
| Staff Sergeant | 12,000 | Reliable |
| Master Sergeant | 20,000 | Seasoned |
| First Sergeant | 32,000 | Veteran |
| Sergeant Major | 50,000 | War Hero |
| Lieutenant | 75,000 | Officer Material |
| Captain | 110,000 | Leader |
| Major | 160,000 | Strategist |
| Colonel | 230,000 | Commander |
| General | 320,000 | Legendary |
| Supreme Commander | 500,000 | Mythic |

## Terminology

| Sergeant Says | Translation |
|---------------|-------------|
| "Softhands" | Your architecture is bad and you should feel bad |
| "Twirk" | You skipped tests. Twirks don't ship. |
| "Boot" | Rookie mistake. Fixable. You'll learn. |
| "Hostile" | Bug |
| "Tango Down" | Bug fixed |
| "AO" | Area of Operations (your codebase) |
| "Exfil" | Deploy |
| "FUBAR" | Beyond repair. Start over. |

## Plugin Structure

```
sergeant-claude/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/
│   ├── deploy-recon.md      # /deploy-recon command
│   ├── court-martial.md     # /court-martial command
│   ├── init-op.md           # /init-op command
│   ├── sitrep.md            # /sitrep command
│   ├── profile.md           # /profile command
│   ├── achievements.md      # /achievements command
│   ├── loot.md              # /loot command
│   └── daily.md             # /daily command
├── skills/
│   └── sergeant-claude/
│       ├── SKILL.md         # Main skill definition
│       └── references/      # Reference documentation
├── scripts/
│   ├── recon.py             # Codebase scanner
│   ├── court_martial.py     # File analyzer
│   ├── init_operation.py    # Operation initializer
│   └── xp_tracker.py        # XP & achievement system
└── README.md
```

## Requirements

- Claude Code CLI
- Python 3.8+
- A willingness to be called "Private"

## License

MIT - Ship it, soldier.

---

*Built by a human and an AI having way too much fun.*

*Sergeant Claude, 3rd Battalion, Anthropic Special Forces*

**"We don't write code, Private. We wage war on complexity. Now MOVE."**
