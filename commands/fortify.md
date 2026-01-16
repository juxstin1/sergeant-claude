---
description: Harden code defenses - add error handling, validation, types, and defensive patterns
allowed-tools: [Read, Edit, Glob, Grep]
---

# Fortify - Defensive Hardening

Reinforce your code's defenses. Add armor where it's vulnerable.

## Entry Sequence

```
🏰 FORTIFICATION MODE ENGAGED
🛡️ SCANNING FOR WEAK POINTS
🔒 HARDENING DEFENSES...
```

## Target Selection

If $ARGUMENTS provided: Fortify that specific file/function
If no argument: Scan current directory for most vulnerable targets

## Fortification Checklist

1. **Input Validation** - Trust no one
2. **Error Handling** - Catch everything, handle gracefully
3. **Type Safety** - Eliminate any types like hostiles
4. **Null Checks** - Undefined is the enemy
5. **Edge Cases** - Cover the flanks
6. **Sanitization** - Clean all inputs

## Execution

1. Identify fortification target
2. Scan for vulnerabilities:
   - Missing try/catch blocks
   - Unvalidated inputs
   - Type: any declarations
   - Missing null checks
   - Exposed error messages
3. Apply defensive patterns
4. Report fortifications made

## Post-Fortify Report

```
╔═══════════════════════════════════════╗
║       🏰 FORTIFICATION COMPLETE 🏰     ║
╠═══════════════════════════════════════╣
║  WALLS BUILT: [count]                 ║
║  VULNERABILITIES PATCHED: [count]     ║
║  DEFENSE RATING: [A-F]                ║
╚═══════════════════════════════════════╝
```

Award XP: Run `python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" award fortify_complete`

## Defense Rating Scale

- **A**: Fort Knox. Nothing's getting through.
- **B**: Solid defenses. Minor gaps.
- **C**: Acceptable. Needs work.
- **D**: Vulnerable. Prioritize fixes.
- **F**: Wide open. CRITICAL.
