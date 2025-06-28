# PlotWeaver Documentation - Dev Container

This folder contains the configuration for running the project in a VS Code Dev Container.

## Features

- **Python 3.12** base image
- **Automatic environment setup** on container creation
- **Pre-installed tools**: git, GitHub CLI, aider
- **Automatic venv activation** in all terminals
- **VS Code extensions** pre-configured
- **Git config and SSH keys** mounted from host

## Usage

### Option 1: Open in Dev Container (Recommended)

1. Install the "Dev Containers" extension in VS Code
2. Open the command palette (Ctrl/Cmd+Shift+P)
3. Run "Dev Containers: Reopen in Container"
4. Wait for the container to build and setup to complete
5. The environment will be ready with venv activated

### Option 2: Open Workspace File

1. Open VS Code
2. File → Open Workspace from File
3. Select `pwdocs.code-workspace`
4. The setup task will run automatically on first open
5. All new terminals will have venv activated

### Option 3: Manual Setup

If you prefer not to use dev containers:

```bash
# Run the setup script
./.setup/setup.sh

# Activate the virtual environment
source venv/bin/activate

# Start coding
aider
```

## Environment Variables

Add your API keys to `.env` file (created automatically):

```bash
OPENROUTER_API_KEY=your-key-here
```

Or set them in VS Code:
- File → Preferences → Settings
- Search for "terminal.integrated.env"
- Add your environment variables

## Troubleshooting

### Container won't start
- Ensure Docker Desktop is running
- Check Docker has WSL 2 integration enabled
- Try "Dev Containers: Rebuild Container"

### Python/pip not found
- The venv should activate automatically
- If not, run: `source /workspaces/pwdocs/venv/bin/activate`

### Git/SSH issues
- Ensure your host has git configured
- Check ~/.ssh folder has your keys
- Keys are mounted read-only in the container