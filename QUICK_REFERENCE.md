# Codespaces Quick Reference

## 🚀 Getting Started
```bash
# Set API key (required)
export OPENROUTER_API_KEY="your-key-here"
echo 'export OPENROUTER_API_KEY="your-key-here"' >> ~/.bashrc

# Start aider
aider
```

## 🤖 Aider Commands
```bash
# Basic usage
aider                                    # Start interactive session
aider file1.md file2.py                # Work on specific files
aider --model openrouter/anthropic/claude-3.7-sonnet  # Use specific model

# Common flags
aider --no-auto-commits                 # Disable auto-commits
aider --weak-model openrouter/anthropic/claude-3.5-haiku  # Use faster model
aider --list-models openrouter/         # Show available models
```

## 📁 Key Files
- `.aider.conf.yml` - Main aider configuration
- `.aider.model.settings.yml` - Provider settings
- `.devcontainer/devcontainer.json` - Codespaces setup
- `plotweaver-docs.code-workspace` - VS Code workspace

## 🔧 Quick Fixes
```bash
# Git ownership issue
git config --global --add safe.directory /workspaces/plotweaver-docs

# Check API key
echo $OPENROUTER_API_KEY

# Test aider
aider --help
```

## 📋 Workflow
1. Open Codespace from GitHub
2. Set OPENROUTER_API_KEY
3. Run `aider` to start coding
4. Commit and push changes
