# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PlotWeaver Documentation is an AI-generated technical documentation system for the PlotWeaver novel writing platform. The system automatically processes GitHub issues to create structured documentation using the OpenRouter API.

## Development Commands

### Environment Setup
```bash
# Setup (creates venv automatically)
./.setup/setup.sh

# Activate environment
source venv/bin/activate

# VS Code workspace (recommended - auto-setup)
code pwdocs.code-workspace
```

### Development Workflow
```bash
# AI-assisted coding
aider                    # Start AI-assisted coding
aider file1.md file2.py  # Work on specific files

# Code Quality
black .                  # Format Python code
flake8 .                # Check code style  
mypy .                  # Type checking

# Testing
pytest                  # Run tests (if available)
```

### Git Aliases
After running setup, these aliases are available:
```bash
gs                      # git status
gcm "message"           # git commit -m "message"
gp                      # git push
gdoc                    # Quick doc commit (add all, commit, push)
```

## Architecture

### Core Components

**Documentation Generation Pipeline:**
- `scripts/process-issue.py` - Processes GitHub issues using OpenRouter API
- `templates/` - Document templates for different content types
- `Claude-Docs/` - AI-generated documentation output

**Template System:**
- `feature-evaluation.md` - Feature analysis with scoring matrices
- `sprint.md` - 20-hour sprint planning for solo development
- `system-spec.md` - Technical specifications
- `api-endpoint.md` - API documentation

### Key Patterns

**Environment Variables Required:**
- `OPENROUTER_API_KEY` - For AI content generation
- `ISSUE_NUMBER`, `ISSUE_TITLE`, `ISSUE_BODY`, `EVENT_TYPE` - For GitHub issue processing

**File Structure:**
- Features organized as `features/proposed/{issue_number}-{clean_title}/`
- Each feature gets a README.md and status.md
- Templates use AI_INSTRUCTIONS comments for OpenRouter prompts

## Development Guidelines

### Python Code Style
- Use Black for formatting (`black .`)
- Follow flake8 linting (`flake8 .`)
- Type hints with mypy checking (`mypy .`)
- Virtual environment required (handled by setup script)

### Documentation Patterns
- YAML metadata in template files for structured content
- Minimal, contract-focused metadata over heavy explicit files
- AI_INSTRUCTIONS comments in templates guide content generation
- Issue processing creates feature directories with standardized structure

### VS Code Configuration
- Python interpreter: `./venv/bin/python`
- Dotfiles hidden in explorer (configured in .vscode/settings.json)
- Auto-formatting on save enabled
- Git autofetch enabled

## Common Issues

**Virtual Environment:** Modern Ubuntu requires venv, not system pip. The setup script handles this correctly.

**Aider Not Found:** Ensure you're in the virtual environment or use `./venv/bin/aider`

**VS Code Python Path:** Should automatically use `./venv/bin/python` - restart VS Code if not working.

## File Processing

**Corrupted Files:** The `process-issue.py` script was recently rebuilt due to corruption. It processes GitHub issues and generates documentation using the OpenRouter API with Claude models.

**Template Usage:** Templates in `/templates/` contain AI_INSTRUCTIONS for content generation. The system uses minimal metadata contracts rather than storing everything explicitly.