# PlotWeaver Agent System Reference

## Core Architecture Principle: Simple Pipeline, Sophisticated Analysis
- **Clear pipeline stages** with well-defined boundaries
- **Deep analysis within each domain** using DH enhancements
- **No overlapping responsibilities** between agents
- **Modular sophistication** - each agent is absolute authority in its domain

## Creative Agents (High Permission, Decision Authority)

### ConceptAgent
**Function:** Story concept development and foundational narrative structure
**Permissions:** Full creative authority, can create critical elements
**Relationships:** 
- Feeds into → PlotAgent (provides concept foundation)
- Creates → `plot/concept.json` in git

### PlotAgent  
**Function:** Chapter and scene outline generation with metadata contracts
**Execution Pattern:** Multi-call (plot summary → chapter outline → scene outlines)
**Permissions:** Can modify importance levels, create critical elements, full metadata access
**Relationships:**
- Receives from → ConceptAgent (story concept)
- Feeds into → SceneWriterAgent (scene specifications)
- Creates → Scene metadata contracts with plot beats
- Triggers → CharacterAgent, SettingAgent for new elements

### CharacterAgent
**Function:** Character profile generation with classification system (protagonist, antagonist, supporting)
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

**Sub-Agent Hierarchy:**

#### WorldPhysicsAgent (merged Geography + Systems)
**Function:** Physical world rules, natural laws, and environmental systems
**Output:** Climate patterns, terrain, natural resources, magic/tech rules, physical constraints
**Templates:** "Earth-like Physics", "High Magic World", "Hard Sci-Fi Universe", "Hybrid Reality"

#### LocationsAgent  
**Function:** Specific places and detailed geographical features
**Output:** Cities, buildings, regions, specific landmarks, travel routes
**Templates:** "Medieval Towns", "Modern Cities", "Fantasy Realms", "Space Stations"

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

### SceneWriterAgent
**Function:** Generate lean narrative focusing on plot, character actions, and essential dialogue
**Focus:** Story beats and character dynamics, not environmental details
**Permissions:** Can create/promote element importance, modify dynamic elements
**Context Access:** Enhanced with three-stage context pipeline
**Receives:** Minimal setting markers (location type, cultural context, time)
**Output:** Story-focused scene, deliberately under-detailed for enrichment
**Relationships:**
- Receives from → PlotAgent (scene specifications)
- Receives from → Context pipeline (filtered, ranked context)
- Triggers → CharacterAgent, SettingAgent (new elements)
- Feeds into → SettingEnrichmentAgent
- Enhanced by → StyleCalibrationAgent, SceneRhythmOrchestrator

## Quality Agents (Restricted Permission, Validation & Fix)

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

### Character Quality System (Micro-Specialized)

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

### Style Consistency

#### StyleConsistencyAgent
**Function:** Narrative style pattern enforcement
**Authority:** Reports to SettingStyleAgent for world-specific patterns
**Execution Pattern:** Validate → Analyze → Escalate if ambiguous
**Decision Logic:** 
- **Auto-fix:** Clear violations with no narrative justification
- **Approve:** Context justifies style deviation
- **Escalate:** Cannot determine if deviation is intentional

### Story Structure Validation

#### PlotBeatValidator (renamed from BeatExecutionAgent)
**Function:** Validate scenes contain promised plot beats
**Domain:** Scene-level plot beat execution
**Sophistication:** Semantic matching of beat intentions vs actual content

#### SceneFlowValidator (renamed from ProfluenceAgent)
**Function:** Scene-to-scene transitions and momentum
**Domain:** Inter-scene connections and pacing
**Sophistication:** Tension curves, pacing analysis, momentum tracking

#### NarrativeCoherenceValidator (renamed from NarrativeCoherenceAgent)
**Function:** Full-manuscript story logic and consistency
**Domain:** Manuscript-wide causality and timeline
**Sophistication:** Causal chain validation, timeline consistency, plot hole detection

#### MetadataValidationAgent
**Function:** YAML syntax and schema validation
**Integration:** Works with MetadataManager for I/O operations

## Context Intelligence Pipeline (3-Stage Architecture)

### Stage 1: RawContextRetrieval (SQLiteSearchIndex)
**Function:** Ultra-fast full-text search with zero intelligence
**Performance:** <50ms for full manuscript
**Output:** Everything potentially relevant (100+ items)
**Technology:** SQLite FTS5 with positional indices

### Stage 2: ComputationalContextFilter
**Function:** All digital humanities pre-processing
**Reduces:** 100+ items to ~20 items
**DH Analysis:**
- Temporal relevance scoring
- Entity overlap analysis
- Lexical similarity computation
- Narrative distance calculation
**Performance:** <200ms per scene

### Stage 3: NarrativeIntelligenceRanker
**Function:** LLM-based final curation for meaning
**Reduces:** 20 items to 5-7 most meaningful
**Intelligence:**
- Emotional resonance scoring
- Plot significance weighting
- Thematic relevance analysis
- Character relationship importance
**Cost Optimization:** 80-90% token reduction

## Advanced Intelligence Systems

### Orchestration & Management

#### IntelligentQualityOrchestrator
**Function:** Impact-based restart decisions
**Algorithm:** Analyzes change impact to determine restart necessity
**Efficiency:** 60% reduction in quality loop iterations

#### QualityLoopManager
**Function:** Enforces restart limits and dependencies
**Constraints:** Maximum 3 restart cycles
**Safety:** Prevents infinite loops

#### StyleCalibrationAgent
**Function:** Learns from human approval patterns
**Learning:** Extracts patterns from approved/rejected content
**Application:** Enhances future generation quality

### Rhythm & Thread Management

#### SceneRhythmOrchestrator
**Function:** Determines optimal scene length based on narrative position
**Range:** 400-1500 words
**Patterns:** 
- Short scenes for climactic moments
- Longer scenes for exposition
- Breathing room after intensity

#### NarrativeThreadManager
**Function:** Tracks foreshadowing and callbacks
**Scope:** Setup/payoff relationships, theme development

## Dependency Management Agents

### ChangeDetectionAgent
**Function:** Identifies semantic differences in edited content
**Scope:** Git diff analysis, metadata contract violations

### ImpactAnalysisAgent  
**Function:** Determines downstream effects and strategy selection
**Output:** Three-tier strategy (surgical, partial, full regeneration)

### ConflictResolutionAgent
**Function:** Presents conflicts and resolution options to humans
**Workflow:** Priority-ordered, consequence visualization

## Infrastructure & Support

### Digital Humanities Core
**Function:** Centralized DH capabilities enhancing multiple agents
**Components:**
- VoiceFingerprinter → Enhances CharacterVoiceAgent
- RepetitionAnalyzer → Enhances PhysicalContinuityAgent
- ComputationalQualityGates → Pre-filters quality checks
- NarrativePacingAnalyzer → Enhances rhythm decisions
**Architecture:** Single source of DH intelligence, multiple agent consumers

### Metadata System

#### MetadataManager
**Function:** Centralized YAML I/O and validation
**Responsibilities:**
- All file operations
- Schema validation
- Syntax checking
- AI auto-fix coordination

#### MetadataInferenceEngine  
**Function:** Just-in-time metadata generation from content
**Efficiency:** 80% storage reduction
**Called by:** MetadataManager when full metadata needed

### Search Infrastructure

#### SearchCacheManager
**Function:** Two-tier caching for search results
**Performance:** 70-80% cache hit rate
**Architecture:** Hot cache (50 items) + Warm cache (200 items)

### User Interaction

#### ActivityStream
**Function:** Real-time hierarchical progress display
**Shows:** Agent decisions, modifications, reasoning

#### HumanReviewInterface
**Function:** Scene approval workflow
**Features:** Diff display, dependency warnings
**Integration:** Feeds StyleCalibrationAgent

### Configuration

#### ConfigurationManager
**Function:** Centralized configuration with hot-reload
**Validation:** Pydantic schemas
**Flexibility:** Environment-specific overrides

#### AgentPermissionManager
**Function:** Enforces agent boundary restrictions
**Rules:** Creative agents high permission, Quality agents restricted

## Agent Execution Order

### Setting Phase (Run Once)
1. ConceptAgent → PlotAgent → CharacterAgent/SettingAgent → PlotAgent (scene level)

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
1. ChangeDetectionAgent → ImpactAnalysisAgent → ConflictResolutionAgent → Human Review

## Key Design Principles

1. **Domain Authority:** Each agent is absolute authority in its domain
2. **No Overlap:** Agents never modify another agent's domain  
3. **Pipeline Clarity:** Fixed stages, configurable depth
4. **DH Enhancement:** Computational analysis reduces costs and improves quality
5. **Human Control:** All major decisions surface to humans

## Cost Model Impact

### Baseline (Without Optimizations)
- Base generation: $150-200 per novel
- Quality loops: $30-60 per scene
- Total: $240-430 per manuscript

### With Architecture Optimizations
- DH pre-filtering: 60-70% quality loop reduction
- Context pipeline: 80-90% token reduction  
- Intelligent restarts: 60% iteration reduction
- Total: $110-250 per manuscript (46-58% cost reduction)

### Performance Targets
- Context pipeline: <2 seconds total
- Quality validations: <100ms computational, <5s LLM
- Full scene generation: <90 seconds including quality loops