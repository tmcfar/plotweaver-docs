# PlotWeaver Documentation

## Quick Start (WSL + Windows)

**Prerequisites:** WSL2, Docker Desktop, Python 3.8+, Git

```bash
git clone <repository-url>
cd pwdocs

# Setup (creates venv automatically)
./.setup/setup.sh

# Start developing
source venv/bin/activate
aider
```

**VS Code integration:**
```bash
code .  # Opens with proper Python paths and clean explorer
```

### Available Commands

```bash
# Development
aider                    # Start AI-assisted coding
aider file1.md file2.py  # Work on specific files

# Setup
./.setup/setup.sh              # Full project setup (includes git aliases)
./.setup/setup-git-aliases.sh  # Install git aliases only

# Code Quality
black .                  # Format Python code
flake8 .                # Check code style
mypy .                  # Type checking

# Git (after installing aliases)
gs                      # git status
gcm "message"           # git commit -m "message"
gp                      # git push
gdoc                    # Quick doc commit (add all, commit, push)

# Project Management
python scripts/process-issue.py  # Process GitHub issues
```

## Purpose

AI-generated technical documentation for PlotWeaver novel writing platform. Triggered by GitHub issues, processed via OpenRouter API.

**Key features:**
- Automated doc generation from issues
- 20-hour sprint planning
- Feature evaluation matrices
- API documentation

## Repository Structure

```
pwdocs/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── active-features.md           # Currently active features
├── roadmap.md                   # Product roadmap overview
│
├── .setup/                      # Setup and configuration
│   ├── setup.sh                # Main setup script
│   ├── setup-git-aliases.sh    # Git aliases installer
│   ├── .git-aliases            # Git aliases definitions
│   ├── DEV_SETUP.md            # Development environment guide
│   ├── GIT_ALIASES_GUIDE.md    # Git aliases documentation
│   └── MIGRATION_SUMMARY.md    # Codespaces → WSL migration notes
│
├── .vscode/                     # VS Code configuration
│   ├── settings.json           # Editor settings
│   ├── tasks.json              # Build tasks
│   └── extensions.json         # Recommended extensions
│
├── Claude-Docs/                 # AI-generated documentation
│   ├── agent-system.md         # Agent system architecture
│   ├── architecture-design.md  # Overall system design
│   └── sprint.yaml             # Current sprint planning
│
├── planning/                    # Project planning documents
│   ├── mvp.md                  # Minimum viable product
│   └── roadmap.md              # Detailed roadmap
│
├── scripts/                     # Automation scripts
│   └── process-issue.py        # GitHub issue processor
│
└── templates/                   # Document templates
    ├── feature-evaluation.md   # Feature evaluation template
    ├── mvp.md                  # MVP template
    ├── sprint.md               # Sprint template
    └── system-spec.md          # System specification template
```

## Development

**Common workflow:**
```bash
source venv/bin/activate
aider file1.md file2.py    # Edit specific files
black . && flake8 .        # Format and lint
git add . && git commit -m "Update" && git push
```

**Git aliases available:** `gs`, `gcm`, `gp`, `gdoc` (see .setup/GIT_ALIASES_GUIDE.md)

## Issues

**Virtual environment problems:** Modern Ubuntu requires venv, not system pip. The setup script handles this correctly.

**Aider not found:** Ensure you're in the virtual environment or use `./venv/bin/aider`

**VS Code Python path:** Should automatically use `./venv/bin/python` - restart VS Code if not working.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run code quality checks: `black . && flake8 .`
5. Commit and push changes
6. Create a pull request

## License

This documentation repository is part of the PlotWeaver project. See the main repository for licensing information.
