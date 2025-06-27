# Quick Reference

## Setup
```bash
./.setup/setup.sh                        # Run setup script (creates venv)
# OR manually:
python3 -m venv venv                     # Create virtual environment  
source venv/bin/activate                 # Activate virtual environment
pip install -r requirements.txt         # Install dependencies

# Git aliases (optional)
./.setup/setup-git-aliases.sh           # Setup git aliases in bashrc
source .setup/.git-aliases              # Load aliases for current session
```

## Development
```bash
source venv/bin/activate                 # Activate venv (if not active)
aider                                    # Start AI-assisted coding
# OR directly:
./venv/bin/aider                        # Run aider from venv
aider file1.md file2.py                 # Work on specific files
code .                                   # Open in VS Code
```

## Code Quality
```bash
black .                                  # Format Python code
flake8 .                                # Check style
mypy .                                  # Type checking
```

## Git Workflow
```bash
# Setup git aliases (one-time)
./.setup/setup-git-aliases.sh           # Install useful git aliases

# Basic workflow (with aliases)
gs                                       # git status
gcb feature/my-feature                   # git checkout -b feature/my-feature
ga .                                     # git add .
gcm "Description"                        # git commit -m "Description"
gp                                       # git push

# Or traditional commands:
git checkout -b feature/my-feature       # Create feature branch
git add .                               # Stage changes
git commit -m "Description"             # Commit changes
git push origin feature/my-feature      # Push to remote

# Quick documentation workflow
gdoc                                     # Add all, commit "Update documentation", push
```

## Useful Git Aliases
```bash
# Status and basic operations
gs          # git status
ga .        # git add all
gcm "msg"   # git commit -m "message"
gp          # git push
gpl         # git pull

# Branching
gcb name    # git checkout -b name
gco main    # git checkout main
gb          # git branch
gm branch   # git merge branch

# History and logs
gl          # git log --oneline (last 10)
glg         # git log --graph (pretty format)
gd          # git diff
gds         # git diff --staged

# Quick shortcuts
gdoc        # Add all, commit "Update documentation", push
ghelp       # Show all available git aliases
```

## VS Code Tasks
- **Ctrl+Shift+P** → "Tasks: Run Task"
- Setup Virtual Environment
- Install Dependencies
- Start Aider
- Format Code
- Show/Hide Dotfiles

## VS Code Explorer
- **Hidden by default**: dotfiles, venv, gitignored files
- **Toggle hidden files**: `Ctrl+Shift+P` → "Files: Toggle Excluded Files"
- **Clean view**: Only shows relevant project files

## Troubleshooting
```bash
source ~/.bashrc                        # Reload shell config
source venv/bin/activate                # Activate virtual environment
which python3                          # Check Python path
docker --version                       # Check Docker
echo $OPENROUTER_API_KEY               # Check API key
```
