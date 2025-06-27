#!/bin/bash

# Git Aliases Setup Script for PlotWeaver Documentation
# Run this script to add useful git aliases to your ~/.bashrc

echo "🔧 Setting up Git aliases..."

# Create backup of existing bashrc
if [ -f ~/.bashrc ]; then
    cp ~/.bashrc ~/.bashrc.backup.$(date +%Y%m%d_%H%M%S)
    echo "✅ Backed up existing .bashrc"
fi

# Add source line for git aliases to bashrc
echo "" >> ~/.bashrc
echo "# Source git aliases for PlotWeaver project" >> ~/.bashrc
echo "if [ -f $PWD/.git-aliases ]; then" >> ~/.bashrc
echo "    source $PWD/.git-aliases" >> ~/.bashrc
echo "fi" >> ~/.bashrc

echo "✅ Git aliases configured in ~/.bashrc"
echo ""
echo "🔄 To use the aliases immediately, run:"
echo "   source ~/.bashrc"
echo "   # OR"
echo "   source .git-aliases"
echo ""
echo "📋 Most useful aliases:"
echo "   gs     - git status"
echo "   ga .   - git add all"
echo "   gcm    - git commit -m 'message'"
echo "   gp     - git push"
echo "   gcb    - git checkout -b 'branch'"
echo "   gl     - git log (last 10 commits)"
echo "   gdoc   - quick doc commit (add all, commit, push)"
echo ""
echo "🆘 Type 'ghelp' to see all available git aliases"
echo ""
echo "🧪 Test now: source .git-aliases && gs"
