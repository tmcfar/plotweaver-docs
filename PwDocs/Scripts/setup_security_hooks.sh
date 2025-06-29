#!/bin/bash
# Setup security pre-commit hooks

echo "🔒 Setting up security pre-commit hooks..."

# Install the pre-commit hook
if [ -f .githooks/pre-commit ]; then
    cp .githooks/pre-commit .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    echo "✅ Pre-commit hook installed"
else
    echo "❌ Pre-commit hook file not found"
    exit 1
fi

# Test the security linter
echo "🧪 Testing security linter..."
python scripts/security-linter.py

linter_exit=$?
if [ $linter_exit -eq 0 ]; then
    echo "✅ Security linter working - no issues found"
elif [ $linter_exit -eq 2 ]; then
    echo "✅ Security linter working - medium issues found (acceptable)"
else
    echo "❌ Security linter found HIGH severity issues"
    echo "Fix these before continuing"
    exit 1
fi

echo "🎉 Security hooks setup complete!"
echo ""
echo "Usage:"
echo "  python scripts/security-linter.py    # Manual run"
echo "  git commit                           # Auto-runs on commit"