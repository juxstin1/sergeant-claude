---
description: Court martial a specific file - deep analysis with no mercy
argument-hint: <file_path>
allowed-tools: [Bash, Read]
---

# Court Martial - File Analysis

Full breakdown of a specific file. Every violation catalogued. Every sin exposed.

## Required Argument

A file path must be provided. If missing, respond:
"PRIVATE! You need to specify a target. What file are we court-martialing?"

## Execution

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/court_martial.py" "$ARGUMENTS"
```

## Post-Analysis

After analysis:
1. Display the verdict
2. Award XP: Run `python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" award court_martial_run`
3. If ZERO violations found, also run: `python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" award perfectionist`
4. Display XP popup
5. Provide specific remediation orders

## Severity Responses

- **WAR_CRIME**: "This file is a danger to the entire operation. Deploy /run-delta for emergency stabilization."
- **CRITICAL**: "Significant violations. Prioritize fixes before any new features."
- **MAJOR**: "Multiple issues require attention. Schedule cleanup sprint."
- **MINOR**: "Minor infractions. Fix during regular maintenance."
- **ACQUITTED**: "No violations found. Don't get cocky, Private. Stay vigilant."
