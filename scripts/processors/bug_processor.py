#!/usr/bin/env python3
"""Bug report processor - handles bug labeled issues."""

from .shared_utils import (clean_title_for_filename, ensure_directory, get_current_timestamp,
                          get_github_metadata, format_github_metadata_markdown, escape_markdown)


def process_bug_report(api_key, issue_number, issue_title, issue_body, is_duplicate=False, other_types=None):
    """Process bug report issues."""
    clean_title = clean_title_for_filename(issue_title)
    bug_dir = f"bugs/{issue_number}-{clean_title}"
    
    ensure_directory(bug_dir)
    
    # Get GitHub metadata
    github_metadata = get_github_metadata(issue_number, issue_title)
    
    # Build content with metadata and duplication warning
    content = f"# Bug Report: {issue_title}\n\n"
    
    # Add duplication warning if needed
    if is_duplicate:
        content += "⚠️ **DUPLICATE PROCESSING NOTICE**\n"
        content += f"This issue was processed multiple ways due to multiple labels: {other_types}\n"
        content += "See other generated files for this issue.\n\n"
    
    content += format_github_metadata_markdown(github_metadata)
    content += "## Issue Description\n\n"
    # Escape markdown in issue body to prevent formatting issues
    content += escape_markdown(issue_body)
    content += "\n\n## Status\n\n"
    content += "- Status: Open\n"
    content += "- Priority: TBD\n"
    content += "- Assigned: TBD\n"
    
    # Write bug report
    with open(f"{bug_dir}/bug-report.md", "w") as f:
        f.write(content)
    
    print(f"✅ Created bug report: {bug_dir}")
    return True