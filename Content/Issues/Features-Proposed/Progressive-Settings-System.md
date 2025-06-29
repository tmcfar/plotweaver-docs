# Feature: Progressive Setting System

ID: 23
Ref: Phase-5

Writers struggle with the classic worldbuilding problem: too much detail up front kills momentum, too little creates inconsistency. This system enables "just-in-time" setting development, starting with genre-appropriate defaults and expanding naturally during writing. Settings evolve organically as needed while maintaining consistency through intelligent caching and version control.

## Classification
**Impact:** *Must Have*
**Complexity:** *Large*
**Strategic Value:** *Core*

## User Value
Problem:
- Writers must either front-load extensive worldbuilding or deal with inconsistencies
- Current tools force choosing between overwhelming detail or insufficient structure
- Manual tracking of discovered setting details during writing is error-prone
- Genre conventions require significant research and planning

Solution:
- Start writing immediately with smart genre defaults
- Discover and expand world details naturally during writing
- System maintains consistency automatically
- Focus on story first, elaborate settings where they matter

## Product Value
Market Impact:
- Only AI writing tool with intelligent setting management
- Attracts both pantsers (minimal upfront work) and planners (consistency guarantees)
- Enables unique workflows impossible with traditional tools
- Clear differentiation from basic prompt-response systems

Strategic Alignment:
- Foundation for marketplace of setting templates
- Enables future multi-project setting sharing
- Positions product for specialized genre features
- Core technology for future AI-assisted worldbuilding tools

## Changes Required
- 🔴 SettingRepository: Core three-tier system for template management and just-in-time generation
- 🔴 TemplateSystem: Genre defaults with inheritance and customization
- 🟡 CacheManager: Instance storage and performance optimization
- 🟡 Setting Agents: Split into 5 specialized sub-agents with hierarchical coordination
- 🟢 UserInterface: Template customization and override controls
- 🟢 VersionControl: Detail tracking and setting evolution with scene references

## Implementation
Dependencies:
- Required: Base agent system, storage system, template engine
- Optional: Digital Humanities pre-processing, version control
- Blocking: Quality agent implementation, context intelligence

Scope:
- MVP: Single genre template, basic discovery, three-tier storage
- Boundaries: No cross-project sharing, no custom templates, no ML generation
- Future: Template marketplace, setting visualization, ML-based discovery

Integration:
- Pipeline: Insert setting enrichment after scene generation, pre-scene enrichment
- Data: New YAML format for settings, three-tier storage, git-tracked discoveries
- Contracts: New setting request/response protocols for agents

Migration:
- Strategy: Parallel run with flag, migrate projects on opt-in, genre-based adoption
- Fallback: Settings can be exported to static YAML, direct setting input

## Planning Review Outcomes
- [date] - [outcome]

-------------------------------------------
Technical Implementation:

Core Components:
- SettingRepository:
  - Three-tier architecture:
    - Genre templates (base layer)
    - User customizations (override layer)  
    - Discovered details (dynamic layer)
  - Location handling:
    - Template-based generation
    - Customization application
    - Instance caching
    - Consistency tracking

Template System:
- Base Location Template:
```yaml
# templates/fantasy/base_location.yaml
base_location:
  environmental:
    weather_affects: true
    time_of_day_matters: true
  cultural:
    social_hierarchy: "medieval_fantasy"
```

- Specialized Templates:
```yaml
# templates/fantasy/tavern.yaml
inherits: "base_location"
location_specific:
  function: "social_gathering"
  typical_events: ["meals", "gossip", "deals", "fights"]
```

- User Customization:
```yaml
# world/customizations/taverns.yaml
user_overrides:
  tavern_default:
    smells: ["incense", "exotic_spices"]  # Cultural
    atmosphere: "always_suspicious"        # World-specific
    special_rules: ["no_weapons_allowed"] # Setting law
```

Implementation Strategy:
Phase 5A - Foundation (Month 1):
- Basic SettingRepository
- Template loading system
- 5 core location types
- Cache management

Phase 5B - Genre Templates (Month 2):
- Fantasy template pack (10 locations)
- Modern template pack (10 locations)
- Template inheritance system
- Consistency validation

Phase 5C - User Customization (Month 1):
- Override system
- Template editing
- Instance storage
- Version control

Phase 5D - Integration (Month 1):
- Agent integration
- Pipeline updates
- Testing framework
- Documentation

Performance Requirements:
- Template loading: <100ms
- Location generation: <50ms
- Cache hit rate: >80%
- Storage efficiency: <1MB per world

Technical Implementation:
```python
class SettingRepository:
    """Progressive elaboration for settings"""
    
    def __init__(self, project_root: Path):
        self.templates = self._load_genre_templates()
        self.user_overrides = self._load_user_customizations()
        self.instances = self._load_discovered_instances()
        self.cache = LRUCache(maxsize=100)
    
    def get_location_for_scene(self, location_type: str, context: dict) -> dict:
        # Check cache first
        cache_key = f"{location_type}:{hash(str(context))}"
        if cache_key in self.cache:
            return self.cache[cache_key]
            
        # Build layered configuration
        base = self.templates.get(location_type, {})
        overrides = self.user_overrides.get(location_type, {})
        instance = self._merge_configs(base, overrides, context)
        
        # Cache and return
        self.cache[cache_key] = instance
        return instance
```

User Workflow Example:
```
Day 1: Author selects "fantasy" genre, starts writing
      → Tavern scene auto-uses default fantasy tavern template

Day 3: Author wants unique cultural element
      → Adds override: taverns burn sacred herbs

Day 10: Scene needs "The Prancing Pony" specifically  
       → System generates instance with defaults + overrides + context
       → Stores instance for future consistency

Day 50: Different scene returns to Prancing Pony
       → System retrieves stored instance, maintains consistency
```

Success Metrics:
- User Adoption:
  - 80% projects use 3+ location types
  - 60% users customize templates
  - 15+ locations per 50-scene project

- Quality Measures:
  - Reduced scene completion time
  - User satisfaction with details
  - Cross-scene consistency scores

Risk Controls:
- Generic Templates:
  - Multiple variations per genre
  - Easy customization system
  - Template sharing (future)
  - Conservative defaults

- Context Handling:
  - Safe default generation
  - User review capabilities
  - Manual override options
  - Clear inheritance

- Complexity Management:
  - Start with 5-10 locations
  - User-driven expansion
  - Clear template hierarchy
  - Progressive enhancement

Competitive Analysis:
- Existing Solutions:
  - World Anvil:
    - Strong: Comprehensive worldbuilding
    - Weak: Front-loaded complexity, separate tool
  - Scrivener + Templates:
    - Strong: Writing environment integration
    - Weak: Static templates only

- PlotWeaver Advantages:
  - Just-in-time detail generation
  - Seamless writing integration
  - Progressive complexity growth
  - Cross-book consistency

Critical Success Requirements:
- Template Design:
  - Simple, broadly applicable defaults
  - Optional customization only
  - Seamless scene integration
  - Early user feedback loops

Notes:
- Genre templates define basic world rules and common elements
- Three-tier storage separates defaults, user choices, and discoveries
- Cache system handles both memory and disk storage
- Setting discovery uses context analysis to identify new elements
- Version control tracks setting evolution with scene references
