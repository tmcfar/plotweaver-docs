# PlotWeaver Feature: Narrative Architect Pattern (DRAFT)

## Overview

Implement a two-tier AI system inspired by Aider's architect mode: an expensive "Narrative Architect" model plans complex changes and understands dependencies, while cheaper "Executor" models implement the specific edits. This optimizes costs while improving narrative coherence.

## Core Concept

```python
# High-level planning with expensive model
architect_plan = NarrativeArchitect.analyze_change_request(
    "Make Elena's character arc darker",
    manuscript_context
)
# Returns: Affected scenes, ripple effects, execution strategy

# Execution with cheaper models  
for change in architect_plan.changes:
    ExecutorAgent.apply_change(change)  # Uses GPT-3.5/Haiku
```

## Two-Tier Architecture

### Tier 1: Narrative Architect (Expensive Model)
- **Model**: GPT-4-turbo or Claude Opus
- **Purpose**: Understand narrative implications, plan changes
- **Cost**: ~$0.50-1.00 per analysis
- **Frequency**: Once per major change request

### Tier 2: Agent Executors (Cheaper Models)
- **Model**: GPT-3.5-turbo or Claude Haiku  
- **Purpose**: Execute specific edits following architect's plan
- **Cost**: ~$0.08 per scene
- **Frequency**: Multiple calls per change

## Use Cases

### Major Plot Change
```
Request: "Remove the betrayal subplot"

Architect Analysis:
- Primary: Remove 8 scenes with betrayal content
- Secondary: Adjust 12 character interaction scenes
- Tertiary: Update 5 foreshadowing moments
- New motivation needed for Chapter 6 conflict

Execution: 25 targeted regenerations (vs 50 full regenerations)
Cost: $0.75 planning + $2.00 execution = $2.75 (vs $20.00)
```

### Character Arc Modification
```
Request: "Make Marcus evolve from coward to hero"

Architect Analysis:
- Early scenes: Emphasize cowardice (5 scenes)
- Middle: Add growth moments (8 scenes)
- Climax: Heroic transformation (3 scenes)
- Skips: 34 scenes with no Marcus development

Savings: 68% fewer regenerations
```

## Implementation Details

### Activation Thresholds
```python
def should_use_architect(request: ChangeRequest) -> bool:
    # Skip architect for simple changes
    if request.type in ["typo", "single_scene", "dialogue_only"]:
        return False
    
    # Use architect for complex changes
    if request.type in ["plot_change", "character_arc", "world_rule"]:
        return True
        
    # Scope-based decision
    if request.estimated_impact > 5_scenes:
        return True
        
    return False
```

### Architect Capabilities
```yaml
narrative_understanding:
  - Cause-effect chains across scenes
  - Character arc progression
  - Thematic consistency
  - Pacing implications
  - Foreshadowing/payoff relationships

planning_strategies:
  - surgical: "Only dialogue changes needed"
  - cascade: "Regenerate in dependency order"  
  - parallel: "These scenes can update independently"
  - mixed: "Some need full rewrite, others need tweaks"
```

### Change Plan Structure
```python
@dataclass
class NarrativeChangePlan:
    # What changes
    affected_scenes: List[SceneChange]
    
    # Why changes needed
    narrative_reasoning: str
    
    # How to change
    execution_strategy: str
    
    # Order matters
    dependency_order: List[str]
    
    # Cost transparency
    estimated_cost: float
    architect_confidence: float
    
    # Human-readable
    summary_for_user: str
```

## Integration with Quality Loop

### Architect-Enhanced Quality Management
```python
class QualityArchitect:
    """Architect diagnoses systemic quality issues"""
    
    def analyze_quality_failures(self, failures: List[QualityFailure]):
        if len(failures) > 5:
            # Multiple failures = systemic issue
            diagnosis = self.architect_model.analyze({
                "failures": failures,
                "context": "Agents keep rejecting content"
            })
            
            return SystemicFixPlan(
                root_cause=diagnosis.cause,
                fix_strategy=diagnosis.strategy,
                affected_agents=diagnosis.adjust_these
            )
```

### Smart Restart Decisions
Instead of blind restarts, architect understands:
- "These failures are due to model mismatch"
- "Character voice inconsistent because backstory changed"
- "Quality agent expectations unrealistic for this genre"

## User Interface

### Change Request Flow
```
┌─────────────────────────────────────────────┐
│ Describe your change:                       │
│ "Make the magic system cost physical pain"  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 🧠 Narrative Architect Analysis             │
│                                             │
│ Understanding change... ████████████ 100%   │
│                                             │
│ Impact Summary:                             │
│ • 12 magic use scenes need pain addition   │
│ • 5 character reactions to adjust          │
│ • 3 worldbuilding updates required         │
│ • 28 scenes unaffected                     │
│                                             │
│ Strategy: Progressive cascade update        │
│ Estimated cost: $3.50 (vs $15.00 naive)    │
│                                             │
│ [View Details] [Approve] [Modify] [Cancel]  │
└─────────────────────────────────────────────┘
```

### Execution Monitoring
```
Executing Changes (12/20 complete)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Chapter 3, Scene 2: ✓ Pain cost added
Chapter 4, Scene 1: ✓ Character reaction updated  
Chapter 4, Scene 3: ⟳ Processing...

[Pause] [View Changes] [Abort]
```

## Benefits

### Cost Optimization
- 60-80% reduction for complex changes
- Architect cost amortized across many executions
- Avoids unnecessary regenerations

### Quality Improvements
- Maintains narrative coherence
- Understands ripple effects
- Preserves story structure

### User Experience
- Clear cost estimates upfront
- Transparent change planning
- Faster execution (parallel where possible)

## Risks & Mitigation

### Risk: Planning Errors Cascade
**Mitigation**: 
- Confidence scores on plans
- Human approval before execution
- Incremental execution with checkpoints

### Risk: Over-Architecture  
**Mitigation**:
- Thresholds for architect activation
- "Quick mode" for simple changes
- Cost/benefit display

### Risk: Context Window Limits
**Mitigation**:
- Summary compression techniques
- Incremental analysis options
- Fallback to section-by-section

### Risk: User Confusion
**Mitigation**:
- Clear UI explaining planning phase
- Progress indicators
- Skip options for power users

## Implementation Phases

### Phase 1: Manual Architect Mode
- User explicitly chooses "Smart Planning"
- Only for major changes
- Measure accuracy and savings

### Phase 2: Automatic Thresholds
- System suggests architect for complex changes
- Learn from user choices
- Refine activation heuristics

### Phase 3: Predictive Architecture
- "This change will likely affect..."
- Preemptive dependency warnings
- Change cost estimation

## Success Metrics

- Cost reduction: >60% for complex changes
- Accuracy: >85% correct dependency identification
- User satisfaction: Prefer over naive approach
- Performance: Planning completes in <30 seconds

## Technical Considerations

### Caching Strategy
```python
@lru_cache(maxsize=100)
def get_narrative_structure(manuscript_hash):
    # Cache expensive analysis
    return architect.analyze_structure(manuscript)
```

### Model Configuration
```yaml
architect_models:
  primary: "gpt-4-turbo"  # Best reasoning
  fallback: "claude-3-opus"  # Alternative
  budget: "gpt-4"  # Cheaper option

executor_models:
  default: "gpt-3.5-turbo"
  quality: "claude-3-haiku"
```

## Competitive Advantage

No other writing tool offers:
- Narrative-aware dependency analysis
- Cost-optimized change execution
- Transparent change planning
- Ripple effect visualization

This positions PlotWeaver as the "intelligent writing environment" vs simple generation tools.

---

**Status**: DRAFT - Requires technical feasibility review  
**Priority**: Phase 7 (After core features stable)  
**Estimated Effort**: 6-8 weeks
**Dependencies**: Stable agent pipeline, change detection system