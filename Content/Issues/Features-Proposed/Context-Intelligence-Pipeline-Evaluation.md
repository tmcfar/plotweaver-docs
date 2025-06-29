<!-- AI_INSTRUCTIONS: Use data-driven scoring. Provide specific examples 
     for risks/benefits. Keep recommendations actionable. -->

# Evaluation: Context Intelligence Pipeline (3-Stage)
ID: 20250628-EVAL-005
Feature Ref: [FEAT-CONTEXT-PIPELINE]

## Executive Summary
- **Recommendation**: PROCEED (staged implementation)
- **Priority**: P1 (Critical for large manuscripts)
- **Confidence**: High (well-understood problem and solution)

## Scoring Matrix
| Factor | Weight | Score (1-10) | Weighted | Justification |
|--------|--------|--------------|----------|---------------|
| User Value | 25% | 9 | 2.25 | Essential for novels >50 scenes |
| Revenue Impact | 20% | 8 | 1.6 | Enables longer, more complex projects |
| Technical Fit | 15% | 8 | 1.2 | Natural extension of current architecture |
| Strategic Alignment | 15% | 9 | 1.35 | Core to series consistency vision |
| Market Differentiation | 10% | 7 | 0.7 | Sophisticated context management |
| Implementation Risk | -10% | 7 | -0.7 | Well-understood technical approach |
| Maintenance Burden | -5% | 6 | -0.3 | Moderate complexity, clear boundaries |
| **TOTAL** | | | **6.1/10** | |

## Feature Description

**Core Problem**: As manuscripts grow beyond 20-30 scenes, finding relevant context becomes overwhelming:
- Manual context selection is time-consuming and error-prone
- Too much context creates expensive, slow generation
- Too little context creates inconsistent, disconnected scenes
- Current approach doesn't scale to 100+ scene novels or series

**Proposed Solution**: Three-stage pipeline that progressively filters context from comprehensive to highly relevant:

### Stage 1: RawContextRetrieval (SQLiteSearchIndex)
**Function**: Ultra-fast full-text search with zero intelligence  
**Technology**: SQLite FTS5 with positional indices  
**Input**: Scene specification (characters, location, plot beats)  
**Output**: Everything potentially relevant (100+ items)  
**Performance Target**: Fast enough for interactive use

### Stage 2: ComputationalContextFilter  
**Function**: Digital humanities pre-processing to rank relevance  
**Reduces**: 100+ items to ~20 items  
**Analysis Types**:
- **Temporal relevance**: How recently mentioned
- **Entity overlap**: Character/location/object intersection  
- **Lexical similarity**: Vocabulary and theme overlap
- **Narrative distance**: Scene proximity in story structure

### Stage 3: NarrativeIntelligenceRanker
**Function**: LLM-based final curation for thematic meaning  
**Reduces**: 20 items to 5-7 most meaningful  
**Intelligence Factors**:
- Emotional resonance with current scene
- Plot significance and foreshadowing relevance  
- Character relationship importance
- Thematic consistency and development

## Technical Analysis

### Stage 1: SQLite Search Implementation

**Advantages**:
- **Proven Technology**: SQLite FTS5 is mature and well-understood
- **Local Performance**: No external dependencies or network calls
- **Incremental Updates**: Can update index as scenes are written
- **Complex Queries**: Supports proximity, phrase, and boolean searches

**Implementation Strategy**:
```sql
-- Scene content search
CREATE VIRTUAL TABLE scene_search USING fts5(
    scene_id,
    content,
    characters,     -- Denormalized for speed
    locations,      -- Denormalized for speed  
    objects,        -- Denormalized for speed
    tokenize='porter unicode61'
);

-- Positional tracking for narrative distance
CREATE TABLE scene_positions (
    scene_id TEXT PRIMARY KEY,
    chapter_num INTEGER,
    scene_num INTEGER,
    absolute_position INTEGER
);
```

**Realistic Performance Expectations**:
- Small manuscripts (20 scenes): Near-instantaneous
- Medium manuscripts (50 scenes): Fast enough for interactive use
- Large manuscripts (100+ scenes): Should remain responsive
- **No specific timing promises** - depends on content and complexity

### Stage 2: Computational Analysis

**Digital Humanities Techniques**:
- **TF-IDF Scoring**: Term frequency analysis for content similarity
- **Named Entity Recognition**: Character and location tracking
- **Temporal Decay Functions**: Weight recent mentions higher
- **Structural Distance**: Chapter/scene proximity calculations

**Benefits Over Pure LLM Approach**:
- **Zero Cost**: Computational analysis has no API costs
- **Deterministic**: Same input always produces same ranking
- **Fast**: Can process large context sets quickly
- **Explainable**: Clear scoring rationale for debugging

### Stage 3: LLM Intelligence

**Purpose**: Handle nuanced relevance that computational methods miss
- **Thematic Connections**: Recognize symbolic relationships
- **Emotional Resonance**: Match mood and tone appropriately  
- **Plot Significance**: Identify foreshadowing and callback opportunities
- **Character Development**: Track psychological and relationship arcs

**Cost Optimization**: 
- Operating on pre-filtered set (20 items vs 100+) reduces token usage significantly
- Focused ranking task vs full content generation

## Real-World Use Cases

### Scenario 1: Large Fantasy Novel (80 scenes)
**Without Pipeline**: Author manually selects 10-15 relevant scenes, misses important connections
**With Pipeline**: 
1. Search finds 60 potentially relevant scenes
2. Computation filters to 18 based on character overlap and proximity
3. LLM ranks to 6 most thematically relevant scenes

### Scenario 2: Series Consistency (Book 3, Scene 45)
**Without Pipeline**: Author can't remember all relevant details from Books 1-2
**With Pipeline**:
1. Search across entire series finds 120 relevant mentions
2. Computation prioritizes recent developments and character relationships
3. LLM identifies thematic callbacks and character development opportunities

### Scenario 3: Complex Plot Threading
**Challenge**: Character subplot needs to resolve with earlier setup from 40 scenes ago
**Solution**: Pipeline automatically surfaces the setup scene even if author forgot about it

## Implementation Concerns

### Database Maintenance
- **Index Updates**: Must update search index when scenes change
- **Schema Evolution**: Need migration strategy for search schema changes
- **Backup Strategy**: SQLite database becomes critical project component

### Computational Accuracy
- **False Positives**: Computational filtering may promote irrelevant but keyword-rich content
- **False Negatives**: May demote subtly relevant content that lacks obvious keywords
- **Tuning Complexity**: Balancing different scoring factors requires experimentation

### LLM Ranking Reliability
- **Consistency**: LLM ranking may vary between calls for same content
- **Context Understanding**: LLM may misinterpret scene relationships
- **Bias**: May favor recent training patterns over manuscript-specific relevance

## Staged Implementation Plan

### Phase 1: Basic Search (2-3 months)
- **SQLite FTS5 implementation** with scene content indexing
- **Simple keyword search** for characters, locations, objects
- **Manual ranking** by author (validate search recall)
- **Success Metric**: Authors find relevant scenes faster than manual browsing

### Phase 2: Computational Filtering (2-3 months)
- **TF-IDF scoring** for content similarity
- **Temporal decay** weighting for recent mentions
- **Named entity extraction** for character/location tracking
- **Success Metric**: 80% of top-20 results judged relevant by authors

### Phase 3: LLM Ranking (2-3 months)
- **Thematic relevance scoring** using focused LLM prompts
- **Integration with scene generation** pipeline
- **A/B testing** against computational-only ranking
- **Success Metric**: Authors prefer LLM-ranked results >70% of the time

### Phase 4: Optimization (Ongoing)
- **Performance tuning** for large manuscripts
- **Ranking algorithm refinement** based on user feedback
- **Advanced search features** (semantic similarity, plot structure awareness)

## Success Metrics

### User Experience
- **Context Selection Time**: Reduce from minutes to seconds
- **Context Relevance**: 80% of suggested context judged useful by authors
- **Discovery Value**: Authors find connections they wouldn't have manually identified

### Technical Performance
- **Search Response Time**: Maintain interactive performance across manuscript sizes
- **Index Update Speed**: Scene changes reflected in search within seconds
- **Memory Usage**: Reasonable resource consumption for desktop applications

### Business Impact
- **Project Complexity**: Enable authors to work on larger, more complex projects
- **Series Support**: Make multi-book series practically manageable
- **User Retention**: Reduce abandonment of large projects due to complexity

## Alternative Approaches

### Simple Keyword Search Only
**Pros**: Easy to implement, reliable, fast
**Cons**: Misses thematic connections, overwhelming results for large projects

### Pure LLM Context Selection
**Pros**: Sophisticated understanding, flexible criteria
**Cons**: Expensive, slow, inconsistent, doesn't scale to large context sets

### Manual Context Curation
**Pros**: Perfect accuracy when done well
**Cons**: Time-consuming, error-prone, doesn't scale

## Recommendation: PROCEED with Staged Implementation

**Strong Justification**:
1. **Clear User Need**: Context management is genuinely difficult for large projects
2. **Technical Feasibility**: Each stage uses proven approaches
3. **Incremental Value**: Each phase delivers immediate benefits
4. **Cost-Effective**: Computational filtering provides high value at zero ongoing cost

**Critical Success Factors**:
1. **Start Simple**: Prove basic search value before adding complexity
2. **User Feedback**: Validate each stage with real author workflows
3. **Performance Focus**: Maintain interactive response times
4. **Fallback Options**: Allow manual override at each stage

**Implementation Priority**: Phase 1 should begin in parallel with Phase 5 (Progressive Settings)

**Next Steps**:
1. **Design SQLite schema** for scene indexing
2. **Prototype basic search** with existing test content
3. **User testing** with authors working on 20+ scene projects
4. **Performance benchmarking** with realistic manuscript sizes