# PlotWeaver - AI Story Generation System

**Current Status**: Active development, core functionality implemented  
**Location**: `/workspaces/pw`  
**Language**: Python 3.12+  
**Architecture**: Multi-agent system with git-native storage

## What PlotWeaver Is

PlotWeaver is a multi-agent AI system for generating long-form novels. It uses specialized agents that work sequentially to create comprehensive stories from initial concepts through full narrative scenes.

## Project Structure

```
src/plotweaver/
├── agents/              # AI agent implementations
│   ├── base/           # Base classes, context, exceptions
│   ├── setting/        # ConceptAgent, PlotAgent, CharacterAgent  
│   ├── writing/        # SceneWriterAgent
│   └── quality/        # (placeholder)
├── core/               # ProjectManager, GitManager, storage
├── orchestration/      # AgentRunner coordination
├── prompts/            # PromptManager + YAML prompt files
├── migration/          # LLM clients (OpenRouter, base classes)
├── utils/              # Shared utilities
└── ui/                 # (placeholder)
```

## Implemented Components

### Core System
- **ProjectManager** - Orchestrates project operations and configuration
- **GitManager** - Handles git operations for version control
- **SceneStorage** - Manages story file storage 
- **AgentRunner** - Simple sequential agent execution
- **AgentContext** - Data passing between agents

### AI Agents (4 working agents)
1. **ConceptAgent** - Generates story concepts and world-building
2. **PlotAgent** - Creates structured plot outlines 
3. **CharacterAgent** - Develops detailed character profiles
4. **SceneWriterAgent** - Writes narrative scenes (800-1500 words)

Agent flow: `ConceptAgent → PlotAgent → CharacterAgent → SceneWriterAgent`

### Infrastructure
- **BaseAgent** - Abstract base class with validation, cost estimation
- **LLM Integration** - OpenRouter client with cost tracking
- **PromptManager** - YAML-based prompt system with templating
- **Exception Handling** - Custom hierarchy for agent errors

## Current Implementation Status

### ✅ Working & Tested
- Complete 4-agent pipeline 
- Git-native storage system
- LLM integration with OpenRouter
- YAML prompt configuration system
- Comprehensive test suite (59+ test files)
- Error handling and validation
- Cost estimation and tracking

### 🚧 Placeholders
- Quality assurance agents (directory exists, empty)
- UI components (directory exists, empty)
- AgentRunner is minimal (27 lines)

### ⚠️ Issues Found
- Git merge conflicts in `tests/conftest.py` (lines 156-270)
- MyPy excludes the main `plotweaver` module

## Development Setup

### Requirements
- Python 3.8+ (3.12+ recommended)
- Dependencies managed via setuptools

### Testing
```bash
pytest                    # Run all tests
pytest -m unit           # Unit tests only  
pytest -m integration    # Integration tests
pytest -m "not slow"     # Skip slow tests
```

### Code Quality
- **Black formatter**: 88 character line length
- **MyPy**: Type checking (currently excludes plotweaver module)
- **Test markers**: unit, integration, functional, slow

## Key Features

### Git-Native Storage
All story content stored in git for version control and collaboration. Each scene becomes a tracked file.

### YAML Prompt Management
Agent prompts stored as external YAML files in `src/plotweaver/prompts/prompts/`:
- `concept_agent.yaml` - Story concept generation
- `plot_agent.yaml` - Plot structure creation  
- `character_agent.yaml` - Character development
- `scene_writer_agent.yaml` - Scene writing

### LLM Integration
- OpenRouter client for multiple model access
- Cost estimation and tracking
- Error handling for API failures

### Context Chaining
Agents pass results through `AgentContext` objects, building story elements incrementally.

## Architecture Notes

This is a **working system**, not just documentation. The core multi-agent pipeline is fully implemented and tested. The git-native approach means each story becomes a git repository with versioned scenes.

The system emphasizes:
- Sequential agent execution (simple but effective)
- Extensive validation at each step
- Cost awareness for LLM usage
- External prompt management for easy iteration

## Test Commands

```bash
pytest                           # Run all tests
pytest -m "unit and not slow"   # Quick unit tests
pytest tests/agents/            # Test specific module
```

## Development Notes

- **Package structure**: src layout with setuptools
- **Version**: 0.1.0 
- **Migration traces**: References to previous "LibriScribe" system
- **Digital humanities**: Some integration components exist

This codebase represents a functional multi-agent story generation system suitable for a solo developer's creative writing projects.