# Setup Scripts

This directory contains setup and configuration scripts for the PlotWeaver documentation project.

## Files

**Scripts:**
- **`setup.sh`** - Main setup script that creates virtual environment, installs dependencies, and optionally sets up git aliases
- **`setup-git-aliases.sh`** - Installs git aliases to ~/.bashrc for permanent use
- **`.git-aliases`** - Git aliases definitions that can be sourced for temporary use

**Documentation:**
- **`DEV_SETUP.md`** - Comprehensive development environment guide
- **`GIT_ALIASES_GUIDE.md`** - Git aliases usage and troubleshooting
- **`MIGRATION_SUMMARY.md`** - Documentation of Codespaces → WSL migration

## Usage

```bash
# Full project setup
./.setup/setup.sh

# Git aliases only
./.setup/setup-git-aliases.sh

# Load git aliases for current session
source .setup/.git-aliases
```

## Quick Start

For new development environments, just run:
```bash
./.setup/setup.sh
```

This will handle everything you need to get started with the project.
