#!/usr/bin/env python3
"""Current state processor - handles documentation labeled issues with full pipeline."""

import requests
from .shared_utils import clean_title_for_filename, ensure_directory, get_current_timestamp


def process_current_state_update(api_key, issue_number, issue_title, issue_body):
    """Process current state documentation updates using full pipeline."""
    
    # Create processing directory
    clean_title = clean_title_for_filename(issue_title)
    work_dir = f"current-state-updates/{issue_number}-{clean_title}"
    ensure_directory(work_dir)
    
    # Analyze content and determine approach using AI
    analysis_prompt = f"""
You are Claude Code processing a current state documentation update.

TASK: Analyze this issue content and determine how to process it using our established documentation pipeline.

ISSUE CONTENT:
Title: {issue_title}
Body: {issue_body}

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
        
    # Save analysis for manual review
    with open(f"{work_dir}/analysis.md", "w") as f:
        f.write(f"# Analysis: {issue_title}\n\n")
        f.write(f"Issue: #{issue_number}\n")
        f.write(f"Created: {get_current_timestamp()}\n\n")
        f.write("## AI Analysis\n\n")
        f.write(analysis)
        f.write("\n\n## Original Issue Content\n\n")
        f.write(f"**Title:** {issue_title}\n\n")
        f.write(f"**Body:**\n{issue_body}")
    
    # Create processing instruction for manual follow-up
    with open(f"{work_dir}/processing-instructions.md", "w") as f:
        f.write(f"# Processing Instructions: {issue_title}\n\n")
        f.write("## Next Steps\n")
        f.write("1. Review the AI analysis in `analysis.md`\n")
        f.write("2. Apply the recommended approach:\n")
        f.write("   - If SPLIT_APPROACH: Create system-spec updates + feature evaluations\n")
        f.write("   - If CURRENT_STATE_ONLY: Update relevant templates\n")
        f.write("   - If FEATURE_EVALUATION_ONLY: Create feature evaluation documents\n")
        f.write("   - If MANUAL_REVIEW: Process manually using established patterns\n")
        f.write("\n## Templates Available\n")
        f.write("- `templates/system-spec.md`\n")
        f.write("- `templates/roadmap.md`\n")
        f.write("- `templates/feature-evaluation.md`\n")
        f.write("\n## Established Patterns\n")
        f.write("- Split approach: Working features → templates, Proposed features → evaluations\n")
        f.write("- Critical analysis with realistic timelines\n")
        f.write("- Purge performance claims and marketing language\n")
        f.write("- Move processed files to avoid duplication\n")
    
    print(f"✅ Current state analysis created: {work_dir}")
    print("📋 Manual processing required - see processing-instructions.md")
    return True