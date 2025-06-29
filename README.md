# PlotWeaver Documentation

## Quick Start

### Option 1: VS Code Workspace (Recommended)
```bash
code PwDocs.code-workspace  # Auto-setup on open
```

### Option 2: Manual Setup (WSL + Windows)

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
python PwDocs/Scripts/process_issue.py  # Process GitHub issues
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
/
├── Readme.md                    # This file
├── Requirements.txt            # Python dependencies
├── Claude.md                   # AI assistant instructions
├── PwDocs.code-workspace      # VS Code workspace
│
├── ClaudeDocs/                 # AI-generated documentation
│   ├── agent-system.md         # Agent system architecture
│   ├── architecture-design.md  # Overall system design
│   └── sprint.yaml             # Current sprint planning
│
├── Content/                    # Documentation content
│   ├── Architecture/          # System architecture docs
│   ├── Issues/                # Processed GitHub issues
│   │   ├── Features-Proposed/ # Feature proposals
│   │   ├── Bugs/             # Bug reports
│   │   └── Questions/        # Q&A documentation
│   ├── Planning/             # Project planning
│   │   ├── MVP.md           # Minimum viable product
│   │   └── Roadmap.md       # Detailed roadmap
│   └── Technical/            # Technical documentation
│       ├── API/             # API documentation
│       └── Guides/          # Technical guides
│
└── PwDocs/                     # Documentation tooling
    ├── Processors/            # Content processors
    ├── Scripts/               # Automation scripts
    │   └── process_issue.py   # GitHub issue processor
    └── Templates/             # Document templates
        ├── Issue-Feature.md   # Feature template
        ├── Planning-MVP.md    # MVP template
        └── Spec-System.md     # System spec template
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
