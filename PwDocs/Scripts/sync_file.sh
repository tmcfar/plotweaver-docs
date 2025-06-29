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

# Function to show usage
show_usage() {
    echo "Usage: $(basename "$0") <source_path> [destination_path]"
    echo ""
    echo "Arguments:"
    echo "  source_path       Path to source file (relative to Content/)"
    echo "  destination_path  Optional: Path in PW project (relative to project root)"
    echo "                    If not provided, uses same path as source"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") Planning/Sprint.md docs/planning/Sprint.md"
    echo "  $(basename "$0") Technical/API/endpoints.md docs/api/endpoints.md"
    echo "  $(basename "$0") Planning/Sprint.md    # Will sync to pw/Planning/Sprint.md"
}

# Check arguments
if [ $# -eq 0 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    show_usage
    exit 1
fi

# Get source path
SOURCE_PATH="$1"
# Remove leading slash if present
SOURCE_PATH="${SOURCE_PATH#/}"

# Get destination path (use source path if not provided)
DEST_PATH="${2:-$SOURCE_PATH}"
# Remove leading slash if present
DEST_PATH="${DEST_PATH#/}"

# Get configured PW project path
WSL_PW_DIR=$(get_json_value "['plotweaver']['wsl_path']" "$CONFIG_FILE")

if [ -z "$WSL_PW_DIR" ]; then
    echo "❌ Error: PlotWeaver WSL path not configured"
    echo "Run config_manager.sh to set up paths"
    exit 1
fi

# Full paths
SOURCE_FILE="$PWDOCS_DIR/../Content/$SOURCE_PATH"
DEST_FILE="$WSL_PW_DIR/$DEST_PATH"

# Check if source exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "❌ Error: Source file not found: $SOURCE_FILE"
    exit 1
fi

# Create destination directory if it doesn't exist
DEST_DIR="$(dirname "$DEST_FILE")"
if ! mkdir -p "$DEST_DIR" 2>/dev/null; then
    echo "❌ Error: Could not create destination directory: $DEST_DIR"
    echo "  Check permissions and path validity"
    exit 1
fi

# Check if destination exists
if [ -f "$DEST_FILE" ]; then
    echo "ℹ️ Overwriting existing file: $DEST_FILE"
fi

# Copy the file (overwrite if exists)
if cp -f "$SOURCE_FILE" "$DEST_FILE" 2>/dev/null; then
    echo "✅ File synced to PlotWeaver project"
    echo "📍 From: $SOURCE_FILE"
    echo "📍 To: $DEST_FILE"
else
    echo "❌ Error syncing file"
    echo "  From: $SOURCE_FILE"
    echo "  To: $DEST_FILE"
    echo "Check file permissions and path validity"
    exit 1
fi

# Verify the copy was successful
if ! cmp -s "$SOURCE_FILE" "$DEST_FILE"; then
    echo "⚠️ Warning: Verification failed - copied file may be different from source"
    echo "Please verify the file contents manually"
    exit 1
fi