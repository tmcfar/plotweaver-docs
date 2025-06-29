# Feature: Progressive Setting System

ID: 23
Ref: Phase-5

Writers struggle with the classic worldbuilding problem: too much detail up front kills momentum, too little creates inconsistency. This system enables "just-in-time" setting development, starting with genre-appropriate defaults and expanding naturally during writing. Settings evolve organically as needed while maintaining consistency through intelligent caching and version control.

## Classification
**Impact:** *Should Have*
**Complexity:** *Large*
**Strategic Value:** *Growth*

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
- 🔴 SettingRepository: New component for template management and just-in-time generation
- 🟡 Setting Agents: Split into 5 specialized sub-agents with hierarchical coordination
- 🟡 Storage System: Add three-tier storage (templates, customization, discovered)
- 🟢 ProjectManager: Add template loading and caching configuration
- 🟢 GitManager: Add version control for discovered settings

## Implementation
Dependencies:
- Required: Base agent system, storage system, git integration
- Optional: Digital Humanities pre-processing
- Blocking: Quality agent implementation, context intelligence

Scope:
- MVP: Single genre template, basic discovery, file-based caching
- Boundaries: No cross-project sharing, no custom templates
- Future: Template marketplace, setting visualization, ML-based discovery

Integration:
- Pipeline: Insert setting enrichment after scene generation
- Data: New YAML format for settings, git-tracked discoveries
- Contracts: New setting request/response protocols for agents

Migration:
- Strategy: Parallel run with flag, migrate projects on opt-in
- Fallback: Settings can be exported to static YAML

-------------------------------------------
Technical Notes:
- Genre templates define basic world rules and common elements
- Three-tier storage separates defaults, user choices, and discoveries
- Cache system handles both memory and disk storage
- Setting discovery uses context analysis to identify new elements
- Version control tracks setting evolution with scene references