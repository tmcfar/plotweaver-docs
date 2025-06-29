#!/usr/bin/env python3
"""Strategic content processor - flags content for Claude Code review."""

import os
from datetime import datetime
from .shared_utils import (ensure_directory, get_content_root,
                         get_github_metadata, format_github_metadata_markdown)

def process_strategic_content(api_key, issue_number, issue_title, issue_body, 
                            is_duplicate=False, other_types=None):
    """Process content that requires Claude Code analysis."""
    
    # Create a pending review in Planning/Analysis
    analysis_dir = os.path.join(get_content_root(), 'Planning', 'Analysis')
    ensure_directory(analysis_dir)
    
    # Create analysis request file
    timestamp = datetime.now().strftime('%Y%m%d-%H%M')
    filename = f"needs-claude-{issue_number}-{timestamp}.md"
    filepath = os.path.join(analysis_dir, filename)
    
    # Get GitHub metadata
    github_metadata = get_github_metadata(issue_number, issue_title)
    
    # Build content
    content = [
        "# Needs Claude Code Analysis\n",
        format_github_metadata_markdown(github_metadata),
        "\n## Original Content\n",
        issue_body,
        "\n## Analysis Required\n",
        "This issue has been flagged as needing Claude Code analysis.",
        "\nPossible areas for analysis:",
        "- Strategic implications",
        "- Priority evaluation",
        "- Resource allocation",
        "- Technical recommendations",
        "- Architecture decisions",
        "\n## Next Steps",
        "1. Human operator should engage Claude Code for analysis",
        "2. Claude Code will analyze and provide recommendations",
        "3. Update relevant planning documents based on analysis",
        f"\n## Review ID: {timestamp}\n"
    ]
    
    # Write the file
    with open(filepath, "w") as f:
        f.write("\n".join(content))
    
    print(f"✨ Created strategic analysis request: {filepath}")
    print("👉 Please engage Claude Code for analysis")
    
    return True