#!/usr/bin/env python3
"""
SERGEANT CLAUDE - COURT MARTIAL
Full breakdown of a specific file. No mercy.
Every violation catalogued. Every sin exposed.
"""

import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List

@dataclass
class Violation:
    line: int
    category: str
    message: str
    severity: str  # MINOR, MAJOR, CRITICAL, WAR_CRIME
    code_snippet: str = ""


def analyze_file(filepath: Path) -> List[Violation]:
    """Perform deep analysis on a single file. No mercy."""
    violations = []
    
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
    except Exception as e:
        return [Violation(0, "UNREADABLE", f"Cannot read file: {e}", "CRITICAL")]
    
    ext = filepath.suffix.lower()
    total_lines = len(lines)
    
    # File length check
    if total_lines > 500:
        violations.append(Violation(
            0, "BLOAT", 
            f"File is {total_lines} lines. Max 300 recommended. This is a novel, not code.",
            "WAR_CRIME"
        ))
    elif total_lines > 300:
        violations.append(Violation(
            0, "BLOAT", 
            f"File is {total_lines} lines. Getting chunky. Consider splitting.",
            "MAJOR"
        ))
    
    # Line-by-line analysis
    current_function_start = None
    current_function_lines = 0
    brace_depth = 0
    function_start_depth = None
    function_started = False
    max_line_length = 0
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        line_len = len(line)
        max_line_length = max(max_line_length, line_len)
        
        # Long lines
        if line_len > 120:
            violations.append(Violation(
                i, "LINE_LENGTH",
                f"Line is {line_len} chars. We have horizontal scrolling trauma here.",
                "MINOR",
                line[:80] + "..."
            ))
        
        # Console.log / print debugging
        if ext in ['.ts', '.tsx', '.js', '.jsx']:
            if 'console.log' in line and '//' not in line.split('console.log')[0]:
                violations.append(Violation(
                    i, "DEBUG_TRASH",
                    "console.log left in code. Clean up after yourself, soldier.",
                    "MINOR",
                    stripped[:60]
                ))
        
        if ext == '.py':
            if re.match(r'^\s*print\s*\(', line) and '#' not in line.split('print')[0]:
                violations.append(Violation(
                    i, "DEBUG_TRASH",
                    "print() left in code. Use proper logging.",
                    "MINOR",
                    stripped[:60]
                ))
        
        # Any type abuse (TypeScript)
        if ext in ['.ts', '.tsx']:
            if ': any' in line or 'as any' in line:
                violations.append(Violation(
                    i, "TYPE_COWARDICE",
                    "Using 'any' is surrender. Fight for your types.",
                    "MAJOR",
                    stripped[:60]
                ))
            
            # @ts-ignore
            if '@ts-ignore' in line or '@ts-nocheck' in line:
                violations.append(Violation(
                    i, "SUPPRESSION",
                    "Suppressing TypeScript errors. Coward's way out.",
                    "CRITICAL",
                    stripped[:60]
                ))
        
        # TODO/FIXME
        if 'TODO' in line.upper() or 'FIXME' in line.upper():
            violations.append(Violation(
                i, "UNFINISHED",
                "TODO/FIXME found. Either do it or delete it.",
                "MINOR",
                stripped[:60]
            ))
        
        # HACK comments
        if 'HACK' in line.upper():
            violations.append(Violation(
                i, "ADMITTED_CRIME",
                "Developer admits this is a hack. At least they're honest.",
                "MAJOR",
                stripped[:60]
            ))
        
        # Empty catch blocks
        if ext in ['.ts', '.tsx', '.js', '.jsx', '.java']:
            if re.search(r'catch\s*\([^)]*\)\s*{\s*}', line):
                violations.append(Violation(
                    i, "SILENT_FAILURE",
                    "Empty catch block. Errors scream into the void.",
                    "CRITICAL",
                    stripped[:60]
                ))
        
        # Nested ternaries
        if line.count('?') >= 2 and line.count(':') >= 2:
            violations.append(Violation(
                i, "TERNARY_HELL",
                "Nested ternaries. This isn't a riddle contest.",
                "MAJOR",
                stripped[:60]
            ))
        
        # Magic numbers
        if ext in ['.ts', '.tsx', '.js', '.jsx', '.py']:
            magic = re.findall(r'[=<>]\s*(\d{3,})', line)
            if magic and 'const' not in line.lower() and '#' not in line:
                violations.append(Violation(
                    i, "MAGIC_NUMBER",
                    f"Magic number {magic[0]}. Extract to named constant.",
                    "MINOR",
                    stripped[:60]
                ))
        
        # God functions (track function length)
        if ext in ['.ts', '.tsx', '.js', '.jsx']:
            open_count = line.count('{')
            close_count = line.count('}')
            if re.match(r'^\s*(function|const\s+\w+\s*=.*=>|async\s+function)', line):
                if current_function_start and current_function_lines > 50:
                    violations.append(Violation(
                        current_function_start, "GOD_FUNCTION",
                        f"Function is {current_function_lines} lines. Max 50. Split it up.",
                        "CRITICAL" if current_function_lines > 100 else "MAJOR"
                    ))
                current_function_start = i
                current_function_lines = 0
                function_start_depth = brace_depth
                function_started = False

            brace_depth += open_count - close_count
            if current_function_start:
                current_function_lines += 1
                if open_count > 0:
                    function_started = True
                if function_started and brace_depth <= function_start_depth:
                    if current_function_lines > 50:
                        violations.append(Violation(
                            current_function_start, "GOD_FUNCTION",
                            f"Function is {current_function_lines} lines. Max 50. Split it up.",
                            "CRITICAL" if current_function_lines > 100 else "MAJOR"
                        ))
                    current_function_start = None
                    current_function_lines = 0
                    function_start_depth = None
                    function_started = False
        
        # Hardcoded secrets
        secret_patterns = [
            (r'password\s*=\s*["\'][^"\']+["\']', "HARDCODED_PASSWORD"),
            (r'api[_-]?key\s*=\s*["\'][^"\']+["\']', "HARDCODED_API_KEY"),
            (r'secret\s*=\s*["\'][^"\']+["\']', "HARDCODED_SECRET"),
        ]
        for pattern, vtype in secret_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                violations.append(Violation(
                    i, vtype,
                    "HARDCODED CREDENTIALS. This is a FELONY.",
                    "WAR_CRIME",
                    "[REDACTED FOR SECURITY]"
                ))
    
    if current_function_start and current_function_lines > 50:
        violations.append(Violation(
            current_function_start, "GOD_FUNCTION",
            f"Function is {current_function_lines} lines. Max 50. Split it up.",
            "CRITICAL" if current_function_lines > 100 else "MAJOR"
        ))

    return violations


def generate_verdict(filepath: Path, violations: List[Violation]) -> str:
    """Generate court martial verdict."""
    report = []
    
    report.append("=" * 70)
    report.append("          ⚖️  COURT MARTIAL PROCEEDINGS  ⚖️")
    report.append("=" * 70)
    report.append(f"\n📁 DEFENDANT: {filepath}")
    report.append(f"📅 DATE: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    if not violations:
        report.append("\n" + "=" * 70)
        report.append("                    ✅ ACQUITTED ✅")
        report.append("=" * 70)
        report.append("\nNo violations found. File passes inspection.")
        report.append("Don't get cocky, Private. Stay vigilant.")
        return "\n".join(report)
    
    # Count by severity
    counts = {"MINOR": 0, "MAJOR": 0, "CRITICAL": 0, "WAR_CRIME": 0}
    for v in violations:
        counts[v.severity] = counts.get(v.severity, 0) + 1
    
    report.append("\n" + "-" * 70)
    report.append("📊 CHARGES SUMMARY")
    report.append("-" * 70)
    report.append(f"  🔵 Minor:    {counts['MINOR']}")
    report.append(f"  🟡 Major:    {counts['MAJOR']}")
    report.append(f"  🟠 Critical: {counts['CRITICAL']}")
    report.append(f"  🔴 War Crime: {counts['WAR_CRIME']}")
    report.append(f"\n  TOTAL VIOLATIONS: {len(violations)}")
    
    # List violations
    report.append("\n" + "-" * 70)
    report.append("📋 DETAILED CHARGES")
    report.append("-" * 70)
    
    severity_icon = {
        "MINOR": "🔵",
        "MAJOR": "🟡", 
        "CRITICAL": "🟠",
        "WAR_CRIME": "🔴"
    }
    
    for v in sorted(violations, key=lambda x: {"WAR_CRIME": 0, "CRITICAL": 1, "MAJOR": 2, "MINOR": 3}[x.severity]):
        icon = severity_icon[v.severity]
        report.append(f"\n{icon} [{v.severity}] Line {v.line}: {v.category}")
        report.append(f"   └─ {v.message}")
        if v.code_snippet:
            report.append(f"   └─ Code: {v.code_snippet}")
    
    # Verdict
    report.append("\n" + "=" * 70)
    
    if counts['WAR_CRIME'] > 0:
        report.append("               🔴 GUILTY - WAR CRIMES 🔴")
        report.append("=" * 70)
        report.append("\nVERDICT: Immediate refactoring required.")
        report.append("SENTENCE: This file is a danger to the entire operation.")
        report.append("         Deploy /run-delta for emergency stabilization.")
    elif counts['CRITICAL'] > 2:
        report.append("              🟠 GUILTY - CRITICAL FAILURES 🟠")
        report.append("=" * 70)
        report.append("\nVERDICT: Significant violations detected.")
        report.append("SENTENCE: Prioritize fixes before any new features.")
    elif counts['MAJOR'] > 3:
        report.append("              🟡 GUILTY - MAJOR VIOLATIONS 🟡")
        report.append("=" * 70)
        report.append("\nVERDICT: Multiple issues require attention.")
        report.append("SENTENCE: Schedule cleanup sprint.")
    else:
        report.append("              🔵 GUILTY - MINOR INFRACTIONS 🔵")
        report.append("=" * 70)
        report.append("\nVERDICT: Minor issues detected.")
        report.append("SENTENCE: Fix during regular maintenance.")
    
    report.append("\n\"Every line of code is a responsibility, Private.\"")
    report.append("    - Sergeant Claude, ASF")
    report.append("=" * 70)
    
    return "\n".join(report)


def main():
    if len(sys.argv) < 2:
        print("Usage: court_martial.py <file_path>")
        print("\nFull breakdown of a specific file. No mercy.")
        sys.exit(1)
    
    filepath = Path(sys.argv[1])
    
    if not filepath.exists():
        print(f"❌ File does not exist: {filepath}")
        sys.exit(1)
    
    if not filepath.is_file():
        print(f"❌ Not a file: {filepath}")
        sys.exit(1)
    
    violations = analyze_file(filepath)
    print(generate_verdict(filepath, violations))


if __name__ == "__main__":
    main()
