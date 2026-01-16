#!/usr/bin/env python3
"""
Leaderboard Export System for Sergeant Claude
Export your stats for flexing on other developers
"""

import json
import os
from datetime import datetime
from pathlib import Path

RANKS = [
    ("Recruit", 0, "Fresh Meat"),
    ("Private", 500, "Boot"),
    ("Private First Class", 1500, "Getting There"),
    ("Corporal", 3500, "Not Terrible"),
    ("Sergeant", 7000, "Competent"),
    ("Staff Sergeant", 12000, "Reliable"),
    ("Master Sergeant", 20000, "Seasoned"),
    ("First Sergeant", 32000, "Veteran"),
    ("Sergeant Major", 50000, "War Hero"),
    ("Lieutenant", 75000, "Officer Material"),
    ("Captain", 110000, "Leader"),
    ("Major", 160000, "Strategist"),
    ("Colonel", 230000, "Commander"),
    ("General", 320000, "Legendary"),
    ("Supreme Commander", 500000, "Mythic")
]

def get_profile_path():
    """Get the profile file path"""
    return Path.home() / ".sergeant_profile.json"

def load_profile():
    """Load user profile"""
    path = get_profile_path()
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {
        "xp": 0,
        "bugs_fixed": 0,
        "features_complete": 0,
        "tests_written": 0,
        "max_streak": 0,
        "unlocked_achievements": []
    }

def get_rank(xp):
    """Get current rank based on XP"""
    current_rank = RANKS[0]
    for rank in RANKS:
        if xp >= rank[1]:
            current_rank = rank
        else:
            break
    return current_rank

def export_markdown(profile, output_path=None):
    """Export stats as markdown for GitHub profile"""
    rank = get_rank(profile.get("xp", 0))
    xp = profile.get("xp", 0)
    achievements = len(profile.get("unlocked_achievements", []))

    md = f"""# 🎖️ Sergeant Claude Stats

> *Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M")}*

## Current Status

| Stat | Value |
|------|-------|
| 🎖️ **Rank** | {rank[0]} |
| ⭐ **Title** | {rank[2]} |
| ⚡ **Total XP** | {xp:,} |
| 🏅 **Achievements** | {achievements} / 15 |

## Combat Record

| Metric | Count |
|--------|-------|
| 🐛 Bugs Fixed | {profile.get('bugs_fixed', 0):,} |
| ✨ Features Shipped | {profile.get('features_complete', 0):,} |
| 🧪 Tests Written | {profile.get('tests_written', 0):,} |
| 🔥 Max Streak | {profile.get('max_streak', 0)} days |
| ⚔️ Ambushes | {profile.get('ambushes', 0):,} |
| 🏰 Fortifications | {profile.get('fortifications', 0):,} |

## Progress Bar

```
{'█' * min(20, int(xp / 25000))}{'░' * (20 - min(20, int(xp / 25000)))} {min(100, int(xp / 5000))}% to Supreme Commander
```

---

*Powered by [Sergeant Claude](https://github.com/juxstin1/sergeant-claude)*
"""

    if output_path:
        with open(output_path, 'w') as f:
            f.write(md)
        print(f"Stats exported to {output_path}")
    else:
        print(md)

    return md

def export_json(profile, output_path=None):
    """Export stats as JSON for integrations"""
    rank = get_rank(profile.get("xp", 0))

    data = {
        "generated_at": datetime.now().isoformat(),
        "rank": {
            "name": rank[0],
            "title": rank[2],
            "min_xp": rank[1]
        },
        "stats": {
            "xp": profile.get("xp", 0),
            "bugs_fixed": profile.get("bugs_fixed", 0),
            "features_complete": profile.get("features_complete", 0),
            "tests_written": profile.get("tests_written", 0),
            "max_streak": profile.get("max_streak", 0),
            "ambushes": profile.get("ambushes", 0),
            "fortifications": profile.get("fortifications", 0)
        },
        "achievements": {
            "unlocked": profile.get("unlocked_achievements", []),
            "count": len(profile.get("unlocked_achievements", []))
        }
    }

    if output_path:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Stats exported to {output_path}")
    else:
        print(json.dumps(data, indent=2))

    return data

def export_badge(profile):
    """Generate shield.io badge URLs"""
    rank = get_rank(profile.get("xp", 0))
    xp = profile.get("xp", 0)

    badges = {
        "rank": f"![Rank](https://img.shields.io/badge/Rank-{rank[0].replace(' ', '%20')}-blue)",
        "xp": f"![XP](https://img.shields.io/badge/XP-{xp:,}-green)",
        "bugs": f"![Bugs Fixed](https://img.shields.io/badge/Bugs%20Fixed-{profile.get('bugs_fixed', 0)}-red)",
        "streak": f"![Streak](https://img.shields.io/badge/Max%20Streak-{profile.get('max_streak', 0)}%20days-orange)"
    }

    print("Add these badges to your README:\n")
    for name, badge in badges.items():
        print(badge)
    print()

    return badges

def display_leaderboard_card(profile):
    """Display a shareable leaderboard card"""
    rank = get_rank(profile.get("xp", 0))
    xp = profile.get("xp", 0)

    print("""
╔═══════════════════════════════════════════════════════════╗
║               🏆 LEADERBOARD CARD 🏆                       ║
╠═══════════════════════════════════════════════════════════╣""")
    print(f"║   🎖️  RANK: {rank[0]:<42} ║")
    print(f"║   ⭐ TITLE: {rank[2]:<42} ║")
    print(f"║   ⚡ XP: {xp:,:<44} ║")
    print("║                                                           ║")
    print(f"║   🐛 Bugs Fixed: {profile.get('bugs_fixed', 0):<37} ║")
    print(f"║   ✨ Features: {profile.get('features_complete', 0):<39} ║")
    print(f"║   🧪 Tests: {profile.get('tests_written', 0):<42} ║")
    print(f"║   🔥 Best Streak: {profile.get('max_streak', 0)} days{' ' * 33}║")
    print("║                                                           ║")
    print("║   github.com/juxstin1/sergeant-claude                     ║")
    print("╚═══════════════════════════════════════════════════════════╝")

if __name__ == "__main__":
    import sys

    profile = load_profile()

    if len(sys.argv) > 1:
        command = sys.argv[1]
        output = sys.argv[2] if len(sys.argv) > 2 else None

        if command == "markdown" or command == "md":
            export_markdown(profile, output)
        elif command == "json":
            export_json(profile, output)
        elif command == "badges":
            export_badge(profile)
        elif command == "card":
            display_leaderboard_card(profile)
        else:
            print("Usage: leaderboard.py [markdown|json|badges|card] [output_path]")
    else:
        display_leaderboard_card(profile)
