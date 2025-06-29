# PlotWeaver: Architecture & Design Specification

## Project Vision

**PlotWeaver: AI-first collaborative manuscript dependency management platform**

Transform traditional linear content generation into a **dynamic dependency graph management system** - a build system for manuscripts where changes propagate intelligently through the dependency tree with human oversight.

### Core Principles
- **Git files as single source of truth** - all content with revision history and version tracking
- **AI agents generate primary content** with structured metadata contracts
- **Human editors manage dependencies** through intelligent conflict resolution
- **Scene-based content storage** to minimize conflicts and enable granular change tracking
- **Three-tier change management** (surgical editing, partial regeneration, full regeneration)
- **Sequential AI coordination** with metadata-driven change detection

## Technical Architecture

### Git-Native Storage Strategy (Single Source of Truth)

**Authentication:** Personal Access Tokens (PATs)
- Users create GitHub tokens with repo permissions
- PlotWeaver stores tokens securely, constructs authenticated URLs
- No SSH keys, no OAuth complexity initially

**Repository Structure:**
```
user-book-repo/
├── content/
│   └── chapters/
│       ├── chapter-1/
│       │   ├── scene-1-opening.md
│       │   ├── scene-1-metadata.yaml
│       │   ├── scene-2-conflict.md
│       │   ├── scene-2-metadata.yaml
│       │   └── scene-3-resolution.md
│       └── chapter-2/
├── characters/
│   ├── protagonist/elena-martinez.yaml
│   ├── antagonist/shadow-council.yaml
│   └── supporting/marcus-mentor.yaml
├── world/
│   ├── foundation/
│   │   ├── physics.yaml
│   │   └── rules.yaml
│   ├── cultures/
│   │   └── northern-kingdom.yaml
│   ├── locations/
│   │   ├── templates/
│   │   │   └── tavern.yaml
│   │   └── instances/
│   │       └── prancing-pony.yaml
│   └── history/
│       └── timeline.yaml
├── plot/
│   ├── concept.yaml
│   ├── outline.yaml
│   ├── chapter-outlines/
│   └── scene-metadata/
├── dependency-graph/
│   ├── change-detection.json
│   ├── impact-analysis.json
│   └── regeneration-queue.json
├── prompts/
│   ├── base/character-generation.md
│   ├── advanced/dialogue-refinement.md
│   └── user-custom/style-guide.md
├── generation/
│   ├── settings.json
│   ├── history.json
│   └── workflows.json
├── .plotweaver/
│   ├── repo-config.json
│   ├── agent-schedules.json
│   ├── dependency-cache.json
│   ├── search-index.db       # SQLite FTS5 search index
│   └── config.yaml           # Validated configuration
```

### Context Loading Pattern

**At Pipeline Start:**
```python
def load_context_from_git(project_root: str) -> AgentContext:
    """Load minimal context from git repository state with search capabilities"""
    context = AgentContext()
    config_manager = ConfigurationManager(project_root / ".plotweaver/config.yaml")
    
    # Initialize search manager with SQLite FTS5
    search_db_path = project_root / ".plotweaver/search-index.db"
    context.search_manager = SQLiteSearchIndex(search_db_path)
    
    # Initialize metadata inference engine
    context.metadata_inference = MetadataInferenceEngine()
    
    # Initialize setting repository for progressive elaboration
    context.setting_repository = SettingRepository(project_root)
    
    # Load minimal character information (core attributes only)
    for char_file in (project_root / "characters").glob("**/*.yaml"):
        context.characters[char_file.stem] = yaml.safe_load(char_file.open())
    
    # Load minimal plot data (critical beats only)
    context.plot_outline = yaml.safe_load((project_root / "plot" / "outline.yaml").open())
    
    # Load minimal scene metadata (core contracts only)
    for metadata_file in (project_root / "content").glob("**/scene-*-metadata.yaml"):
        scene_id = metadata_file.stem.replace("-metadata", "")
        context.scene_metadata[scene_id] = yaml.safe_load(metadata_file.open())
    
    # Set up context caching
    context.metadata_cache = LRUCache(maxsize=config_manager.config.search.cache_size_mb)
    
    return context
```

## Setting System Architecture

### Progressive Elaboration Philosophy

**Core Principle:** "Start minimal, expand as the story demands"

The setting system uses a three-tier progressive elaboration approach that balances rich worldbuilding with practical workflow needs.

### Three-Tier Setting Storage

**Tier 1: Genre Templates (Automatic)**
- Basic physics assumptions and world rules
- Common location archetypes
- Cultural baselines and social structures
- Standard terminology and naming conventions
- Loaded automatically based on genre selection

**Tier 2: User Customization (Optional)**
- Major divergences from genre norms
- Unique world elements (magic systems, technologies)
- Key locations central to the story
- Special terminology or linguistic patterns
- Cultural modifications from templates

**Tier 3: Discovered Details (Dynamic)**
- Specific locations created as scenes need them
- Cultural details revealed through character interactions
- Historical events mentioned in narrative
- Sensory details for specific scenes
- Environmental conditions as story progresses

### Setting Repository Pattern

```python
class SettingRepository:
    """Centralized setting access with progressive elaboration"""
    
    def get_location_for_scene(self, location_ref: str, scene_context: dict) -> Location:
        # Check if specific instance exists
        if self.location_exists(location_ref):
            return self.get_location(location_ref)
            
        # Check if we can infer from context
        location_type = self.infer_location_type(location_ref, scene_context)
        template = self.get_template(location_type)
        
        # Create just-in-time instance
        new_location = self.create_location_instance(
            template=template,
            name=location_ref,
            context=scene_context
        )
        
        # Store for consistency
        self.store_location(location_ref, new_location)
        return new_location
```

### Modular Creative Assets Design

To support future extensibility for importing/exporting creative components:

**Component Metadata Structure:**
```yaml
# Every setting component includes metadata
component_metadata:
  type: "location_template"
  extractable: true
  dependencies: ["world_physics.gravity", "culture.social_structure"]
  variations_allowed: ["atmosphere", "size", "condition"]
  source: "original"
  version: "1.0"
```

**Abstraction Layers:**
- **Instance Level:** "The Prancing Pony tavern" (specific details)
- **Template Level:** "Tavern archetype" (reusable pattern)
- **Pattern Level:** "Gathering place dynamics" (universal principle)

## Staged Enrichment Architecture

### Core Problem Solved

Instead of requiring SceneWriterAgent to juggle 9+ complex dimensions simultaneously (plot, characters, setting, context, style, etc.), we use a staged enrichment pattern where each agent focuses on its specialty.

### Enrichment Pipeline

**Stage 1: Lean Narrative Generation**
- SceneWriterAgent focuses on plot beats and character actions
- Receives minimal setting markers (location type, time, cultural context)
- Produces story-focused scenes without rich environmental detail

**Stage 2: Environmental Enhancement**
- SettingEnrichmentAgent adds sensory details and atmosphere
- Draws from SettingRepository for location-specific elements
- Applies cultural markers and environmental conditions

**Stage 3: Character Enhancement**
- Micro-specialized agents refine character representation
- Voice, body language, and subtext added progressively
- Each agent focuses on its specific domain

**Stage 4: Continuity Integration**
- Physical and atmospheric continuity verified
- Style consistency checked and adjusted
- Final validation passes

### Benefits of Staged Approach

- **Cognitive Load Reduction:** Each agent handles focused tasks
- **Quality Improvement:** Specialized attention to each aspect
- **Cost Efficiency:** Smaller, focused prompts
- **Debugging Clarity:** Issues traceable to specific stages

## Context Retrieval Strategy

### Search-Based Context Assembly with SQLite Optimization

**Primary Context Mechanism:**
```python
class SQLiteSearchIndex:
    """
    High-performance search using SQLite's FTS5 full-text search engine.
    Provides sub-second search across entire manuscripts.
    """
    
    def _initialize_schema(self):
        """Create FTS5 virtual tables for efficient search"""
        self.conn.executescript("""
            -- Main content search table
            CREATE VIRTUAL TABLE IF NOT EXISTS scene_search USING fts5(
                scene_id,
                content,
                characters,  -- Denormalized for speed
                locations,   -- Denormalized for speed
                objects,     -- Denormalized for speed
                tokenize='porter unicode61'
            );
            
            -- Metadata search table
            CREATE VIRTUAL TABLE IF NOT EXISTS metadata_search USING fts5(
                scene_id,
                plot_beats,
                emotional_beats,
                narrative_purpose
            );
            
            -- Position tracking for narrative distance
            CREATE TABLE IF NOT EXISTS scene_positions (
                scene_id TEXT PRIMARY KEY,
                chapter_num INTEGER,
                scene_num INTEGER,
                absolute_position INTEGER,
                word_count INTEGER
            );
            
            -- Create indices for fast lookups
            CREATE INDEX IF NOT EXISTS idx_position ON scene_positions(absolute_position);
            CREATE INDEX IF NOT EXISTS idx_chapter ON scene_positions(chapter_num, scene_num);
        """)
```

### Three-Stage Context Pipeline

**Stage 1: RawContextRetrieval**
- Ultra-fast FTS5 search
- Returns everything potentially relevant (100+ items)
- No intelligence, pure retrieval
- Performance: <50ms for full manuscript

**Stage 2: ComputationalContextFilter**
- All digital humanities pre-processing
- Temporal relevance scoring
- Entity overlap analysis
- Lexical similarity computation
- Narrative distance calculation
- Reduces 100+ items to ~20 items
- Performance: <200ms per scene

**Stage 3: NarrativeIntelligenceRanker**
- LLM-based final curation for meaning
- Emotional resonance scoring
- Plot significance weighting
- Thematic relevance analysis
- Character relationship importance
- Reduces 20 items to 5-7 most meaningful
- Cost Optimization: 80-90% token reduction

## Digital Humanities Integration

### Computational Analysis Layer

Digital humanities techniques provide zero-cost, instant analysis that pre-filters expensive LLM operations:

**Core Components:**
```python
class DigitalHumanitiesCore:
    """Centralized DH capabilities enhancing multiple agents"""
    
    def __init__(self):
        self.voice_fingerprinter = VoiceFingerprinter()
        self.repetition_analyzer = RepetitionAnalyzer()
        self.quality_gates = ComputationalQualityGates()
        self.context_filter = ComputationalContextFilter()
        self.pacing_analyzer = NarrativePacingAnalyzer()
```

**Key DH Components:**

### VoiceFingerprinter
- Statistical character voice analysis
- Sentence length, formality, vocabulary richness tracking
- Modal verb usage patterns
- Cost: $0.00 vs $0.50 LLM analysis
- Performance: <200ms baseline creation, <50ms validation

### RepetitionAnalyzer
- Detects repeated phrases and patterns
- Identifies overused words
- Calculates sentence/paragraph similarity
- Cost: $0.00 vs $0.20 LLM analysis
- Performance: <100ms per scene

### ComputationalQualityGates
- Dialogue ratio analysis
- Sentence variety scoring
- Readability metrics
- Paragraph balance checking
- Performance: <50ms per scene

### Cost Impact

**Without DH:** $240-430 per manuscript
**With DH Stage 1:** $110-250 per manuscript (46-58% reduction)
- Computational pre-filtering: 60-70% quality loop reduction
- Context optimization: 80-90% token reduction
- Voice analysis: $0 vs $0.50 per check

## Scene Metadata Architecture

### Metadata as Change Detection Contracts (Minimized)

**Minimal Metadata Contract (YAML):**
```yaml
# scene-3-metadata.yaml
scene_id: "chapter_3_scene_2"

# Only critical plot-level data that can't be inferred
core_contract:
  plot_beats: ["Mary discovers the letter", "Confronts John about betrayal"]
  narrative_purpose: "reveal_betrayal"
  
# Dependencies that affect generation order
dependencies:
  requires_scenes: ["chapter_2_scene_4"]
  
# Human-curated critical elements ONLY
critical_overrides:
  fathers_ring:
    importance: "critical"
```

### Metadata Inference Engine

```python
class MetadataInferenceEngine:
    """
    Infers metadata from scene content on-demand rather than storing everything.
    Dramatically reduces metadata file complexity.
    """
    
    def infer_scene_metadata(self, scene_content: str, minimal_metadata: dict) -> dict:
        """
        Combines minimal stored metadata with inferred data.
        Called just-in-time when agents need full context.
        """
        inferred = {
            "characters_present": self._extract_characters(scene_content),
            "locations": self._extract_locations(scene_content),
            "objects_mentioned": self._extract_objects(scene_content),
            "emotional_tone": self._analyze_tone(scene_content),
            "scene_length": len(scene_content.split()),
            "dialogue_percentage": self._calculate_dialogue_ratio(scene_content)
        }
        
        # Merge with minimal stored metadata
        return {**inferred, **minimal_metadata}
```

## Change Management System

### Three-Tier Strategy Selection

The system intelligently chooses between strategies based on **impact analysis** of user edits:

#### 1. Surgical Editing
**When:** Few affected scenes, isolated changes
**Criteria:** <10% of scenes affected, scattered distribution, surface-level changes
**Examples:** 
- Character name change across 15 scattered scenes
- Dialogue style consistency fixes
- Minor plot detail corrections

#### 2. Partial Regeneration
**When:** Contiguous block of affected scenes  
**Criteria:** 10-70% of scenes affected, clustered distribution, structural changes
**Examples:**
- Plot twist in chapter 6 affects chapters 6-12
- Character arc change affects middle third of book
- Setting expansion affects specific story section

#### 3. Full Regeneration
**When:** Widespread/fundamental changes affecting most of manuscript
**Criteria:** >70% of scenes affected, core concept/character changes
**Examples:**
- Core concept change affects 80% of scenes
- Protagonist personality overhaul
- Genre shift (fantasy → sci-fi)

### Change Strategy Decision Matrix

```python
def determine_change_strategy(impact_analysis: ImpactAnalysis) -> ChangeStrategy:
    """Intelligent strategy selection based on impact analysis"""
    affected_percentage = impact_analysis.affected_scenes / impact_analysis.total_scenes
    distribution = impact_analysis.get_distribution_pattern()  # scattered, clustered, widespread
    change_depth = impact_analysis.get_change_depth()  # surface, structural, fundamental
    
    if affected_percentage < 0.1 and distribution == "scattered":
        return ChangeStrategy.SURGICAL
    elif affected_percentage < 0.7 and distribution == "clustered": 
        return ChangeStrategy.PARTIAL
    else:
        return ChangeStrategy.FULL_REGENERATION
```

## Configuration Management System

### Master Configuration Structure

```python
class PlotWeaverConfig(BaseModel):
    """Master configuration for PlotWeaver"""
    
    # Sub-configurations
    narrative: NarrativeIntelligenceConfig
    quality: QualityLoopConfig
    generation: SceneGenerationConfig
    search: SearchConfig
    setting: SettingConfig
    
    # Global settings
    project_root: str
    enable_telemetry: bool = False
    log_level: str = "INFO"
    
    # Model settings
    primary_model: str = "gpt-4"
    fast_model: str = "gpt-3.5-turbo"
    embedding_model: str = "text-embedding-ada-002"
```

### Key Configuration Sections

**NarrativeIntelligenceConfig:**
- Context ranking parameters (max items, weighting)
- Distance calculation settings
- Thread management options

**QualityLoopConfig:**
- Restart logic controls
- Agent specialization toggles
- Processing limits

**SceneGenerationConfig:**
- Dynamic rhythm settings
- Word count ranges
- Staged enrichment toggles
- Lean narrative mode

**SettingConfig:**
- Elaboration mode (progressive/front_loaded/minimal)
- Detail level defaults
- Template usage options
- Just-in-time discovery settings

## Enhanced Scene Generation Pipeline

### Complete Staged Implementation

```python
class EnhancedSceneGenerationPipeline:
    """
    Implements staged enrichment pattern for scene generation.
    """
    
    def generate_scene(self, scene_spec: SceneSpecification) -> Scene:
        # Stage 1: Context Assembly (with DH pre-filtering)
        raw_context = self.search_manager.get_all_context(scene_spec)
        computationally_filtered = self.dh_core.context_filter.pre_filter(raw_context)
        ranked_context = self.narrative_ranker.rank_by_significance(computationally_filtered)
        
        # Stage 2: Rhythm Determination
        rhythm_spec = self.rhythm_orchestrator.determine_optimal_length(scene_spec)
        
        # Stage 3: Lean Narrative Generation
        lean_scene = self.scene_writer.generate_lean_narrative(
            plot_beats=scene_spec.plot_beats,
            character_actions=scene_spec.required_actions,
            minimal_setting=self.setting_repo.get_minimal_markers(scene_spec.location),
            rhythm_spec=rhythm_spec
        )
        
        # Stage 4: Environmental Enhancement
        enriched_scene = self.setting_enrichment.add_environmental_details(
            lean_scene=lean_scene,
            location_details=self.setting_repo.get_full_location(scene_spec.location),
            cultural_context=self.setting_repo.get_cultural_context(scene_spec.culture)
        )
        
        # Stage 5: Character Enhancement Pipeline
        scene_with_voice = self.voice_agent.enhance_dialogue_authenticity(enriched_scene)
        scene_with_body = self.body_language_agent.add_physical_manifestations(scene_with_voice)
        scene_with_subtext = self.subtext_agent.add_unspoken_tensions(scene_with_body)
        
        # Stage 6: Continuity Validation
        scene_with_continuity = self.physical_continuity.ensure_consistency(scene_with_subtext)
        final_scene = self.atmospheric_continuity.verify_sensory_consistency(scene_with_continuity)
        
        # Stage 7: Quality Orchestration
        if self.quality_orchestrator.requires_restart(final_scene):
            return self.handle_quality_restart(final_scene)
            
        return final_scene
```

## Human-AI Collaboration Workflows

### Conflict Resolution Process

**Priority Order for Conflict Resolution:**
1. **Concept/Genre changes** (affects entire manuscript)
2. **Plot structure changes** (affects chapter sequences)  
3. **Character profile changes** (affects character-dependent scenes)
4. **Scene-level changes** (affects individual scenes)

### Scene Approval Workflow

**HumanReviewInterface provides:**
- Scene content with change highlighting
- Metadata contract compliance status
- Dependency impact visualization
- Options: approve_as_is, request_edits, regenerate_scene, edit_dependencies

### Change Transaction System

**For complex multi-step changes:**
- Stage changes in dependency order
- Provide rollback capability
- Track progress through workflow
- Allow abandonment with checkpoint restoration

## Performance & Cost Targets

### Performance Requirements
- Full-text search: <50ms (SQLite FTS5)
- Context assembly: <2 seconds total
- Quality gates: <50ms computational, <5s LLM
- Scene generation: <90 seconds including quality loops
- Memory usage: <50MB for 100-scene novels

### Cost Model
- **Base generation:** $150-200 per 80,000-word novel
- **Without optimizations:** $240-430 per manuscript
- **With DH + staged enrichment:** $110-250 per manuscript (46-58% reduction)

## Key Architectural Advantages

**Complexity Management:**
- Staged enrichment reduces cognitive load
- Metadata contracts make change detection feasible
- Progressive elaboration handles organic growth
- Clear dependency boundaries prevent analysis paralysis

**Scalability & Collaboration:**
- Git-native storage enables unlimited scaling
- Scene-based architecture minimizes merge conflicts
- Modular components support future import/export
- Version control integration provides complete audit trails

**User Experience:**
- Writers focus on story while system handles consistency
- Transparent dependency tracking shows change implications
- Flexible intervention points allow human oversight
- Professional workflow scales from individual writers to teams

## Conclusion

PlotWeaver represents a fundamental advancement in AI-assisted creative tools - evolving from "AI writes content" to "AI manages creative complexity with professional-grade quality control and performance optimization." 

The combination of **git-native storage**, **progressive setting elaboration**, **staged enrichment**, **digital humanities optimization**, and **intelligent dependency management** creates a platform that supports both initial manuscript generation and long-term collaborative development with unprecedented quality and efficiency.