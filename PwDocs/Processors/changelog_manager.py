#!/usr/bin/env python3
"""Changelog management for core documentation files."""

import os
import yaml
from datetime import datetime
from .shared_utils import get_current_timestamp


def add_changelog_entry(template_file, issue_metadata, change_description):
    """Add changelog entry for core documentation updates."""
    changelog_file = f"{template_file.replace('.md', '-changelog.yaml')}"
    
    # Load existing changelog or create new
    if os.path.exists(changelog_file):
        with open(changelog_file, 'r') as f:
            changelog = yaml.safe_load(f) or {'changelog': []}
    else:
        changelog = {'changelog': []}
    
    # Add new entry
    entry = {
        'date': get_current_timestamp(),
        'github_issue': issue_metadata['github_issue'],
        'github_url': issue_metadata['github_url'],
        'issue_title': issue_metadata['issue_title'],
        'change_description': change_description,
        'entry_id': f"{issue_metadata['github_issue'].replace('#', '')}-{get_current_timestamp()}"
    }
    
    changelog['changelog'].insert(0, entry)  # Most recent first
    
    # Write updated changelog
    with open(changelog_file, 'w') as f:
        yaml.dump(changelog, f, default_flow_style=False, sort_keys=False)
    
    return changelog_file


def get_changelog_summary(template_file, limit=5):
    """Get recent changelog entries for a template file."""
    changelog_file = f"{template_file.replace('.md', '-changelog.yaml')}"
    
    if not os.path.exists(changelog_file):
        return "No changelog entries found."
    
    with open(changelog_file, 'r') as f:
        changelog = yaml.safe_load(f) or {'changelog': []}
    
    entries = changelog.get('changelog', [])[:limit]
    
    if not entries:
        return "No changelog entries found."
    
    summary = "## Recent Changes\n\n"
    for entry in entries:
        summary += f"- **{entry['date']}** - [{entry['github_issue']}]({entry['github_url']}): {entry['change_description']}\n"
    
    return summary


def create_core_doc_metadata_section(template_file, issue_metadata, change_description):
    """Create metadata section for core documentation files."""
    changelog_file = add_changelog_entry(template_file, issue_metadata, change_description)
    changelog_summary = get_changelog_summary(template_file)
    
    metadata_section = f"""<!-- AUTOMATED METADATA - DO NOT EDIT MANUALLY -->
<!-- Last updated from {issue_metadata['github_issue']}: {issue_metadata['issue_title']} -->
<!-- Full changelog: {os.path.basename(changelog_file)} -->

{changelog_summary}

---

"""
    
    return metadata_section