#!/usr/bin/env python3
"""Bi-directional label synchronization between local content and GitHub issues."""

import os
import sys
import json
import subprocess
from datetime import datetime
from issue_status_manager import IssueStatusManager

class LabelSyncManager:
    def __init__(self):
        self.status_manager = IssueStatusManager()
        
        # Label mappings between local states and GitHub labels
        self.local_to_github = {
            'Closed/Features-Not-Planned': ['wontfix'],
            'Closed/Other/duplicate': ['duplicate'],
            'Closed/Other/invalid': ['invalid'],
            'Closed/Bugs': ['closed'],
            'Closed/Questions': ['closed'],
            'content/planning/roadmap': ['roadmap-approved']
        }
        
        self.github_to_local = {
            'wontfix': 'Closed/Features-Not-Planned',
            'duplicate': 'Closed/Other',
            'invalid': 'Closed/Other',
            'roadmap-approved': 'content/planning/roadmap'
        }

    def _run_gh_command(self, args):
        """Run a GitHub CLI command and return the result."""
        try:
            result = subprocess.run(['gh'] + args, 
                                 capture_output=True, 
                                 text=True, 
                                 check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"❌ GitHub CLI error: {e.stderr}")
            return None

    def sync_to_github(self, issue_number, local_path, reason=None):
        """Sync local state changes to GitHub labels."""
        # Determine labels based on local path
        labels_to_add = []
        labels_to_remove = []
        
        # Find matching labels for the local path
        for local_pattern, gh_labels in self.local_to_github.items():
            if local_pattern in local_path:
                labels_to_add.extend(gh_labels)
                
                # If moved to Closed, add 'closed' label
                if 'Closed/' in local_path:
                    labels_to_add.append('closed')
        
        if not labels_to_add:
            print("ℹ️ No GitHub labels to sync for this path")
            return True
            
        # Remove duplicate labels
        labels_to_add = list(set(labels_to_add))
        
        # Add labels
        for label in labels_to_add:
            result = self._run_gh_command([
                'issue', 'edit', str(issue_number),
                '--add-label', label
            ])
            if result is None:
                return False
                
        # Add comment if reason provided
        if reason:
            comment = f"Status updated: {reason}"
            result = self._run_gh_command([
                'issue', 'comment', str(issue_number),
                '--body', comment
            ])
            if result is None:
                return False
        
        print(f"✅ Synced local changes to GitHub: Added labels {', '.join(labels_to_add)}")
        return True

    def sync_from_github(self, issue_number, old_labels, new_labels, issue_title):
        """Sync GitHub label changes to local content structure."""
        # Convert label lists from JSON if needed
        if isinstance(old_labels, str):
            old_labels = json.loads(old_labels)
        if isinstance(new_labels, str):
            new_labels = json.loads(new_labels)
        
        # Extract label names
        old_label_names = set(label.get('name', '') for label in old_labels)
        new_label_names = set(label.get('name', '') for label in new_labels)
        
        # Find added labels
        added_labels = new_label_names - old_label_names
        
        for label in added_labels:
            if label in self.github_to_local:
                target_location = self.github_to_local[label]
                
                # Determine issue type from existing labels
                issue_type = None
                if 'feature' in new_label_names or 'enhancement' in new_label_names:
                    issue_type = 'features-proposed'
                elif 'bug' in new_label_names:
                    issue_type = 'bugs'
                elif 'question' in new_label_names:
                    issue_type = 'questions'
                
                if issue_type:
                    if 'duplicate' in new_label_names:
                        self.status_manager.move_to_other(
                            issue_number, issue_type, 
                            f"Marked as duplicate on GitHub"
                        )
                    elif 'invalid' in new_label_names:
                        self.status_manager.move_to_other(
                            issue_number, issue_type,
                            f"Marked as invalid on GitHub"
                        )
                    elif 'wontfix' in new_label_names:
                        self.status_manager.move_to_closed(
                            issue_number, issue_type,
                            f"Marked as wontfix on GitHub"
                        )
                    elif 'roadmap-approved' in new_label_names:
                        # Use existing roadmap script
                        subprocess.run([
                            'python3', 
                            'scripts/feature_to_roadmap.py', 
                            str(issue_number)
                        ])

def print_usage():
    print("Usage:")
    print("1. Sync local changes to GitHub:")
    print("   label_sync_manager.py to-github <issue_number> <local_path> [reason]")
    print("")
    print("2. Sync GitHub changes to local:")
    print("   label_sync_manager.py from-github <issue_number> <old_labels_json> <new_labels_json> <issue_title>")
    print("")
    print("Examples:")
    print("  Sync to GitHub:")
    print("    label_sync_manager.py to-github 42 content/issues/Closed/Features-Not-Planned 'Not aligned with strategy'")
    print("")
    print("  Sync from GitHub:")
    print("    label_sync_manager.py from-github 42 \"$OLD_LABELS\" \"$NEW_LABELS\" \"$ISSUE_TITLE\"")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)
    
    action = sys.argv[1]
    try:
        issue_number = int(sys.argv[2])
    except ValueError:
        print("❌ Error: Issue number must be an integer")
        sys.exit(1)
    
    syncer = LabelSyncManager()
    
    if action == 'to-github':
        if len(sys.argv) < 4:
            print_usage()
            sys.exit(1)
        local_path = sys.argv[3]
        reason = ' '.join(sys.argv[4:]) if len(sys.argv) > 4 else None
        success = syncer.sync_to_github(issue_number, local_path, reason)
    
    elif action == 'from-github':
        if len(sys.argv) < 6:
            print_usage()
            sys.exit(1)
        old_labels = sys.argv[3]
        new_labels = sys.argv[4]
        issue_title = sys.argv[5]
        success = syncer.sync_from_github(issue_number, old_labels, new_labels, issue_title)
    
    else:
        print(f"❌ Error: Invalid action '{action}'")
        print_usage()
        sys.exit(1)
    
    if not success:
        sys.exit(1)