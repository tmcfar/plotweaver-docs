<!-- AI_INSTRUCTIONS: Focus on realistic timelines and dependencies. 
     Prioritize delivered value over ambitious features. -->

# PlotWeaver Development Roadmap

## Project Vision
AI-first collaborative manuscript management platform designed for long-form fiction series, emphasizing consistency, dependency tracking, and professional workflow integration.

## Development Philosophy
- **Git-native storage** as foundation for all operations
- **Agent specialization** over monolithic generation  
- **Progressive complexity** - start simple, add sophistication incrementally
- **Series consistency** as core differentiator from single-book tools

## Implementation Phases

### Phase 1: Core Infrastructure  **COMPLETE**
**Duration**: Completed
**Key Deliverables**:
- Git operations foundation with PAT authentication
- Scene-based file operations system  
- Basic project management with multi-project switching
- Agent foundation with BaseAgent pattern

**Status**: Fully implemented and tested

### Phase 2: Agent Foundation  **COMPLETE**  
**Duration**: Completed
**Key Deliverables**:
- Agent base classes with type hints and error handling
- PromptManager integration with external YAML files
- Basic orchestration framework
- LLM client integration

**Status**: 328+ tests passing, 90%+ coverage maintained

### Phase 3: Content Generation  **COMPLETE**
**Duration**: Completed  
**Key Deliverables**:
- ConceptAgent with user iteration workflow
- PlotAgent with multi-call pattern
- CharacterAgent with git storage  
- SceneWriterAgent with character context access

**Status**: Full pipeline operational (Concept � Plot � Character � Scene)

### Phase 4: Staged Enrichment = **IN PROGRESS**
**Duration**: Current sprint (estimated 4 weeks)
**Key Deliverables**:
- Refactor SceneWriterAgent for lean narrative generation (600-1000 words)
- Implement SettingEnrichmentAgent for environmental details
- Update pipeline for staged processing
- Integrate with existing quality validation

**Current Status**: 
- SceneWriterAgent refactoring underway
- SettingEnrichmentAgent in development
- Feature flags implemented for safe deployment

**Success Criteria**:
- Scene generation completes in <90 seconds
- Token usage reduction through focused prompts
- Quality maintained or improved through specialization

### Phase 5: Progressive Setting System =� **PLANNED** 
**Duration**: Estimated 4 months
**Dependencies**: Phase 4 completion

**Key Deliverables**:
- **Setting Repository Infrastructure**:
  - Three-tier template system (genre defaults, user customizations, dynamic instances)
  - Just-in-time location generation
  - Consistency tracking across scenes

- **Five-Agent Setting Hierarchy**:
  - **WorldPhysicsAgent**: Physical world rules and natural laws
  - **LocationsAgent**: Specific places and geographical features
  - **CulturePoliticsAgent**: Societies, governments, belief systems
  - **HistoryAgent**: Timeline creation and historical events
  - **SettingStyleAgent**: Narrative style and linguistic patterns

- **User-Driven Complexity Control**:
  - Importance ratings (High/Medium/Low/Skip) for each agent
  - Genre-based templates and smart defaults
  - Progressive elaboration as story develops

**Phase 5 Breakdown**:
- **5A (Month 1)**: Basic SettingRepository, WorldPhysicsAgent, LocationsAgent
- **5B (Month 2)**: CulturePoliticsAgent, HistoryAgent, agent coordination
- **5C (Month 3)**: SettingStyleAgent, user customization interface
- **5D (Month 4)**: Template system, integration testing, optimization

### Phase 6: Dependency Management =� **PLANNED**
**Duration**: Estimated 6-12 months  
**Dependencies**: Phase 5 completion, extensive user testing

**Key Deliverables**:
- **Basic Dependency Tracking** (Stage 1):
  - Character trait consistency across scenes
  - Simple world rule violation detection
  - Manual dependency definition interface

- **Relationship Mapping** (Stage 2):
  - Character relationship tracking
  - Plot thread continuity validation
  - Basic timeline integrity checking

- **Advanced Analysis** (Stage 3):
  - Automated dependency inference
  - Change impact analysis
  - Resolution strategy suggestions

**Warning**: This phase has highest implementation risk due to complexity

### Phase 7: Agent Specialization & Quality Enhancement 📋 **PLANNED**
**Duration**: Estimated 4-6 months
**Dependencies**: Phase 5 completion, user feedback on core agents

**Agent Development Features**:
- **Context Intelligence Pipeline**: 3-stage context retrieval and ranking system for large manuscripts
- **Character Enhancement Agents**: Unified character enhancement (micro-specialization deferred until validated)
- **Quality Orchestration**: Basic restart limits and obvious optimizations to reduce unnecessary iterations
- **Continuity Agents**: Physical and atmospheric consistency tracking with clear domain boundaries

**Advanced Features** (Subject to evaluation):
- **Micro-Agent Specialization**: Character voice/body language/subtext separation
- **Advanced Search Integration**: Semantic similarity and plot structure awareness
- **Series Management Tools**: Cross-book dependency tracking
- **Professional Workflow Integration**: Advanced git operations and collaboration

**Note**: Feature selection will depend on user feedback, performance validation, and business impact assessment. See `features/proposed/` for detailed evaluations of each component.

## Success Metrics by Phase

### Phase 4 (Current)
- Scene generation time: <90 seconds
- User satisfaction with staged output quality
- Token usage reduction: target 20-30%

### Phase 5
- 80% of projects use multiple location types
- 60% of users customize templates
- Average 15+ location instances per 50-scene project

### Phase 6  
- Dependency violation detection accuracy >90%
- False positive rate <20%
- User adoption of dependency features >70%

## Risk Management

### High-Risk Elements
1. **Dependency Management Complexity**: May prove too complex for practical implementation
2. **User Workflow Disruption**: Staged enrichment could feel awkward
3. **Performance Degradation**: Additional processing could slow generation

### Mitigation Strategies
1. **Staged Implementation**: Each phase delivers independent value
2. **Feature Flags**: Safe rollback mechanisms for problematic features
3. **User Testing**: Early validation before full implementation
4. **Performance Monitoring**: Continuous tracking of generation times

## Market Positioning

### Competitive Advantages
- **Series Focus**: Only tool designed for multi-book consistency
- **Git Integration**: Professional version control for manuscripts
- **Agent Architecture**: Specialized AI for different writing aspects
- **Progressive Complexity**: Scales from simple to sophisticated use cases

### Target Market Evolution
- **Phase 4-5**: Individual authors writing series
- **Phase 6+**: Professional authors and small publishing teams
- **Long-term**: Enterprise publishing workflows

## Technology Evolution

### Current Technology Stack
- Python with comprehensive testing
- Git operations via command line
- OpenAI API integration
- YAML configuration management

### Planned Enhancements
- SQLite for local search indexing (Phase 6+)
- Template engine for customizable outputs (Phase 5)
- Dependency graph analysis (Phase 6)
- Performance optimization (ongoing)

## Timeline Summary

| Phase | Status | Timeline | Key Focus |
|-------|--------|----------|-----------|
| 1-3 |  Complete | Historical | Foundation & Basic Generation |
| 4 | = In Progress | 4 weeks | Staged Enrichment |
| 5 | =� Planned | 4 months | Progressive Settings |
| 6 | =� Planned | 6-12 months | Dependency Management |
| 7 | =� Planned | 3-6 months | Enhanced Quality |

**Total Estimated Development**: 13-22 months from Phase 4 start

## Next Milestones

### Immediate (Next 2 weeks)
- Complete SceneWriterAgent lean narrative refactoring
- Initial SettingEnrichmentAgent implementation
- Pipeline integration testing

### Short-term (Next 2 months)  
- Phase 4 completion and validation
- Phase 5 planning and design
- User feedback collection on staged enrichment

### Medium-term (6 months)
- Progressive setting system fully operational
- Begin dependency management research and prototyping
- Market validation for advanced features

## Cross-References
- Technical implementation: See `system-spec.md`
- Current development status: See `updated_mvp.txt`
- Feature evaluations: See `features/proposed/` directory