# PlotWeaver Setting System Design Discussion

## Core Design Questions

### 1. When is Setting Used?

**Current Architecture:** Setting runs once during setup phase
**Reality Check:** Setting is needed throughout the writing process

**Setting Touchpoints:**
- **Setup Phase:** World foundation, rules, constraints
- **Writing Phase:** Location details for each scene, discovered locations, environmental continuity
- **Quality Phase:** Atmospheric consistency, cultural authenticity

**Key Question:** Should Setting be static (front-loaded) or dynamic (progressive elaboration)?

### 2. Level of Detail Balance

**The Goldilocks Problem:**

**Too Much Detail:**
- Users overwhelmed with worldbuilding questionnaires
- 90% of details never used in story
- Creates consistency maintenance burden
- Slows down getting to actual writing

**Too Little Detail:**
- Scenes feel generic and placeless
- Inconsistent world rules break immersion
- Missed opportunities for rich sensory description
- Cultural elements feel tacked-on

**Sweet Spot:** Just enough detail to make scenes feel authentic, not so much that it overwhelms the narrative

### 3. Setting Integration Patterns

**Option A: Front-loaded Approach**
```yaml
# All locations created during setup
locations/the_prancing_pony.yaml:
  name: "The Prancing Pony"
  type: "tavern"
  atmosphere: "Smoky, crowded, mysterious"
  layout: "Low ceiling, dark corners, central fireplace"
  sounds: ["crackling fire", "muted conversations", "creaking floors"]
  smells: ["ale", "woodsmoke", "wet wool"]
  unique_features: ["secret back room", "elvish artifacts"]
```
**Pros:** Consistency, rich detail available
**Cons:** High upfront effort, many unused locations

**Option B: Just-in-Time Generation**
```python
# Locations created when first needed
def get_location_for_scene(location_type: str, scene_context: dict):
    if location_exists(location_type):
        return load_existing_location(location_type)
    else:
        # Generate only what this scene needs
        return LocationsAgent.create_minimal_location(location_type, scene_context)
```
**Pros:** No wasted effort, contextually relevant
**Cons:** Risk of inconsistency, less rich detail

**Option C: Template + Progressive Elaboration**
```yaml
# Generic template
templates/tavern.yaml:
  archetype: "gathering_place"
  typical_features: ["bar", "tables", "fireplace"]
  atmosphere_options: ["rowdy", "mysterious", "cozy"]

# Specific instance when needed
locations/prancing_pony.yaml:
  base_template: "tavern"
  atmosphere: "mysterious"  # picked from options
  discovered_features:  # added as story develops
    scene_5: "secret back room"
    scene_12: "elvish artifacts on walls"
```
**Pros:** Balance of consistency and flexibility
**Cons:** More complex system

### 4. Setting Agent Hierarchy Analysis

**Current 5-Agent System:**
- WorldPhysicsAgent (physics + magic/tech systems)
- LocationsAgent (specific places)
- CulturePoliticsAgent (societies + governments)
- HistoryAgent (timeline + events)
- SettingStyleAgent (linguistic patterns)

**Questions:**
- Is this overwhelming for users who "just want to write"?
- Should some agents be optional based on genre?
- How do we handle contemporary fiction that needs minimal worldbuilding?

## Proposed Setting Philosophy: Progressive Elaboration

### Core Principle
"Start minimal, expand as the story demands"

### Three-Tier System

**Tier 1: Genre Defaults (Automatic)**
- Basic physics assumptions
- Common location types
- Cultural baselines
- Standard terminology

**Tier 2: User Overrides (Optional)**
- Major world differences
- Unique elements
- Key locations
- Special terminology

**Tier 3: Discovered Details (Dynamic)**
- Specific locations as referenced
- Cultural details when relevant
- Historical events when needed
- Sensory details for scenes

### Implementation Approach

```python
class ProgressiveSettingSystem:
    """Setting that grows organically with the story"""
    
    def __init__(self, genre: str, user_preferences: dict):
        # Start with sensible defaults
        self.world_template = GenreTemplates.load(genre)
        
        # Apply only user-specified changes
        self.user_overrides = user_preferences
        
        # Build detail as we write
        self.discovered_elements = {}
        
    def get_setting_for_scene(self, scene_spec: dict):
        # Return only what's needed for this scene
        # Generate missing elements just-in-time
        # Cache for consistency
```

## Key Design Decisions Needed

### 1. Mandatory vs Optional
- What setting elements are required vs optional?
- Should contemporary fiction skip worldbuilding entirely?
- How do we handle genre expectations?

### 2. Generation Timing
- Front-load during setup?
- Generate as needed during writing?
- Hybrid approach?

### 3. Detail Depth Control
- User preference slider (minimal → standard → rich)?
- Automatic based on genre?
- Learning from user behavior?

### 4. Cultural Integration
- How much dialect/terminology variation?
- When does cultural flavor become overwhelming?
- How to maintain authenticity without alienation?

### 5. Location Reuse
- How to handle returning to previous locations?
- Evolution of locations over story time?
- Consistency vs natural change?

## Recommended Approach

### 1. Adaptive Detail Level
```python
class AdaptiveSettingDetail:
    def determine_detail_level(self, user_history, genre, story_type):
        if genre == "contemporary_fiction":
            return "minimal"
        elif user.prefers_worldbuilding:
            return "rich"
        else:
            return "standard"
```

### 2. Smart Defaults by Genre
```yaml
genre_defaults:
  contemporary_fiction:
    worldbuilding_required: false
    focus: "real_world_authenticity"
    
  fantasy:
    worldbuilding_required: true
    focus: "magic_systems_and_cultures"
    
  sci_fi:
    worldbuilding_required: true
    focus: "technology_and_physics"
```

### 3. Context-Sensitive Generation
```python
def generate_setting_details(scene_needs: dict):
    # Only generate what enhances this specific scene
    if scene_needs.dialogue_heavy:
        generate_acoustic_properties()
    if scene_needs.action_sequence:
        generate_spatial_layout()
    if scene_needs.atmosphere_focus:
        generate_sensory_details()
```

### 4. Progressive Discovery Pattern
- Start with location type ("tavern")
- Add details as characters observe them
- Build history as characters learn it
- Develop culture through interactions

## Benefits of Progressive Elaboration

1. **Lower Barrier to Entry:** Writers can start immediately
2. **No Wasted Effort:** Only develop what's used
3. **Organic Growth:** World feels discovered, not prescribed
4. **Consistency Through Caching:** Reuse what's established
5. **Genre Appropriate:** Contemporary needs less, fantasy needs more

## Implementation Priority

### Phase 1: Template System
- Genre-based defaults
- Basic location templates
- Minimal required input

### Phase 2: Progressive Generation
- Just-in-time location creation
- Context-sensitive detail level
- Caching for consistency

### Phase 3: Adaptive Intelligence
- Learn user preferences
- Predict needed details
- Suggest worldbuilding opportunities

## Open Questions for Team Discussion

1. Should we require ANY worldbuilding for contemporary fiction?
2. How do we balance automation with user control?
3. What's the minimum viable setting for a good story?
4. How do we teach the system when setting details matter vs. when they're fluff?
5. Should setting evolution be tracked in version control?

## Conclusion

The Setting system should be a **supportive background artist**, not a demanding worldbuilding taskmaster. It should provide just enough detail to make scenes feel real and consistent, without overwhelming the narrative flow or creating unnecessary upfront work.

**Recommended approach:** Start with smart genre defaults, let users override what matters to them, and progressively elaborate details as the story naturally demands them.