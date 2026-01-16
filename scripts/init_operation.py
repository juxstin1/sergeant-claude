#!/usr/bin/env python3
"""
SERGEANT CLAUDE - OPERATION INITIALIZATION
Sets up tactical command structure for new mission.
"""

import sys
from pathlib import Path
from datetime import datetime

STATE_TEMPLATE = """# SITREP - {date}

## CURRENT RANK: Private

## MISSION STATUS: 🟢 ACTIVE

## ACTIVE OBJECTIVES
- [ ] Objective Alpha: Initial reconnaissance complete
- [ ] Objective Bravo: Architecture review
- [ ] Objective Charlie: First implementation phase

## HOSTILES (Blockers)
- None identified yet. Stay frosty.

## RECENT VICTORIES
- Operation initialized
- Command structure established

## NEXT ACTION
Run /deploy-recon to scan the AO and identify targets.

---
*Last updated: {date}*
*Commanding Officer: Sergeant Claude, ASF*
"""

PROJECT_TEMPLATE = """# OPERATION: {name}

## MISSION BRIEF
{description}

## TECH STACK MANIFEST
| Layer | Technology | Status |
|-------|------------|--------|
| Frontend | TBD | ⏳ |
| Backend | TBD | ⏳ |
| Database | TBD | ⏳ |
| Infrastructure | TBD | ⏳ |

## ROADMAP

### Phase 1: RECONNAISSANCE (Codename: EAGLE EYE)
- [ ] Codebase analysis complete
- [ ] Architecture documented
- [ ] Tech debt identified
- [ ] Test coverage assessed

### Phase 2: FORTIFICATION (Codename: IRON WALL)
- [ ] Critical bugs eliminated
- [ ] Test coverage improved
- [ ] Documentation updated
- [ ] CI/CD established

### Phase 3: ADVANCEMENT (Codename: FORWARD MARCH)
- [ ] Core features implemented
- [ ] Integration tests passing
- [ ] Performance benchmarks met
- [ ] Security audit complete

### Phase 4: EXTRACTION (Codename: HOMECOMING)
- [ ] Production deployment ready
- [ ] Monitoring configured
- [ ] Rollback procedures documented
- [ ] Mission complete

## ARCHITECTURE DECISIONS LOG

| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| {date} | Operation initialized | New mission commenced | ✅ |

## RULES OF ENGAGEMENT

### Code Standards
- TypeScript strict mode: MANDATORY
- No `any` types without documented justification
- All functions under 50 lines
- All files under 300 lines

### Commit Protocol
- Conventional commits required
- No commits without tests (don't be a twirk)
- Squash before merge

### Testing Doctrine
- Unit tests: Required for all business logic
- Integration tests: Required for all API endpoints
- E2E tests: Required for critical user flows

### Review Protocol
- All code reviewed before merge
- No self-approvals
- Address all comments or document disagreement

---

*Operation established: {date}*
*Commanding Officer: Sergeant Claude, 3rd Battalion ASF*

"We ship clean code or we die trying." - Sergeant Claude
"""


def init_operation(path: Path, name: str, description: str = ""):
    """Initialize operation command structure."""
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if not description:
        description = f"Operation {name} - Mission parameters pending reconnaissance."
    
    # Create state.md
    state_path = path / "state.md"
    state_content = STATE_TEMPLATE.format(date=date)
    
    # Create project.md
    project_path = path / "project.md"
    project_content = PROJECT_TEMPLATE.format(
        name=name.upper().replace("-", " ").replace("_", " "),
        description=description,
        date=date
    )
    
    # Write files
    state_path.write_text(state_content, encoding="utf-8")
    project_path.write_text(project_content, encoding="utf-8")
    
    return state_path, project_path


def main():
    if len(sys.argv) < 3:
        print("Usage: init_operation.py <target_directory> <operation_name> [description]")
        print("\nInitializes tactical command structure for new operation.")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    name = sys.argv[2]
    description = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
    
    if not target.exists():
        print(f"Creating target directory: {target}")
        target.mkdir(parents=True)
    
    state_path, project_path = init_operation(target, name, description)
    
    print("=" * 50)
    print("    🎖️  OPERATION INITIALIZED  🎖️")
    print("=" * 50)
    print(f"\n📍 AO: {target.absolute()}")
    print(f"🎯 Operation: {name.upper()}")
    print(f"\n✅ Created: {state_path.name}")
    print(f"✅ Created: {project_path.name}")
    print("\n" + "-" * 50)
    print("STANDING ORDERS:")
    print("-" * 50)
    print("1. Run /deploy-recon to scan the codebase")
    print("2. Review project.md and update tech stack")
    print("3. Begin Phase 1: RECONNAISSANCE")
    print("\n\"The mission starts now, Private. Don't disappoint me.\"")
    print("    - Sergeant Claude, ASF")
    print("=" * 50)


if __name__ == "__main__":
    main()
