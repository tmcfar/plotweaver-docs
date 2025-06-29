#!/usr/bin/env python3
"""Generate a one-page documentation state summary showing staleness, bugs, questions, and sprint status."""

import os
import yaml
import glob
from datetime import datetime, timedelta
from pathlib import Path


def get_changelog_info(template_file):
    """Get last update info from changelog."""
    changelog_file = template_file.replace('.md', '-changelog.yaml')
    
    if not os.path.exists(changelog_file):
        return None, None
    
    try:
        with open(changelog_file, 'r') as f:
            changelog = yaml.safe_load(f) or {'changelog': []}
        
        entries = changelog.get('changelog', [])
        if entries:
            latest = entries[0]
            return latest['date'], latest['github_issue']
    except:
        pass
    
    return None, None


def get_file_age(file_path, last_changelog_date=None):
    """Get file age in days."""
    if last_changelog_date:
        # Use changelog date if available
        try:
            update_date = datetime.strptime(last_changelog_date, '%Y-%m-%d')
            age = (datetime.now() - update_date).days
            return age
        except:
            pass
    
    # Fall back to file modification time
    mtime = os.path.getmtime(file_path)
    update_date = datetime.fromtimestamp(mtime)
    age = (datetime.now() - update_date).days
    return age


def get_staleness_indicator(age_days):
    """Get staleness indicator based on age."""
    if age_days < 7:
        return "✅ Fresh"
    elif age_days < 30:
        return "🟡 Recent"
    elif age_days < 90:
        return "🟠 Aging"
    else:
        return "🔴 Stale"


def get_bugs_summary():
    """Get summary of open bugs."""
    bugs_dir = "bugs"
    if not os.path.exists(bugs_dir):
        return []
    
    bugs = []
    for bug_dir in sorted(glob.glob(f"{bugs_dir}/*")):
        if os.path.isdir(bug_dir):
            bug_file = os.path.join(bug_dir, "bug-report.md")
            if os.path.exists(bug_file):
                # Extract issue number and title from directory name
                dir_name = os.path.basename(bug_dir)
                parts = dir_name.split('-', 1)
                issue_num = parts[0] if parts else "?"
                title = parts[1].replace('-', ' ').title() if len(parts) > 1 else dir_name
                
                bugs.append({
                    'issue': f"#{issue_num}",
                    'title': title,
                    'path': bug_file
                })
    
    return bugs[:5]  # Top 5 bugs


def get_questions_summary():
    """Get summary of open questions."""
    questions_dir = "questions"
    if not os.path.exists(questions_dir):
        return []
    
    questions = []
    for q_dir in sorted(glob.glob(f"{questions_dir}/*")):
        if os.path.isdir(q_dir):
            q_file = os.path.join(q_dir, "question.md")
            if os.path.exists(q_file):
                # Extract issue number and title from directory name
                dir_name = os.path.basename(q_dir)
                parts = dir_name.split('-', 1)
                issue_num = parts[0] if parts else "?"
                title = parts[1].replace('-', ' ').title() if len(parts) > 1 else dir_name
                
                questions.append({
                    'issue': f"#{issue_num}",
                    'title': title,
                    'path': q_file
                })
    
    return questions[:5]  # Top 5 questions


def get_current_sprint():
    """Get current sprint from roadmap."""
    roadmap_file = "templates/roadmap.md"
    if not os.path.exists(roadmap_file):
        return None
    
    try:
        with open(roadmap_file, 'r') as f:
            content = f.read()
        
        # Look for IN PROGRESS phase
        import re
        # Try different IN PROGRESS patterns  
        patterns = [
            r'### Phase (\d+):\s*([^=\n]+)\s*[=⏳🔄]\s*\*\*IN PROGRESS\*\*(.*?)(?=###|\Z)'
        ]
        
        match = None
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                break
                
        if match:
            phase_num = match.group(1)
            phase_title = match.group(2).strip()
            phase_content = match.group(3)
            
            # Extract duration
            duration_match = re.search(r'\*\*Duration\*\*:\s*([^\n]+)', phase_content)
            duration = duration_match.group(1) if duration_match else "Unknown"
            
            return {
                'phase': phase_num,
                'title': phase_title,
                'duration': duration.strip()
            }
    except:
        pass
    
    return None


def generate_summary():
    """Generate the documentation state summary."""
    print("# 📊 Documentation State Summary")
    print(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    
    # Core Documentation Status
    print("## 📚 Core Documentation Status\n")
    print("| Document | Last Update | Age | Status | Link |")
    print("|----------|-------------|-----|--------|------|")
    
    core_docs = [
        "templates/system-spec.md",
        "templates/roadmap.md",
        "templates/agent-spec.md",
        "CLAUDE.md"
    ]
    
    for doc in core_docs:
        if os.path.exists(doc):
            last_update, issue = get_changelog_info(doc)
            age = get_file_age(doc, last_update)
            status = get_staleness_indicator(age)
            update_str = f"{last_update} ({issue})" if last_update else "No changelog"
            
            doc_name = os.path.basename(doc).replace('.md', '')
            print(f"| {doc_name} | {update_str} | {age}d | {status} | [{doc}]({doc}) |")
    
    # Current Sprint
    print("\n## 🏃 Current Sprint\n")
    sprint = get_current_sprint()
    if sprint:
        print(f"**Phase {sprint['phase']}**: {sprint['title']}")
        print(f"- **Duration**: {sprint['duration']}")
        print(f"- **Details**: [View Roadmap](templates/roadmap.md#phase-{sprint['phase']})")
    else:
        print("*No active sprint found in roadmap*")
    
    # Open Bugs
    print("\n## 🐛 Open Bugs\n")
    bugs = get_bugs_summary()
    if bugs:
        for bug in bugs:
            print(f"- {bug['issue']}: {bug['title']} ([view]({bug['path']}))")
        
        total_bugs = len(glob.glob("bugs/*"))
        if total_bugs > 5:
            print(f"\n*...and {total_bugs - 5} more bugs*")
    else:
        print("*No open bugs found*")
    
    # Open Questions
    print("\n## ❓ Open Questions\n")
    questions = get_questions_summary()
    if questions:
        for q in questions:
            print(f"- {q['issue']}: {q['title']} ([view]({q['path']}))")
        
        total_questions = len(glob.glob("questions/*"))
        if total_questions > 5:
            print(f"\n*...and {total_questions - 5} more questions*")
    else:
        print("*No open questions found*")
    
    # Recent Processing
    print("\n## 🔄 Recent Issue Processing\n")
    
    # Check for recent feature proposals
    features = sorted(glob.glob("features/proposed/*"), key=os.path.getmtime, reverse=True)[:3]
    if features:
        print("### Latest Features")
        for feature in features:
            dir_name = os.path.basename(feature)
            parts = dir_name.split('-', 1)
            issue_num = parts[0] if parts else "?"
            print(f"- #{issue_num}: {os.path.basename(feature)} ([view]({feature}/README.md))")
    
    # Check for recent documentation updates
    doc_updates = sorted(glob.glob("current-state-updates/*"), key=os.path.getmtime, reverse=True)[:3]
    if doc_updates:
        print("\n### Latest Documentation Updates")
        for update in doc_updates:
            dir_name = os.path.basename(update)
            parts = dir_name.split('-', 1)
            issue_num = parts[0] if parts else "?"
            print(f"- #{issue_num}: {os.path.basename(update)} ([view]({update}/analysis.md))")
    
    print("\n---")
    print("\n*Use `gdocs` alias to pull latest issues and regenerate this summary*")


if __name__ == "__main__":
    generate_summary()