#!/bin/bash

# PlotWeaver Documentation Setup Script for WSL
# Run this script to set up your development environment

set -e  # Exit on any error

echo "🚀 Setting up PlotWeaver Documentation environment..."

# Check if we're in WSL
if ! grep -q microsoft /proc/version 2>/dev/null; then
    echo "⚠️  Warning: This script is optimized for WSL on Windows"
    echo "   It may work on other Linux systems but is not tested"
    read -p "   Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check Python version
echo "📋 Checking Python version..."
python3 --version
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "❌ Python 3.8+ is required"
    exit 1
fi

# Check if we're in a virtual environment
echo "📦 Setting up Python environment..."
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Virtual environment detected: $VIRTUAL_ENV"
    pip install -r requirements.txt
else
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created in ./venv"
    echo "📦 Installing dependencies..."
    ./venv/bin/pip install -r requirements.txt
    echo ""
    echo "⚠️  Virtual environment created!"
    echo "   Activate it with: source venv/bin/activate"
    echo "   Or use: ./venv/bin/aider instead of aider"
fi

# Check if Docker is available
echo "🐳 Checking Docker availability..."
if command -v docker &> /dev/null; then
    if docker info &> /dev/null; then
        echo "✅ Docker is running"
    else
        echo "⚠️  Docker is installed but not running"
        echo "   Please start Docker Desktop"
    fi
else
    echo "⚠️  Docker not found"
    echo "   Install Docker Desktop for Windows with WSL2 backend"
fi

# Check if VS Code is available
echo "📝 Checking VS Code availability..."
if command -v code &> /dev/null; then
    echo "✅ VS Code is available"
else
    echo "⚠️  VS Code not found in PATH"
    echo "   Install VS Code and enable 'code' command in WSL"
fi

# Configure git if not already configured
echo "🔧 Checking Git configuration..."
if ! git config --global user.name &> /dev/null; then
    echo "   Git user.name not set"
    read -p "   Enter your name: " git_name
    git config --global user.name "$git_name"
fi

if ! git config --global user.email &> /dev/null; then
    echo "   Git user.email not set"
    read -p "   Enter your email: " git_email
    git config --global user.email "$git_email"
fi

# Check API key
echo "🔑 Checking API key configuration..."
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "⚠️  OPENROUTER_API_KEY not set"
    echo "   Add this to your ~/.bashrc:"
    echo "   export OPENROUTER_API_KEY=\"your-api-key-here\""
    echo ""
    read -p "   Set API key now? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "   Enter your OpenRouter API key: " api_key
        echo "export OPENROUTER_API_KEY=\"$api_key\"" >> ~/.bashrc
        echo "✅ API key added to ~/.bashrc"
        echo "   Run 'source ~/.bashrc' or restart your terminal"
    fi
else
    echo "✅ OPENROUTER_API_KEY is set"
fi

# Optional: Setup git aliases
echo ""
echo "🔧 Git aliases setup..."
read -p "   Install useful git aliases? (Y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    ./setup-git-aliases.sh
    echo "✅ Git aliases installed"
    echo "   Run 'source ~/.bashrc' to activate them"
else
    echo "   Skipped git aliases setup"
    echo "   Run './setup-git-aliases.sh' later if needed"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. source ~/.bashrc    # Reload your shell config"
echo "2. code .              # Open in VS Code"
echo "3. aider               # Start AI-assisted coding"
echo ""
echo "Available VS Code tasks:"
echo "- Install Dependencies (Ctrl+Shift+P → Tasks: Run Task)"
echo "- Start Aider"
echo "- Format Code"
