#!/usr/bin/env python3
"""Feature proposal processor - handles enhancement/feature labeled issues."""

import requests
from .shared_utils import clean_title_for_filename, ensure_directory, get_current_timestamp


def process_feature_proposal(api_key, issue_number, issue_title, issue_body):
    """Process feature proposal issues (existing functionality)."""
    clean_title = clean_title_for_filename(issue_title)
    feature_dir = f"features/proposed/{issue_number}-{clean_title}"
    
    ensure_directory(feature_dir)
    
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
        f.write(f"Created: {get_current_timestamp()}\n\n")
        f.write(ai_content)
    
    # Create status file
    with open(f"{feature_dir}/status.md", "w") as f:
        f.write(f"## Status: {issue_title}\n\n")
        f.write(f"- Created: {get_current_timestamp()}\n")
        f.write("- Status: Proposal\n")
        f.write("- Stage: Evaluation Pending\n")
    
    print(f"✅ Created feature proposal: {feature_dir}")
    return True