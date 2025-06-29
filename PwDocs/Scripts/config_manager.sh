#!/bin/bash

# Get the PWDocs root directory
PWDOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_FILE="$PWDOCS_DIR/config.json"

# Function to read JSON value
get_json_value() {
    local key=$1
    local config_file=$2
    python3 -c "import json; f=open('$config_file'); c=json.load(f); print(c$key)" 2>/dev/null
}

# Function to update JSON value
set_json_value() {
    local key=$1
    local value=$2
    local config_file=$3
    
    # Create a temporary Python script
    local tmp_script=$(mktemp)
    cat > "$tmp_script" << EOF
import json
import sys

key = sys.argv[1]
value = sys.argv[2]
config_file = sys.argv[3]

with open(config_file, 'r') as f:
    config = json.load(f)

# Parse the key path (e.g., "['plotweaver']['windows_path']")
keys = [k.strip("'[]") for k in key.split('][')]
current = config
for k in keys[:-1]:
    current = current[k]
current[keys[-1]] = value

with open(config_file, 'w') as f:
    json.dump(config, f, indent=4)
EOF

    python3 "$tmp_script" "$key" "$value" "$config_file"
    rm "$tmp_script"
}

# Function to check if config exists
check_config() {
    if [ ! -f "$CONFIG_FILE" ]; then
        echo "❌ Error: Config file not found at $CONFIG_FILE"
        return 1
    fi
    return 0
}

# Function to initialize config with detected paths
init_config() {
    local win_path=$1
    local wsl_path=$2
    
    if [ ! -f "$CONFIG_FILE" ]; then
        echo "{}" > "$CONFIG_FILE"
    fi
    
    # Update config with detected paths
    set_json_value "['plotweaver']['windows_path']" "$win_path" "$CONFIG_FILE"
    set_json_value "['plotweaver']['wsl_path']" "$wsl_path" "$CONFIG_FILE"
    
    echo "✅ Configuration initialized"
    echo "📍 Paths set:"
    echo "  Windows: $win_path"
    echo "  WSL: $wsl_path"
}

# Function to show current config
show_config() {
    if ! check_config; then
        return 1
    fi
    
    echo "Current Configuration:"
    python3 -c "import json; import sys; f=open('$CONFIG_FILE'); c=json.load(f); print(json.dumps(c, indent=2))"
}

# Function to set a config value
set_config() {
    local key=$1
    local value=$2
    
    if ! check_config; then
        return 1
    fi
    
    set_json_value "$key" "$value" "$CONFIG_FILE"
    echo "✅ Updated $key = $value"
}

# Main command handling
case "$1" in
    "init")
        if [ -z "$2" ] && [ -z "$3" ]; then
            echo "Usage: $0 init [windows_path] <wsl_path>"
            echo "Note: windows_path is optional for WSL-only setups"
            exit 1
        fi
        init_config "$2" "$3"
        ;;
    "show")
        show_config
        ;;
    "set")
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: $0 set <key> <value>"
            echo "Example: $0 set \"['plotweaver']['windows_path']\" \"C:\\Users\\user\\dev\\plotweaver\""
            exit 1
        fi
        set_config "$2" "$3"
        ;;
    *)
        echo "Usage:"
        echo "  $0 init <windows_path> <wsl_path>"
        echo "  $0 show"
        echo "  $0 set <key> <value>"
        exit 1
        ;;
esac