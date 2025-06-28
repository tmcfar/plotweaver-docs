#!/usr/bin/env python3
"""Shared utilities for issue processing."""

import os
import re
import yaml
import html
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


def validate_issue_number(issue_number):
    """Validate and sanitize issue number."""
    # Remove any non-numeric characters
    clean_number = re.sub(r'\D', '', str(issue_number))
    if not clean_number:
        raise ValueError(f"Invalid issue number: {issue_number}")
    return clean_number


def escape_markdown(text):
    """Escape markdown special characters."""
    if not text:
        return text
    # Escape markdown special characters
    text = str(text)
    for char in ['*', '_', '[', ']', '(', ')', '#', '`', '>', '|', '\\']:
        text = text.replace(char, '\\' + char)
    return text


def sanitize_for_ai(text):
    """Sanitize text for AI prompts to prevent injection."""
    if not text:
        return text
    # Remove potential prompt injection patterns
    text = str(text)
    # Remove common injection attempts
    injection_patterns = [
        r'ignore.*previous.*instructions',
        r'disregard.*above',
        r'forget.*everything',
        r'new.*instructions.*:',
        r'system.*prompt.*:',
        r'assistant.*:',
        r'</.*>',  # HTML/XML tags
        r'```.*```',  # Code blocks that might contain instructions
    ]
    for pattern in injection_patterns:
        text = re.sub(pattern, '[REMOVED]', text, flags=re.IGNORECASE)
    return text


def get_github_metadata(issue_number, issue_title):
    """Generate GitHub issue metadata with validation."""
    # Validate issue number
    clean_issue_number = validate_issue_number(issue_number)
    
    return {
        'github_issue': f"#{clean_issue_number}",
        'github_url': f"https://github.com/tmcfar/plotweaver-docs/issues/{clean_issue_number}",
        'issue_title': issue_title,  # Will be escaped when formatted
        'processed_date': get_current_timestamp()
    }


def format_github_metadata_yaml(metadata):
    """Format GitHub metadata as YAML frontmatter with proper escaping."""
    # Use yaml.dump for safe string escaping
    yaml_content = {
        'github_issue': metadata['github_issue'],
        'github_url': metadata['github_url'],
        'issue_title': metadata['issue_title'],
        'processed_date': metadata['processed_date']
    }
    
    # Dump with safe formatting
    yaml_str = yaml.dump(yaml_content, default_flow_style=False, allow_unicode=True)
    
    return f"---\n{yaml_str}---\n\n"


def format_github_metadata_markdown(metadata):
    """Format GitHub metadata as markdown section with proper escaping."""
    # Escape the title for markdown
    escaped_title = escape_markdown(metadata['issue_title'])
    
    return f"""## GitHub Issue Reference
- **Issue**: [{metadata['github_issue']}]({metadata['github_url']})
- **Title**: {escaped_title}
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