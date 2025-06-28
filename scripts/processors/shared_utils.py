#!/usr/bin/env python3
"""Shared utilities for issue processing."""

import os
import re
from datetime import datetime


def get_issue_type(labels):
    """Determine issue type based on labels only."""
    if not labels:
        return 'STANDARD_ISSUE'
    
    label_names = [label.lower() for label in labels]
    
    if 'documentation' in label_names:
        return 'CURRENT_STATE_UPDATE'
    
    if 'enhancement' in label_names or 'feature' in label_names:
        return 'FEATURE_PROPOSAL'
    
    # No matching label = no processing
    return 'STANDARD_ISSUE'


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