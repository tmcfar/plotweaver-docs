#!/usr/bin/env python3
import os
import json
import sys
from processors.shared_utils import get_issue_type, validate_issue_number
from processors.feature_processor import process_feature_proposal
from processors.current_state_processor import process_current_state_update
from processors.bug_processor import process_bug_report
from processors.question_processor import process_question

# Get environment variables
api_key = os.environ.get('OPENROUTER_API_KEY')
issue_number = os.environ.get('ISSUE_NUMBER')
issue_title = os.environ.get('ISSUE_TITLE')
issue_body = os.environ.get('ISSUE_BODY', '')
issue_labels_json = os.environ.get('ISSUE_LABELS', '[]')
event_type = os.environ.get('EVENT_TYPE')

# Parse labels from JSON
try:
    issue_labels = json.loads(issue_labels_json)
except json.JSONDecodeError:
    issue_labels = []

# Validate required environment variables
if not api_key:
    print("ERROR: OPENROUTER_API_KEY environment variable not set")
    sys.exit(1)
if not issue_number or not issue_title:
    print("ERROR: Required issue environment variables not set")
    sys.exit(1)

# Validate issue number
try:
    issue_number = validate_issue_number(issue_number)
except ValueError as e:
    print(f"ERROR: {e}")
    sys.exit(1)

# Determine issue type from labels with title fallback
issue_type = get_issue_type(issue_labels, issue_title)

print(f"Processing issue #{issue_number}: {issue_title}")
print(f"Labels: {issue_labels}")
print(f"Detected type: {issue_type}")

if event_type == "opened":
    success = True
    processors_run = []
    
    # Handle multiple types (list) or single type (string)
    types_to_process = issue_type if isinstance(issue_type, list) else [issue_type]
    is_duplicate = len(types_to_process) > 1
    
    for process_type in types_to_process:
        other_types = [t for t in types_to_process if t != process_type] if is_duplicate else None
        
        if process_type == 'CURRENT_STATE_UPDATE':
            print("🔄 Processing as current state documentation update...")
            success &= process_current_state_update(api_key, issue_number, issue_title, issue_body, 
                                                   is_duplicate, other_types)
            processors_run.append('documentation')
            
        elif process_type == 'FEATURE_PROPOSAL':
            print("✨ Processing as feature proposal...")
            success &= process_feature_proposal(api_key, issue_number, issue_title, issue_body,
                                               is_duplicate, other_types)
            processors_run.append('feature')
            
        elif process_type == 'BUG_REPORT':
            print("🐛 Processing as bug report...")
            success &= process_bug_report(api_key, issue_number, issue_title, issue_body,
                                         is_duplicate, other_types)
            processors_run.append('bug')
            
        elif process_type == 'QUESTION':
            print("❓ Processing as question...")
            success &= process_question(api_key, issue_number, issue_title, issue_body,
                                       is_duplicate, other_types)
            processors_run.append('question')
            
        elif process_type == 'STANDARD_ISSUE':
            print("📋 Standard issue - no automated processing")
            # Not an error, just no processing needed
            
        else:
            print(f"❌ Unknown issue type: {process_type}")
            success = False
    
    if processors_run:
        print(f"✅ Processed as: {', '.join(processors_run)}")
        if is_duplicate:
            print("⚠️  Multiple processing due to multiple labels")
    
    if not success:
        print("❌ Processing failed")
        sys.exit(1)
    
elif event_type == "closed":
    print("🔒 Issue closed - no processing needed")
    
else:
    print(f"🔄 Event type '{event_type}' - no processing needed")