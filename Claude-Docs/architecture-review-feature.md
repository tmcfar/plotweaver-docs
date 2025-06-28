# PlotWeaver Feature: Post-Setup Architecture Review System (DRAFT)

## Overview

After users complete story setup (concept, characters, setting, plot), an Architecture Review Agent analyzes project complexity and provides transparent recommendations for agent configuration and model selection, empowering informed cost/quality decisions.

## Core Concept

The system performs comprehensive analysis after setup but before writing begins, providing users with:
- Clear complexity metrics
- Agent configuration options
- Cost/quality tradeoffs
- Transparent recommendations

## Key Components

### 1. Architecture Review Agent

```python
class ArchitectureReviewAgent:
    """Analyzes project and recommends optimal configuration"""
    
    def analyze_project(self, project: Project) -> ArchitectureReport:
        # Gather all complexity metrics
        complexity = {
            "setting": self._analyze_setting_complexity(project),
            "characters": self._analyze_character_complexity(project),
            "plot": self._analyze_plot_complexity(project),
            "scope": self._analyze_scope_metrics(project)
        }
        
        # Generate recommendations
        recommendations = self._generate_recommendations(complexity)
        
        # Calculate cost projections
        cost_analysis = self._project_costs(recommendations, project.estimated_length)
        
        return ArchitectureReport(
            complexity_breakdown=complexity,
            recommendations=recommendations,
            cost_projections=cost_analysis,
            risk_factors=self._identify_risks(complexity)
        )
```

### 2. Complexity Analysis System

```python
class ComplexityMetrics:
    """Quantify project complexity across dimensions"""
    
    def analyze_setting(self, setting_data: Dict) -> SettingComplexity:
        return SettingComplexity(
            location_count=len(setting_data.get("locations", [])),
            culture_count=len(setting_data.get("cultures", [])),
            unique_systems=self._count_unique_systems(setting_data),
            cross_references=self._count_interconnections(setting_data),
            detail_depth=self._measure_average_detail(setting_data),
            overall_score=self._calculate_weighted_score()
        )
    
    def analyze_characters(self, characters: List[Character]) -> CharacterComplexity:
        return CharacterComplexity(
            total_count=len(characters),
            pov_count=len([c for c in characters if c.is_pov]),
            major_count=len([c for c in characters if c.importance == "major"]),
            relationship_web_density=self._calculate_relationship_density(characters),
            arc_complexity=self._assess_arc_intricacy(characters)
        )
```

### 3. Configuration Generator

```python
class ConfigurationGenerator:
    """Generate tiered configuration options"""
    
    def generate_options(self, complexity: ComplexityReport) -> List[Configuration]:
        configs = []
        
        # Premium - Maximum quality
        configs.append(self._generate_premium_config(complexity))
        
        # Balanced - Smart optimization
        configs.append(self._generate_balanced_config(complexity))
        
        # Budget - Minimum viable
        configs.append(self._generate_budget_config(complexity))
        
        # Custom - User modifiable
        configs.append(self._generate_custom_template(complexity))
        
        return configs
    
    def _generate_balanced_config(self, complexity: ComplexityReport) -> Configuration:
        """Smart middle ground based on actual needs"""
        
        agents = []
        
        # Character agents based on cast size
        if complexity.characters.total_count > 20:
            agents.extend([
                AgentSpec("CharacterLead", "GPT-4", temp=0.5),
                AgentSpec("CharacterSupport", "Claude-Haiku", temp=0.6)
            ])
        else:
            agents.append(AgentSpec("CharacterUnified", "GPT-3.5", temp=0.5))
            
        # Setting agents based on world complexity
        if complexity.setting.overall_score > 0.7:
            agents.extend([
                AgentSpec("WorldConsistency", "Claude-Sonnet", temp=0.3),
                AgentSpec("CultureTracker", "Mistral-Medium", temp=0.4)
            ])
            
        return Configuration(
            name="Balanced",
            agents=agents,
            estimated_cost_per_scene=self._calculate_scene_cost(agents),
            quality_score=self._estimate_quality(agents, complexity)
        )
```

## User Experience Flow

### Step 1: Completion of Setup
```
✓ Concept defined
✓ Characters created (23)
✓ World built (High complexity)
✓ Plot outlined (75 scenes)

[Begin Writing] → [Review Architecture]
```

### Step 2: Architecture Analysis
```
Analyzing your project architecture...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Progress bar animation]

✓ Setting complexity evaluated
✓ Character web analyzed  
✓ Plot structure assessed
✓ Optimal configurations generated
```

### Step 3: Review Interface
```
Architecture Analysis Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROJECT COMPLEXITY BREAKDOWN
┌─────────────────────────────────────────────┐
│ Setting:     ████████░░ HIGH (23 locations) │
│ Characters:  ██████░░░░ MEDIUM (18 tracked) │
│ Plot:        ████████░░ HIGH (3 plotlines)  │
│ Overall:     ████████░░ HIGH COMPLEXITY     │
└─────────────────────────────────────────────┘

⚠️ IMPORTANT CONSIDERATION
Your rich worldbuilding requires specialized attention
to maintain consistency. This impacts cost and quality.

RECOMMENDED CONFIGURATIONS

┌─[ 🏆 PREMIUM QUALITY ]──────────────────────┐
│ 7 specialized agents with top models        │
│ • Quality Score: 95%                        │
│ • Cost per scene: $0.65                     │
│ • Total estimate: $487.50                   │
│ Perfect for: Publication-ready quality      │
└─────────────────────────────────────────────┘

┌─[ ⚖️ SMART BALANCE ]───────────────────────┐
│ 4 agents with mixed models (RECOMMENDED)    │
│ • Quality Score: 88%                        │
│ • Cost per scene: $0.35                     │
│ • Total estimate: $262.50                   │
│ Perfect for: Great quality, reasonable cost │
└─────────────────────────────────────────────┘

┌─[ 💰 BUDGET CONSCIOUS ]─────────────────────┐
│ 2 general agents with efficient models      │
│ • Quality Score: 72%                        │
│ • Cost per scene: $0.15                     │
│ • Total estimate: $112.50                   │
│ Perfect for: First draft, cost sensitive    │
└─────────────────────────────────────────────┘

[Select Configuration] [Customize] [Learn More]
```

### Step 4: Configuration Details
```
Smart Balance Configuration (Detailed View)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AGENT ASSIGNMENT
┌────────────────────┬─────────────┬────────┐
│ Agent              │ Model       │ Focus  │
├────────────────────┼─────────────┼────────┤
│ CharacterLead      │ GPT-4       │ 8 main │
│ CharacterSupport   │ Claude-Haiku│ Others │
│ WorldConsistency   │ GPT-3.5     │ Setting│
│ QualityValidator   │ Mistral-Med │ All    │
└────────────────────┴─────────────┴────────┘

WHAT THIS MEANS
✓ Main characters get premium attention
✓ Supporting cast handled efficiently  
✓ World consistency maintained
✓ Quality checks on everything

TRADEOFFS
⚠️ Supporting character dialogue less nuanced
⚠️ Some worldbuilding details may drift
⚠️ Quality catches ~88% of issues vs 95%

[Confirm] [Modify] [Compare All]
```

## Key Features

### Transparent Communication

```python
def generate_user_explanation(self, complexity: ComplexityReport) -> str:
    """Create clear, non-technical explanation"""
    
    if complexity.setting.overall_score > 0.8:
        return """
        Your world is richly detailed with {num_locations} locations 
        and {num_cultures} distinct cultures. This is fantastic for 
        immersion but requires careful tracking. Think of it like 
        juggling - more balls need more attention (and cost more).
        """.format(
            num_locations=complexity.setting.location_count,
            num_cultures=complexity.setting.culture_count
        )
```

### Risk Communication

```
⚠️ COMPLEXITY WARNINGS

High Character Count (47 characters)
• Risk: Inconsistent minor character voices
• Mitigation: Focus resources on main cast
• Alternative: Reduce tracked characters

Dense World References (1,200+ connections)
• Risk: Continuity errors in later chapters
• Mitigation: Dedicated consistency agent
• Alternative: Simplify non-critical elements

[Acknowledge Risks] [Modify Project] [Proceed Anyway]
```

## Benefits

- **Informed Decisions**: Users understand cost/quality tradeoffs
- **Transparency**: No surprise bills or quality issues
- **Optimization**: Right-sized resources for each project
- **Education**: Users learn what drives complexity

## Risks & Skepticism

### Risk: Analysis Paralysis
**Skeptical take**: "Great, another 10 screens before they can write. You've turned starting a novel into filing taxes."

**Mitigation**:
- Analysis happens automatically during setup
- Single review screen with clear recommendation
- "Use Recommended" one-click option
- Can skip and use defaults

### Risk: Overwhelming Information
**Skeptical take**: "Showing complexity metrics and agent configurations to writers is like showing engine diagnostics to drivers."

**Mitigation**:
- Layer information (simple → detailed)
- Use visual representations
- Focus on impact, not implementation
- Provide clear recommendations

### Risk: Budget Shock
**Skeptical take**: "Users will see $487 and run away screaming, even if that's reasonable for a novel."

**Mitigation**:
- Always show multiple options
- Emphasize per-scene costs
- Compare to human editing costs
- Allow pay-as-you-go options

### Risk: False Precision
**Skeptical take**: "Quality Score: 88%' is meaningless. You can't quantify story quality."

**Mitigation**:
- Explain metrics clearly
- Focus on consistency/error catching
- Use ranges not exact numbers
- A/B test predictions vs outcomes

## Implementation Phases

### Phase 1: Basic Analysis
- Simple complexity counting
- 3 preset configurations
- Basic cost estimates

### Phase 2: Smart Recommendations
- DH complexity analysis
- Tailored configurations
- Risk identification

### Phase 3: Learning System
- Track actual vs predicted costs
- Refine quality estimates
- Personalized recommendations

## Success Metrics

- User understanding: 90%+ grasp tradeoffs
- Choice satisfaction: 85%+ happy with selection
- Cost accuracy: Within 20% of estimates
- Completion rate: 95%+ proceed to writing

---

**Status**: DRAFT - Requires UX testing
**Priority**: Phase 5 (Critical for user trust)
**Dependencies**: Agent system, DH metrics
**Estimated Effort**: 4-6 weeks