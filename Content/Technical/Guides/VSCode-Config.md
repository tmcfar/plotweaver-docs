# VS Code Configuration Guide

## 🧹 Clean Explorer View

The VS Code explorer has been configured to hide clutter and show only relevant project files.

### What's Hidden by Default

**System/Cache Files:**
- `.git/` (Git repository metadata)
- `__pycache__/` (Python bytecode cache)
- `.pytest_cache/`, `.mypy_cache/` (Testing/linting cache)
- `.DS_Store`, `Thumbs.db` (OS-specific files)

**Development Environment:**
- `venv/`, `.venv/`, `env/` (Python virtual environments)
- `.env` (Environment variables)
- `.aider*` (Aider AI tool files)
- `node_modules/` (Node.js dependencies)

**Gitignored Files:**
- All files and folders listed in `.gitignore`
- Automatically respects gitignore patterns

### What's Visible

**Core Project Files:**
- `Readme.md`, documentation files
- `Requirements.txt`, configuration files
- Source code directories (`ClaudeDocs/`, `Planning/`, `Scripts/`, `Templates/`)
- Project-specific files

### Toggle Hidden Files

**When you need to see hidden files:**

1. **Command Palette Method:**
   - Press `Ctrl+Shift+P`
   - Type "Files: Toggle Excluded Files"
   - Press Enter

2. **Task Method:**
   - Press `Ctrl+Shift+P`
   - Type "Tasks: Run Task"
   - Select "Show/Hide Dotfiles"

3. **Settings Method:**
   - Open VS Code settings (`Ctrl+,`)
   - Search for "files.exclude"
   - Temporarily disable patterns

## 🔍 Search Configuration

**Search also respects gitignore:**
- Won't search in virtual environments
- Skips cache directories
- Ignores build artifacts
- Uses `.gitignore` patterns

**Search Settings:**
- `search.useIgnoreFiles: true` - Respects .gitignore
- `search.useGlobalIgnoreFiles: true` - Respects global gitignore
- Custom exclude patterns for common dev files

## 🎯 Benefits

**Cleaner Development:**
- ✅ Focus on project files, not clutter
- ✅ Faster file navigation
- ✅ Reduced visual noise
- ✅ Better performance (fewer files to index)

**Maintained Functionality:**
- ✅ Can still access hidden files when needed
- ✅ Git operations work normally
- ✅ Search is more relevant
- ✅ Easy to toggle visibility

## 🔧 Customization

**To show specific dotfiles permanently:**

Edit `.vscode/settings.json`:
```json
{
  "files.exclude": {
    "**/.git": true,
    "**/.env": false,  // This would show .env files
    // ... other patterns
  }
}
```

**To add more exclusions:**
```json
{
  "files.exclude": {
    "**/logs": true,        // Hide logs directory
    "**/*.log": true,       // Hide all .log files
    "**/temp": true         // Hide temp directory
  }
}
```

## 🚨 Troubleshooting

**Can't find a file you know exists?**
1. Check if it's in `.gitignore`
2. Toggle excluded files visibility
3. Use `Ctrl+P` to open files by name (works regardless of visibility)

**Want to permanently show certain hidden files?**
- Edit the `files.exclude` settings in `.vscode/settings.json`
- Set the pattern to `false` instead of `true`

**Performance issues?**
- The current settings should improve performance
- If you need to see everything, use the toggle feature temporarily
