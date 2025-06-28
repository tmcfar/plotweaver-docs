#!/bin/bash
set -e

echo "🚀 Setting up PlotWeaver Documentation environment in devcontainer..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
echo "📦 Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Set up git (if not already configured)
if ! git config --global user.name &> /dev/null; then
    echo "⚠️  Git user.name not configured"
    echo "   Run: git config --global user.name \"Your Name\""
fi

if ! git config --global user.email &> /dev/null; then
    echo "⚠️  Git user.email not configured"
    echo "   Run: git config --global user.email \"your.email@example.com\""
fi

# Check for API key
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo ""
    echo "⚠️  OPENROUTER_API_KEY not set"
    echo "   Add it to your VS Code settings or .env file:"
    echo "   File > Preferences > Settings > Remote > Environment Variables"
    echo "   Or create a .env file with: OPENROUTER_API_KEY=your-key-here"
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "📝 Creating .env file template..."
    cat > .env << 'EOF'
# OpenRouter API Key for Aider
# Get your key from: https://openrouter.ai/keys
OPENROUTER_API_KEY=

# Optional: Other API keys
# ANTHROPIC_API_KEY=
# OPENAI_API_KEY=
EOF
    echo "   Created .env file - add your API keys there"
fi

# Set up git aliases if requested
if [ -f ".setup/setup-git-aliases.sh" ]; then
    echo ""
    echo "📝 Git aliases available. Run this to install them:"
    echo "   ./.setup/setup-git-aliases.sh"
fi

echo ""
echo "✅ Devcontainer setup complete!"
echo ""
echo "🎯 Quick start:"
echo "   1. Add your OPENROUTER_API_KEY to .env file"
echo "   2. Open a new terminal (Ctrl+Shift+`)"
echo "   3. Run: aider"
echo ""
echo "The virtual environment is automatically activated in all terminals."