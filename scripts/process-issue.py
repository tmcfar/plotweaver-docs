#!/usr/bin/env python3
import os
import json
import requests
import re
from datetime import datetime

# Get environment variables
api_key = os.environ.get('OPENROUTER_API_KEY')
issue_number = os.environ.get('ISSUE_NUMBER')
issue_title = os.environ.get('ISSUE_TITLE')
issue_body = os.environ.get('ISSUE_BODY', '')
event_type = os.environ.get('EVENT_TYPE')

# Validate required environment variables
if not api_key:
    print("ERROR: OPENROUTER_API_KEY environment variable not set")
    exit(1)
if not issue_number or not issue_title:
    print("ERROR: Required issue environment variables not set")
    exit(1)

# Clean title for folder name - remove invalid characters
clean_title = re.sub(r'[<>:"/\\|?*\[\]]', '', issue_title.lower())
clean_title = re.sub(r'\s+', '-', clean_title.strip('-'))
clean_title = re.sub(r'-+', '-', clean_title)

feature_dir = f"features/proposed/{issue_number}-{clean_title}"

if event_type == "opened":
    # Create feature directory
    os.makedirs(feature_dir, exist_ok=True)
    
    # Generate documentation using OpenRouter
    prompt = f"""
Based on this GitHub issue, create a brief technical specification.
Follow the template format with sections for Overview, Requirements, and Technical Approach.
Be concise and specific.

Issue Title: {issue_title}
Issue Description: {issue_body}
"""
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        }
    )
    
    if response.status_code == 200:
        ai_content = response.json()['choices'][0]['message']['content']
    else:
        ai_content = f"Error generating content: {response.status_code} - {response.text}"
    
    # Write README
    with open(f"{feature_dir}/README.md", "w") as f:
        f.write(f"# Feature: {issue_title}\n\n")
        f.write(f"Issue: #{issue_number}\n")
        f.write(f"Created: {datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write(ai_content)
    
    # Create status file
    with open(f"{feature_dir}/status.md", "w") as f:
        f.write(f"## Status: {issue_title}\n\n")
        f.write(f"- Created: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("- Status: Proposal\n")
        f.write("- Stage: Evaluation Pending\n")

elif event_type == "closed":
    # Move to completed
    pass