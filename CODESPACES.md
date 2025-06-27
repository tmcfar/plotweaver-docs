# PlotWeaver Documentation - Codespaces Setup

## Quick Start

1. **Open in Codespaces**: Click the "Code" button → "Codespaces" → "Create codespace"
2. **Wait for Setup**: The environment will automatically configure (2-3 minutes)
3. **Set API Key**: Add your OpenRouter API key (see below)
4. **Start Coding**: Run `aider-docs` to begin!

## Environment Variables

### Required
- `OPENROUTER_API_KEY`: Your OpenRouter API key for Claude access

### Setting Secrets in Codespaces
1. Go to your repository settings
2. Navigate to "Secrets and variables" → "Codespaces"
3. Add your secrets:
   - Name: `OPENROUTER_API_KEY`
   - Value: `sk-or-v1-your-key-here`

## Available Commands

### Aider (AI Assistant)
```bash
aider-docs          # Start aider in this project directory
aider --help        # View all aider options
```

### Code Quality
```bash
lint-check          # Check formatting without changes
lint-fix            # Auto-format all code
black .             # Format Python files
flake8 .            # Check style guide compliance
mypy .              # Type checking
```

### Git Shortcuts
```bash
gs                  # git status
ga .                # git add all
gc -m "message"     # git commit with message
gp                  # git push
gl                  # git log (last 10 commits)
```

## Performance Tips

### Codespaces Configuration
- **CPU**: 2 cores (configured)
- **Memory**: 4GB (configured)
- **Storage**: 16GB (configured)

### For Better Performance
1. **Use machine types**: Upgrade to 4-core if doing heavy AI work
2. **Prebuilt containers**: Will be faster after first use
3. **Keep codespace running**: Pause instead of stopping for quick resume

### VS Code Extensions (Auto-installed)
- Python language support
- Code formatters (Black, Flake8, MyPy)
- GitHub Copilot (if you have access)
- YAML and JSON support

## Troubleshooting

### Aider Not Found
```bash
source ~/.bashrc    # Reload shell configuration
```

### Git Not Configured
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### API Key Issues
1. Check Codespaces secrets are set
2. Restart the codespace
3. Verify with: `echo $OPENROUTER_API_KEY`

## Migration from Local Dev

### What Changed
- ✅ No more Docker Desktop overhead
- ✅ No more Windows/WSL2 performance issues
- ✅ Pre-configured development environment
- ✅ Automatic dependency installation
- ✅ Global tool installation (no venv needed)

### Benefits
- **Faster startup**: No local container build
- **Better performance**: Dedicated cloud resources
- **Consistent environment**: Same setup for everyone
- **Easy sharing**: Share codespace links
- **Multiple workspaces**: Work on different branches simultaneously

## Advanced Usage

### Custom Aider Configuration
Your `.aider.conf.yml` is automatically loaded with:
- OpenRouter Claude models
- Auto-commit and auto-lint enabled
- Optimized for modified files only

### Multiple Projects
Create separate codespaces for:
- Main PlotWeaver repository
- Documentation repository (this one)
- Any experimental branches

## Cost Management

### Free Tier
- 120 core-hours/month for personal accounts
- 2-core codespace = 60 hours/month

### Tips to Save Hours
- Use "Stop codespace" when not actively coding
- Use "Pause" for short breaks (auto-resumes)
- Delete old/unused codespaces
- Use prebuilt containers when possible
