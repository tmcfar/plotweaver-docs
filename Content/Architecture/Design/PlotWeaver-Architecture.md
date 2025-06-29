# PlotWeaver Architecture

A practical guide to the PlotWeaver system architecture.

## Development View

### Directory Structure
```
src/plotweaver/
├── agents/                   # Core generation system
│   ├── base/                # Agent infrastructure
│   │   ├── agent_context.py # Shared context
│   │   ├── agent_result.py  # Result handling
│   │   ├── base_agent.py    # Base classes
│   │   └── exceptions.py    # Agent exceptions
│   ├── setting/             # Setting generation
│   │   ├── character_agent.py
│   │   ├── concept_agent.py
│   │   └── plot_agent.py
│   ├── writing/             # Content generation
│   │   └── scene_writer_agent.py
│   └── quality/             # Quality validation
├── core/                    # System infrastructure
│   ├── git_manager.py      # Content versioning
│   ├── project_config.py   # Configuration
│   ├── project_manager.py  # Project handling
│   └── storage.py          # File management
├── digital_humanities/      # DH analysis tools
│   └── core.py            # Core DH functionality
├── migration/              # LLM integration
│   ├── llm_client.py      # Base client
│   ├── openrouter_client.py # OpenRouter integration
│   ├── config_adapter.py  # Configuration
│   └── utilities.py       # Shared utilities
├── orchestration/          # Process management
│   └── agent_runner.py    # Agent coordination
├── prompts/               # Agent instructions
│   ├── concept.yaml      # Base concept prompts
│   ├── plot_agent.yaml   # Base plot prompts
│   ├── concept/          # Concept generation
│   │   └── generate_concepts.yaml
│   ├── plot/            # Plot generation
│   │   └── generate_outline.yaml
│   ├── prompts/         # Core prompts
│   │   ├── character_agent.yaml
│   │   ├── concept_agent.yaml
│   │   ├── plot_agent.yaml
│   │   └── scene_writer_agent.yaml
│   └── prompt_manager.py # Prompt management
├── ui/                   # User interface (placeholder)
└── utils/               # Shared utilities
    └── exceptions.py    # System exceptions

tests/                   # Test suite mirrors src structure
├── agents/             # Agent tests
│   ├── base/          # Base functionality tests
│   ├── setting/       # Setting agent tests
│   └── writing/       # Writing agent tests
├── digital_humanities/ # DH analysis tests
├── functional.disabled/ # Disabled functional tests
├── integration/        # Integration tests
├── migration/         # LLM integration tests
└── prompts/           # Prompt system tests
```

### Key Components
- Agents: Self-contained generation units
  - Base: Core agent functionality
  - Setting: World/character generation
  - Writing: Content creation
  - Quality: Content validation
- Core: Critical infrastructure
  - Git integration
  - Project management
  - Storage handling
- Digital Humanities: Analysis tools
- Migration: LLM provider integration
- Orchestration: Process management
- Prompts: Agent behavior definitions
- UI: User interface (future)
- Utils: Shared utilities

[rest of document remains the same...]