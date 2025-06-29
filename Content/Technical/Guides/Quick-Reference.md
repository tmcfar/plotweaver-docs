# Quick Reference

## Setup
```bash
./.setup/setup.sh               # Full setup (creates venv, installs deps)
source venv/bin/activate        # Activate environment
source .setup/.git-aliases      # Load git aliases
```

## Development
```bash
aider                           # AI-assisted coding
aider file1.md file2.py         # Work on specific files
black . && flake8 .             # Format and lint
```

## Git (with aliases)
```bash
gs                              # git status
ga . && gcm "msg" && gp         # add, commit, push
gcb feature/name                # create branch
gdoc                            # quick doc commit+push
```

## VS Code
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Start Aider"
- `Ctrl+Shift+P` → "Files: Toggle Excluded Files" (show/hide dotfiles)
- Explorer hides: venv, .git, __pycache__, gitignored files

## Issues
```bash
source ~/.bashrc                # If aliases don't work
./venv/bin/aider                # If aider not found
which python3                   # Check Python path
echo $OPENROUTER_API_KEY        # Verify API key
```

**Common problem:** `gs` conflicts with ghostscript on some systems. Use `git status` if needed.
