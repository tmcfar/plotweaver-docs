# Feature: Progressive Setting System

ID: 57
Ref: Setting-2

A three-tier progressive elaboration system that grows setting detail organically as the story demands it. Enables immediate writing with sensible genre defaults while supporting deep customization, solving the classic worldbuilding paralysis problem through just-in-time detail generation.

## Classification
**Impact:** *Must Have*
**Complexity:** *Large*
**Strategic Value:** *Core*

## User Value
Problem:
- Front-loaded worldbuilding paralysis
- Inconsistent "wing it" approach
- Mid-writing research disruption
- Poor setting maintenance

Solution:
- Genre-based smart defaults
- Optional world customization
- Just-in-time detail generation
- Automatic consistency tracking

## Product Value
Market Impact:
- Reduces writer's block
- Enables longer projects
- Maintains consistency
- Genre-specific support

Strategic Alignment:
- Template marketplace foundation
- Multi-project world support
- Series consistency enabler 
- Core worldbuilding engine

## Changes Required
- 🔴 SettingRepository: Core system
- 🔴 TemplateSystem: Genre defaults
- 🟡 CacheManager: Instance storage
- 🟢 UserInterface: Customization
- 🟢 VersionControl: Detail tracking

## Implementation
Dependencies:
- Required: Template engine, storage system
- Optional: Version control
- Blocking: None

Scope:
- MVP: Basic three-tier system
- Boundaries: No ML generation
- Future: Template marketplace

Integration:
- Pipeline: Pre-scene enrichment
- Data: Three-tier storage
- Contracts: Setting protocols

Migration:
- Strategy: Genre-based adoption
- Fallback: Direct setting input

## Planning Review Outcomes

-------------------------------------------
Technical Details:

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

Implementation Advantages:
- Performance optimization via caching
- Storage efficiency through inheritance
- Easy template extensibility
- Full user control over defaults
- Series-level consistency tracking

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

Initial Implementation Steps:
1. Core location template design (5 types)
2. Basic SettingRepository implementation
3. Simple override mechanism creation
4. Fantasy author testing group