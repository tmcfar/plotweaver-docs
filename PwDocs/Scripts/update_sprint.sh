#!/bin/bash

# Paths
PWDOCS_PROJECT="/home/tmcfar/dev/pwdocs"
PW_PROJECT="/home/tmcfar/dev/pw"
SOURCE_DIR="$PWDOCS_PROJECT/Content/Planning"
DEST_DIR="$PW_PROJECT/docs/planning"

# Generate timestamp
timestamp=$(date +%Y%m%d-%H%M)
sprint_file="Sprint-${timestamp}.md"

# Create new sprint doc with timestamp
SOURCE_FILE="$SOURCE_DIR/$sprint_file"
DEST_FILE="$DEST_DIR/Sprint.md"

# Check if we have write permission to create sprint doc
if [ ! -w "$SOURCE_DIR" ]; then
    echo "❌ Error: Cannot write to $SOURCE_DIR"
    exit 1
fi

# Create timestamped sprint doc
if cp "$SOURCE_DIR/Sprint.md" "$SOURCE_FILE" 2>/dev/null; then
    echo "✅ Created new sprint document with timestamp"
    echo "📍 At: $SOURCE_FILE"
    
    # Create symlink to latest
    ln -sf "$sprint_file" "$SOURCE_DIR/Sprint.md"
    echo "🔗 Updated latest symlink"
    
    # Copy to pw project
    if cp "$SOURCE_FILE" "$DEST_FILE"; then
        echo "✅ Sprint document sent to pw project"
        echo "📍 To: $DEST_FILE"
    else
        echo "❌ Error copying to pw project"
        echo "  To: $DEST_FILE"
        exit 1
    fi
else
    echo "❌ Error creating sprint document"
    echo "  At: $SOURCE_FILE"
    exit 1
fi