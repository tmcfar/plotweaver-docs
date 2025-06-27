# Development Setup for WSL + Windows

## Environment Overview

This project is optimized for development in WSL (Windows Subsystem for Linux) on Windows with Docker Desktop. This setup provides:

- **Native Linux development environment** within Windows
- **Docker integration** through Docker Desktop's WSL2 backend
- **VS Code integration** with seamless WSL support
- **Python development** with proper tooling and linting

## Initial Setup

### 1. Prerequisites

Ensure you have:
- Windows 10/11 with WSL2 enabled
- Docker Desktop for Windows with WSL2 backend
- VS Code with Remote-WSL extension
- Python 3.8+ installed in WSL

### 2. Quick Setup

```bash
# Clone and enter the project
git clone <repository-url>
cd pwdocs

# Run the setup script
./setup.sh

# Or manual setup:
pip install -r requirements.txt
export OPENROUTER_API_KEY="your-key-here"
echo 'export OPENROUTER_API_KEY="your-key-here"' >> ~/.bashrc
```

### 3. VS Code Integration

Open the project in VS Code from WSL:
```bash
code .
```

This will:
- Install recommended extensions automatically
- Configure Python formatting and linting
- Set up development tasks
- Enable WSL integration
- Hide clutter files (dotfiles, venv, gitignored files) in explorer

**Toggle hidden files visibility**: `Ctrl+Shift+P` → "Files: Toggle Excluded Files"

## Daily Workflow

### Starting Development
1. Open WSL terminal
2. Navigate to project: `cd ~/dev/pwdocs`
3. Open VS Code: `code .`
4. Start aider: `aider` (or use VS Code task)

### Making Changes
1. Use aider for AI-assisted editing
2. Format code automatically (on save) or manually: `black .`
3. Check for issues: `flake8 .`
4. Commit changes with descriptive messages

### Code Quality
The project enforces code quality through:
- **Black**: Automatic Python code formatting
- **Flake8**: Style guide enforcement
- **MyPy**: Type checking
- **VS Code**: Real-time linting and formatting

## Tools and Commands

### Aider (AI Assistant)
```bash
aider                    # Interactive AI coding session
aider file1.md file2.py  # Work on specific files
aider --help            # View all options
```

### Code Formatting
```bash
black .                 # Format all Python files
flake8 .               # Check style compliance
mypy .                 # Type checking
```

### VS Code Tasks
Access via `Ctrl+Shift+P` → "Tasks: Run Task":
- **Install Dependencies**: Runs `pip install -r requirements.txt`
- **Start Aider**: Launches aider in terminal
- **Format Code**: Runs black and flake8

### Git Integration
```bash
# Use VS Code's integrated git or command line:
git checkout -b feature/my-feature
git add .
git commit -m "Add new feature"
git push origin feature/my-feature
```

## Project Structure

```
pwdocs/
├── setup.sh                    # Setup script for new environments
├── requirements.txt             # Python dependencies
├── QUICK_REFERENCE.md          # Command reference
├── DEV_SETUP.md               # This file
│
├── .vscode/                    # VS Code configuration
│   ├── settings.json          # Python, formatting, WSL settings
│   ├── tasks.json             # Development tasks
│   └── extensions.json        # Recommended extensions
│
├── Claude-Docs/               # AI-generated documentation
├── planning/                  # Project planning documents
├── scripts/                   # Automation scripts
└── templates/                 # Document templates
```

## Troubleshooting

### Common Issues

**VS Code can't find Python**:
- Check `.vscode/settings.json` has correct Python path
- Verify Python installation: `which python3`

**Aider command not found**:
```bash
pip install --upgrade aider-chat
source ~/.bashrc
```

**Docker not accessible**:
- Ensure Docker Desktop is running
- Check WSL integration is enabled in Docker Desktop settings
- Test: `docker --version`

**Git issues**:
```bash
# Configure git if not already done
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Permission issues**:
```bash
# Common WSL permission fix
sudo chown -R $USER:$USER /home/$USER/dev/
```

### Performance Tips

1. **Keep projects on WSL filesystem** (not Windows drives)
2. **Use VS Code's WSL integration** instead of Windows VS Code
3. **Configure Docker Desktop** for optimal WSL2 performance
4. **Use .gitignore** to exclude unnecessary files from indexing

## Migration Notes

### Changes from Codespaces Setup
- ✅ Removed `.devcontainer/` configuration
- ✅ Removed Codespaces-specific documentation
- ✅ Updated VS Code settings for local development
- ✅ Added WSL-specific troubleshooting
- ✅ Created setup script for easy installation
- ✅ Optimized gitignore for local development

### Benefits of WSL Setup
- **Better performance**: No container overhead
- **Native development**: Direct access to system resources
- **Docker integration**: Full Docker Desktop integration
- **Persistence**: No auto-suspend like Codespaces
- **Customization**: Full control over development environment
