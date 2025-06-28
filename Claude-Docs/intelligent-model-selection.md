# PlotWeaver Feature: Intelligent Model Selection & Provider Management (DRAFT)

## Overview

Implement a sophisticated model selection system that matches task requirements to model capabilities across multiple providers, optimizing for cost while maintaining quality. Support 2-3 direct AI providers plus OpenRouter for extended model access.

## Core Concept: 5x5 Architecture

### 5 Model Tiers
```yaml
frontier:
  examples: ["GPT-4-latest", "Claude-Opus", "Gemini-Ultra"]
  cost_multiplier: 10x
  use_cases: ["Complex reasoning", "Plot coherence", "Character psychology"]

performance:
  examples: ["GPT-4", "Claude-Sonnet", "Command-R+"]
  cost_multiplier: 5x
  use_cases: ["Scene generation", "Quality validation"]

balanced:
  examples: ["GPT-3.5-turbo", "Claude-Haiku", "Gemini-Pro"]
  cost_multiplier: 1x
  use_cases: ["Basic generation", "Simple continuity"]

efficient:
  examples: ["Mistral-7B", "Llama-3-8B", "Phi-3"]
  cost_multiplier: 0.2x
  use_cases: ["Pattern detection", "Grammar", "Formatting"]

specialized:
  examples: ["CodeLlama", "StableLM", "WizardLM"]
  cost_multiplier: Varies
  use_cases: ["Specific domains", "Unique capabilities"]
```

### 5 Quality Profiles
```yaml
perfectionist:
  description: "Every word matters"
  critical_tasks: frontier
  standard_tasks: performance
  simple_tasks: balanced

professional:
  description: "Publication-ready"
  critical_tasks: performance
  standard_tasks: balanced
  simple_tasks: efficient

smart_saver:
  description: "Quality where it counts"
  critical_tasks: performance
  standard_tasks: efficient
  simple_tasks: efficient

draft_mode:
  description: "Get words on page"
  critical_tasks: balanced
  standard_tasks: efficient
  simple_tasks: efficient

experimental:
  description: "User-defined mix"
  all_tasks: custom
```

## Key Features

### 1. Multi-Provider Architecture

```python
class ProviderManager:
    """Manage multiple AI providers with transparent pricing"""
    
    def __init__(self):
        self.providers = {
            "openai": OpenAIProvider(),      # Direct integration
            "anthropic": AnthropicProvider(), # Direct integration
            "openrouter": OpenRouterProvider() # Gateway to 50+ models
        }
    
    def get_best_price(self, model: str) -> PriceComparison:
        """Show transparent pricing across providers"""
        prices = {}
        
        # Check each provider
        for name, provider in self.providers.items():
            if provider.has_model(model):
                prices[name] = provider.get_price(model)
                
        return PriceComparison(
            model=model,
            prices=prices,
            cheapest=min(prices, key=prices.get),
            markup_info=self._calculate_markups(prices)
        )
```

### 2. DH-Driven Task Analysis

```python
class TaskComplexityAnalyzer:
    """Use DH metrics to quantify task requirements"""
    
    def analyze_task(self, task: Task, context: Context) -> TaskRequirements:
        if isinstance(task, CharacterDialogueGeneration):
            return TaskRequirements(
                reasoning=0.4,      # Character consistency
                creativity=0.8,     # Unique voice needed
                consistency=0.7,    # Match established patterns
                knowledge=0.3,      # Domain-specific
                nuance=0.9         # Subtext critical
            )
            
        elif isinstance(task, RepetitionDetection):
            return TaskRequirements(
                reasoning=0.1,      # Simple pattern matching
                creativity=0.0,     # Not needed
                consistency=0.9,    # Reliability crucial
                knowledge=0.1,      # Minimal
                nuance=0.1         # Not needed
            )
    
    def map_to_model_tier(self, requirements: TaskRequirements, 
                         complexity: ComplexityScore) -> str:
        """Convert requirements to model tier"""
        
        # Weight and combine scores
        capability_needed = (
            requirements.reasoning * 0.3 +
            requirements.creativity * 0.2 +
            requirements.consistency * 0.2 +
            requirements.knowledge * 0.15 +
            requirements.nuance * 0.15
        ) * complexity.multiplier
        
        # Map to tier
        if capability_needed > 0.8:
            return "frontier"
        elif capability_needed > 0.6:
            return "performance"
        elif capability_needed > 0.4:
            return "balanced"
        else:
            return "efficient"
```

### 3. Smart Routing System

```python
class SmartModelRouter:
    """Route requests to optimal provider/model combo"""
    
    def route(self, request: ModelRequest) -> RoutingDecision:
        model = request.model
        
        # Check user preferences
        if request.force_provider:
            return self._route_to_provider(request.force_provider, model)
            
        # Prefer direct providers for mainstream models
        if model in ["gpt-4", "claude-3-opus"] and self.has_direct_access(model):
            return self._route_direct(model)
            
        # Use OpenRouter for specialized models
        if model in self.openrouter_exclusive_models:
            return self._route_to_openrouter(model)
            
        # Cost optimization routing
        return self._route_by_cost(model, request.quality_requirements)
```

### 4. Cost Learning System

```python
class CostOptimizationLearner:
    """Learn which models handle tasks well at lower cost"""
    
    def track_performance(self, task: Task, model: Model, result: Result):
        """Build performance database"""
        quality_score = self._evaluate_quality(result)
        cost = model.cost_per_1k_tokens
        
        self.performance_db.add(
            task_type=task.type,
            model=model.id,
            quality=quality_score,
            cost=cost,
            efficiency=quality_score / cost
        )
    
    def suggest_downgrades(self, current_config: Dict) -> List[Suggestion]:
        """Find cheaper models that maintain quality"""
        suggestions = []
        
        for task_type, current_model in current_config.items():
            # Find models with 90%+ quality at lower cost
            alternatives = self.performance_db.query(
                task_type=task_type,
                min_quality=0.9 * self._get_current_quality(task_type),
                max_cost=self._get_current_cost(task_type) * 0.8
            )
            
            if alternatives:
                suggestions.append(CostSavingSuggestion(
                    task=task_type,
                    current=current_model,
                    suggested=alternatives[0],
                    monthly_savings=self._calculate_savings(task_type, alternatives[0])
                ))
                
        return suggestions
```

## User Experience

### Provider Configuration

```
AI Provider Setup
━━━━━━━━━━━━━━━

Step 1: Primary Providers (Best Pricing)
┌─────────────────────────────────────────┐
│ ✓ OpenAI                                │
│   API Key: ••••••••••••••••••••••••    │
│   Status: Connected ✓                   │
│   Models: GPT-4, GPT-3.5               │
│                                         │
│ ✓ Anthropic                             │
│   API Key: ••••••••••••••••••••••••    │
│   Status: Connected ✓                   │
│   Models: Claude 3 family               │
└─────────────────────────────────────────┘

Step 2: Extended Access (+20% cost, 50+ models)
┌─────────────────────────────────────────┐
│ ○ OpenRouter                            │
│   Provides: Llama, Mistral, WizardLM,   │
│             Qwen, Yi, 40+ more          │
│   Premium: ~20% markup for convenience  │
│   [Enable OpenRouter]                   │
└─────────────────────────────────────────┘
```

### Cost Dashboard

```
Model Usage This Month
━━━━━━━━━━━━━━━━━━━

By Provider:
OpenAI Direct:    $34.20 (68%) ⭐ Best rate
Anthropic Direct: $12.80 (26%) ⭐ Best rate  
OpenRouter:       $3.20 (6%)   ⚡ Specialty

By Task:
Plot Development:    GPT-4 ($18.40)
Scene Generation:    Claude-Haiku ($8.20)
Quality Checks:      Mistral-7B ($2.10)
Continuity:          Phi-3 ($0.90)

💡 Optimization Available:
Switch dialogue generation to Claude-Haiku
Estimated savings: $12/month
[Apply] [Details] [Ignore]
```

## Benefits

- **Cost Optimization**: 50-80% reduction vs single model
- **Quality Preservation**: Match models to task needs
- **Future Proof**: New models integrate easily
- **Transparency**: Users see exactly what they pay
- **Flexibility**: From budget to premium control

## Risks & Skepticism

### Risk: Analysis Paralysis
**Skeptical take**: "Great, now users need a PhD in model selection. They came to write, not optimize AI procurement."

**Mitigation**:
- Smart defaults that just work
- 5 simple presets cover 95% of users
- "Auto" mode that learns and optimizes
- Hide complexity unless requested

### Risk: Model Quality Variance
**Skeptical take**: "Cheaper models will produce garbage. Users will blame PlotWeaver when Phi-3 writes terrible dialogue."

**Mitigation**:
- Extensive testing of model/task combinations
- Minimum quality thresholds enforced
- Clear labeling of quality tradeoffs
- One-click upgrade if unsatisfied

### Risk: Provider Dependency
**Skeptical take**: "What happens when OpenRouter raises prices 50%? Or when Anthropic changes their API?"

**Mitigation**:
- Direct relationships with primary providers
- Multiple routing options for each model tier
- Pricing alerts and automatic rebalancing
- Local model support on roadmap

### Risk: Complexity Explosion
**Skeptical take**: "This turns a writing tool into an AI orchestration platform. Feature creep at its finest."

**Mitigation**:
- Default "Professional" preset works for most
- Complexity only exposed on demand
- Focus remains on writing, not configuration
- "Set and forget" for most users

## Implementation Phases

### Phase 1: Multi-Provider Basics
- OpenAI + Anthropic direct
- Simple model selection
- Basic cost tracking

### Phase 2: Smart Routing
- Add OpenRouter
- Cost comparison UI
- Auto-routing logic

### Phase 3: Learning System
- Performance tracking
- Cost optimization suggestions
- Automatic rebalancing

## Success Metrics

- Cost reduction: 50%+ average savings
- Quality maintenance: 95%+ user satisfaction
- Setup time: <5 minutes for new users
- Model selection accuracy: 90%+ optimal choices

---

**Status**: DRAFT - Requires provider partnerships
**Priority**: Phase 4 (High value, moderate complexity)
**Dependencies**: Stable agent system, Usage tracking
**Estimated Effort**: 6-8 weeks