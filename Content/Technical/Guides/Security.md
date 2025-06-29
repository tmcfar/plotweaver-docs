# Security Protection for PlotWeaver Documentation Processing

This repository processes untrusted user input from GitHub issues and converts it into documentation. To prevent code injection attacks, we have implemented security measures.

## Security Threats

**GitHub issues can contain malicious content that could:**
- Inject commands through issue titles/bodies
- Break YAML/Markdown formatting
- Manipulate AI prompts to produce harmful content
- Create malicious file paths

## Protection Measures

### 1. Input Sanitization (`shared_utils.py`)
- **Issue number validation** - strips non-numeric characters
- **Markdown escaping** - escapes special characters (`*`, `_`, `[`, `]`, etc.)
- **AI prompt sanitization** - removes injection patterns
- **YAML safe formatting** - uses `yaml.dump()` for proper escaping

### 2. Security Linter (`security-linter.py`)
Checks for dangerous patterns:
- `eval()` and `exec()` usage
- `os.system()` and `subprocess` with shell=True
- Unsafe f-strings with user input
- `yaml.load()` without Loader
- Raw user input in file operations

### 3. Pre-commit Hook (`.githooks/pre-commit`)
- Automatically runs security linter before commits
- Blocks commits with HIGH severity issues
- Allows commits with MEDIUM severity (warnings)

## Setup

```bash
# Install security hooks
bash scripts/setup-security-hooks.sh

# Manual security check
python scripts/security-linter.py
```

## Current Security Status

✅ **Protected Against:**
- Command injection through issue content
- YAML/Markdown format breaking
- Basic AI prompt manipulation
- Path traversal in generated files

⚠️ **Known Medium-Risk Areas:**
- Some f-strings with validated user input (acceptable risk)
- Print statements for logging (low risk)

## Security Guidelines

### When Processing User Input:
1. **Always validate issue numbers** with `validate_issue_number()`
2. **Escape markdown content** with `escape_markdown()` 
3. **Sanitize AI prompts** with `sanitize_for_ai()`
4. **Use YAML safe formatting** with `format_github_metadata_yaml()`

### Red Flags to Avoid:
- Never use `eval()` or `exec()` with user input
- Never use `os.system()` or `subprocess` with shell=True
- Never use raw user input in file paths without validation
- Never use `yaml.load()` without specifying a safe Loader

## Testing Security

```bash
# Test with malicious inputs
python scripts/test-security.py

# Manually test patterns
python scripts/security-linter.py
```

## Incident Response

If a security vulnerability is discovered:
1. **Stop processing** - disable GitHub Actions if needed
2. **Assess impact** - check if any malicious content was processed
3. **Apply fix** - update sanitization functions
4. **Test thoroughly** - run security linter and tests
5. **Update this document** - add new protections to the list

## Contact

For security concerns, create a GitHub issue with the `security` label.