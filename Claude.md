# Claude.md

Configuration and guidance for Claude Code (claude.ai/code) in this repository.

## Project Structure

### Key Directories
- `PwDocs/` - Documentation tooling and processors
- `Content/` - Generated documentation content
- `ClaudeDocs/` - AI-generated documentation awaiting processing

### Naming Conventions
- Directories: PascalCase (Content, Scripts, Templates)
- Python files: lowercase_with_underscores
- Markdown files: Title-Case-With-Hyphens.md
- Shell scripts: lowercase_with_underscores.sh

## Content Processing

### Issue Types
- Features → Content/Issues/Features-Proposed/
- Bugs → Content/Issues/Bugs/
- Questions → Content/Issues/Questions/
- Updates → Content/Technical/Updates/

### Content States
- Proposed → Content/Issues/{Type}/
- Closed → Content/Issues/Closed/{Type}/
- Approved Features → Content/Planning/Roadmap/

### Template Guidelines
- Use AI_INSTRUCTIONS comments for generation guidance
- Follow YAML frontmatter for metadata
- Maintain minimal, contract-focused structure

## Code Quality Requirements

### Python
- Black formatting required
- Flake8 compliance required
- MyPy type checking required
- Follow PEP 8 naming conventions

### Documentation
- Documentation must use Title-Case for headings
- Links must use relative paths from repository root
- Each feature proposal requires Readme.md and Status.md
- Technical guides go in Content/Technical/Guides/

## Security Guidelines

### Content Processing
- Sanitize all user inputs before AI processing
- Validate issue metadata before generation
- Follow principle of least privilege
- No sensitive data in documentation

### File Operations
- Verify paths before file operations
- Use case-insensitive path handling
- Maintain path traversal protection
- Follow symbolic link policies

## File Synchronization

### Receiving from pw
```bash
# Updates arrive in Content/Technical/Updates/
# Process them with:
./PwDocs/Scripts/process_current_state.py Content/Technical/Updates/PROJECT_STATE.md
```

### Sending to pw
```bash
# Sync file from Content/ to pw project
# IMPORTANT: Do not include 'Content/' in the source path - script adds it automatically
# Usage: ./PwDocs/Scripts/sync_file.sh <source_path> <destination_path>

# Examples:
./PwDocs/Scripts/sync_file.sh Planning/Sprint.md docs/planning/sprint.md           # Explicit destination
./PwDocs/Scripts/sync_file.sh Technical/API/Endpoints.md docs/api/endpoints.md     # Follow lowercase convention
./PwDocs/Scripts/sync_file.sh Planning/Sprint.md                                  # Uses same path in pw

# Source path is relative to Content/
# Destination path is relative to pw project root
# If destination path is omitted, uses same path as source
```