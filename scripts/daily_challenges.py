#!/usr/bin/env python3
"""
Daily Challenge System for Sergeant Claude
Rotating challenges with bonus XP rewards
"""

import json
import random
from datetime import datetime, date
from pathlib import Path

# Challenge pool organized by difficulty
CHALLENGES = {
    "easy": [
        {
            "id": "bug_hunter",
            "name": "Bug Hunter",
            "description": "Fix 2 bugs today",
            "requirement": {"bugs_fixed": 2},
            "xp_reward": 75
        },
        {
            "id": "test_soldier",
            "name": "Test Soldier",
            "description": "Write 3 tests",
            "requirement": {"tests_written": 3},
            "xp_reward": 60
        },
        {
            "id": "scout_duty",
            "name": "Scout Duty",
            "description": "Run 2 recon scans",
            "requirement": {"recons": 2},
            "xp_reward": 50
        },
        {
            "id": "clean_sweep",
            "name": "Clean Sweep",
            "description": "Complete 1 court martial",
            "requirement": {"court_martials": 1},
            "xp_reward": 65
        }
    ],
    "medium": [
        {
            "id": "exterminator",
            "name": "Exterminator",
            "description": "Fix 5 bugs today",
            "requirement": {"bugs_fixed": 5},
            "xp_reward": 150
        },
        {
            "id": "feature_warrior",
            "name": "Feature Warrior",
            "description": "Complete 2 features",
            "requirement": {"features_complete": 2},
            "xp_reward": 200
        },
        {
            "id": "fortress_duty",
            "name": "Fortress Duty",
            "description": "Run 3 fortifications",
            "requirement": {"fortifications": 3},
            "xp_reward": 175
        },
        {
            "id": "ambush_master",
            "name": "Ambush Master",
            "description": "Complete 4 ambush strikes",
            "requirement": {"ambushes": 4},
            "xp_reward": 160
        }
    ],
    "hard": [
        {
            "id": "bug_genocide",
            "name": "Bug Genocide",
            "description": "Fix 10 bugs today",
            "requirement": {"bugs_fixed": 10},
            "xp_reward": 350
        },
        {
            "id": "perfect_day",
            "name": "Perfect Day",
            "description": "Complete 3 features with tests",
            "requirement": {"features_complete": 3, "tests_written": 6},
            "xp_reward": 500
        },
        {
            "id": "full_assault",
            "name": "Full Assault",
            "description": "Run recon, 5 court martials, and 3 fortifications",
            "requirement": {"recons": 1, "court_martials": 5, "fortifications": 3},
            "xp_reward": 400
        }
    ]
}

def get_challenges_path():
    """Get the challenges state file path"""
    return Path.home() / ".sergeant_challenges.json"

def get_profile_path():
    """Get the profile file path"""
    return Path.home() / ".sergeant_profile.json"

def load_challenges_state():
    """Load current challenge state"""
    path = get_challenges_path()
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_challenges_state(state):
    """Save challenge state"""
    with open(get_challenges_path(), 'w') as f:
        json.dump(state, f, indent=2)

def load_profile():
    """Load user profile"""
    path = get_profile_path()
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_profile(profile):
    """Save user profile"""
    with open(get_profile_path(), 'w') as f:
        json.dump(profile, f, indent=2)

def get_daily_seed():
    """Get a seed based on today's date for consistent daily selection"""
    today = date.today()
    return int(today.strftime("%Y%m%d"))

def select_daily_challenges():
    """Select today's challenges (1 easy, 1 medium, 1 hard)"""
    seed = get_daily_seed()
    random.seed(seed)

    daily = {
        "date": str(date.today()),
        "challenges": [
            random.choice(CHALLENGES["easy"]),
            random.choice(CHALLENGES["medium"]),
            random.choice(CHALLENGES["hard"])
        ],
        "progress": {},
        "completed": []
    }

    return daily

def get_todays_challenges():
    """Get or generate today's challenges"""
    state = load_challenges_state()
    today = str(date.today())

    if state.get("date") != today:
        # New day, new challenges
        state = select_daily_challenges()
        save_challenges_state(state)

    return state

def update_progress(action, count=1):
    """Update progress towards daily challenges"""
    state = get_todays_challenges()
    profile = load_profile()

    # Update daily progress
    if "daily_progress" not in state:
        state["daily_progress"] = {}

    current = state["daily_progress"].get(action, 0)
    state["daily_progress"][action] = current + count

    # Check for completions
    newly_completed = []
    for challenge in state["challenges"]:
        if challenge["id"] in state.get("completed", []):
            continue

        completed = True
        for req_key, req_val in challenge["requirement"].items():
            progress = state["daily_progress"].get(req_key, 0)
            if progress < req_val:
                completed = False
                break

        if completed:
            state["completed"].append(challenge["id"])
            newly_completed.append(challenge)

            # Award XP
            profile["xp"] = profile.get("xp", 0) + challenge["xp_reward"]

    save_challenges_state(state)
    save_profile(profile)

    return newly_completed

def display_daily_challenges():
    """Display today's challenges with progress"""
    state = get_todays_challenges()
    challenges = state["challenges"]
    progress = state.get("daily_progress", {})
    completed = state.get("completed", [])

    print("╔═══════════════════════════════════════════════════════════╗")
    print("║              📋 DAILY COMBAT ORDERS 📋                    ║")
    print(f"║              {date.today().strftime('%B %d, %Y'):^40}   ║")
    print("╠═══════════════════════════════════════════════════════════╣")

    difficulty_icons = {"easy": "🟢", "medium": "🟡", "hard": "🔴"}

    for i, challenge in enumerate(challenges, 1):
        diff = "easy" if i == 1 else ("medium" if i == 2 else "hard")
        icon = difficulty_icons[diff]
        status = "✅" if challenge["id"] in completed else "⬜"

        print(f"║  {status} {icon} {challenge['name']:<25} +{challenge['xp_reward']} XP     ║")
        print(f"║      {challenge['description']:<49} ║")

        # Show progress
        req = challenge["requirement"]
        progress_parts = []
        for key, target in req.items():
            current = progress.get(key, 0)
            progress_parts.append(f"{key}: {current}/{target}")

        progress_str = " | ".join(progress_parts)
        print(f"║      Progress: {progress_str:<40} ║")
        print("║                                                           ║")

    completed_count = len(completed)
    total = len(challenges)
    print(f"║  MISSIONS COMPLETE: {completed_count}/{total}                              ║")

    if completed_count == total:
        print("║                                                           ║")
        print("║  🏆 ALL DAILY CHALLENGES COMPLETE! OUTSTANDING! 🏆        ║")

    print("╚═══════════════════════════════════════════════════════════╝")

def display_completion(challenge):
    """Display challenge completion notification"""
    print(f"""
╔═══════════════════════════════════════════════════════════╗
║            ⭐ DAILY CHALLENGE COMPLETE! ⭐                 ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║   {challenge['name']:^50}  ║
║   "{challenge['description']}"
║                                                           ║
║   +{challenge['xp_reward']} XP EARNED                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "show":
            display_daily_challenges()
        elif command == "progress":
            if len(sys.argv) > 2:
                action = sys.argv[2]
                count = int(sys.argv[3]) if len(sys.argv) > 3 else 1
                completed = update_progress(action, count)
                for c in completed:
                    display_completion(c)
        else:
            print("Usage: daily_challenges.py [show|progress <action> [count]]")
    else:
        display_daily_challenges()
