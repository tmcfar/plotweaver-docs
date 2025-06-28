<!-- AI_INSTRUCTIONS: Document working agents and immediate planned features.
     Focus on implemented functionality and near-term roadmap items. -->

# PlotWeaver Agent System Specification

## Overview
PlotWeaver uses a sequential agent pipeline for AI-assisted manuscript generation. Each agent specializes in a specific aspect of story creation, from initial concept through final scene writing.

## Core Architecture Principles

- **Domain Authority**: Each agent is the absolute authority in its specialized domain
- **Sequential Pipeline**: Clear stages with well-defined boundaries and dependencies  
- **No Overlap**: Agents never modify content outside their domain
- **Git Integration**: All agents read from and write to git-based project structure
- **Modular Enhancement**: Agents can be enhanced or replaced without affecting the pipeline

## Agent Classification System

### Creative Agents (High Permission, Decision Authority)
Agents that generate new content and have broad permissions to create story elements.

### Quality/Enhancement Agents (Restricted Permission) 
Agents that enhance, validate, or refine existing content within specific boundaries.

## Working Agent Pipeline (Phases 1-3 Complete)

### ConceptAgent
**Location**: `src/plotweaver/agents/setting/concept_agent.py`  
**Function**: Story concept development and foundational narrative structure  
**Status**:  Implemented and tested  
**Permissions**: Full creative authority, can create critical story elements  

**Execution Pattern**:
- Generates multiple story concept options
- Creates foundational world-building elements
- Establishes genre and tone framework

**Outputs**:
- `plot/concept.yaml` - Core story concept and world foundation
- Initial genre classification and tone guidance

**Relationships**:
- Feeds into ’ PlotAgent (provides concept foundation)
- Creates foundation for ’ CharacterAgent, SettingAgent

### PlotAgent  
**Location**: `src/plotweaver/agents/setting/plot_agent.py`  
**Function**: Chapter and scene outline generation with metadata contracts  
**Status**:  Implemented and tested  
**Permissions**: Can modify importance levels, create critical elements, full metadata access  

**Execution Pattern**: Multi-call progression
1. **Plot Summary**: High-level story arc development
2. **Chapter Outline**: Chapter-by-chapter structure creation  
3. **Scene Outline**: Detailed scene specifications with metadata

**Outputs**:
- `plot/outline.yaml` - Complete story structure
- `plot/chapter-outlines/` - Individual chapter specifications
- Scene metadata contracts with plot beats and dependencies

**Relationships**:
- Receives from ’ ConceptAgent (story concept foundation)
- Feeds into ’ SceneWriterAgent (scene specifications)
- Triggers ’ CharacterAgent, SettingAgent for new story elements

### CharacterAgent
**Location**: `src/plotweaver/agents/setting/character_agent.py`  
**Function**: Character profile generation with classification system  
**Status**:  Implemented and tested  
**Permissions**: Full character profile management and development

**Character Classification**:
- **Protagonist**: Main character(s) driving the story
- **Antagonist**: Primary opposition and conflict sources
- **Deuteragonist**: Secondary main characters with significant roles
- **Supporting**: Characters with specific plot functions
- **Dynamic**: Characters with significant development arcs

**Outputs**:
- `characters/protagonist/*.yaml` - Main character profiles
- `characters/antagonist/*.yaml` - Opposition character profiles  
- `characters/supporting/*.yaml` - Supporting character profiles

**Relationships**:
- Triggered by ’ PlotAgent (new characters in outline)
- Triggered by ’ SceneWriterAgent (new characters discovered during writing)
- Provides profiles for ’ All character quality agents (planned)

### SceneWriterAgent
**Location**: `src/plotweaver/agents/writing/scene_writer_agent.py`  
**Function**: Generate narrative scenes from plot specifications  
**Status**:  Implemented and tested (Phase 4 refactoring in progress)  
**Permissions**: Can create/promote element importance, modify dynamic story elements

**Current Focus**: Full scene generation (800-1500 words)  
**Phase 4 Target**: Lean narrative generation (600-1000 words, plot + actions + dialogue)

**Context Access**:
- Plot specifications from PlotAgent
- Character profiles for scene participants
- Basic setting markers (location type, cultural context, time)

**Outputs**:
- `content/chapters/*/scene-*.md` - Narrative scene content
- `content/chapters/*/scene-*-metadata.yaml` - Scene metadata and dependencies

**Relationships**:
- Receives from ’ PlotAgent (scene specifications)
- Uses ’ Character profiles for authentic dialogue and actions
- Feeds into ’ SettingEnrichmentAgent (Phase 4)
- Can trigger ’ CharacterAgent for newly discovered characters

## Agent Foundation (BaseAgent Pattern)

### BaseAgent
**Location**: `src/plotweaver/agents/base/base_agent.py`  
**Function**: Common agent functionality and interface  
**Status**:  Implemented with 328+ tests passing

**Core Capabilities**:
- Standardized execution pattern
- Error handling and validation
- Context management and state tracking
- Git integration for content persistence
- Progress reporting and logging

**Agent Execution Interface**:
```python
class BaseAgent:
    def execute_agent(self, context: AgentContext) -> AgentResult:
        # Standard agent execution pattern
        # Input validation, prompt building, LLM interaction, result validation
```

## Phase 4: Staged Enrichment (In Progress)

### Current Enhancement: SceneWriterAgent Refactoring
**Goal**: Transform monolithic scene generation into focused narrative creation  
**Status**: = In development  

**Changes**:
- Reduce target word count from 800-1500 to 600-1000 words
- Focus on plot beats, character actions, and essential dialogue
- Remove environmental detail generation (delegated to SettingEnrichmentAgent)
- Maintain story structure while reducing cognitive load

### SettingEnrichmentAgent (Phase 4 - Planned)
**Function**: Add environmental and cultural details to lean narrative  
**Status**: =Ë In development  
**Permissions**: Can add descriptive elements, cannot change plot or dialogue

**Domain Boundaries**:
- **Adds**: Environmental details, cultural markers, sensory elements, atmosphere
- **Never Touches**: Plot events, character actions, dialogue content

**Integration**:
- Uses SettingRepository for location and cultural data
- Preserves all story structure from SceneWriterAgent
- Adds rich environmental context without changing narrative flow

**Examples of Enhancement**:
- Lean: "They entered the tavern"
- Enhanced: "They pushed through the heavy oak door into the smoky interior, where the sounds of clinking mugs and raucous laughter filled the air"

## Agent Permission System (Planned)

### Permission Philosophy
**Restrictive by Default**: Agents can only modify content within their explicit domain  
**Creative vs Quality**: Different permission levels based on agent classification

### Creative Agent Permissions (Planned)
```yaml
SceneWriterAgent:
  allowed_sections: ["dynamic_elements", "critical_elements", "search_context"]
  can_modify_importance: true
  can_create_critical_elements: true
  default_importance: "minor"
  forbidden_sections: ["static_metadata.plot_beats", "dependencies"]
```

### Quality Agent Permissions (Planned)
```yaml
SettingEnrichmentAgent:
  allowed_sections: ["descriptive_elements", "sensory_details", "atmosphere"]
  can_modify_importance: false
  can_create_elements: true
  forbidden_sections: ["plot_beats", "character_actions", "dialogue"]
```

## Configuration Management

### AgentContext
**Function**: Shared context object passed between agents  
**Contains**:
- Project configuration and file paths
- Currently loaded character profiles
- Plot outline and scene specifications
- Git repository state and change tracking

### Agent Configuration
**Pattern**: YAML-based prompt management  
**Location**: `prompts/` directory with agent-specific configuration  
**Features**:
- Environment-specific overrides (development/production)
- Hot-reload capability for prompt updates
- Validation and schema checking

## Current Pipeline Execution

### Setting Phase (Run Once Per Project)
1. **ConceptAgent** ’ Creates foundational story concept
2. **PlotAgent** (1st call) ’ Generates high-level plot summary
3. **CharacterAgent** ’ Creates initial character profiles
4. **PlotAgent** (2nd call) ’ Develops chapter outlines
5. **CharacterAgent** ’ Refines character profiles based on plot
6. **PlotAgent** (3rd call) ’ Creates detailed scene specifications

### Writing Phase (Per Scene)
1. **Context Preparation** ’ Load relevant story context
2. **SceneWriterAgent** ’ Generate scene content from specifications
3. **Validation** ’ Check scene meets plot beat requirements
4. **Git Commit** ’ Save scene and metadata to repository

### Phase 4 Pipeline (In Development)
1. **Context Preparation** ’ Enhanced context loading
2. **SceneWriterAgent** ’ Generate lean narrative (plot + actions + dialogue)
3. **SettingEnrichmentAgent** ’ Add environmental and cultural details
4. **Validation** ’ Verify plot beats and setting consistency
5. **Git Commit** ’ Save enhanced scene and metadata

## Quality Assurance

### Test Coverage
- **Status**: 90%+ test coverage maintained
- **Test Count**: 328+ tests passing
- **Pattern**: Comprehensive test suite for BaseAgent pattern
- **Validation**: All agent outputs validated against expected schemas

### Error Handling
- **Standardized Exceptions**: Agent-specific error types for debugging
- **Graceful Degradation**: Fallback strategies for API failures
- **Activity Logging**: Detailed logging for agent decisions and modifications

## Planned Enhancements (Phase 5+)

### Setting System Integration
- **SettingAgent**: Coordinate world-building with user importance ratings
- **SettingRepository**: Progressive elaboration for location and culture details
- **Template System**: Genre-based defaults with user customization

### Quality Agent Pipeline
- **CharacterVoiceAgent**: Dialogue authenticity and consistency
- **ContinuityAgent**: Physical and atmospheric consistency tracking
- **ValidationAgents**: Plot beat execution and narrative coherence

### Advanced Features (Future)
- **Context Intelligence Pipeline**: Multi-stage context retrieval and ranking
- **Dependency Management**: Change impact analysis and conflict resolution
- **Quality Orchestration**: Intelligent restart decisions and optimization

## Performance Characteristics

### Current Performance
- **Scene Generation**: Completes in under 90 seconds including validation
- **Agent Execution**: Sequential with clear progress reporting
- **Memory Usage**: Efficient context management for large projects

### Optimization Targets
- **Token Efficiency**: Focused prompts reduce LLM costs
- **Context Relevance**: Load only necessary story context per scene
- **Pipeline Efficiency**: Minimize redundant processing between agents

## Cross-References
- **Implementation Details**: See `updated_mvp.txt` for current development status
- **System Architecture**: See `system-spec.md` for overall platform design
- **Future Roadmap**: See `roadmap.md` for planned agent enhancements
- **Feature Evaluations**: See `features/proposed/` for advanced agent concepts