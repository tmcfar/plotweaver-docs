# GitHub Codespaces Setup Guide for PlotWeaver Documentation

This guide walks you through setting up and using GitHub Codespaces for the PlotWeaver documentation project.

## Quick Start

1. **Open in Codespaces**:
   - Go to your GitHub repository: `https://github.com/[your-username]/plotweaver-docs`
   - Click the green "Code" button
   - Select "Codespaces" tab
   - Click "Create codespace on main"

2. **Wait for Setup**: The devcontainer will automatically:
   - Install Python, Node.js, and development tools
   - Set up the VS Code environment
   - Install project dependencies

## Environment Configuration

### API Keys Setup

Once your Codespace is running, you need to set up your API keys:

```bash
# Set your OpenRouter API key
export OPENROUTER_API_KEY="your-api-key-here"

# Add to your shell profile for persistence
echo 'export OPENROUTER_API_KEY="your-api-key-here"' >> ~/.bashrc
```

### Verify Aider Configuration

```bash
# Test aider setup
aider --help

# Test with your models
aider --model openrouter/anthropic/claude-3.7-sonnet --list-models
```

## Development Workflow

### Using Aider

```bash
# Start aider in your project directory
cd /workspaces/plotweaver-docs
aider

# Or specify files to work on
aider README.md planning/mvp.md

# Use with specific model
aider --model openrouter/anthropic/claude-3.7-sonnet
```

### VS Code Integration

The workspace is pre-configured with:
- **Extensions**: Python, Markdown, Git tools
- **Settings**: Optimized for documentation work
- **Tasks**: Build and deployment workflows
- **Debugging**: Ready for Python development

### Git Workflow

```bash
# Check status
git status

# Stage and commit changes
git add .
git commit -m "Your commit message"

# Push to GitHub
git push origin main
```

## File Structure

```
plotweaver-docs/
├── .devcontainer/          # Codespaces configuration
│   └── devcontainer.json
├── .github/               # GitHub workflows
├── .vscode/              # VS Code settings
├── .aider.conf.yml       # Aider configuration
├── .aider.model.settings.yml  # Model settings
├── Claude-Docs/          # AI-generated documentation
├── api/                  # API documentation
├── features/             # Feature specifications
├── planning/             # Project planning
├── scripts/              # Automation scripts
└── templates/           # Document templates
```

## Troubleshooting

### Common Issues

1. **API Key Not Set**:
   ```bash
   echo $OPENROUTER_API_KEY
   # Should display your API key
   ```

2. **Aider Model Issues**:
   ```bash
   # List available models
   aider --list-models openrouter/
   
   # Test specific model
   aider --model openrouter/anthropic/claude-3.5-haiku --no-auto-commits
   ```

3. **Git Issues**:
   ```bash
   # Configure git if needed
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### Performance Tips

1. **Use weak model for simple tasks**:
   ```bash
   # Faster for simple edits
   aider --weak-model openrouter/anthropic/claude-3.5-haiku
   ```

2. **Limit file scope**:
   ```bash
   # Work on specific files only
   aider specific-file.md
   ```

3. **Use auto-commits wisely**:
   ```bash
   # Disable for experimental work
   aider --no-auto-commits
   ```

## Advanced Features

### Custom Model Settings

Edit `.aider.model.settings.yml` to:
- Control provider routing
- Set privacy preferences
- Configure fallback options

### Workspace Customization

Edit `.vscode/settings.json` to:
- Customize editor preferences
- Add new extensions
- Configure debugging

### Automation Scripts

Use `scripts/` directory for:
- Issue processing (`process-issue.py`)
- Documentation generation
- Deployment automation

## Getting Help

- **Aider docs**: https://aider.chat/docs/
- **OpenRouter docs**: https://openrouter.ai/docs
- **Codespaces docs**: https://docs.github.com/codespaces

## Next Steps

1. Set up your API keys
2. Test aider with a simple edit
3. Explore the VS Code workspace
4. Start working on documentation
5. Use the planning templates in `templates/`
