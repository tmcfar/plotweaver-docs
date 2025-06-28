#!/usr/bin/env python3
"""Shared utilities for issue processing."""

import os
import re
from datetime import datetime


def get_issue_type(labels, title=None):
    """Determine issue type based on labels with title fallback."""
    label_names = [label.lower() for label in labels] if labels else []
    
    # Check for multiple processing labels
    processing_types = []
    if 'documentation' in label_names or 'docs' in label_names:
        processing_types.append('CURRENT_STATE_UPDATE')
    if 'enhancement' in label_names or 'feature' in label_names:
        processing_types.append('FEATURE_PROPOSAL')
    if 'bug' in label_names:
        processing_types.append('BUG_REPORT')
    if 'question' in label_names:
        processing_types.append('QUESTION')
    
    # If multiple processing types, return list for dual processing
    if len(processing_types) > 1:
        return processing_types
    elif len(processing_types) == 1:
        return processing_types[0]
    
    # Fallback to first word of title
    if title:
        first_word = title.split()[0].lower() if title.split() else ''
        if first_word in ['feature', 'feat', 'add', 'implement']:
            return 'FEATURE_PROPOSAL'
        elif first_word in ['doc', 'docs', 'documentation', 'update']:
            return 'CURRENT_STATE_UPDATE'
        elif first_word in ['bug', 'fix', 'error', 'issue']:
            return 'BUG_REPORT'
        elif first_word in ['question', 'help', 'how']:
            return 'QUESTION'
    
    # No processing needed
    return 'STANDARD_ISSUE'


def get_github_metadata(issue_number, issue_title):
    """Generate GitHub issue metadata."""
    return {
        'github_issue': f"#{issue_number}",
        'github_url': f"https://github.com/tmcfar/plotweaver-docs/issues/{issue_number}",
        'issue_title': issue_title,
        'processed_date': get_current_timestamp()
    }


def format_github_metadata_yaml(metadata):
    """Format GitHub metadata as YAML frontmatter."""
    return f"""---
github_issue: "{metadata['github_issue']}"
github_url: "{metadata['github_url']}"
issue_title: "{metadata['issue_title']}"
processed_date: "{metadata['processed_date']}"
---

"""


def format_github_metadata_markdown(metadata):
    """Format GitHub metadata as markdown section."""
    return f"""## GitHub Issue Reference
- **Issue**: [{metadata['github_issue']}]({metadata['github_url']})
- **Title**: {metadata['issue_title']}
- **Processed**: {metadata['processed_date']}

"""


def clean_title_for_filename(title):
    """Clean title for use in folder/file names."""
    clean_title = re.sub(r'[<>:"/\\|?*\[\]]', '', title.lower())
    clean_title = re.sub(r'\s+', '-', clean_title.strip('-'))
    clean_title = re.sub(r'-+', '-', clean_title)
    return clean_title


def ensure_directory(path):
    """Ensure directory exists."""
    os.makedirs(path, exist_ok=True)


def get_current_timestamp():
    """Get current timestamp in standard format."""
    return datetime.now().strftime('%Y-%m-%d')