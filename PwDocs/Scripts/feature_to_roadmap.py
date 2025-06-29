#!/usr/bin/env python3
"""Script to move approved features to the roadmap directory."""

import os
import sys
import shutil
from datetime import datetime
from Processors.shared_utils import ensure_directory, get_content_root

def update_status_file(status_path):
    """Update the status.md file to reflect roadmap inclusion."""
    with open(status_path, 'r') as f:
        content = f.read()
    
    # Update Roadmap Ready status
    content = content.replace('Roadmap Ready: No', 'Roadmap Ready: Yes')
    
    # Add migration timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    roadmap_section = '## Roadmap Integration'
    if roadmap_section in content:
        content = content.replace(
            roadmap_section,
            f'## Roadmap Integration\nMoved to roadmap: {timestamp}'
        )
    
    with open(status_path, 'w') as f:
        f.write(content)

def move_to_roadmap(feature_number):
    """Move an approved feature to the roadmap directory."""
    features_dir = os.path.join(get_content_root(), 'Issues', 'Features-Proposed')
    roadmap_dir = 'content/planning/roadmap'
    
    # Find feature directory
    feature_dir = None
    for d in os.listdir(features_dir):
        if d.startswith(str(feature_number) + '-'):
            feature_dir = d
            break
    
    if not feature_dir:
        print(f"❌ Error: Feature #{feature_number} not found")
        sys.exit(1)
    
    source_path = os.path.join(features_dir, feature_dir)
    target_path = os.path.join(roadmap_dir, feature_dir)
    
    # Check if feature exists
    if not os.path.exists(source_path):
        print(f"❌ Error: Feature directory not found: {source_path}")
        sys.exit(1)
    
    # Check if already in roadmap
    if os.path.exists(target_path):
        print(f"❌ Error: Feature already exists in roadmap: {target_path}")
        sys.exit(1)
    
    # Update status.md
    status_path = os.path.join(source_path, 'status.md')
    if os.path.exists(status_path):
        update_status_file(status_path)
    
    # Move to roadmap directory
    ensure_directory(roadmap_dir)
    shutil.move(source_path, target_path)
    
    print(f"✅ Moved feature #{feature_number} to roadmap")
    print(f"📍 New location: {target_path}")
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: feature_to_roadmap.py <feature_number>")
        print("Example: feature_to_roadmap.py 42")
        sys.exit(1)
    
    try:
        feature_number = int(sys.argv[1])
    except ValueError:
        print("❌ Error: Feature number must be an integer")
        sys.exit(1)
    
    move_to_roadmap(feature_number)