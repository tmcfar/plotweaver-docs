#!/usr/bin/env python3
import os
import json
import sys
from processors.shared_utils import get_issue_type
from processors.feature_processor import process_feature_proposal
from processors.current_state_processor import process_current_state_update

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

# Determine issue type from labels
issue_type = get_issue_type(issue_labels)

print(f"Processing issue #{issue_number}: {issue_title}")
print(f"Labels: {issue_labels}")
print(f"Detected type: {issue_type}")

if event_type == "opened":
    success = False
    
    if issue_type == 'CURRENT_STATE_UPDATE':
        print("🔄 Processing as current state documentation update...")
        success = process_current_state_update(api_key, issue_number, issue_title, issue_body)
        
    elif issue_type == 'FEATURE_PROPOSAL':
        print("✨ Processing as feature proposal...")
        success = process_feature_proposal(api_key, issue_number, issue_title, issue_body)
        
    elif issue_type == 'STANDARD_ISSUE':
        print("📋 Standard issue - no automated processing")
        success = True  # Not an error, just no processing needed
        
    else:
        print(f"❌ Unknown issue type: {issue_type}")
        success = False
    
    if not success:
        print("❌ Processing failed")
        sys.exit(1)
    
elif event_type == "closed":
    print("🔒 Issue closed - no processing needed")
    
else:
    print(f"🔄 Event type '{event_type}' - no processing needed")