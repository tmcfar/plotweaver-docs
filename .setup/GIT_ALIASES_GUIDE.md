# Git Aliases Guide

## Setup

```bash
# Load for current session
source .setup/.git-aliases

# Install permanently 
./.setup/setup-git-aliases.sh
source ~/.bashrc
```

## Test

```bash
gs          # git status
gl          # git log
ghelp       # show all aliases
```

## Most Useful Aliases

**Daily workflow:**
```bash
gs              # git status
ga .            # git add all
gcm "message"   # git commit -m "message"
gp              # git push
gpl             # git pull
```

**Branching:**
```bash
gcb branch      # git checkout -b branch
gco main        # git checkout main
gb              # git branch
gm branch       # git merge branch
```

**History:**
```bash
gl              # git log --oneline (last 10)
glg             # git log --graph (pretty)
gd              # git diff
gds             # git diff --staged
```

**Quick doc update:**
```bash
gdoc            # git add . && git commit -m "Update documentation" && git push
```

## Advanced

```bash
gst             # git stash
gstp            # git stash pop
grh             # git reset HEAD
grhh            # git reset --hard HEAD
gclean          # git clean -fd
```

## Help

```bash
ghelp           # show all git aliases
git --help      # standard git help
```

## Issues

**Aliases not working?**
1. Run `source ~/.bashrc`
2. Restart terminal
3. Check conflicts: `which gs` (ghostscript conflicts are common)

**Remove aliases:**
- Edit `~/.bashrc` and delete Git Aliases section
- Or restore backup: `~/.bashrc.backup.YYYYMMDD_HHMMSS`

**Note:** Some systems have `gs` (ghostscript) pre-installed. This is a common source of confusion for new users who expect git aliases to work immediately.
