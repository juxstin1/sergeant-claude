#!/usr/bin/env python3
"""
SERGEANT CLAUDE - COMBAT XP & ACHIEVEMENT SYSTEM
Maximum dopamine. Mobile game mechanics. Progress bars everywhere.
"""

import json
import os
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import random

# XP VALUES - Calibrated for dopamine
XP_VALUES = {
    # Combat Actions (Coding)
    "file_created": 25,
    "file_edited": 15,
    "bug_fixed": 50,
    "feature_complete": 100,
    "test_written": 40,
    "test_passing": 20,
    "refactor_clean": 75,
    "code_review_passed": 60,
    "zero_warnings": 30,
    
    # Recon & Analysis
    "recon_complete": 35,
    "court_martial_run": 25,
    "hostile_eliminated": 45,  # Fixed a flagged issue
    
    # Mission Progress
    "objective_complete": 80,
    "phase_complete": 250,
    "mission_complete": 1000,
    
    # Streaks & Bonuses
    "daily_login": 50,
    "streak_day": 25,  # Per day of streak
    "combo_bonus": 10,  # Per combo level
    
    # Special
    "first_blood": 100,  # First bug fix of session
    "perfectionist": 150,  # Zero issues on court martial
    "speed_demon": 200,  # Complete objective under time
}

# RANKS - Military progression with XP thresholds
RANKS = [
    {"name": "Recruit", "xp": 0, "icon": "🔰", "title": "Fresh Meat"},
    {"name": "Private", "xp": 500, "icon": "💂", "title": "Boot"},
    {"name": "Private First Class", "xp": 1500, "icon": "🎖️", "title": "Getting There"},
    {"name": "Corporal", "xp": 3500, "icon": "⭐", "title": "Not Terrible"},
    {"name": "Sergeant", "xp": 7000, "icon": "⭐⭐", "title": "Competent"},
    {"name": "Staff Sergeant", "xp": 12000, "icon": "⭐⭐⭐", "title": "Reliable"},
    {"name": "Master Sergeant", "xp": 20000, "icon": "🌟", "title": "Seasoned"},
    {"name": "First Sergeant", "xp": 32000, "icon": "🌟🌟", "title": "Veteran"},
    {"name": "Sergeant Major", "xp": 50000, "icon": "🌟🌟🌟", "title": "War Hero"},
    {"name": "Lieutenant", "xp": 75000, "icon": "🎗️", "title": "Officer Material"},
    {"name": "Captain", "xp": 110000, "icon": "🎗️🎗️", "title": "Leader"},
    {"name": "Major", "xp": 160000, "icon": "🏅", "title": "Strategist"},
    {"name": "Colonel", "xp": 230000, "icon": "🏅🏅", "title": "Commander"},
    {"name": "General", "xp": 320000, "icon": "⚔️", "title": "Legendary"},
    {"name": "Supreme Commander", "xp": 500000, "icon": "👑", "title": "Mythic"},
]

# ACHIEVEMENTS
ACHIEVEMENTS = {
    # Combat Achievements
    "first_blood": {
        "name": "First Blood",
        "desc": "Fix your first bug",
        "icon": "🩸",
        "xp_reward": 100,
        "rarity": "COMMON"
    },
    "bug_hunter": {
        "name": "Bug Hunter",
        "desc": "Fix 10 bugs",
        "icon": "🐛",
        "xp_reward": 250,
        "rarity": "COMMON",
        "threshold": 10
    },
    "exterminator": {
        "name": "Exterminator",
        "desc": "Fix 50 bugs",
        "icon": "☠️",
        "xp_reward": 1000,
        "rarity": "RARE",
        "threshold": 50
    },
    "bug_genocide": {
        "name": "Bug Genocide",
        "desc": "Fix 200 bugs",
        "icon": "💀",
        "xp_reward": 5000,
        "rarity": "LEGENDARY",
        "threshold": 200
    },
    
    # Testing Achievements
    "test_curious": {
        "name": "Test Curious",
        "desc": "Write your first test",
        "icon": "🧪",
        "xp_reward": 100,
        "rarity": "COMMON"
    },
    "test_believer": {
        "name": "Test Believer",
        "desc": "Write 25 tests",
        "icon": "🔬",
        "xp_reward": 500,
        "rarity": "UNCOMMON",
        "threshold": 25
    },
    "test_zealot": {
        "name": "Test Zealot",
        "desc": "Write 100 tests",
        "icon": "⚗️",
        "xp_reward": 2000,
        "rarity": "EPIC",
        "threshold": 100
    },
    "not_a_twirk": {
        "name": "Not A Twirk",
        "desc": "100% test coverage on a file",
        "icon": "✅",
        "xp_reward": 300,
        "rarity": "RARE"
    },
    
    # Streak Achievements
    "showing_up": {
        "name": "Showing Up",
        "desc": "3 day coding streak",
        "icon": "📅",
        "xp_reward": 150,
        "rarity": "COMMON",
        "threshold": 3
    },
    "dedicated": {
        "name": "Dedicated",
        "desc": "7 day coding streak",
        "icon": "🔥",
        "xp_reward": 500,
        "rarity": "UNCOMMON",
        "threshold": 7
    },
    "committed": {
        "name": "Committed",
        "desc": "14 day coding streak",
        "icon": "🔥🔥",
        "xp_reward": 1500,
        "rarity": "RARE",
        "threshold": 14
    },
    "unstoppable": {
        "name": "Unstoppable",
        "desc": "30 day coding streak",
        "icon": "🔥🔥🔥",
        "xp_reward": 5000,
        "rarity": "EPIC",
        "threshold": 30
    },
    "no_life": {
        "name": "No Life",
        "desc": "100 day coding streak",
        "icon": "💎🔥",
        "xp_reward": 25000,
        "rarity": "LEGENDARY",
        "threshold": 100
    },
    
    # Code Quality
    "clean_hands": {
        "name": "Clean Hands",
        "desc": "Pass court martial with 0 violations",
        "icon": "🧼",
        "xp_reward": 200,
        "rarity": "UNCOMMON"
    },
    "perfectionist": {
        "name": "Perfectionist",
        "desc": "5 clean court martials in a row",
        "icon": "💎",
        "xp_reward": 1000,
        "rarity": "RARE",
        "threshold": 5
    },
    "softhands_reformed": {
        "name": "Softhands Reformed",
        "desc": "Refactor a 500+ line file under 300",
        "icon": "💪",
        "xp_reward": 750,
        "rarity": "RARE"
    },
    
    # Speed Achievements
    "speed_demon": {
        "name": "Speed Demon",
        "desc": "Complete objective in under 30 min",
        "icon": "⚡",
        "xp_reward": 300,
        "rarity": "UNCOMMON"
    },
    "blitz": {
        "name": "Blitz",
        "desc": "Complete 3 objectives in 1 hour",
        "icon": "⚡⚡",
        "xp_reward": 800,
        "rarity": "RARE"
    },
    "lightning_war": {
        "name": "Lightning War",
        "desc": "Complete entire phase in one session",
        "icon": "🌩️",
        "xp_reward": 2000,
        "rarity": "EPIC"
    },
    
    # Mission Achievements
    "mission_possible": {
        "name": "Mission Possible",
        "desc": "Complete your first mission",
        "icon": "🎯",
        "xp_reward": 500,
        "rarity": "UNCOMMON"
    },
    "veteran": {
        "name": "Veteran",
        "desc": "Complete 5 missions",
        "icon": "🎖️",
        "xp_reward": 2500,
        "rarity": "RARE",
        "threshold": 5
    },
    "war_hero": {
        "name": "War Hero",
        "desc": "Complete 20 missions",
        "icon": "🏆",
        "xp_reward": 10000,
        "rarity": "EPIC",
        "threshold": 20
    },
    
    # Combo Achievements
    "combo_starter": {
        "name": "Combo Starter",
        "desc": "Reach 5x combo",
        "icon": "🎮",
        "xp_reward": 100,
        "rarity": "COMMON",
        "threshold": 5
    },
    "combo_king": {
        "name": "Combo King",
        "desc": "Reach 15x combo",
        "icon": "👑",
        "xp_reward": 500,
        "rarity": "RARE",
        "threshold": 15
    },
    "combo_god": {
        "name": "Combo GOD",
        "desc": "Reach 50x combo",
        "icon": "🌟👑",
        "xp_reward": 3000,
        "rarity": "LEGENDARY",
        "threshold": 50
    },
    
    # Special / Secret
    "night_owl": {
        "name": "Night Owl",
        "desc": "Code between 2-5 AM",
        "icon": "🦉",
        "xp_reward": 200,
        "rarity": "UNCOMMON"
    },
    "weekend_warrior": {
        "name": "Weekend Warrior Redeemed",
        "desc": "Ship feature on weekend",
        "icon": "⚔️",
        "xp_reward": 400,
        "rarity": "UNCOMMON"
    },
    "typescript_purist": {
        "name": "TypeScript Purist",
        "desc": "0 'any' types in 1000+ line project",
        "icon": "🎯",
        "xp_reward": 1500,
        "rarity": "EPIC"
    },
    "polyglot": {
        "name": "Polyglot",
        "desc": "Use 3+ languages in one project",
        "icon": "🌍",
        "xp_reward": 600,
        "rarity": "RARE"
    },
}

# RARITY COLORS
RARITY_COLORS = {
    "COMMON": "⬜",
    "UNCOMMON": "🟩",
    "RARE": "🟦",
    "EPIC": "🟪",
    "LEGENDARY": "🟨",
}

# LOOT TABLE - Random rewards
LOOT_TABLE = {
    "common": [
        {"type": "xp", "amount": 50, "name": "Small XP Pack"},
        {"type": "xp", "amount": 75, "name": "XP Bundle"},
        {"type": "title", "name": "Code Monkey"},
        {"type": "title", "name": "Keyboard Warrior"},
    ],
    "uncommon": [
        {"type": "xp", "amount": 150, "name": "Medium XP Pack"},
        {"type": "xp", "amount": 200, "name": "XP Chest"},
        {"type": "multiplier", "amount": 1.5, "duration": 30, "name": "30min 1.5x XP Boost"},
        {"type": "title", "name": "Bug Slayer"},
    ],
    "rare": [
        {"type": "xp", "amount": 500, "name": "Large XP Pack"},
        {"type": "multiplier", "amount": 2.0, "duration": 60, "name": "1hr 2x XP Boost"},
        {"type": "title", "name": "Code Assassin"},
        {"type": "title", "name": "Silent Deployer"},
    ],
    "epic": [
        {"type": "xp", "amount": 1000, "name": "Epic XP Chest"},
        {"type": "multiplier", "amount": 2.0, "duration": 120, "name": "2hr 2x XP Boost"},
        {"type": "title", "name": "Architect"},
        {"type": "title", "name": "The Refactorer"},
    ],
    "legendary": [
        {"type": "xp", "amount": 2500, "name": "Legendary XP Hoard"},
        {"type": "multiplier", "amount": 3.0, "duration": 60, "name": "1hr 3x XP Boost"},
        {"type": "title", "name": "Legend"},
        {"type": "title", "name": "The One Who Ships"},
    ],
}


class XPTracker:
    def __init__(self, save_path: str = None):
        if save_path is None:
            # Use global profile in ~/.sergeant/
            sergeant_dir = Path.home() / ".sergeant"
            sergeant_dir.mkdir(parents=True, exist_ok=True)
            self.save_path = sergeant_dir / "profile.json"
        else:
            self.save_path = Path(save_path)
        self.data = self._load()
    
    def _load(self) -> dict:
        """Load profile or create new one."""
        default = {
            "xp": 0,
            "lifetime_xp": 0,
            "rank_index": 0,
            "achievements": [],
            "titles": ["Recruit"],
            "active_title": "Recruit",
            "stats": {
                "bugs_fixed": 0,
                "tests_written": 0,
                "files_created": 0,
                "objectives_completed": 0,
                "missions_completed": 0,
                "clean_court_martials": 0,
                "clean_court_martial_streak": 0,
            },
            "streak": {
                "current": 0,
                "longest": 0,
                "last_active": None,
            },
            "combo": {
                "current": 0,
                "highest": 0,
                "last_action": None,
            },
            "multiplier": {
                "value": 1.0,
                "expires": None,
            },
            "daily": {
                "xp_earned": 0,
                "actions": 0,
                "date": None,
            },
            "inventory": [],
            "created": datetime.now().isoformat(),
            "last_session": None,
        }
        
        if self.save_path.exists():
            try:
                with open(self.save_path, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    # Merge with defaults for new fields
                    for key in default:
                        if key not in loaded:
                            loaded[key] = default[key]
                    return loaded
            except:
                pass
        return default
    
    def _save(self):
        """Save profile."""
        with open(self.save_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, default=str)
    
    def _check_streak(self):
        """Update streak based on last active date."""
        today = datetime.now().date().isoformat()
        last = self.data["streak"]["last_active"]
        
        if last is None:
            self.data["streak"]["current"] = 1
        elif last == today:
            pass  # Same day, no change
        elif last == (datetime.now().date() - timedelta(days=1)).isoformat():
            self.data["streak"]["current"] += 1
        else:
            self.data["streak"]["current"] = 1  # Streak broken
        
        self.data["streak"]["last_active"] = today
        self.data["streak"]["longest"] = max(
            self.data["streak"]["longest"],
            self.data["streak"]["current"]
        )
    
    def _update_combo(self, action_time: datetime = None):
        """Update combo system."""
        if action_time is None:
            action_time = datetime.now()
        
        last = self.data["combo"]["last_action"]
        if last:
            last_time = datetime.fromisoformat(last)
            delta = (action_time - last_time).total_seconds()
            
            # Combo window: 5 minutes
            if delta < 300:
                self.data["combo"]["current"] += 1
            else:
                self.data["combo"]["current"] = 1
        else:
            self.data["combo"]["current"] = 1
        
        self.data["combo"]["last_action"] = action_time.isoformat()
        self.data["combo"]["highest"] = max(
            self.data["combo"]["highest"],
            self.data["combo"]["current"]
        )
    
    def _get_multiplier(self) -> float:
        """Get current XP multiplier."""
        mult = self.data["multiplier"]
        if mult["expires"]:
            if datetime.now() < datetime.fromisoformat(mult["expires"]):
                return mult["value"]
            else:
                mult["value"] = 1.0
                mult["expires"] = None
        return 1.0
    
    def _calculate_xp(self, base_xp: int) -> int:
        """Calculate XP with all bonuses."""
        combo = self.data["combo"]["current"]
        combo_mult = 1 + (min(combo, 50) * 0.02)  # Max 2x from combo
        
        streak = self.data["streak"]["current"]
        streak_mult = 1 + (min(streak, 30) * 0.01)  # Max 1.3x from streak
        
        boost_mult = self._get_multiplier()
        
        total_mult = combo_mult * streak_mult * boost_mult
        return int(base_xp * total_mult)
    
    def award_xp(self, action: str, custom_amount: int = None) -> dict:
        """Award XP for an action."""
        self._check_streak()
        self._update_combo()
        
        base_xp = custom_amount if custom_amount else XP_VALUES.get(action, 10)
        final_xp = self._calculate_xp(base_xp)
        
        self.data["xp"] += final_xp
        self.data["lifetime_xp"] += final_xp
        
        # Update daily
        today = datetime.now().date().isoformat()
        if self.data["daily"]["date"] != today:
            self.data["daily"] = {"xp_earned": 0, "actions": 0, "date": today}
        self.data["daily"]["xp_earned"] += final_xp
        self.data["daily"]["actions"] += 1
        
        # Check rank up
        rank_up = self._check_rank_up()
        
        # Check achievements
        new_achievements = self._check_achievements(action)
        
        self._save()
        
        return {
            "xp_earned": final_xp,
            "base_xp": base_xp,
            "combo": self.data["combo"]["current"],
            "streak": self.data["streak"]["current"],
            "multiplier": self._get_multiplier(),
            "total_xp": self.data["xp"],
            "rank_up": rank_up,
            "new_achievements": new_achievements,
        }
    
    def _check_rank_up(self) -> Optional[dict]:
        """Check if user ranked up."""
        current_rank = self.data["rank_index"]
        xp = self.data["xp"]
        
        for i, rank in enumerate(RANKS):
            if xp >= rank["xp"]:
                continue
            else:
                new_rank = i - 1
                break
        else:
            new_rank = len(RANKS) - 1
        
        if new_rank > current_rank:
            self.data["rank_index"] = new_rank
            return RANKS[new_rank]
        return None
    
    def _check_achievements(self, action: str) -> List[dict]:
        """Check for new achievements."""
        new = []
        earned = self.data["achievements"]
        stats = self.data["stats"]
        
        # Update stats based on action
        stat_map = {
            "bug_fixed": "bugs_fixed",
            "test_written": "tests_written",
            "file_created": "files_created",
            "objective_complete": "objectives_completed",
            "mission_complete": "missions_completed",
        }
        if action in stat_map:
            stats[stat_map[action]] = stats.get(stat_map[action], 0) + 1
        
        # Check each achievement
        checks = [
            ("first_blood", stats.get("bugs_fixed", 0) >= 1),
            ("bug_hunter", stats.get("bugs_fixed", 0) >= 10),
            ("exterminator", stats.get("bugs_fixed", 0) >= 50),
            ("bug_genocide", stats.get("bugs_fixed", 0) >= 200),
            ("test_curious", stats.get("tests_written", 0) >= 1),
            ("test_believer", stats.get("tests_written", 0) >= 25),
            ("test_zealot", stats.get("tests_written", 0) >= 100),
            ("showing_up", self.data["streak"]["current"] >= 3),
            ("dedicated", self.data["streak"]["current"] >= 7),
            ("committed", self.data["streak"]["current"] >= 14),
            ("unstoppable", self.data["streak"]["current"] >= 30),
            ("no_life", self.data["streak"]["current"] >= 100),
            ("combo_starter", self.data["combo"]["highest"] >= 5),
            ("combo_king", self.data["combo"]["highest"] >= 15),
            ("combo_god", self.data["combo"]["highest"] >= 50),
            ("mission_possible", stats.get("missions_completed", 0) >= 1),
            ("veteran", stats.get("missions_completed", 0) >= 5),
            ("war_hero", stats.get("missions_completed", 0) >= 20),
        ]
        
        # Night owl check
        hour = datetime.now().hour
        if 2 <= hour <= 5 and "night_owl" not in earned:
            checks.append(("night_owl", True))
        
        for ach_id, condition in checks:
            if condition and ach_id not in earned:
                earned.append(ach_id)
                ach = ACHIEVEMENTS[ach_id]
                self.data["xp"] += ach["xp_reward"]
                self.data["lifetime_xp"] += ach["xp_reward"]
                new.append(ach)
        
        return new
    
    def get_rank(self) -> dict:
        """Get current rank info."""
        rank = RANKS[self.data["rank_index"]]
        next_rank = RANKS[self.data["rank_index"] + 1] if self.data["rank_index"] < len(RANKS) - 1 else None
        
        if next_rank:
            progress = (self.data["xp"] - rank["xp"]) / (next_rank["xp"] - rank["xp"])
        else:
            progress = 1.0
        
        return {
            "current": rank,
            "next": next_rank,
            "progress": progress,
            "xp": self.data["xp"],
        }
    
    def open_loot_box(self, rarity: str = None) -> dict:
        """Open a loot box!"""
        if rarity is None:
            # Random rarity weighted
            roll = random.random()
            if roll < 0.5:
                rarity = "common"
            elif roll < 0.8:
                rarity = "uncommon"
            elif roll < 0.95:
                rarity = "rare"
            elif roll < 0.99:
                rarity = "epic"
            else:
                rarity = "legendary"
        
        loot = random.choice(LOOT_TABLE[rarity])
        
        if loot["type"] == "xp":
            self.data["xp"] += loot["amount"]
            self.data["lifetime_xp"] += loot["amount"]
        elif loot["type"] == "multiplier":
            self.data["multiplier"]["value"] = loot["amount"]
            self.data["multiplier"]["expires"] = (
                datetime.now() + timedelta(minutes=loot["duration"])
            ).isoformat()
        elif loot["type"] == "title":
            if loot["name"] not in self.data["titles"]:
                self.data["titles"].append(loot["name"])
        
        self._save()
        return {"rarity": rarity, "loot": loot}
    
    def get_profile_display(self) -> str:
        """Generate full profile display."""
        rank_info = self.get_rank()
        rank = rank_info["current"]
        next_rank = rank_info["next"]
        progress = rank_info["progress"]
        
        lines = []
        lines.append("╔════════════════════════════════════════════════════════════╗")
        lines.append("║            🎖️  SOLDIER PROFILE  🎖️                          ║")
        lines.append("╠════════════════════════════════════════════════════════════╣")
        
        # Rank & Title
        lines.append(f"║  {rank['icon']} RANK: {rank['name']:<20} [{rank['title']}]")
        lines.append(f"║  🏷️  TITLE: {self.data['active_title']}")
        lines.append("║")
        
        # XP Bar
        xp = self.data["xp"]
        lines.append(f"║  ⚡ XP: {xp:,}")
        if next_rank:
            bar_width = 30
            filled = int(progress * bar_width)
            bar = "█" * filled + "░" * (bar_width - filled)
            lines.append(f"║  [{bar}] {progress*100:.1f}%")
            lines.append(f"║  → Next: {next_rank['name']} ({next_rank['xp'] - xp:,} XP needed)")
        else:
            lines.append(f"║  [██████████████████████████████] MAX RANK")
        lines.append("║")
        
        # Stats row
        stats = self.data["stats"]
        lines.append(f"║  📊 COMBAT STATS")
        lines.append(f"║  🐛 Bugs Fixed: {stats.get('bugs_fixed', 0):,}")
        lines.append(f"║  🧪 Tests Written: {stats.get('tests_written', 0):,}")
        lines.append(f"║  🎯 Objectives: {stats.get('objectives_completed', 0):,}")
        lines.append(f"║  🏆 Missions: {stats.get('missions_completed', 0):,}")
        lines.append("║")
        
        # Streak & Combo
        streak = self.data["streak"]["current"]
        combo = self.data["combo"]["current"]
        lines.append(f"║  🔥 STREAK: {streak} days (Best: {self.data['streak']['longest']})")
        lines.append(f"║  💥 COMBO: {combo}x (Best: {self.data['combo']['highest']}x)")
        
        mult = self._get_multiplier()
        if mult > 1.0:
            lines.append(f"║  ⚡ BOOST ACTIVE: {mult}x XP")
        lines.append("║")
        
        # Achievements
        earned = len(self.data["achievements"])
        total = len(ACHIEVEMENTS)
        ach_progress = earned / total
        ach_bar = "█" * int(ach_progress * 20) + "░" * (20 - int(ach_progress * 20))
        lines.append(f"║  🏅 ACHIEVEMENTS: {earned}/{total}")
        lines.append(f"║  [{ach_bar}] {ach_progress*100:.1f}%")
        lines.append("║")
        
        # Recent achievements (last 3)
        if self.data["achievements"]:
            lines.append(f"║  📜 RECENT:")
            for ach_id in self.data["achievements"][-3:]:
                ach = ACHIEVEMENTS[ach_id]
                rarity = RARITY_COLORS[ach["rarity"]]
                lines.append(f"║     {rarity} {ach['icon']} {ach['name']}")
        
        lines.append("║")
        lines.append("╚════════════════════════════════════════════════════════════╝")
        
        return "\n".join(lines)
    
    def get_xp_popup(self, result: dict) -> str:
        """Generate XP gain popup."""
        lines = []
        
        # Main XP gain
        lines.append("┌─────────────────────────────────┐")
        lines.append(f"│     ⚡ +{result['xp_earned']} XP ⚡              │")
        
        # Bonuses breakdown
        if result["combo"] > 1:
            lines.append(f"│     💥 {result['combo']}x COMBO              │")
        if result["streak"] > 1:
            lines.append(f"│     🔥 {result['streak']} DAY STREAK          │")
        if result["multiplier"] > 1:
            lines.append(f"│     ⚡ {result['multiplier']}x BOOST           │")
        
        lines.append("└─────────────────────────────────┘")
        
        # Rank up?
        if result["rank_up"]:
            rank = result["rank_up"]
            lines.append("")
            lines.append("╔═══════════════════════════════════╗")
            lines.append("║       🎖️  RANK UP!  🎖️             ║")
            lines.append(f"║   {rank['icon']} {rank['name']:<24}    ║")
            lines.append(f"║   \"{rank['title']}\"                  ║")
            lines.append("╚═══════════════════════════════════╝")
        
        # Achievements?
        for ach in result.get("new_achievements", []):
            rarity = RARITY_COLORS[ach["rarity"]]
            lines.append("")
            lines.append("┌───────────────────────────────────┐")
            lines.append(f"│  {rarity} ACHIEVEMENT UNLOCKED! {rarity}     │")
            lines.append(f"│  {ach['icon']} {ach['name']:<24}     │")
            lines.append(f"│  +{ach['xp_reward']} XP                        │")
            lines.append("└───────────────────────────────────┘")
        
        return "\n".join(lines)
    
    def get_daily_summary(self) -> str:
        """Generate daily progress summary."""
        daily = self.data["daily"]
        today = datetime.now().date().isoformat()
        
        if daily["date"] != today:
            return "No activity today yet. Get to work, soldier!"
        
        lines = []
        lines.append("╔═══════════════════════════════════╗")
        lines.append("║      📅 TODAY'S COMBAT LOG 📅      ║")
        lines.append("╠═══════════════════════════════════╣")
        lines.append(f"║  ⚡ XP Earned: {daily['xp_earned']:,}")
        lines.append(f"║  🎯 Actions: {daily['actions']}")
        lines.append(f"║  🔥 Streak: Day {self.data['streak']['current']}")
        lines.append(f"║  💥 Best Combo: {self.data['combo']['highest']}x")
        lines.append("╚═══════════════════════════════════╝")
        
        return "\n".join(lines)


def main():
    """CLI interface for XP tracker."""
    import sys
    
    tracker = XPTracker()
    
    if len(sys.argv) < 2:
        print(tracker.get_profile_display())
        return
    
    cmd = sys.argv[1]
    
    if cmd == "profile":
        print(tracker.get_profile_display())
    
    elif cmd == "award":
        if len(sys.argv) < 3:
            print("Usage: xp_tracker.py award <action>")
            print(f"Actions: {', '.join(XP_VALUES.keys())}")
            return
        action = sys.argv[2]
        result = tracker.award_xp(action)
        print(tracker.get_xp_popup(result))
    
    elif cmd == "loot":
        rarity = sys.argv[2] if len(sys.argv) > 2 else None
        result = tracker.open_loot_box(rarity)
        print(f"\n🎁 LOOT BOX OPENED! [{result['rarity'].upper()}]")
        print(f"   → {result['loot']['name']}")
        if result['loot']['type'] == 'xp':
            print(f"   → +{result['loot']['amount']} XP!")
        elif result['loot']['type'] == 'multiplier':
            print(f"   → {result['loot']['amount']}x XP for {result['loot']['duration']} minutes!")
        elif result['loot']['type'] == 'title':
            print(f"   → New title unlocked!")
    
    elif cmd == "daily":
        print(tracker.get_daily_summary())
    
    elif cmd == "achievements":
        print("\n🏅 ALL ACHIEVEMENTS\n")
        for ach_id, ach in ACHIEVEMENTS.items():
            earned = "✅" if ach_id in tracker.data["achievements"] else "⬜"
            rarity = RARITY_COLORS[ach["rarity"]]
            print(f"{earned} {rarity} {ach['icon']} {ach['name']}")
            print(f"      {ach['desc']} (+{ach['xp_reward']} XP)")
    
    else:
        print(f"Unknown command: {cmd}")
        print("Commands: profile, award, loot, daily, achievements")


if __name__ == "__main__":
    main()
