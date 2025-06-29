#!/bin/bash

# Paths
PW_PROJECT="/home/tmcfar/dev/pw"
PWDOCS_PROJECT="/home/tmcfar/dev/pwdocs"
SOURCE_FILE="$PW_PROJECT/docs/planning/PROJECT_STATE.md"
DEST_DIR="$PWDOCS_PROJECT/Technical/Updates"

# Generate timestamp
timestamp=$(date +%Y%m%d-%H%M)
DEST_FILE="$DEST_DIR/PROJECT_STATE-${timestamp}.md"

# Check if source exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "❌ Error: PROJECT_STATE.md not found in pw project"
    echo "Expected location: $SOURCE_FILE"
    exit 1
fi

# Create destination directory if needed
mkdir -p "$DEST_DIR"

# Copy new file with timestamp
if cp "$SOURCE_FILE" "$DEST_FILE"; then
    echo "✅ State document copied with timestamp"
    echo "📍 From: $SOURCE_FILE"
    echo "📍 To: $DEST_FILE"
    
    # Create symlink to latest
    ln -sf "$DEST_FILE" "$DEST_DIR/PROJECT_STATE-latest.md"
    echo "🔗 Updated latest symlink"
else
    echo "❌ Error copying file"
    echo "  From: $SOURCE_FILE"
    echo "  To: $DEST_FILE"
    exit 1
fi