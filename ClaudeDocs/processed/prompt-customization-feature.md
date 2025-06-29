# PlotWeaver Feature: User-Owned Prompt Customization & Reference Management (DRAFT)

## Overview

Allow users to customize AI prompts and model selection directly in their GitHub repository, providing granular cost/quality control and enabling reference manuscript processing for series continuity.

## Core Components

### 1. User-Owned Prompt Templates

```yaml
# In user's repo: prompts/setting/world_physics.yaml
template_version: "1.2.3"
agent: "WorldPhysicsAgent"

system_prompt:
  # ⚠️ DO NOT MODIFY - Required for agent coordination
  role: "You are a world physics designer..."
  
user_content:
  # ✅ CUSTOMIZE THIS SECTION
  inspiration: |
    [User's custom worldbuilding instructions]
  constraints: |
    [User's specific limitations]

required_outputs:  # Contract with other agents
  - physics_rules: array
  - limitations: object
```

### 2. Model Configuration Control

```yaml
# .plotweaver/model_config.yaml
model_assignments:
  PlotAgent:
    model: "gpt-4-turbo"
    temperature: 0.8
    
  # Cost optimization - cheaper models for setting
  WorldPhysicsAgent:
    model: "gpt-3.5-turbo"
    temperature: 0.7
    
optimization:
  monthly_budget: 100.00
  fallback_model: "gpt-3.5-turbo"
```

### 3. Reference Manuscript Processing

```
user-book-repo/
├── reference/
│   ├── series/       # Extracted patterns from previous books
│   │   ├── book-1-patterns.json
│   │   └── series-bible.yaml
│   └── style-analysis/
│       └── author-voice-patterns.json
```

## Pros

### Legal Protection
- User owns all creative customizations
- PlotWeaver executes user instructions only
- Clear IP separation

### Cost Control
- Granular model selection per agent
- Budget enforcement
- Transparent pricing

### Power User Features
- Deep prompt customization
- Series continuity from uploaded references
- Version controlled prompt evolution

### Competitive Advantage
- No other tool offers this level of control
- Appeals to professional authors
- Enables complex workflows

## Cons

### Complexity Explosion
- **Skeptical take**: We're turning a writing tool into a prompt engineering platform
- Support burden: "Why doesn't my custom prompt work?"
- Testing nightmare with infinite prompt variations

### Feature Creep Risk
- Model config → hosting preferences → custom embeddings → ...
- Where does it end?

### User Experience Fragmentation
- Power users get different results than casual users
- Hard to debug issues with custom prompts
- Documentation becomes massive

### Reference Processing Concerns
- **Skeptical take**: "Extract patterns" is hand-wavy
- What patterns? How accurate?
- Users expect magic, get statistical analysis

## Impact on Architecture

### Required Changes

```python
# New components needed
class PromptTemplateManager:
    """Load and validate user prompts"""
    
class ModelSelectionEngine:
    """Dynamic model selection per agent"""
    
class ReferenceProcessor:
    """Extract patterns from uploaded manuscripts"""
    
class CostTracker:
    """Real-time cost monitoring"""
```

### Git Repository Bloat
- Prompts + references + patterns = larger repos
- Sync performance impact
- Storage costs for users

### Agent Complexity
- Each agent must handle prompt variation
- Validation becomes critical
- Fallback strategies needed

### Testing Implications
- Can't test all prompt combinations
- Need robust schema validation
- Prompt compatibility matrix

## Implementation Considerations

### MVP Scope
1. Start with model selection only (no prompt customization)
2. Add prompt viewing (read-only)
3. Enable prompt editing for 2-3 agents
4. Gradually expand

### Schema Enforcement
```python
def validate_user_prompt(prompt_yaml):
    # Strict validation to prevent breaks
    if not has_required_sections(prompt_yaml):
        raise InvalidPromptError
    if modifies_protected_sections(prompt_yaml):
        raise ProtectedSectionError
```

### Reference Processing Reality
- Limit to factual extraction (character names, ages, locations)
- No style analysis initially (too vague)
- Clear disclaimers about what's extracted

## Critical Questions

1. **Is this our core value prop?** Or a distraction from dependency tracking and quality agents?

2. **Support burden**: Can we handle "my custom prompt broke everything" tickets?

3. **Prompt engineering barrier**: Do writers want to be prompt engineers?

4. **Legal complexity**: Does "user owns prompts" actually protect us if output infringes?

5. **Feature focus**: Does this serve the "just help me write" user or only power users?

## Recommendation

**Phase 1**: Model selection only - simple, valuable, low risk

**Phase 2**: View prompts (read-only) - transparency without complexity

**Phase 3**: Limited customization - test with power users

**Delay**: Reference processing until core features are rock solid

## Risk Mitigation

- Require prompt schema version matching
- Automated rollback on validation failure  
- Clear docs: "Customization voids support"
- Sandboxed execution for custom prompts

---

**Status**: DRAFT - Requires team review  
**Priority**: Phase 9+ (after core features)  
**Estimated Effort**: 8-12 weeks full implementation