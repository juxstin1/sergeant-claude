# SERGEANT CLAUDE - PROGRESSION SYSTEM

## XP ECONOMY

### Combat Actions
| Action | Base XP | Notes |
|--------|---------|-------|
| file_created | 25 | New file added to codebase |
| file_edited | 15 | Meaningful edit to existing file |
| bug_fixed | 50 | Squashed a hostile |
| feature_complete | 100 | Shipped a feature |
| test_written | 40 | Added test coverage |
| test_passing | 20 | Green checkmark |
| refactor_clean | 75 | Clean refactor without breaking |
| code_review_passed | 60 | Passed review with minimal issues |
| zero_warnings | 30 | Clean build |

### Recon Actions
| Action | Base XP | Notes |
|--------|---------|-------|
| recon_complete | 35 | Ran /deploy-recon |
| court_martial_run | 25 | Analyzed a file |
| hostile_eliminated | 45 | Fixed flagged issue |

### Mission Progress
| Action | Base XP | Notes |
|--------|---------|-------|
| objective_complete | 80 | Single objective done |
| phase_complete | 250 | Entire phase done |
| mission_complete | 1000 | Full operation complete |

### Bonuses
| Action | Base XP | Notes |
|--------|---------|-------|
| daily_login | 50 | First action of day |
| streak_day | 25 | Per day of streak (auto-applied) |
| combo_bonus | 10 | Per combo level (auto-applied) |

### Special
| Action | Base XP | Notes |
|--------|---------|-------|
| first_blood | 100 | First bug of session |
| perfectionist | 150 | Zero court martial violations |
| speed_demon | 200 | Complete objective fast |

---

## MULTIPLIER SYSTEM

### Combo Multiplier
- Window: 5 minutes between actions
- Formula: `1 + (combo * 0.02)`
- Max: 2x at 50 combo
- Resets if no action for 5 minutes

**Example:**
- 1x combo: 1.00x
- 5x combo: 1.10x
- 10x combo: 1.20x
- 25x combo: 1.50x
- 50x combo: 2.00x

### Streak Multiplier
- Requirement: Code every day
- Formula: `1 + (streak_days * 0.01)`
- Max: 1.3x at 30 days
- Resets if a day is missed

**Example:**
- Day 1: 1.01x
- Day 7: 1.07x
- Day 14: 1.14x
- Day 30: 1.30x

### Boost Multiplier
- Source: Loot boxes
- Duration: 30-120 minutes
- Values: 1.5x, 2x, 3x
- Stacks multiplicatively with other bonuses

### Total XP Formula
```
Final XP = Base XP × Combo Mult × Streak Mult × Boost Mult
```

**Max Possible:**
- 50 combo (2x) × 30 streak (1.3x) × 3x boost = 7.8x multiplier

---

## RANK SYSTEM

| Level | Rank | XP Required | Title |
|-------|------|-------------|-------|
| 0 | Recruit | 0 | Fresh Meat |
| 1 | Private | 500 | Boot |
| 2 | Private First Class | 1,500 | Getting There |
| 3 | Corporal | 3,500 | Not Terrible |
| 4 | Sergeant | 7,000 | Competent |
| 5 | Staff Sergeant | 12,000 | Reliable |
| 6 | Master Sergeant | 20,000 | Seasoned |
| 7 | First Sergeant | 32,000 | Veteran |
| 8 | Sergeant Major | 50,000 | War Hero |
| 9 | Lieutenant | 75,000 | Officer Material |
| 10 | Captain | 110,000 | Leader |
| 11 | Major | 160,000 | Strategist |
| 12 | Colonel | 230,000 | Commander |
| 13 | General | 320,000 | Legendary |
| 14 | Supreme Commander | 500,000 | Mythic |

### Rank Up Rewards
- Rank up notification with animation
- Title unlocked
- Potential loot box (epic+ at Colonel)

---

## ACHIEVEMENTS

### Combat Achievements
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| 🩸 First Blood | Fix 1 bug | 100 | Common |
| 🐛 Bug Hunter | Fix 10 bugs | 250 | Common |
| ☠️ Exterminator | Fix 50 bugs | 1,000 | Rare |
| 💀 Bug Genocide | Fix 200 bugs | 5,000 | Legendary |

### Testing Achievements
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| 🧪 Test Curious | Write 1 test | 100 | Common |
| 🔬 Test Believer | Write 25 tests | 500 | Uncommon |
| ⚗️ Test Zealot | Write 100 tests | 2,000 | Epic |
| ✅ Not A Twirk | 100% coverage on file | 300 | Rare |

### Streak Achievements
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| 📅 Showing Up | 3 day streak | 150 | Common |
| 🔥 Dedicated | 7 day streak | 500 | Uncommon |
| 🔥🔥 Committed | 14 day streak | 1,500 | Rare |
| 🔥🔥🔥 Unstoppable | 30 day streak | 5,000 | Epic |
| 💎🔥 No Life | 100 day streak | 25,000 | Legendary |

### Code Quality
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| 🧼 Clean Hands | 0 violations court martial | 200 | Uncommon |
| 💎 Perfectionist | 5 clean in a row | 1,000 | Rare |
| 💪 Softhands Reformed | Refactor 500+ lines under 300 | 750 | Rare |

### Speed Achievements
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| ⚡ Speed Demon | Objective in <30 min | 300 | Uncommon |
| ⚡⚡ Blitz | 3 objectives in 1 hour | 800 | Rare |
| 🌩️ Lightning War | Phase in one session | 2,000 | Epic |

### Mission Achievements
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| 🎯 Mission Possible | Complete 1 mission | 500 | Uncommon |
| 🎖️ Veteran | Complete 5 missions | 2,500 | Rare |
| 🏆 War Hero | Complete 20 missions | 10,000 | Epic |

### Combo Achievements
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| 🎮 Combo Starter | 5x combo | 100 | Common |
| 👑 Combo King | 15x combo | 500 | Rare |
| 🌟👑 Combo GOD | 50x combo | 3,000 | Legendary |

### Secret Achievements
| Achievement | Requirement | XP | Rarity |
|-------------|-------------|----|----|
| 🦉 Night Owl | Code 2-5 AM | 200 | Uncommon |
| ⚔️ Weekend Warrior Redeemed | Ship on weekend | 400 | Uncommon |
| 🎯 TypeScript Purist | 0 'any' in 1000+ lines | 1,500 | Epic |
| 🌍 Polyglot | 3+ languages in project | 600 | Rare |

---

## LOOT BOXES

### Drop Rates
| Rarity | Chance |
|--------|--------|
| Common | 50% |
| Uncommon | 30% |
| Rare | 15% |
| Epic | 4% |
| Legendary | 1% |

### Possible Rewards

**Common Loot:**
- Small XP Pack (50 XP)
- XP Bundle (75 XP)
- Title: "Code Monkey"
- Title: "Keyboard Warrior"

**Uncommon Loot:**
- Medium XP Pack (150 XP)
- XP Chest (200 XP)
- 30min 1.5x XP Boost
- Title: "Bug Slayer"

**Rare Loot:**
- Large XP Pack (500 XP)
- 1hr 2x XP Boost
- Title: "Code Assassin"
- Title: "Silent Deployer"

**Epic Loot:**
- Epic XP Chest (1,000 XP)
- 2hr 2x XP Boost
- Title: "Architect"
- Title: "The Refactorer"

**Legendary Loot:**
- Legendary XP Hoard (2,500 XP)
- 1hr 3x XP Boost
- Title: "Legend"
- Title: "The One Who Ships"

---

## DAILY CHALLENGES (FUTURE)

Potential future additions:
- Daily quests (e.g., "Fix 3 bugs", "Write 5 tests")
- Weekly challenges
- Seasonal events
- Leaderboards
- Squad battles

---

## PRESTIGE SYSTEM (FUTURE)

At Supreme Commander (500,000 XP):
- Option to "Prestige" and reset to Recruit
- Earn Prestige Star (shown on profile)
- Permanent 5% XP bonus per prestige
- Exclusive Prestige titles
- Max Prestige: 10 (50% permanent bonus)
