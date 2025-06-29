#!/usr/bin/env python3
"""Feature proposal processor - handles enhancement/feature labeled issues."""

import requests
from .shared_utils import (clean_title_for_filename, ensure_directory, get_current_timestamp,
                          get_github_metadata, format_github_metadata_markdown, sanitize_for_ai)


def process_feature_proposal(api_key, issue_number, issue_title, issue_body, is_duplicate=False, other_types=None):
    """Process feature proposal issues with GitHub metadata."""
    clean_title = clean_title_for_filename(issue_title)
    base_path = get_proper_path([get_content_root(), 'Issues', 'Features-Proposed'])
    feature_dir = os.path.join(base_path, f"{issue_number}-{clean_title}")
    
    ensure_directory(feature_dir)
    
    # Get GitHub metadata
    github_metadata = get_github_metadata(issue_number, issue_title)
    
    # Sanitize inputs for AI
    safe_title = sanitize_for_ai(issue_title)
    safe_body = sanitize_for_ai(issue_body)
    
    # Generate documentation using OpenRouter
    prompt = f"""
Based on this GitHub issue, create a brief technical specification.
Follow the template format with sections for Overview, Requirements, and Technical Approach.
Be concise and specific.

Issue Title: {safe_title}
Issue Description: {safe_body}
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
    
    # Build content with metadata and duplication warning
    content = f"# Feature: {issue_title}\n\n"
    
    # Add duplication warning if needed
    if is_duplicate:
        content += "⚠️ **DUPLICATE PROCESSING NOTICE**\n"
        content += f"This issue was processed multiple ways due to multiple labels: {other_types}\n"
        content += "See other generated files for this issue.\n\n"
    
    content += format_github_metadata_markdown(github_metadata)
    content += ai_content
    
    # Write README
    with open(f"{feature_dir}/README.md", "w") as f:
        f.write(content)
    
    # Create status file with metadata
    with open(f"{feature_dir}/status.md", "w") as f:
        f.write(f"## Status: {issue_title}\n\n")
        f.write(format_github_metadata_markdown(github_metadata))
        f.write(f"- Created: {get_current_timestamp()}\n")
        f.write("- Status: Proposal\n")
        f.write("- Stage: Evaluation Pending\n")
        f.write("- Roadmap Ready: No\n")
        f.write("\n## Roadmap Integration\n")
        f.write("When this feature is approved for the roadmap:\n")
        f.write("1. Set 'Roadmap Ready: Yes' above\n")
        f.write("2. Move this directory to content/planning/roadmap/\n")
        f.write("3. Update relevant roadmap planning documents\n")
        
        if is_duplicate:
            f.write(f"\n### Duplicate Processing\n")
            f.write(f"Also processed as: {', '.join(other_types)}\n")
    
    print(f"✅ Created feature proposal: {feature_dir}")
    return True