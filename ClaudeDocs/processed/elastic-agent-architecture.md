# PlotWeaver Feature: Elastic Agent Architecture (DRAFT)

## Overview

Implement dynamic agent spawning based on project complexity, allowing PlotWeaver to scale computational resources precisely to match story needs. Instead of fixed agent assignments, the system spawns specialized agents based on actual requirements.

## Core Concept

```python
# Static (Current)
Every project gets:
- 1 CharacterAgent (handles 3 or 300 characters)
- 1 SettingAgent (modern town or galactic empire)
- Fixed computational overhead

# Elastic (Proposed)
Project complexity determines:
- 0-N CharacterAgents (scale with cast size)
- 0-N SettingAgents (scale with world complexity)
- Adaptive quality validation
- Pay for what you use
```

## Key Features

### 1. Dynamic Agent Spawning

```python
class ElasticAgentManager:
    """Spawn agents based on project complexity"""
    
    def analyze_and_spawn(self, project: Project) -> List[Agent]:
        complexity = self.analyze_complexity(project)
        
        agents = []
        # Character management scales with cast
        if complexity.character_count < 5:
            agents.append(MinimalCharacterAgent())
        elif complexity.character_count < 20:
            agents.append(StandardCharacterAgent())
        else:
            # Spawn specialized teams
            agents.extend([
                ProtagonistAgent(),
                SupportingCastAgent(count=complexity.character_count//10),
                BackgroundCastAgent()
            ])
            
        # Setting complexity drives world agents
        if complexity.has_magic_system:
            agents.append(MagicSystemAgent())
        if complexity.culture_count > 1:
            for culture in complexity.cultures:
                agents.append(CultureAgent(culture))
                
        return agents
```

### 2. Temperature-Based Character Modeling

```python
class CharacterTemperatureMapping:
    """Match AI temperature to character personality"""
    
    def assign_temperatures(self, characters: List[Character]) -> Dict:
        mapping = {}
        for char in characters:
            if "unpredictable" in char.traits:
                mapping[char.id] = {"agent": CharacterAgent(char), "temp": 0.9}
            elif "methodical" in char.traits:
                mapping[char.id] = {"agent": CharacterAgent(char), "temp": 0.3}
            else:
                mapping[char.id] = {"agent": CharacterAgent(char), "temp": 0.5}
        return mapping
```

### 3. Complexity Analysis via Digital Humanities

```python
class DHComplexityAnalyzer:
    """Quantify project complexity using DH metrics"""
    
    def analyze(self, project: Project) -> ComplexityScore:
        metrics = {
            # Breadth
            "location_count": len(project.locations),
            "character_count": len(project.characters),
            "culture_count": len(project.cultures),
            
            # Depth
            "avg_detail_depth": self._calculate_detail_depth(project),
            "interconnections": self._count_cross_references(project),
            
            # Narrative load
            "new_terms_per_chapter": self._count_unique_terminology(project),
            "concept_density": self._measure_concept_introduction_rate(project)
        }
        
        return ComplexityScore(
            raw_score=self._weighted_score(metrics),
            agent_recommendation=self._recommend_agents(metrics),
            cost_estimate=self._estimate_cost(metrics)
        )
```

### 4. PromptWriter Meta-Agent

```python
class PromptWriterAgent:
    """Dynamically generate specialized agent prompts"""
    
    def create_specialized_agent(self, spec: AgentSpec) -> Agent:
        prompt = self._generate_prompt(
            base_template=self.templates[spec.type],
            specialization=spec.focus,
            constraints=spec.constraints
        )
        
        return DynamicAgent(
            prompt=prompt,
            model=self._select_model_for_complexity(spec),
            lifecycle_rules=spec.lifecycle
        )
```

## User Experience

### Post-Setting Architecture Review

```
Setting Analysis Complete
━━━━━━━━━━━━━━━━━━━━━━━

Your world complexity: VERY HIGH
- 23 unique locations
- 4 distinct cultures  
- 2 magic systems
- 1,247 cross-references

Recommended Configuration:
┌─────────────────────────────────────────┐
│ 7 Specialized Agents:                   │
│ • 3 LocationTracker (by region)         │
│ • 2 CultureConsistency                  │
│ • 1 MagicSystem                         │
│ • 1 CrossReference Coordinator          │
│                                         │
│ Estimated cost: $0.45-0.65/scene        │
└─────────────────────────────────────────┘

Alternative Configurations:
[Premium] [Balanced] [Budget] [Custom]
```

## Benefits

- **Cost Efficiency**: 60-80% savings for simple projects
- **Quality Scaling**: Complex projects get needed resources
- **Flexibility**: Agents adapt to project evolution
- **Specialization**: Each agent optimized for its domain

## Risks & Skepticism

### Risk: Coordination Overhead
**Skeptical take**: "More agents = more orchestration complexity. Your 'simple' system now needs a distributed systems engineer to debug agent communication failures."

**Mitigation**:
- Start with max 5 agents for MVP
- Clear communication protocols
- Hierarchical organization (lead agents coordinate sub-agents)
- Extensive logging for debugging

### Risk: PromptWriter Quality
**Skeptical take**: "Dynamically generated prompts will be garbage. You can't just template-generate nuanced AI instructions."

**Mitigation**:
- Human-reviewed prompt templates as base
- Extensive testing of generated prompts
- Fallback to pre-written prompts
- A/B testing dynamic vs static prompts

### Risk: User Confusion
**Skeptical take**: "Users don't want to manage an AI agent swarm. They want to write a book, not play StarCraft."

**Mitigation**:
- Default to automatic configuration
- Hide complexity behind presets
- Simple cost/quality slider
- "What's running" dashboard, not control panel

### Risk: Unpredictable Costs
**Skeptical take**: "Dynamic spawning means users won't know what they're paying until the bill arrives."

**Mitigation**:
- Cost estimates before execution
- Hard budget limits
- Real-time cost tracking
- Automatic downscaling at thresholds

## Implementation Phases

### Phase 1: Fixed Configurations (MVP)
- 3 preset configurations (Minimal, Balanced, Complex)
- Manual selection only
- Basic cost tracking

### Phase 2: Semi-Dynamic
- Complexity analysis after setup
- Recommended configuration
- User can modify

### Phase 3: Fully Elastic
- Real-time spawning
- Automatic load balancing
- Learning optimization

## Success Metrics

- Cost reduction: 50%+ for simple projects
- Quality maintenance: 95%+ vs fixed architecture
- User satisfaction: Prefer over fixed agents
- Debug time: <2x current architecture

---

**Status**: DRAFT - Requires architecture review
**Priority**: Phase 7+ (After core stability)
**Dependencies**: Stable base agents, DH integration
**Estimated Effort**: 10-12 weeks full implementation