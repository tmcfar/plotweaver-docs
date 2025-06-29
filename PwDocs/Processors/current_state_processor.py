#!/usr/bin/env python3
"""Current state processor - handles documentation labeled issues with full pipeline."""

import requests
from .shared_utils import (clean_title_for_filename, ensure_directory, get_current_timestamp,
                          get_github_metadata, format_github_metadata_markdown, sanitize_for_ai)
from .changelog_manager import create_core_doc_metadata_section


def process_current_state_update(api_key, issue_number, issue_title, issue_body, is_duplicate=False, other_types=None):
    """Process current state documentation updates using full pipeline."""
    
    # Create processing directory
    clean_title = clean_title_for_filename(issue_title)
    base_path = get_proper_path([get_content_root(), 'Technical', 'Updates'])
    work_dir = os.path.join(base_path, f"{issue_number}-{clean_title}")
    ensure_directory(work_dir)
    
    # Get GitHub metadata
    github_metadata = get_github_metadata(issue_number, issue_title)
    
    # Sanitize inputs for AI
    safe_title = sanitize_for_ai(issue_title)
    safe_body = sanitize_for_ai(issue_body)
    
    # Analyze content and determine approach using AI
    analysis_prompt = f"""
You are Claude Code processing a current state documentation update.

TASK: Analyze this issue content and determine how to process it using our established documentation pipeline.

ISSUE CONTENT:
Title: {safe_title}
Body: {safe_body}

APPROACH OPTIONS:
1. SPLIT_APPROACH: Content contains both current state and proposed features
2. CURRENT_STATE_ONLY: Content is purely current state documentation  
3. FEATURE_EVALUATION_ONLY: Content is proposing new features/enhancements
4. REQUIRES_MANUAL_REVIEW: Content is unclear or complex

ANALYSIS CRITERIA:
- Does it describe what currently exists vs what's proposed?
- Is it documenting working features vs planning future ones?
- Would this benefit from our split approach (current state + feature evaluations)?
- Is the scope appropriate for automated processing?

PROVIDE:
1. Recommended approach (1-4 above)
2. Brief justification (2-3 sentences)
3. Suggested file structure and content organization

Be critical and realistic about what can be automated vs what needs manual review.
"""
    
    # Get AI analysis
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": analysis_prompt}],
            "max_tokens": 800
        }
    )
    
    if response.status_code == 200:
        analysis = response.json()['choices'][0]['message']['content']
    else:
        analysis = f"Error in analysis: {response.status_code} - {response.text}"
        
    # Build analysis content with metadata and duplication warning
    analysis_content = f"# Analysis: {issue_title}\n\n"
    
    # Add duplication warning if needed
    if is_duplicate:
        analysis_content += "⚠️ **DUPLICATE PROCESSING NOTICE**\n"
        analysis_content += f"This issue was processed multiple ways due to multiple labels: {other_types}\n"
        analysis_content += "See other generated files for this issue.\n\n"
    
    analysis_content += format_github_metadata_markdown(github_metadata)
    analysis_content += "## AI Analysis\n\n"
    analysis_content += analysis
    analysis_content += "\n\n## Original Issue Content\n\n"
    analysis_content += f"**Title:** {issue_title}\n\n"
    analysis_content += f"**Body:**\n{issue_body}"
    
    # Save analysis for manual review
    with open(f"{work_dir}/analysis.md", "w") as f:
        f.write(analysis_content)
    
    # Create processing instruction for manual follow-up
    instructions_content = f"# Processing Instructions: {issue_title}\n\n"
    instructions_content += format_github_metadata_markdown(github_metadata)
    
    if is_duplicate:
        instructions_content += "⚠️ **DUPLICATE PROCESSING NOTICE**\n"
        instructions_content += f"Also processed as: {', '.join(other_types)}\n\n"
    
    instructions_content += "## Next Steps\n"
    instructions_content += "1. Review the AI analysis in `analysis.md`\n"
    instructions_content += "2. Apply the recommended approach:\n"
    instructions_content += "   - If SPLIT_APPROACH: Create spec_system updates + feature evaluations\n"
    instructions_content += "   - If CURRENT_STATE_ONLY: Update relevant templates\n"
    instructions_content += "   - If FEATURE_EVALUATION_ONLY: Create feature evaluation documents\n"
    instructions_content += "   - If MANUAL_REVIEW: Process manually using established patterns\n"
    instructions_content += "\n## Templates Available\n"
    instructions_content += "- `templates/spec_system.md`\n"
    instructions_content += "- `templates/planning_roadmap.md`\n"
    instructions_content += "- `templates/issue_feature.md`\n"
    instructions_content += "\n## Changelog Management\n"
    instructions_content += "- For core template updates, use changelog system\n"
    instructions_content += "- Changelog files: `{template}-changelog.yaml`\n"
    instructions_content += "- Use `changelog_manager.py` functions\n"
    instructions_content += "\n## Established Patterns\n"
    instructions_content += "- Split approach: Working features → templates, Proposed features → evaluations\n"
    instructions_content += "- Critical analysis with realistic timelines\n"
    instructions_content += "- Purge performance claims and marketing language\n"
    instructions_content += "- Move processed files to avoid duplication\n"
    
    with open(f"{work_dir}/processing-instructions.md", "w") as f:
        f.write(instructions_content)
    
    print(f"✅ Current state analysis created: {work_dir}")
    print("📋 Manual processing required - see processing-instructions.md")
    return True