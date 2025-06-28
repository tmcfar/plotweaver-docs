# Feature: Basic Security Linter for Issue Processing

## GitHub Issue Reference
- **Issue**: Feature Proposal (Manual Entry)
- **Title**: Add simple security linter to check for common vulnerabilities
- **Processed**: 2025-06-28

## Overview

Add a basic security linter that runs before commits to check for the most common and dangerous code patterns in our issue processing scripts.

## Requirements

### Core Checks (5 patterns only)
1. **Detect `eval()` and `exec()`** - Never safe with user input
2. **Detect `os.system()` and `subprocess` with shell=True** - Command injection risk
3. **Detect f-strings with user input going to files/commands** - Injection risk
4. **Detect `yaml.load()` without Loader** - Arbitrary code execution
5. **Detect missing input validation** - Check if issue_number/title are used raw

### Simple Output
- List findings with file:line number
- Show severity (HIGH/MEDIUM)
- One-line description of risk
- Exit code 1 if HIGH severity found

## Technical Approach

### Single Python Script
```python
#!/usr/bin/env python3
"""Basic security linter for PlotWeaver scripts."""

import re
import sys
import glob

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
        'pattern': r'f["\'].*{(issue_number|issue_title|issue_body)}.*["\'].*\.(md|py|sh)',
        'severity': 'MEDIUM',
        'message': 'User input in filenames needs validation'
    },
    'unsafe_yaml': {
        'pattern': r'yaml\.load\s*\([^)]*\)(?!.*Loader)',
        'severity': 'HIGH',
        'message': 'Use yaml.safe_load() instead'
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
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, 1):
        for check_name, check in DANGEROUS_PATTERNS.items():
            if re.search(check['pattern'], line):
                findings.append({
                    'file': filepath,
                    'line': i,
                    'severity': check['severity'],
                    'message': check['message'],
                    'code': line.strip()
                })
    
    return findings

def main():
    """Run security linter on all Python files."""
    files = glob.glob('scripts/**/*.py', recursive=True)
    all_findings = []
    
    for file in files:
        findings = scan_file(file)
        all_findings.extend(findings)
    
    # Report findings
    if all_findings:
        print("🔒 Security Linter Results:\n")
        for finding in all_findings:
            print(f"{finding['severity']}: {finding['file']}:{finding['line']}")
            print(f"  {finding['message']}")
            print(f"  > {finding['code']}\n")
        
        # Exit with error if HIGH severity found
        if any(f['severity'] == 'HIGH' for f in all_findings):
            print("❌ HIGH severity issues found - fix before committing!")
            sys.exit(1)
    else:
        print("✅ No security issues found!")
    
    return 0

if __name__ == '__main__':
    main()
```

## Usage

### Manual Run
```bash
python scripts/security-linter.py
```

### Pre-commit Hook
```bash
# In .git/hooks/pre-commit
#!/bin/bash
python scripts/security-linter.py || exit 1
```

### GitHub Action
```yaml
- name: Security Lint
  run: python scripts/security-linter.py
```

## Implementation Timeline
- **Day 1**: Write the linter script (2 hours)
- **Day 2**: Test on existing codebase (1 hour)
- **Day 3**: Add pre-commit hook (30 minutes)
- **Total**: ~4 hours of work

## Success Metrics
- Catches 100% of eval/exec usage
- Catches 100% of shell=True usage
- Zero false positives on safe code
- Runs in <1 second

## Future Enhancements (if needed)
- Add more patterns based on actual vulnerabilities found
- Create auto-fix suggestions for common issues
- Add configuration file for custom rules
- Integration with IDE warnings

## Why This Approach
- **Simple**: One file, ~100 lines of code
- **Fast**: Regex-based, no complex parsing
- **Effective**: Catches the most dangerous patterns
- **Maintainable**: Easy to add/remove patterns
- **Non-intrusive**: Doesn't change existing code

This basic linter provides 80% of the security value with 5% of the complexity.