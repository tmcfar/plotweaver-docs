#!/usr/bin/env python3
"""Basic security linter for PlotWeaver scripts."""

import re
import sys
import glob
import os

DANGEROUS_PATTERNS = {
    'eval_exec': {
        'pattern': r'\b(eval|exec)\s*\(',
        'severity': 'HIGH',
        'message': 'Never use eval/exec with user input'
    },
    'shell_command': {
        'pattern': r'(os\.system|subprocess.*shell=True)',
        'severity': 'HIGH', 
        'message': 'Shell commands can be injected'
    },
    'unsafe_f_string': {
        'pattern': r'f["\'].*{(issue_number|issue_title|issue_body)}.*["\']',
        'severity': 'MEDIUM',
        'message': 'User input in f-strings needs validation'
    },
    'unsafe_yaml': {
        'pattern': r'yaml\.load\s*\([^)]*\)(?!.*Loader)',
        'severity': 'HIGH',
        'message': 'Use yaml.safe_load() instead of yaml.load()'
    },
    'raw_input_usage': {
        'pattern': r'open\s*\([^)]*{(issue_number|issue_title|issue_body)}',
        'severity': 'HIGH',
        'message': 'Validate/sanitize before using in file operations'
    }
}


def scan_file(filepath):
    """Scan a single file for security issues."""
    findings = []
    
    # Skip the security linter itself to avoid false positives
    if 'security-linter.py' in filepath:
        return findings
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except (UnicodeDecodeError, IOError):
        return findings  # Skip unreadable files
    
    for i, line in enumerate(lines, 1):
        # Skip comments and string literals that contain pattern definitions
        if re.match(r'\s*#', line) or "'pattern':" in line or '"pattern":' in line:
            continue
            
        for check_name, check in DANGEROUS_PATTERNS.items():
            if re.search(check['pattern'], line):
                findings.append({
                    'file': filepath,
                    'line': i,
                    'severity': check['severity'],
                    'message': check['message'],
                    'code': line.strip(),
                    'check': check_name
                })
    
    return findings


def main():
    """Run security linter on all Python files."""
    # Find all Python files in scripts directory
    script_files = []
    for root, dirs, files in os.walk('scripts'):
        for file in files:
            if file.endswith('.py'):
                script_files.append(os.path.join(root, file))
    
    if not script_files:
        print("No Python files found in scripts/ directory")
        return 0
    
    all_findings = []
    
    for file in script_files:
        findings = scan_file(file)
        all_findings.extend(findings)
    
    # Report findings
    if all_findings:
        print("🔒 Security Linter Results:\n")
        
        high_count = 0
        medium_count = 0
        
        for finding in all_findings:
            severity_icon = "🚨" if finding['severity'] == 'HIGH' else "⚠️"
            print(f"{severity_icon} {finding['severity']}: {finding['file']}:{finding['line']}")
            print(f"   {finding['message']}")
            print(f"   > {finding['code']}")
            print()
            
            if finding['severity'] == 'HIGH':
                high_count += 1
            else:
                medium_count += 1
        
        print(f"Summary: {high_count} HIGH, {medium_count} MEDIUM severity issues")
        
        # Exit with error if HIGH severity found
        if high_count > 0:
            print("\n❌ HIGH severity issues found - fix before committing!")
            return 1
        else:
            print("\n⚠️ Medium severity issues found - consider fixing")
            return 0
    else:
        print("✅ No security issues found!")
        return 0


if __name__ == '__main__':
    sys.exit(main())