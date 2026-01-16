---
description: Deploy recon agent to scan codebase for hostiles, code smells, and tactical assessment
argument-hint: [directory]
allowed-tools: [Bash, Read, Glob, Grep]
---

# Deploy Recon - Tactical Codebase Scanner

Execute helicopter drop sequence and scan the AO (Area of Operations).

## Dramatic Entry Sequence

Display this dramatic entry:

```
🚁 BLACKHAWK INBOUND...
🪂 AGENT REPELLING...
👢 BOOTS ON GROUND
🔍 SCANNING PERIMETER...
```

## Execution

Run the recon script on the target directory (default: current directory):

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/recon.py" "$ARGUMENTS"
```

If no argument provided, use current working directory.

## Post-Recon

After scanning:
1. Display the tactical SITREP
2. Award XP: Run `python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" award recon_complete`
3. Display XP popup
4. Provide tactical recommendations based on threat level

## Threat Level Responses

- **CRITICAL**: "SITUATION IS DIRE. IMMEDIATE ACTION REQUIRED. Deploy /run-delta."
- **HIGH**: "HEAVY RESISTANCE EXPECTED. Systematic /court-martial recommended."
- **MEDIUM**: "Moderate cleanup required. Proceed with standard operations."
- **LOW**: "AO is relatively secure. Good work, soldier."
