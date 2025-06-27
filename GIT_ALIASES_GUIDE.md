# Git Aliases Test and Usage Guide

## 🔧 Installation Complete!

Your git aliases have been successfully added to `~/.bashrc`. 

## 🔄 Activation

To use the aliases, you have several options:

```bash
# Option 1: Load for current session (immediate)
source .setup/.git-aliases

# Option 2: Install permanently (adds to ~/.bashrc)
./.setup/setup-git-aliases.sh
source ~/.bashrc

# Option 3: Manual setup
echo 'source ~/path/to/pwdocs/.setup/.git-aliases' >> ~/.bashrc
source ~/.bashrc
```

## ✅ Testing Your Aliases

Run this to test if aliases are working:

```bash
# Test basic git status
gs

# Test git log
gl

# Show all git aliases
ghelp
```

## 📋 Most Useful Aliases

### Daily Workflow
```bash
gs              # git status
ga .            # git add all files
gcm "message"   # git commit with message
gp              # git push
gpl             # git pull
```

### Branch Management
```bash
gcb mybranch    # git checkout -b mybranch
gco main        # git checkout main
gb              # git branch (list all)
gm mybranch     # git merge mybranch
```

### Viewing History
```bash
gl              # git log --oneline (last 10)
glg             # git log --graph (pretty format)
gd              # git diff
gds             # git diff --staged
```

### Quick Documentation Workflow
```bash
gdoc            # Add all, commit "Update documentation", push
                # Equivalent to: git add . && git commit -m "Update documentation" && git push
```

### Advanced Operations
```bash
gst             # git stash
gstp            # git stash pop
grh             # git reset HEAD
grhh            # git reset --hard HEAD
gclean          # git clean -fd
```

## 🆘 Getting Help

```bash
ghelp           # Show all available git aliases
git --help      # Standard git help
```

## 🔧 Customization

To add your own aliases, edit `~/.bashrc` and add lines like:
```bash
alias myalias='git command'
```

Then reload: `source ~/.bashrc`

## 🚨 Troubleshooting

**Aliases not working?**
1. Run: `source ~/.bashrc`
2. Or restart your terminal
3. Check if aliases exist: `alias | grep git`

**Conflict with existing commands?**
- Some systems have `gs` (ghostscript) installed
- Use `which gs` to check conflicts
- Use full git commands if needed

**Want to remove aliases?**
- Edit `~/.bashrc` and remove the Git Aliases section
- Or restore from backup: `~/.bashrc.backup.YYYYMMDD_HHMMSS`
