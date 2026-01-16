#!/usr/bin/env python3
"""
Achievement and Medal System for Sergeant Claude
Handles unlock notifications and progress tracking
"""

import json
import os
from datetime import datetime
from pathlib import Path

ACHIEVEMENTS = {
    # Combat Medals
    "purple_heart": {
        "name": "Purple Heart",
        "description": "First bug fixed",
        "category": "combat",
        "requirement": {"bugs_fixed": 1},
        "xp_bonus": 50
    },
    "bronze_star": {
        "name": "Bronze Star",
        "description": "10 bugs eliminated",
        "category": "combat",
        "requirement": {"bugs_fixed": 10},
        "xp_bonus": 100
    },
    "silver_star": {
        "name": "Silver Star",
        "description": "50 bugs eliminated",
        "category": "combat",
        "requirement": {"bugs_fixed": 50},
        "xp_bonus": 250
    },
    "medal_of_honor": {
        "name": "Medal of Honor",
        "description": "100 bugs eliminated",
        "category": "combat",
        "requirement": {"bugs_fixed": 100},
        "xp_bonus": 500
    },

    # Service Ribbons
    "good_conduct": {
        "name": "Good Conduct",
        "description": "7 day streak",
        "category": "service",
        "requirement": {"max_streak": 7},
        "xp_bonus": 100
    },
    "meritorious_service": {
        "name": "Meritorious Service",
        "description": "30 day streak",
        "category": "service",
        "requirement": {"max_streak": 30},
        "xp_bonus": 300
    },
    "distinguished_service": {
        "name": "Distinguished Service",
        "description": "100 day streak",
        "category": "service",
        "requirement": {"max_streak": 100},
        "xp_bonus": 1000
    },

    # Campaign Stars
    "first_campaign": {
        "name": "First Campaign",
        "description": "Complete first operation",
        "category": "campaign",
        "requirement": {"operations_complete": 1},
        "xp_bonus": 100
    },
    "veteran": {
        "name": "Veteran",
        "description": "Complete 10 operations",
        "category": "campaign",
        "requirement": {"operations_complete": 10},
        "xp_bonus": 300
    },
    "war_hero": {
        "name": "War Hero",
        "description": "Complete 50 operations",
        "category": "campaign",
        "requirement": {"operations_complete": 50},
        "xp_bonus": 750
    },

    # Special Decorations
    "code_ninja": {
        "name": "Code Ninja",
        "description": "5 ambush strikes",
        "category": "special",
        "requirement": {"ambushes": 5},
        "xp_bonus": 150
    },
    "fortress_builder": {
        "name": "Fortress Builder",
        "description": "10 fortifications",
        "category": "special",
        "requirement": {"fortifications": 10},
        "xp_bonus": 200
    },
    "supreme_commander": {
        "name": "Supreme Commander",
        "description": "Reach maximum rank",
        "category": "special",
        "requirement": {"xp": 500000},
        "xp_bonus": 0  # Already at max
    },

    # Hidden Achievements
    "early_bird": {
        "name": "Early Bird",
        "description": "Code before 6 AM",
        "category": "hidden",
        "requirement": {"special": "early_bird"},
        "xp_bonus": 75
    },
    "night_owl": {
        "name": "Night Owl",
        "description": "Code after midnight",
        "category": "hidden",
        "requirement": {"special": "night_owl"},
        "xp_bonus": 75
    }
}

def get_profile_path():
    """Get the profile file path"""
    return Path.home() / ".sergeant_profile.json"

def load_profile():
    """Load user profile"""
    profile_path = get_profile_path()
    if profile_path.exists():
        with open(profile_path, 'r') as f:
            return json.load(f)
    return {
        "xp": 0,
        "bugs_fixed": 0,
        "features_complete": 0,
        "tests_written": 0,
        "operations_complete": 0,
        "ambushes": 0,
        "fortifications": 0,
        "current_streak": 0,
        "max_streak": 0,
        "unlocked_achievements": [],
        "last_active": None
    }

def save_profile(profile):
    """Save user profile"""
    with open(get_profile_path(), 'w') as f:
        json.dump(profile, f, indent=2)

def check_achievement(profile, achievement_id):
    """Check if an achievement should be unlocked"""
    if achievement_id in profile.get("unlocked_achievements", []):
        return False  # Already unlocked

    achievement = ACHIEVEMENTS.get(achievement_id)
    if not achievement:
        return False

    requirement = achievement["requirement"]

    for key, value in requirement.items():
        if key == "special":
            # Special achievements checked elsewhere
            continue
        if profile.get(key, 0) < value:
            return False

    return True

def unlock_achievement(profile, achievement_id):
    """Unlock an achievement and display notification"""
    achievement = ACHIEVEMENTS[achievement_id]

    if "unlocked_achievements" not in profile:
        profile["unlocked_achievements"] = []

    profile["unlocked_achievements"].append(achievement_id)
    profile["xp"] = profile.get("xp", 0) + achievement["xp_bonus"]

    # Display unlock notification
    print(f"""
╔═══════════════════════════════════════════════════════════╗
║              🎖️ ACHIEVEMENT UNLOCKED! 🎖️                   ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║   {achievement['name']:^50}  ║
║   "{achievement['description']}"
║                                                           ║
║   +{achievement['xp_bonus']} XP BONUS                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""")

    save_profile(profile)
    return achievement["xp_bonus"]

def check_all_achievements(profile):
    """Check and unlock all eligible achievements"""
    newly_unlocked = []

    for achievement_id in ACHIEVEMENTS:
        if check_achievement(profile, achievement_id):
            unlock_achievement(profile, achievement_id)
            newly_unlocked.append(achievement_id)

    return newly_unlocked

def get_achievement_progress(profile, achievement_id):
    """Get progress towards an achievement"""
    achievement = ACHIEVEMENTS.get(achievement_id)
    if not achievement:
        return None

    requirement = achievement["requirement"]
    progress = {}

    for key, target in requirement.items():
        if key == "special":
            progress[key] = {"current": "?", "target": "special"}
        else:
            current = profile.get(key, 0)
            progress[key] = {"current": current, "target": target, "percent": min(100, int(current/target*100))}

    return progress

def display_medals(profile):
    """Display all medals with unlock status"""
    categories = {
        "combat": "🏅 COMBAT MEDALS",
        "service": "🎗️ SERVICE RIBBONS",
        "campaign": "⭐ CAMPAIGN STARS",
        "special": "🏆 SPECIAL DECORATIONS",
        "hidden": "🔮 HIDDEN ACHIEVEMENTS"
    }

    unlocked = profile.get("unlocked_achievements", [])
    total_unlocked = len(unlocked)
    total_achievements = len(ACHIEVEMENTS)

    print("╔═══════════════════════════════════════════════════════════╗")
    print("║                    🎖️ MEDAL CABINET 🎖️                     ║")
    print("╠═══════════════════════════════════════════════════════════╣")

    for cat_id, cat_name in categories.items():
        print(f"║  {cat_name:<55} ║")

        cat_achievements = [(k, v) for k, v in ACHIEVEMENTS.items() if v["category"] == cat_id]

        for ach_id, ach in cat_achievements:
            if ach_id in unlocked:
                status = "✓"
                print(f"║  ├── {status} {ach['name']:<20} - {ach['description']:<25} ║")
            else:
                progress = get_achievement_progress(profile, ach_id)
                if progress:
                    key = list(progress.keys())[0]
                    if key != "special":
                        pct = progress[key]["percent"]
                        print(f"║  ├── 🔒 {ach['name']:<18} - {ach['description']:<15} ({pct}%) ║")
                    else:
                        print(f"║  ├── 🔒 {ach['name']:<18} - ???                        ║")
        print("║                                                           ║")

    print(f"║  TOTAL DECORATIONS: {total_unlocked} / {total_achievements:<32} ║")
    print("╚═══════════════════════════════════════════════════════════╝")

if __name__ == "__main__":
    import sys

    profile = load_profile()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "check":
            check_all_achievements(profile)
        elif command == "medals":
            display_medals(profile)
        elif command == "unlock" and len(sys.argv) > 2:
            achievement_id = sys.argv[2]
            if achievement_id in ACHIEVEMENTS:
                unlock_achievement(profile, achievement_id)
        else:
            print("Usage: achievements.py [check|medals|unlock <id>]")
    else:
        display_medals(profile)
