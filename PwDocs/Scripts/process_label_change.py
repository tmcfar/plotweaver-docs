#!/usr/bin/env python3
"""Script to process GitHub label changes."""

import os
import sys
import json
from issue_status_manager import IssueStatusManager

def process_label_change(issue_number, old_labels, new_labels, issue_title):
    """Process changes in GitHub labels."""
    
    # Convert label lists from JSON if needed
    if isinstance(old_labels, str):
        old_labels = json.loads(old_labels)
    if isinstance(new_labels, str):
        new_labels = json.loads(new_labels)
    
    # Extract label names
    old_label_names = set(label.get('name', '') for label in old_labels)
    new_label_names = set(label.get('name', '') for label in new_labels)
    
    # Check for status changes
    manager = IssueStatusManager()
    
    # Handle 'wontfix' label
    if 'wontfix' in new_label_names and 'wontfix' not in old_label_names:
        # Determine issue type
        if 'feature' in old_label_names or 'enhancement' in old_label_names:
            manager.move_to_closed(issue_number, 'features-proposed', 'Marked as wontfix')
        elif 'bug' in old_label_names:
            manager.move_to_closed(issue_number, 'bugs', 'Marked as wontfix')
        elif 'question' in old_label_names:
            manager.move_to_closed(issue_number, 'questions', 'Marked as wontfix')
    
    # Handle 'duplicate' label
    if 'duplicate' in new_label_names and 'duplicate' not in old_label_names:
        # Move to Other for duplicates
        if 'feature' in old_label_names or 'enhancement' in old_label_names:
            manager.move_to_other(issue_number, 'features-proposed', 'Duplicate issue')
        elif 'bug' in old_label_names:
            manager.move_to_other(issue_number, 'bugs', 'Duplicate issue')
        elif 'question' in old_label_names:
            manager.move_to_other(issue_number, 'questions', 'Duplicate issue')
    
    # Handle closing via 'invalid' label
    if 'invalid' in new_label_names and 'invalid' not in old_label_names:
        if 'feature' in old_label_names or 'enhancement' in old_label_names:
            manager.move_to_other(issue_number, 'features-proposed', 'Marked as invalid')
        elif 'bug' in old_label_names:
            manager.move_to_other(issue_number, 'bugs', 'Marked as invalid')
        elif 'question' in old_label_names:
            manager.move_to_other(issue_number, 'questions', 'Marked as invalid')

if __name__ == '__main__':
    # Get environment variables
    issue_number = os.environ.get('ISSUE_NUMBER')
    issue_title = os.environ.get('ISSUE_TITLE')
    old_labels_json = os.environ.get('OLD_LABELS', '[]')
    new_labels_json = os.environ.get('NEW_LABELS', '[]')
    
    if not all([issue_number, issue_title]):
        print("❌ Error: Required environment variables not set")
        print("Required: ISSUE_NUMBER, ISSUE_TITLE")
        print("Optional: OLD_LABELS, NEW_LABELS")
        sys.exit(1)
    
    try:
        issue_number = int(issue_number)
    except ValueError:
        print("❌ Error: ISSUE_NUMBER must be an integer")
        sys.exit(1)
    
    process_label_change(issue_number, old_labels_json, new_labels_json, issue_title)