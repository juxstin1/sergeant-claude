---
description: Initialize a new operation with tactical command structure
argument-hint: <operation_name> [description]
allowed-tools: [Bash, Write]
---

# Initialize Operation

Sets up tactical command structure for a new mission.

## Required Argument

Operation name must be provided. If missing, respond:
"PRIVATE! Every operation needs a codename. What are we calling this mission?"

## Execution

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/init_operation.py" "." "$ARGUMENTS"
```

## Created Files

This will create:
- `state.md` - Tactical SITREP with objectives and status
- `project.md` - Strategic command with roadmap and rules of engagement

## Post-Initialization

After creating files:
1. Display operation initialization banner
2. Award XP: Run `python "${CLAUDE_PLUGIN_ROOT}/scripts/xp_tracker.py" award daily_login`
3. Display XP popup
4. Issue standing orders:
   - Run /deploy-recon to scan the codebase
   - Review project.md and update tech stack
   - Begin Phase 1: RECONNAISSANCE

## Response

```
╔═══════════════════════════════════════╗
║      🎖️  OPERATION INITIALIZED  🎖️     ║
╚═══════════════════════════════════════╝

Operation [NAME] is now active.
Command structure established.

STANDING ORDERS:
1. Run /deploy-recon to scan the AO
2. Review project.md and update tech stack
3. Begin Phase 1: RECONNAISSANCE

"The mission starts now, Private. Don't disappoint me."
```
