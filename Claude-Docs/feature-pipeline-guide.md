# Solo Developer Feature Pipeline Guide

## Overview

A lightweight feature management system for solo developers. Track ideas from inception to implementation without overhead.

## Pipeline Stages

### 1. Capture (features/ideas.md)
```markdown
- [2024-01-15] Elastic agents - scale with complexity
- [2024-01-16] Model selection UI - provider comparison
- [2024-01-16] Series planning mode - multi-book arcs
```
**Rule:** Date + one line description. Don't overthink.

### 2. Refine (features/[feature-name].md)
When an idea feels solid, create a dedicated doc:

```markdown
# Feature: Elastic Agents

## Problem
Fixed agents waste resources on simple projects

## Solution  
Dynamic agent spawning based on project complexity

## MVP Scope
3 preset configurations (simple/balanced/complex)

## Full Vision
Automatic scaling with learned optimization
```

### 3. Evaluate (features/evaluation.md)
```markdown
| Feature | Impact | Effort | Risk | Score | Decision |
|---------|--------|--------|------|-------|----------|
| Elastic agents | High | High | Med | 6/10 | Later |
| Model selection | High | Med | Low | 8/10 | Next |
| Series planning | Med | High | Low | 5/10 | Backlog |
```
**Scoring:** Impact - Effort - Risk = Priority Score

### 4. Prioritize (features/roadmap.md)
```markdown
## Now (This Month)
- Model selection MVP

## Next (Next Quarter)  
- Progressive setting
- DH pre-filtering

## Later (Someday)
- Elastic agents
- Series planning
```

### 5. Scope (In Feature Doc)
Expand the feature doc with implementation phases:

```markdown
## Implementation Phases

### MVP (Week 1-2)
- [ ] Basic provider switching
- [ ] Cost comparison
- [ ] Simple UI

### Enhancement (Week 3-4)
- [ ] Smart routing
- [ ] Usage tracking
- [ ] Learning system
```

### 6. Plan (tasks/current-sprint.md)
```markdown
# Sprint: Model Selection MVP

## This Week
- [x] Provider interface design
- [x] OpenAI integration
- [ ] Anthropic integration
- [ ] Cost calculation
- [ ] Basic UI

## Blockers
- Need Anthropic API docs

## Notes
- OpenAI integration easier than expected
- Consider rate limiting
```

## File Structure

```
project-root/
├── features/
│   ├── ideas.md          # Quick capture
│   ├── evaluation.md     # Decision matrix
│   ├── roadmap.md        # Three-bucket priority
│   ├── elastic-agents.md # Feature specs
│   └── model-selection.md
└── tasks/
    ├── current-sprint.md # Active work
    └── completed/        # Archive
```

## Tools & Workflow

### Use These
- Markdown files in your repo
- Git history for decisions
- GitHub issues for bugs only
- Text editor of choice

### Skip These
- Project management apps
- Kanban boards
- Gantt charts
- Approval processes
- Complicated workflows

## Weekly Rhythm

**Monday (15 min)**
- Review evaluation matrix
- Pick this week's focus
- Update current-sprint.md

**Daily (2 min)**
- Check off completed tasks
- Add new discoveries

**Friday (10 min)**
- Archive completed work
- Update roadmap if needed
- Capture new ideas

## Decision Criteria

### High Impact
- Solves user pain point
- Enables new use cases
- Significant cost savings
- Competitive advantage

### Low Effort  
- Clear implementation path
- Existing patterns to follow
- Minimal dependencies
- Good library support

### Low Risk
- Doesn't break existing features
- Fallback options available
- Well-understood domain
- Testable

## Anti-Patterns to Avoid

❌ **Over-documenting:** If the doc is longer than the code, stop  
❌ **Perfect categories:** "Is this a feature or enhancement?" Don't care  
❌ **Detailed estimates:** "3.5 days" → Just use S/M/L  
❌ **Process for process:** If it doesn't help ship, delete it  

## Success Metrics

✅ **Ideas → Implementation:** <4 weeks for small features  
✅ **Documentation time:** <10 min/week  
✅ **Decision clarity:** Can pick next task in <1 minute  
✅ **Low friction:** Never think "ugh, I should update the tracker"  

## Remember

The code is the product, not the process. This system should help you ship, not create busywork. If any part becomes a burden, simplify or remove it.

---

*Keep it simple. Ship features. The best process is the one you actually use.*