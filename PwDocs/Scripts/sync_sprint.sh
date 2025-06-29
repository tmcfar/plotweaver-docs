#!/bin/bash

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PWDOCS_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$PWDOCS_DIR/config.json"

# Function to read JSON value
get_json_value() {
    local key=$1
    local config_file=$2
    python3 -c "import json; f=open('$config_file'); c=json.load(f); print(c$key)" 2>/dev/null
}

# Get configured paths
WSL_PW_DIR=$(get_json_value "['plotweaver']['wsl_path']" "$CONFIG_FILE")
DOCS_DIR=$(get_json_value "['plotweaver']['docs_dir']" "$CONFIG_FILE")

if [ -z "$WSL_PW_DIR" ]; then
    echo "❌ Error: PlotWeaver WSL path not configured"
    echo "Run config_manager.sh to set up paths"
    exit 1
fi

# Source and destination files
SPRINT_SOURCE="$PWDOCS_DIR/../Content/Planning/Sprint.md"
SPRINT_DEST="$WSL_PW_DIR/$DOCS_DIR/Sprint.md"

# Check if source exists
if [ ! -f "$SPRINT_SOURCE" ]; then
    echo "❌ Error: Sprint document not found at $SPRINT_SOURCE"
    exit 1
fi

# Create destination directory if it doesn't exist
dest_dir="$(dirname "$SPRINT_DEST")"
if ! mkdir -p "$dest_dir" 2>/dev/null; then
    echo "❌ Error: Could not create destination directory: $dest_dir"
    echo "  Check permissions and path validity"
    exit 1
fi

# Copy the file
if cp "$SPRINT_SOURCE" "$SPRINT_DEST" 2>/dev/null; then
    echo "✅ Sprint document synced to PlotWeaver project"
    echo "📍 Location: $SPRINT_DEST"
else
    echo "❌ Error syncing sprint document"
    echo "  From: $SPRINT_SOURCE"
    echo "  To: $SPRINT_DEST"
    echo "Check file permissions and path validity"
    exit 1
fi

# Verify the copy was successful
if ! cmp -s "$SPRINT_SOURCE" "$SPRINT_DEST"; then
    echo "⚠️ Warning: Verification failed - copied file may be different from source"
    echo "Please verify the file contents manually"
    exit 1
fi