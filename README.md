# PlotWeaver Documentation Repository

## 🚀 Quick Start (WSL on Windows)

### Prerequisites
- Windows 10/11 with WSL2 installed
- Docker Desktop for Windows (with WSL2 backend)
- Python 3.8+ in WSL
- Git configured in WSL

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd pwdocs
   ```

2. **Install Python dependencies**:
   ```bash
   # Option 1: Use virtual environment (recommended)
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   
   # Option 2: Run setup script (creates venv automatically)
   ./.setup/setup.sh
   ```

3. **Configure API key** (for aider):
   ```bash
   export OPENROUTER_API_KEY="your-api-key-here"
   echo 'export OPENROUTER_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```

4. **Start developing**:
   ```bash
   # If using virtual environment
   source venv/bin/activate
   aider  # Start AI-assisted coding
   
   # Or directly from venv
   ./venv/bin/aider
   ```

### VS Code Integration

Open the project in VS Code from WSL:
```bash
code .
```

The workspace includes:
- **Tasks**: Install dependencies, start aider, format code
- **Settings**: Python linting, formatting, and development optimizations
- **Extensions**: Recommended Python and Markdown tools
- **Clean Explorer**: Hides dotfiles, virtual environment, and gitignored files

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

## Overview

This repository contains automatically generated and curated documentation for the PlotWeaver AI-assisted novel writing platform. Documentation is generated via GitHub Actions triggered by issue creation in the main PlotWeaver repository.

## Purpose

- **Automated Documentation**: AI-generated technical specifications from GitHub issues
- **Feature Planning**: Structured evaluation and planning documents
- **API Documentation**: Comprehensive API references and examples
- **Sprint Management**: 20-hour sprint planning and tracking
- **Product Roadmap**: Strategic planning and feature pipeline management

## Repository Structure

```
pwdocs/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── active-features.md           # Currently active features
├── roadmap.md                   # Product roadmap overview
│
├── .setup/                      # Setup and configuration scripts
│   ├── setup.sh                # Main setup script
│   ├── setup-git-aliases.sh    # Git aliases installer
│   └── .git-aliases            # Git aliases definitions
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

## Development Workflow

### Working with Issues
1. Create issue in main PlotWeaver repository
2. GitHub Action automatically generates documentation
3. Review and refine generated content
4. Use aider for AI-assisted editing

### Documentation Standards
- Use Markdown for all documentation
- Follow templates in `templates/` directory
- Maintain consistent structure and formatting
- Include examples and code samples where applicable

### Git Workflow
```bash
git checkout -b feature/new-documentation
# Make changes
git add .
git commit -m "Add documentation for new feature"
git push origin feature/new-documentation
# Create pull request
```

## Troubleshooting

### Common Issues

**Aider not found**:
```bash
pip install --upgrade aider-chat
source ~/.bashrc
```

**Python path issues**:
```bash
which python3
# Update .vscode/settings.json if needed
```

**Git configuration**:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Docker not running**:
```bash
# Start Docker Desktop on Windows
# Verify Docker is accessible from WSL
docker --version
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run code quality checks: `black . && flake8 .`
5. Commit and push changes
6. Create a pull request

## License

This documentation repository is part of the PlotWeaver project. See the main repository for licensing information.
