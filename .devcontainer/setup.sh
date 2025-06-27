#!/bin/bash

# PlotWeaver Documentation - Codespaces Setup Script
set -e

echo "🚀 Setting up PlotWeaver Documentation environment..."

# Update system packages
echo "📦 Updating system packages..."
sudo apt-get update -qq

# Install Python development tools globally
echo "🐍 Installing Python development tools..."
pip3 install --user --upgrade pip
pip3 install --user aider-chat black flake8 mypy pytest

# Add user bin to PATH if not already there
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    export PATH="$HOME/.local/bin:$PATH"
fi

# Create useful aliases
echo "⚡ Setting up aliases..."
cat >> ~/.bashrc << 'EOF'

# PlotWeaver Documentation aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias aider-docs='cd /workspaces/plotweaver-docs && aider'
alias lint-check='black --check --diff . && flake8 . && mypy .'
alias lint-fix='black . && flake8 . && mypy .'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline -10'
EOF

# Verify installations
echo "🔍 Verifying installations..."
python3 --version
pip3 --version
aider --version || echo "⚠️  Aider not in PATH yet - restart terminal or source ~/.bashrc"

# Set up git if not already configured
if ! git config user.name > /dev/null 2>&1; then
    echo "📝 Git user not configured. You'll need to run:"
    echo "   git config --global user.name 'Your Name'"
    echo "   git config --global user.email 'your.email@example.com'"
fi

# Clean up any existing venv from previous setup
if [ -d "/workspaces/plotweaver-docs/.venv" ]; then
    echo "🧹 Cleaning up old virtual environment..."
    rm -rf "/workspaces/plotweaver-docs/.venv"
fi

echo "✅ Setup complete! Your PlotWeaver Documentation environment is ready."
echo ""
echo "🎯 Quick start:"
echo "   • Run 'aider-docs' to start aider in this project"
echo "   • Run 'lint-check' to check code formatting"
echo "   • Run 'lint-fix' to auto-format code"
echo ""
echo "💡 Don't forget to set your OPENROUTER_API_KEY environment variable!"
echo "   You can add it to Codespaces secrets for automatic loading."
