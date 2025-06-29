#!/usr/bin/env python3
"""Script to manage issue status changes and moves to Closed folders."""

import os
import sys
import shutil
from datetime import datetime
from Processors.shared_utils import ensure_directory, clean_title_for_filename, get_content_root

class IssueStatusManager:
    def __init__(self):
        self.base_dir = os.path.join(get_content_root(), 'Issues')
        self.closed_dir = os.path.join(self.base_dir, 'Closed')
        
        # Mapping of source directories to their closed destinations
        self.path_mapping = {
            'features-proposed': 'Features-Not-Planned',
            'bugs': 'Bugs',
            'questions': 'Questions'
        }
    
    def _get_issue_path(self, issue_number, source_type):
        """Find issue directory given the number and type."""
        source_dir = os.path.join(self.base_dir, source_type)
        if not os.path.exists(source_dir):
            return None
            
        for d in os.listdir(source_dir):
            if d.startswith(str(issue_number) + '-'):
                return os.path.join(source_dir, d)
        return None
    
    def _update_status_file(self, status_path, new_status, reason=None):
        """Update the status.md file with closure information."""
        try:
            with open(status_path, 'r') as f:
                content = f.read()
            
            # Update status
            if '- Status:' in content:
                content = content.replace('Status: Proposal', f'Status: {new_status}')
                content = content.replace('Status: Open', f'Status: {new_status}')
            else:
                content += f'\n- Status: {new_status}\n'
            
            # Add closure timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            content += f'\n## Closure Information\n'
            content += f'- Closed: {timestamp}\n'
            if reason:
                content += f'- Reason: {reason}\n'
            
            with open(status_path, 'w') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"❌ Error updating status file: {e}")
            return False

    def move_to_closed(self, issue_number, source_type, reason=None):
        """Move an issue to its appropriate Closed folder."""
        if source_type not in self.path_mapping:
            print(f"❌ Error: Invalid source type '{source_type}'")
            print(f"Valid types: {', '.join(self.path_mapping.keys())}")
            return False
        
        # Find issue directory
        source_path = self._get_issue_path(issue_number, source_type)
        if not source_path:
            print(f"❌ Error: Issue #{issue_number} not found in {source_type}")
            return False
        
        # Determine target directory
        target_dir = os.path.join(self.closed_dir, self.path_mapping[source_type])
        ensure_directory(target_dir)
        
        # Get directory name and create target path
        dir_name = os.path.basename(source_path)
        target_path = os.path.join(target_dir, dir_name)
        
        # Check if already closed
        if os.path.exists(target_path):
            print(f"❌ Error: Issue already exists in closed folder: {target_path}")
            return False
        
        # Update status before moving
        status_path = os.path.join(source_path, 'status.md')
        if os.path.exists(status_path):
            if not self._update_status_file(status_path, 'Closed', reason):
                return False
        
        # Move to closed directory
        try:
            shutil.move(source_path, target_path)
            print(f"✅ Moved issue #{issue_number} to Closed/{self.path_mapping[source_type]}")
            print(f"📍 New location: {target_path}")
            return True
        except Exception as e:
            print(f"❌ Error moving issue: {e}")
            return False
    
    def move_to_other(self, issue_number, source_type, reason=None):
        """Move an issue to the Closed/Other folder."""
        source_path = self._get_issue_path(issue_number, source_type)
        if not source_path:
            print(f"❌ Error: Issue #{issue_number} not found in {source_type}")
            return False
        
        target_dir = os.path.join(self.closed_dir, 'Other')
        ensure_directory(target_dir)
        
        dir_name = os.path.basename(source_path)
        target_path = os.path.join(target_dir, dir_name)
        
        # Update status before moving
        status_path = os.path.join(source_path, 'status.md')
        if os.path.exists(status_path):
            if not self._update_status_file(status_path, 'Closed', reason):
                return False
        
        try:
            shutil.move(source_path, target_path)
            print(f"✅ Moved issue #{issue_number} to Closed/Other")
            print(f"📍 New location: {target_path}")
            return True
        except Exception as e:
            print(f"❌ Error moving issue: {e}")
            return False

def print_usage():
    print("Usage:")
    print("1. Close issue:")
    print("   issue_status_manager.py close <issue_number> <type> [reason]")
    print("   Types: features-proposed, bugs, questions")
    print("")
    print("2. Move to Other:")
    print("   issue_status_manager.py other <issue_number> <type> [reason]")
    print("")
    print("Examples:")
    print("  Close feature:")
    print("    issue_status_manager.py close 42 features-proposed 'Not aligned with roadmap'")
    print("")
    print("  Move to Other:")
    print("    issue_status_manager.py other 42 bugs 'Duplicate of #43'")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print_usage()
        sys.exit(1)
    
    action = sys.argv[1]
    try:
        issue_number = int(sys.argv[2])
    except ValueError:
        print("❌ Error: Issue number must be an integer")
        sys.exit(1)
        
    issue_type = sys.argv[3]
    reason = ' '.join(sys.argv[4:]) if len(sys.argv) > 4 else None
    
    manager = IssueStatusManager()
    
    if action == 'close':
        success = manager.move_to_closed(issue_number, issue_type, reason)
    elif action == 'other':
        success = manager.move_to_other(issue_number, issue_type, reason)
    else:
        print(f"❌ Error: Invalid action '{action}'")
        print_usage()
        sys.exit(1)
    
    if not success:
        sys.exit(1)