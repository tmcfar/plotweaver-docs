#!/usr/bin/env python3
"""Question processor - handles question labeled issues."""

from .shared_utils import (clean_title_for_filename, ensure_directory, get_current_timestamp,
                          get_github_metadata, format_github_metadata_markdown)


def process_question(api_key, issue_number, issue_title, issue_body, is_duplicate=False, other_types=None):
    """Process question issues."""
    clean_title = clean_title_for_filename(issue_title)
    question_dir = f"questions/{issue_number}-{clean_title}"
    
    ensure_directory(question_dir)
    
    # Get GitHub metadata
    github_metadata = get_github_metadata(issue_number, issue_title)
    
    # Build content with metadata and duplication warning
    content = f"# Question: {issue_title}\n\n"
    
    # Add duplication warning if needed
    if is_duplicate:
        content += "⚠️ **DUPLICATE PROCESSING NOTICE**\n"
        content += f"This issue was processed multiple ways due to multiple labels: {other_types}\n"
        content += "See other generated files for this issue.\n\n"
    
    content += format_github_metadata_markdown(github_metadata)
    content += "## Question\n\n"
    content += issue_body
    content += "\n\n## Answer\n\n"
    content += "*To be answered...*\n"
    content += "\n\n## Status\n\n"
    content += "- Status: Open\n"
    content += "- Priority: TBD\n"
    
    # Write question
    with open(f"{question_dir}/question.md", "w") as f:
        f.write(content)
    
    print(f"✅ Created question: {question_dir}")
    return True