#!/usr/bin/env python3
"""
SERGEANT CLAUDE RECON UNIT
Tactical Codebase Analysis System

Drops an agent into the codebase via helicopter.
Scans perimeter. Reports hostiles. Provides tactical assessment.
"""

import os
import sys
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# File patterns
CODE_EXTENSIONS = {
    '.ts': 'TypeScript',
    '.tsx': 'TypeScript/React',
    '.js': 'JavaScript',
    '.jsx': 'JavaScript/React',
    '.py': 'Python',
    '.java': 'Java',
    '.go': 'Go',
    '.rs': 'Rust',
    '.cpp': 'C++',
    '.c': 'C',
    '.cs': 'C#',
    '.rb': 'Ruby',
    '.php': 'PHP',  # Sergeant sighs
    '.swift': 'Swift',
    '.kt': 'Kotlin',
}

CONFIG_FILES = [
    'package.json', 'tsconfig.json', 'pyproject.toml', 'Cargo.toml',
    'go.mod', 'pom.xml', 'build.gradle', 'Makefile', 'docker-compose.yml',
    'Dockerfile', '.env', '.env.example', 'requirements.txt'
]

IGNORE_DIRS = {
    'node_modules', '.git', '__pycache__', 'venv', '.venv', 'dist', 
    'build', 'target', '.next', '.nuxt', 'coverage', '.pytest_cache'
}

# Code smells thresholds
MAX_FILE_LINES = 300
MAX_FUNCTION_LINES = 50
MAX_NESTING_DEPTH = 4


def scan_directory(path: Path) -> dict:
    """Scan directory structure and gather intel."""
    intel = {
        'total_files': 0,
        'total_lines': 0,
        'languages': defaultdict(lambda: {'files': 0, 'lines': 0}),
        'config_files': [],
        'large_files': [],  # Potential hostiles
        'structure': [],
        'test_files': 0,
        'has_tests': False,
    }
    
    for root, dirs, files in os.walk(path):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        rel_root = Path(root).relative_to(path)
        depth = len(rel_root.parts)
        
        if depth <= 2:
            intel['structure'].append({
                'path': str(rel_root) if str(rel_root) != '.' else '/',
                'depth': depth,
                'files': len(files),
                'dirs': len(dirs)
            })
        
        for file in files:
            filepath = Path(root) / file
            ext = filepath.suffix.lower()
            
            # Check if config file
            if file in CONFIG_FILES:
                intel['config_files'].append(str(filepath.relative_to(path)))
            
            # Check if code file
            if ext in CODE_EXTENSIONS:
                intel['total_files'] += 1
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = len(f.readlines())
                        intel['total_lines'] += lines
                        intel['languages'][CODE_EXTENSIONS[ext]]['files'] += 1
                        intel['languages'][CODE_EXTENSIONS[ext]]['lines'] += lines
                        
                        # Flag large files as hostiles
                        if lines > MAX_FILE_LINES:
                            intel['large_files'].append({
                                'path': str(filepath.relative_to(path)),
                                'lines': lines,
                                'severity': 'CRITICAL' if lines > 500 else 'WARNING'
                            })
                except Exception:
                    pass
            
            # Check for tests
            if 'test' in file.lower() or 'spec' in file.lower():
                intel['test_files'] += 1
                intel['has_tests'] = True
    
    return intel


def analyze_code_smells(path: Path) -> list:
    """Detect code smells and violations."""
    smells = []
    
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            filepath = Path(root) / file
            ext = filepath.suffix.lower()
            
            if ext not in CODE_EXTENSIONS:
                continue
                
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.split('\n')
                    rel_path = str(filepath.relative_to(path))
                    
                    # Check for console.log spam (JS/TS)
                    if ext in ['.js', '.ts', '.jsx', '.tsx']:
                        console_count = content.count('console.log')
                        if console_count > 5:
                            smells.append({
                                'file': rel_path,
                                'type': 'DEBUG_SPAM',
                                'message': f'{console_count} console.log statements. Clean your foxhole.',
                                'severity': 'WARNING'
                            })
                    
                    # Check for any type abuse (TypeScript)
                    if ext in ['.ts', '.tsx']:
                        any_count = content.count(': any')
                        if any_count > 3:
                            smells.append({
                                'file': rel_path,
                                'type': 'TYPE_COWARDICE',
                                'message': f'{any_count} uses of "any". TypeScript is your weapon. Use it.',
                                'severity': 'CRITICAL'
                            })
                    
                    # Check for TODO/FIXME (unfinished business)
                    todo_count = content.lower().count('todo') + content.lower().count('fixme')
                    if todo_count > 3:
                        smells.append({
                            'file': rel_path,
                            'type': 'UNFINISHED_BUSINESS',
                            'message': f'{todo_count} TODOs/FIXMEs. Finish what you started, soldier.',
                            'severity': 'WARNING'
                        })
                    
                    # Check nesting depth (looking for arrow hell)
                    max_depth = 0
                    current_depth = 0
                    for char in content:
                        if char in '{[(':
                            current_depth += 1
                            max_depth = max(max_depth, current_depth)
                        elif char in '}])':
                            current_depth = max(0, current_depth - 1)
                    
                    if max_depth > 8:
                        smells.append({
                            'file': rel_path,
                            'type': 'CALLBACK_HELL',
                            'message': f'Nesting depth of {max_depth}. This is not Inception.',
                            'severity': 'CRITICAL'
                        })
                        
            except Exception:
                pass
    
    return smells


def generate_sitrep(path: Path) -> str:
    """Generate tactical situation report."""
    intel = scan_directory(path)
    smells = analyze_code_smells(path)
    
    report = []
    report.append("=" * 60)
    report.append("          🎖️  TACTICAL SITREP - RECON COMPLETE  🎖️")
    report.append("=" * 60)
    report.append(f"\n📍 AO (Area of Operations): {path.absolute()}")
    report.append(f"📅 Recon Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Force composition
    report.append("\n" + "-" * 40)
    report.append("📊 FORCE COMPOSITION")
    report.append("-" * 40)
    report.append(f"Total Files: {intel['total_files']}")
    report.append(f"Total Lines: {intel['total_lines']:,}")
    report.append(f"Test Files: {intel['test_files']}")
    
    if not intel['has_tests']:
        report.append("\n⚠️  NO TEST FILES DETECTED. ARE YOU A TWIRK, PRIVATE?")
    
    # Language breakdown
    report.append("\n" + "-" * 40)
    report.append("🔫 ARSENAL (Languages)")
    report.append("-" * 40)
    for lang, data in sorted(intel['languages'].items(), key=lambda x: x[1]['lines'], reverse=True):
        pct = (data['lines'] / intel['total_lines'] * 100) if intel['total_lines'] > 0 else 0
        bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
        report.append(f"{lang:20} {bar} {pct:5.1f}% ({data['files']} files, {data['lines']:,} lines)")
    
    # Config files (equipment)
    if intel['config_files']:
        report.append("\n" + "-" * 40)
        report.append("⚙️  EQUIPMENT (Config)")
        report.append("-" * 40)
        for cf in intel['config_files'][:10]:
            report.append(f"  • {cf}")
    
    # Hostiles (large files)
    if intel['large_files']:
        report.append("\n" + "-" * 40)
        report.append("🎯 HOSTILES DETECTED (Oversized Files)")
        report.append("-" * 40)
        for hostile in sorted(intel['large_files'], key=lambda x: x['lines'], reverse=True)[:10]:
            icon = "🔴" if hostile['severity'] == 'CRITICAL' else "🟡"
            report.append(f"  {icon} {hostile['path']} ({hostile['lines']} lines)")
    
    # Code smells (enemy positions)
    if smells:
        report.append("\n" + "-" * 40)
        report.append("💀 ENEMY POSITIONS (Code Smells)")
        report.append("-" * 40)
        for smell in smells[:15]:
            icon = "🔴" if smell['severity'] == 'CRITICAL' else "🟡"
            report.append(f"  {icon} [{smell['type']}] {smell['file']}")
            report.append(f"      └─ {smell['message']}")
    
    # Tactical assessment
    report.append("\n" + "=" * 60)
    report.append("📋 TACTICAL ASSESSMENT")
    report.append("=" * 60)
    
    threat_level = "LOW"
    if len(smells) > 10 or len(intel['large_files']) > 5:
        threat_level = "HIGH"
    elif len(smells) > 5 or len(intel['large_files']) > 2:
        threat_level = "MEDIUM"
    
    if not intel['has_tests']:
        threat_level = "CRITICAL"
    
    threat_icons = {"LOW": "🟢", "MEDIUM": "🟡", "HIGH": "🟠", "CRITICAL": "🔴"}
    report.append(f"\nTHREAT LEVEL: {threat_icons[threat_level]} {threat_level}")
    
    if threat_level == "CRITICAL":
        report.append("\n⚠️  SITUATION IS DIRE. IMMEDIATE ACTION REQUIRED.")
        report.append("    Sergeant recommends /run-delta for emergency stabilization.")
    elif threat_level == "HIGH":
        report.append("\n⚠️  HEAVY RESISTANCE EXPECTED. Plan your approach carefully.")
        report.append("    Sergeant recommends systematic /court-martial of each hostile.")
    elif threat_level == "MEDIUM":
        report.append("\n📍 Moderate cleanup required. Nothing we can't handle.")
        report.append("    Proceed with /run-alpha when ready.")
    else:
        report.append("\n✅ AO is relatively secure. Good work, soldier.")
        report.append("    Minor improvements can proceed with standard operations.")
    
    report.append("\n" + "=" * 60)
    report.append("        END TRANSMISSION - SERGEANT CLAUDE, ASF")
    report.append("=" * 60)
    
    return "\n".join(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: recon.py <target_directory>")
        print("\nDrops a recon agent into the specified codebase.")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    
    if not target.exists():
        print(f"❌ Target directory does not exist: {target}")
        sys.exit(1)
    
    if not target.is_dir():
        print(f"❌ Target is not a directory: {target}")
        sys.exit(1)
    
    print(generate_sitrep(target))


if __name__ == "__main__":
    main()
