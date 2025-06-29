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
    echo "  source_path       Path to file in PW project (relative to project root)"
    echo "  destination_path  Optional: Path in pwdocs (relative to Content/)"
    echo "                    If not provided, file will go to Content/Intake/"
    echo ""
    echo "Examples:"
    echo "  $(basename "$0") docs/architecture/specs/API_REFERENCE.md"
    echo "  $(basename "$0") docs/planning/roadmap.md Planning/Roadmap/roadmap.md"
    exit 1
}

# Check arguments
if [ $# -eq 0 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    show_usage
fi

# Get source path
SOURCE_PATH="$1"
# Remove leading slash if present
SOURCE_PATH="${SOURCE_PATH#/}"

# Get destination path (use Intake/ if not provided)
if [ -n "$2" ]; then
    DEST_PATH="$2"
    # Remove leading slash if present
    DEST_PATH="${DEST_PATH#/}"
else
    # Extract filename from source path
    FILENAME=$(basename "$SOURCE_PATH")
    DEST_PATH="Intake/$FILENAME"
fi

# Get configured PW project path
WSL_PW_DIR=$(get_json_value "['plotweaver']['wsl_path']" "$CONFIG_FILE")

if [ -z "$WSL_PW_DIR" ]; then
    echo "❌ Error: PlotWeaver WSL path not configured"
    echo "Run config_manager.sh to set up paths"
    exit 1
fi

# Full paths
SOURCE_FILE="$WSL_PW_DIR/$SOURCE_PATH"
DEST_FILE="$PWDOCS_DIR/../Content/$DEST_PATH"

# Check if source exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "❌ Error: Source file not found: $SOURCE_FILE"
    exit 1
fi

# Create destination directory if needed
DEST_DIR="$(dirname "$DEST_FILE")"
if ! mkdir -p "$DEST_DIR" 2>/dev/null; then
    echo "❌ Error: Could not create destination directory: $DEST_DIR"
    echo "  Check permissions and path validity"
    exit 1
fi

# Copy the file
if cp "$SOURCE_FILE" "$DEST_FILE" 2>/dev/null; then
    echo "✅ File copied successfully"
    echo "📍 From: $SOURCE_FILE"
    echo "📍 To: $DEST_FILE"
else
    echo "❌ Error copying file"
    echo "  From: $SOURCE_FILE"
    echo "  To: $DEST_FILE"
    echo "Check file permissions and path validity"
    exit 1
fi