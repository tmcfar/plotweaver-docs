# PlotWeaver: Agent System & Coordination

*This document details the agent architecture and workflow systems for PlotWeaver. See [PlotWeaver Architecture Design](PlotWeaver-Architecture-Design.md) for core architectural principles.*

## Agent Architecture & Workflow

### Core Architecture Principle: Simple Pipeline, Sophisticated Analysis

- **Clear pipeline stages** with well-defined boundaries
- **Deep analysis within each domain** using DH enhancements
- **No overlapping responsibilities** between agents
- **Modular sophistication** - each agent is absolute authority in its domain

### Agent Classification & Permission System

**Creative Agents (High Permission, Decision Authority):**
- **ConceptAgent:** Story concept development
- **PlotAgent:** Chapter and scene outline generation with metadata contracts
- **CharacterAgent:** Character profile generation with classification system
- **SettingAgent:** World-building with 5-agent hierarchy
- **SceneWriterAgent:** Lean narrative generation (plot + actions + dialogue)

**Quality/Enhancement Agents (Restricted Permission, Enhance & Fix):**
- **SettingEnrichmentAgent:** Environmental detail enhancement
- **CharacterVoiceAgent:** Dialogue authenticity specialization
- **CharacterBodyLanguageAgent:** Non-verbal communication
- **CharacterSubtextAgent:** Unspoken tensions and implications
- **PhysicalContinuityAgent:** Concrete facts and object tracking
- **AtmosphericContinuityAgent:** Environmental and sensory consistency
- **StyleConsistencyAgent:** Narrative style pattern enforcement
- **PlotBeatValidator:** Scene-level plot beat execution
- **SceneFlowValidator:** Scene-to-scene transitions
- **NarrativeCoherenceValidator:** Full-manuscript story logic
- **MetadataValidationAgent:** YAML syntax and schema validation

### Agent Permission Matrix

**Permission Philosophy: Restrictive**
- Agents can edit anything EXCEPT explicitly forbidden fields
- Creative agents have broader permissions and decision authority
- Quality agents have constrained permissions focused on their validation scope

**Creative Agent Permissions:**
```yaml
PlotAgent:
  allowed_sections: ["static_metadata", "critical_elements", "search_context", "dependencies"]
  can_modify_importance: true  # Can promote/demote element importance
  can_create_critical_elements: true
  forbidden_sections: []

SceneWriterAgent:
  allowed_sections: ["dynamic_elements", "critical_elements", "search_context"]
  can_modify_importance: true  # Starts items at minor, can promote incrementally
  can_create_critical_elements: true
  default_importance: "minor"  # New elements start at minor level
  forbidden_sections: ["static_metadata.plot_beats", "dependencies"]
```

**Quality Agent Permissions:**
```yaml
SettingEnrichmentAgent:
  allowed_sections: ["descriptive_elements", "sensory_details", "atmosphere"]
  can_modify_importance: false
  can_create_elements: true  # Can add environmental details
  forbidden_sections: ["plot_beats", "character_actions", "dialogue"]

PhysicalContinuityAgent:
  allowed_sections: ["critical_elements.*.current_state", "critical_elements.*.description", "search_context.objects"]
  can_modify_importance: false  # Cannot decide narrative importance
  can_create_elements: true  # Can add newly discovered objects/states
  forbidden_sections: ["static_metadata", "dependencies", "critical_elements.*.importance"]
```

## Creative Agents (High Permission, Decision Authority)

### ConceptAgent
**Function:** Story concept development and foundational narrative structure
**Permissions:** Full creative authority, can create critical elements
**Output:** Multiple concept options with dependency implications
**Relationships:** 
- Feeds into → PlotAgent (provides concept foundation)
- Creates → `plot/concept.yaml` in git

### PlotAgent  
**Function:** Chapter and scene outline generation with metadata contracts
**Execution Pattern:** Multi-call (plot summary → chapter outline → scene outlines)
**Permissions:** Can modify importance levels, create critical elements, full metadata access
**Importance Authority:** Can create elements at any importance level when plot-significant
**Relationships:**
- Receives from → ConceptAgent (story concept)
- Feeds into → SceneWriterAgent (scene specifications)
- Creates → Scene metadata contracts with plot beats
- Triggers → CharacterAgent, SettingAgent for new elements

### CharacterAgent
**Function:** Character profile generation with classification system
**Classification:** Protagonist, antagonist, deuteragonist, supporting, dynamic
**Storage:** Git-based with YAML files
**Permissions:** Full character profile management
**Relationships:**
- Triggered by → PlotAgent (new characters in outline)
- Triggered by → SceneWriterAgent (new characters discovered)
- Feeds into → All character quality agents
- Creates → `characters/*.yaml` files

### SettingAgent (with 5-Agent Hierarchy)
**Function:** Comprehensive world-building coordination with user-driven selective population
**Permissions:** Full world-building authority and sub-agent coordination
**User Integration:** Accepts importance ratings (High/Medium/Low/Skip) and standard templates vs. custom freeform input
**Progressive Elaboration:** Supports just-in-time location discovery

**Sub-Agent Hierarchy:**

#### WorldPhysicsAgent (merged Geography + Systems)
**Function:** Physical world rules, natural laws, and environmental systems
**Output:** Climate patterns, terrain, natural resources, magic/tech rules, physical constraints
**Templates:** "Earth-like Physics", "High Magic World", "Hard Sci-Fi Universe", "Hybrid Reality"
**When Run:** Based on user importance rating + when physics questions arise

#### LocationsAgent  
**Function:** Specific places and detailed geographical features
**Output:** Cities, buildings, regions, specific landmarks, travel routes
**Templates:** "Medieval Towns", "Modern Cities", "Fantasy Realms", "Space Stations"
**Progressive Mode:** Creates locations just-in-time as scenes reference them

#### CulturePoliticsAgent (merged Culture + Politics)
**Function:** Societies, governments, belief systems, power structures
**Output:** Cultural profiles, political systems, social hierarchies, traditions, conflicts
**Templates:** "Medieval Feudalism", "Corporate Dystopia", "Tribal Federation", "Democratic Republic"

#### HistoryAgent  
**Function:** Timeline creation, historical events, cause-and-effect chains
**Output:** Historical timelines, past events affecting current story, foundational myths
**Templates:** "Ancient Civilizations", "Recent Conflicts", "Technological Evolution", "Magical History"

#### SettingStyleAgent
**Function:** Narrative style elements and world-specific linguistic patterns
**Output:** Dialect patterns, fantasy terminology, cultural speech patterns, narrative voice rules
**Examples:** Formal address systems, magic terminology consistency, cultural idioms
**Feeds:** StyleConsistencyAgent for enforcement

### SceneWriterAgent
**Function:** Generate lean narrative focusing on plot, character actions, and essential dialogue
**Focus:** Story beats and character dynamics, not environmental details
**Permissions:** Can create/promote element importance, modify dynamic elements
**Context Access:** Enhanced with three-stage context pipeline
**Receives:** Minimal setting markers (location type, cultural context, time)
**Output:** Story-focused scene, deliberately under-detailed for enrichment
**Word Count:** Determined by SceneRhythmOrchestrator (400-1500 words)
**Relationships:**
- Receives from → PlotAgent (scene specifications)
- Receives from → Context pipeline (filtered, ranked context)
- Triggers → CharacterAgent, SettingAgent (new elements)
- Feeds into → SettingEnrichmentAgent
- Enhanced by → StyleCalibrationAgent, SceneRhythmOrchestrator

## Quality/Enhancement Agents (Restricted Permission, Enhance & Fix)

### Environmental Enhancement

#### SettingEnrichmentAgent
**Function:** Add setting-specific details to lean narrative
**Domain Boundaries:**
- Adds: Environmental details, cultural markers, sensory elements, atmosphere
- Never touches: Plot events, character actions, dialogue content
**Permissions:** Can add descriptive elements, cannot change story structure
**Integration:** Uses SettingRepository for location/culture data
**Examples:**
- Adds: "smoky interior," "sounds of clinking mugs," "morning mist"
- Enriches: Sparse rooms with appropriate furnishings
- Applies: Cultural decorations, architectural details
**Relationships:**
- Receives from → SceneWriterAgent (lean scene)
- Uses → SettingRepository for location/culture data
- Feeds into → CharacterVoiceAgent
- Coordinates with → AtmosphericContinuityAgent

### Micro-Specialized Character Agents

#### CharacterVoiceAgent
**Function:** ONLY dialogue authenticity and voice consistency
**Domain Boundaries:** 
- Analyzes: Words spoken in dialogue, speech patterns, vocabulary
- Never touches: Body language, narrative description, actions
**DH Enhancement:** VoiceFingerprinter for statistical voice consistency
**Sophistication:**
- Emotional tone progression in dialogue
- Linguistic pattern consistency
- Dialect/accent maintenance
- Modal verb usage patterns
**Performance:** <100ms computational analysis vs $0.50 LLM checks
**Relationships:**
- Receives from → SettingEnrichmentAgent
- Feeds into → CharacterBodyLanguageAgent
- Enhanced by → StyleCalibrationAgent learning

#### CharacterBodyLanguageAgent  
**Function:** ONLY non-verbal communication and physical manifestations
**Domain Boundaries:**
- Analyzes: Gestures, posture, micro-expressions, physical tells
- Never touches: Dialogue content, internal thoughts, narrative voice
**Sophistication:**
- Character-specific gesture vocabulary
- Physical manifestations of emotion
- Breathing and tension descriptions
- Consistent mannerism tracking
**Relationships:**
- Receives from → CharacterVoiceAgent
- Feeds into → CharacterSubtextAgent
- Coordinates with → AtmosphericContinuityAgent

#### CharacterSubtextAgent
**Function:** ONLY unspoken tensions and implications
**Domain Boundaries:**
- Analyzes: What's not being said, power dynamics, hidden meanings
- Never touches: Direct dialogue edits, physical descriptions
**Sophistication:**
- Unspoken history references
- Contextual irony and sarcasm
- Power dynamic shifts
- Emotional undercurrents
**Relationships:**
- Receives from → CharacterBodyLanguageAgent  
- Feeds into → PhysicalContinuityAgent
- Final character enhancement pass

### Physical World Continuity

#### PhysicalContinuityAgent (renamed from ContinuityAgent)
**Function:** Concrete, measurable facts and object tracking
**Domain Boundaries:**
- Tracks: Object locations, character appearance, spatial relationships, physical states
- Never touches: Subjective experiences, atmosphere, emotions
**DH Enhancement:** ComputationalQualityGates, RepetitionAnalyzer
**Examples:**
- The gun is in the drawer (not on the table)
- Mary wears a red shirt (not blue)
- The window is broken (not intact)
- John sits across from (not next to) Sarah
**Relationships:**
- Receives from → Character enhancement pipeline
- Coordinates with → AtmosphericContinuityAgent
- Updates → Scene metadata for consistency
- Feeds into → Structural validation

#### AtmosphericContinuityAgent (renamed from SensoryContinuityAgent)
**Function:** Environmental and sensory experience consistency
**Domain Boundaries:**
- Tracks: Weather, lighting, sounds, smells, temperature, emotional atmosphere
- Never touches: Concrete object states, measurable facts
**Sophistication:**
- Weather progression modeling
- Acoustic environment tracking
- Olfactory memory
- Emotional atmosphere evolution
**Relationships:**
- Receives from → SettingAgent (location profiles)
- Coordinates with → PhysicalContinuityAgent
- Validates → SettingEnrichmentAgent additions
- Tracks sensory profiles across scenes

### Style Consistency

#### StyleConsistencyAgent
**Function:** Narrative style pattern enforcement
**Authority:** Reports to SettingStyleAgent for world-specific patterns
**Execution Pattern:** Validate → Analyze → Escalate if ambiguous
**Decision Logic:** 
- **Auto-fix:** Clear violations with no narrative justification
- **Approve:** Context justifies style deviation
- **Escalate:** Cannot determine if deviation is intentional
**Relationships:**
- Receives patterns from → SettingStyleAgent
- Validates → All agent outputs for style consistency
- Runs in → Quality loop alongside other validators
- Escalates to → HumanReviewInterface for ambiguous cases

### Story Structure Validation

#### PlotBeatValidator (renamed from BeatExecutionAgent)
**Function:** Validate scenes contain promised plot beats
**Domain:** Scene-level plot beat execution
**Sophistication:** Semantic matching of beat intentions vs actual content
**Relationships:**
- Validates → SceneWriterAgent output
- Checks against → PlotAgent specifications
- Feeds into → SceneFlowValidator

#### SceneFlowValidator (renamed from ProfluenceAgent)
**Function:** Scene-to-scene transitions and momentum
**Domain:** Inter-scene connections and pacing
**Sophistication:** Tension curves, pacing analysis, momentum tracking
**Relationships:**
- Runs parallel to → PlotBeatValidator
- Validates → Scene transitions
- Feeds into → NarrativeCoherenceValidator

#### NarrativeCoherenceValidator (renamed from NarrativeCoherenceAgent)
**Function:** Full-manuscript story logic and consistency
**Domain:** Manuscript-wide causality and timeline
**Sophistication:** Causal chain validation, timeline consistency, plot hole detection
**Relationships:**
- Final structural validation
- Validates → Overall narrative integrity
- Uses → Dependency graph

#### MetadataValidationAgent
**Function:** YAML syntax and schema validation
**Integration:** Works with MetadataManager for I/O operations
**Auto-fix:** AI-powered syntax correction (2 attempts)
**Relationships:**
- Validates → All agent metadata outputs
- Triggers → AI auto-fix for YAML syntax errors
- Escalates to → Human review on failure

## Advanced Intelligence Systems

### Context Intelligence Pipeline (3-Stage Architecture)

#### Stage 1: RawContextRetrieval (SQLiteSearchIndex)
**Function:** Ultra-fast full-text search with zero intelligence
**Performance:** <50ms for full manuscript
**Output:** Everything potentially relevant (100+ items)
**Technology:** SQLite FTS5 with positional indices
**Relationships:**
- Serves → ComputationalContextFilter
- Indexed by → Scene content updates

#### Stage 2: ComputationalContextFilter
**Function:** All digital humanities pre-processing
**Reduces:** 100+ items to ~20 items
**DH Analysis:**
- Temporal relevance scoring
- Entity overlap analysis
- Lexical similarity computation
- Narrative distance calculation
**Performance:** <200ms per scene
**Relationships:**
- Receives from → RawContextRetrieval
- Feeds into → NarrativeIntelligenceRanker

#### Stage 3: NarrativeIntelligenceRanker
**Function:** LLM-based final curation for meaning
**Reduces:** 20 items to 5-7 most meaningful
**Intelligence:**
- Emotional resonance scoring
- Plot significance weighting
- Thematic relevance analysis
- Character relationship importance
**Cost Optimization:** 80-90% token reduction
**Relationships:**
- Final context curation
- Serves → SceneWriterAgent enhanced context

### Orchestration & Management

#### IntelligentQualityOrchestrator
**Function:** Impact-based restart decisions
**Algorithm:** Analyzes change impact to determine restart necessity
**Efficiency:** 60% reduction in quality loop iterations
**Decision Types:**
- NO_RESTART: Trivial changes
- TARGETED_RESTART: Specific agents only
- SELECTIVE_RESTART: Identified affected agents
- FULL_RESTART: Major changes
**Relationships:**
- Manages → Quality agent restart cycles
- Analyzes → Change impact for restart necessity
- Coordinates → QualityLoopManager

#### QualityLoopManager
**Function:** Enforces restart limits and dependencies
**Constraints:** Maximum 3 restart cycles
**Safety:** Prevents infinite loops
**Dependency Matrix:** Fallback for restart chains
**Relationships:**
- Managed by → IntelligentQualityOrchestrator
- Enforces → Agent permission boundaries
- Prevents → Infinite restart loops

#### StyleCalibrationAgent
**Function:** Learns from human approval patterns
**Learning:** Extracts patterns from approved/rejected content
**Application:** Enhances future generation quality
**Pattern Types:**
- Approved dialogue patterns
- Rejected style elements
- Genre-specific preferences
**Relationships:**
- Learns from → HumanReviewInterface decisions
- Enhances → SceneWriterAgent prompts
- Improves → CharacterVoiceAgent output quality

### Rhythm & Thread Management

#### SceneRhythmOrchestrator (DynamicSceneRhythm)
**Function:** Determines optimal scene length based on narrative position
**Range:** 400-1500 words
**Patterns:** 
- Short scenes (400-600 words) for climactic moments
- Standard scenes (800-1200 words) for regular narrative
- Longer scenes (1200-1500 words) for exposition
- Breathing room (600-800 words) after intensity
**Relationships:**
- Configures → SceneWriterAgent generation parameters
- Considers → Narrative arc position
- Prevents → Monotonous pacing

#### NarrativeThreadManager
**Function:** Tracks foreshadowing and callbacks
**Scope:** Setup/payoff relationships, theme development
**Capabilities:**
- Thread planting suggestions
- Payoff opportunity identification
- Theme consistency tracking
**Relationships:**
- Analyzes → Cross-scene narrative threads
- Suggests → Thread resolution opportunities
- Coordinates with → NarrativeCoherenceValidator

## Dependency Management Agents

### ChangeDetectionAgent
**Function:** Identifies semantic differences in edited content
**Scope:** Git diff analysis, metadata contract violations
**Capabilities:**
- Semantic diff analysis
- Contract violation detection
- Change classification
**Relationships:**
- Triggers on → Git commits with content changes
- Feeds → ImpactAnalysisAgent
- Validates → Metadata contract compliance

### ImpactAnalysisAgent  
**Function:** Determines downstream effects and strategy selection
**Output:** Three-tier strategy (surgical, partial, full regeneration)
**Analysis Types:**
- Distribution pattern (scattered/clustered/widespread)
- Change depth (surface/structural/fundamental)
- Affected percentage calculation
**Relationships:**
- Receives from → ChangeDetectionAgent
- Analyzes → Dependency graph impacts
- Feeds → ConflictResolutionAgent

### ConflictResolutionAgent
**Function:** Presents conflicts and resolution options to humans
**Workflow:** Priority-ordered, consequence visualization
**Conflict Types:**
- Plot structure conflicts
- Character consistency issues
- Setting violations
**Relationships:**
- Receives from → ImpactAnalysisAgent
- Interfaces with → HumanReviewInterface
- Manages → ChangeTransactionManager

## Infrastructure & Support

### Digital Humanities Core
**Function:** Centralized DH capabilities enhancing multiple agents
**Components:**
- VoiceFingerprinter → Enhances CharacterVoiceAgent
- RepetitionAnalyzer → Enhances PhysicalContinuityAgent
- ComputationalQualityGates → Pre-filters quality checks
- NarrativePacingAnalyzer → Enhances rhythm decisions
- ComputationalContextFilter → Enhances context pipeline
**Architecture:** Single source of DH intelligence, multiple agent consumers
**Performance:** All DH operations <200ms

### Setting Infrastructure

#### SettingRepository
**Function:** Centralized setting access with progressive elaboration
**Capabilities:**
- Template management
- Just-in-time location creation
- Cultural rule access
- Setting caching
**Storage:**
- Templates in `world/templates/`
- Instances in `world/locations/`
- Cultural data in `world/cultures/`
**Relationships:**
- Serves → SettingEnrichmentAgent
- Serves → SceneWriterAgent (minimal markers)
- Manages → Progressive elaboration

### Metadata System

#### MetadataManager
**Function:** Centralized YAML I/O and validation
**Responsibilities:**
- All file operations
- Schema validation
- Syntax checking
- AI auto-fix coordination
**Relationships:**
- Handles → All metadata file operations
- Works with → MetadataValidationAgent
- Integrates → MetadataInferenceEngine

#### MetadataInferenceEngine  
**Function:** Just-in-time metadata generation from content
**Efficiency:** 80% storage reduction
**Inference Types:**
- Character extraction from dialogue
- Location inference from descriptions
- Object tracking from mentions
- Emotional tone analysis
**Called by:** MetadataManager when full metadata needed

### Search Infrastructure

#### SQLiteSearchIndex
**Function:** High-performance full-text search
**Technology:** SQLite FTS5
**Performance:** <50ms full manuscript search
**Indexed Data:**
- Scene content
- Character mentions
- Location references
- Object appearances

#### SearchCacheManager
**Function:** Two-tier caching for search results
**Performance:** 70-80% cache hit rate
**Architecture:** Hot cache (50 items) + Warm cache (200 items)
**Cache Strategy:**
- Hot cache for current session
- Warm cache for broader context
- Pattern tracking for optimization

### User Interaction

#### ActivityStream
**Function:** Real-time hierarchical progress display
**Shows:** Agent decisions, modifications, reasoning
**Format:** Tree structure with operation status
**Detail Levels:** Minimal, standard, full
**Relationships:**
- Integrates with → All agents for progress reporting
- Displays → Quality loop restart reasoning
- Shows → Agent modification rationale

#### HumanReviewInterface
**Function:** Scene approval workflow
**Features:** 
- Diff display
- Dependency warnings
- Metadata contract status
- Edit integration
**Workflow Options:**
- Approve as-is
- Request edits
- Regenerate scene
- Edit dependencies
**Integration:** Feeds StyleCalibrationAgent

### Configuration

#### ConfigurationManager
**Function:** Centralized configuration with hot-reload
**Validation:** Pydantic schemas
**Flexibility:** Environment-specific overrides
**Hot-reload:** Watches for configuration changes
**Relationships:**
- Manages → All agent configurations
- Validates → Configuration changes
- Notifies → Components of updates

#### PlotWeaverConfig
**Function:** Master configuration structure
**Sections:**
- NarrativeIntelligenceConfig
- QualityLoopConfig  
- SceneGenerationConfig
- SearchConfig
- SettingConfig
**Environment Overrides:**
- Development: Fast iteration settings
- Production: Full quality settings
- Testing: Predictable outputs

#### AgentPermissionManager
**Function:** Enforces agent boundary restrictions
**Rules:** Creative agents high permission, Quality agents restricted
**Validation:** Pre-execution permission checks
**Relationships:**
- Validates → All agent operations
- Enforces → Metadata modification restrictions
- Prevents → Unauthorized cross-agent operations

### Transaction Management

#### ChangeTransactionManager
**Function:** Staged change execution with rollback
**Features:**
- Dependency ordering
- Atomic commits
- Progress tracking
- Rollback capability
**Use Cases:**
- Complex multi-scene changes
- Plot restructuring
- Character arc modifications
**Relationships:**
- Managed by → ConflictResolutionAgent
- Executes → Multi-step changes
- Provides → Checkpoint restoration

## Agent Execution Order

### Setting Phase (Run Once)
1. ConceptAgent → Creates story concept
2. PlotAgent (1st call) → Setting-agnostic plot summary
3. SettingAgent → User rates importance, relevant sub-agents run
4. CharacterAgent → Initial character profiles
5. PlotAgent (2nd call) → Chapter outlines
6. CharacterAgent → Refined profiles based on plot
7. PlotAgent (3rd call) → Scene-level outlines with metadata

### Writing Phase (Per Scene)
1. **Context Pipeline:** RawContextRetrieval → ComputationalContextFilter → NarrativeIntelligenceRanker
2. **Rhythm:** SceneRhythmOrchestrator determines optimal length
3. **Generation:** SceneWriterAgent creates lean narrative (plot + actions + essential dialogue)
4. **Environmental Enhancement:** SettingEnrichmentAgent adds setting details
5. **Character Polish:** CharacterVoiceAgent → CharacterBodyLanguageAgent → CharacterSubtextAgent  
6. **Continuity:** PhysicalContinuityAgent → AtmosphericContinuityAgent → StyleConsistencyAgent
7. **Validation:** PlotBeatValidator → SceneFlowValidator → NarrativeCoherenceValidator
8. **Metadata:** MetadataValidationAgent
9. **Orchestration:** IntelligentQualityOrchestrator manages any restarts

### Change Detection (Post-Edit)
1. ChangeDetectionAgent → Analyzes git diffs
2. ImpactAnalysisAgent → Determines change strategy
3. ConflictResolutionAgent → Presents options to human
4. ChangeTransactionManager → Executes approved changes

## Key Design Principles

1. **Domain Authority:** Each agent is absolute authority in its domain
2. **No Overlap:** Agents never modify another agent's domain  
3. **Pipeline Clarity:** Fixed stages, configurable depth
4. **DH Enhancement:** Computational analysis reduces costs and improves quality
5. **Human Control:** All major decisions surface to humans
6. **Progressive Elaboration:** Start minimal, expand as needed
7. **Staged Enrichment:** Reduce cognitive load through specialization

## Cost Model Impact

### Baseline (Without Optimizations)
- Base generation: $150-200 per novel
- Quality loops: $30-60 per scene
- Total: $240-430 per manuscript

### With Architecture Optimizations
- DH pre-filtering: 60-70% quality loop reduction
- Context pipeline: 80-90% token reduction  
- Intelligent restarts: 60% iteration reduction
- Staged enrichment: Smaller, focused prompts
- Total: $110-250 per manuscript (46-58% cost reduction)

### Performance Targets
- Context pipeline: <2 seconds total
- DH analysis: <200ms per operation
- Quality validations: <100ms computational, <5s LLM
- Full scene generation: <90 seconds including quality loops
- Setting elaboration: <500ms for location creation

---

*Related Documents:*
- [PlotWeaver Architecture Design](PlotWeaver-Architecture-Design.md) - Core architecture and technical design
- [PlotWeaver Implementation Plan](PlotWeaver-Implementation-Plan.md) - Development roadmap and execution strategy