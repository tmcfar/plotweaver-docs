# PlotWeaver API Reference

PlotWeaver is a Python library for AI-powered story generation using a multi-agent architecture. This document provides a comprehensive reference for all public APIs.

## Table of Contents

- [Core Module](#core-module)
  - [ProjectManager](#projectmanager)
  - [GitManager](#gitmanager)
  - [SceneStorage](#scenestorage)
  - [ProjectConfig](#projectconfig)
- [Agent System](#agent-system)
  - [BaseAgent](#baseagent)
  - [AgentContext](#agentcontext)
  - [AgentResult](#agentresult)
  - [Concrete Agents](#concrete-agents)
- [Orchestration](#orchestration)
  - [AgentRunner](#agentrunner)
- [Prompt Management](#prompt-management)
  - [PromptManager](#promptmanager)
- [Migration Utilities](#migration-utilities)
  - [LLMClient](#llmclient)
  - [OpenRouterClient](#openrouterclient)
  - [ConfigAdapter](#configadapter)

## Core Module

The core module provides project management, git operations, and storage functionality.

### ProjectManager

Main entry point for managing PlotWeaver projects.

**Location:** `src/plotweaver/core/project_manager.py`

#### Constructor

```python
ProjectManager(config: Union[Dict[str, Any], str]) -> None
```

Initialize ProjectManager with configuration.

**Parameters:**
- `config`: Configuration dictionary containing git and project settings

**Raises:**
- `ConfigurationError`: If configuration is invalid

#### Methods

##### `initialize_project`

```python
initialize_project(name: str, repo_url: str, token: str, local_path: str) -> bool
```

Initialize a new project or clone existing repository.

**Parameters:**
- `name`: Project name
- `repo_url`: Git repository URL (empty string for new project)
- `token`: Authentication token
- `local_path`: Local project path

**Returns:** `True` if successful

**Raises:**
- `ValueError`: If required parameters are empty
- `GitOperationError`: If git operations fail
- `StorageError`: If storage operations fail

##### `setup_project_structure`

```python
setup_project_structure() -> None
```

Setup the project directory structure.

**Raises:**
- `ConfigurationError`: If storage not initialized
- `StorageError`: If structure creation fails

##### `get_project_status`

```python
get_project_status() -> Dict[str, Any]
```

Get comprehensive project status information.

**Returns:** Dictionary containing:
- `project_initialized`: Boolean indicating if project is initialized
- `git_status`: Git repository status
- `structure_status`: Project directory structure validation
- `scene_count`: Count of scenes by chapter
- `last_sync`: Information about last sync/commit

**Raises:**
- `ConfigurationError`: If project not initialized

##### `sync_to_remote`

```python
sync_to_remote() -> bool
```

Sync local changes to remote repository.

**Returns:** `True` if successful

**Raises:**
- `ConfigurationError`: If git manager not initialized
- `GitOperationError`: If commit fails

### GitManager

Manages git operations for PlotWeaver projects.

**Location:** `src/plotweaver/core/git_manager.py`

#### Key Methods

- `initialize_repo()`: Initialize a new git repository
- `clone_repo(repo_url, project_path, token)`: Clone existing repository
- `commit_changes(message)`: Commit current changes
- `push_with_fallback()`: Push to remote with automatic retry
- `get_repo_status()`: Get current repository status

### SceneStorage

Handles file storage operations for project content.

**Location:** `src/plotweaver/core/storage.py`

#### Key Methods

- `ensure_project_structure()`: Create required directories
- `save_plot_data(data_type, data)`: Save plot-related data
- `load_plot_data(data_type)`: Load plot-related data
- `save_scene(chapter, scene_number, content)`: Save scene content
- `load_scene(chapter, scene_number)`: Load scene content

### ProjectConfig

Configuration management for PlotWeaver projects.

**Location:** `src/plotweaver/core/project_config.py`

## Agent System

The agent system provides the foundation for AI-powered content generation.

### BaseAgent

Abstract base class for all PlotWeaver agents.

**Location:** `src/plotweaver/agents/base/base_agent.py`

#### Constructor

```python
BaseAgent(name: str, llm_client: Optional[LLMClient] = None, config: Optional[Dict[str, Any]] = None)
```

**Parameters:**
- `name`: Unique agent identifier
- `llm_client`: Language model client (creates default if not provided)
- `config`: Agent-specific configuration

#### Key Methods

##### `execute`

```python
execute(context: AgentContext) -> AgentResult
```

Execute the agent with the given context.

**Parameters:**
- `context`: Agent context with project info and previous results

**Returns:** `AgentResult` containing execution outcome

##### `validate_context` (abstract)

```python
validate_context(context: AgentContext) -> None
```

Validate that the context is appropriate for this agent.

##### `estimate_cost` (abstract)

```python
estimate_cost(context: AgentContext) -> float
```

Estimate the cost of executing this agent.

### AgentContext

Carries context information between agents.

**Location:** `src/plotweaver/agents/base/agent_context.py`

**Key Attributes:**
- `project_path`: Path to the project
- `previous_results`: Results from previous agents
- `metadata`: Additional context metadata

### AgentResult

Represents the result of agent execution.

**Location:** `src/plotweaver/agents/base/agent_result.py`

**Key Methods:**
- `success_result()`: Create a successful result
- `error_result()`: Create an error result

**Attributes:**
- `agent_name`: Name of the executing agent
- `status`: Success or error status
- `content`: Generated content (if successful)
- `error_message`: Error description (if failed)
- `execution_time`: Time taken to execute
- `cost_estimate`: Estimated cost

### Concrete Agents

#### ConceptAgent

Generates story foundations and core concepts.

**Location:** `src/plotweaver/agents/setting/concept_agent.py`

**Purpose:** Creates the initial story concept including themes, settings, and core narrative elements.

#### PlotAgent

Creates detailed plot outlines and scene plans.

**Location:** `src/plotweaver/agents/setting/plot_agent.py`

**Purpose:** Develops chapter and scene structure based on the story concept.

#### CharacterAgent

Develops character profiles and relationships.

**Location:** `src/plotweaver/agents/setting/character_agent.py`

**Purpose:** Creates detailed character backgrounds, motivations, and relationship dynamics.

#### SceneWriterAgent

Generates actual story content.

**Location:** `src/plotweaver/agents/writing/scene_writer_agent.py`

**Purpose:** Writes individual scenes based on outlines and character information.

## Orchestration

### AgentRunner

Executes multiple agents in sequence with context chaining.

**Location:** `src/plotweaver/orchestration/agent_runner.py`

#### Key Methods

##### `execute_agents`

```python
execute_agents(agents: List[BaseAgent], initial_context: AgentContext) -> List[AgentResult]
```

Run multiple agents sequentially, passing results between them.

**Parameters:**
- `agents`: List of agents to execute
- `initial_context`: Starting context

**Returns:** List of results from all agents

## Prompt Management

### PromptManager

Manages YAML-based prompt templates for agents.

**Location:** `src/plotweaver/prompts/prompt_manager.py`

#### Constructor

```python
PromptManager(prompts_dir: Optional[str] = None)
```

**Parameters:**
- `prompts_dir`: Directory containing YAML prompt files

#### Key Methods

##### `get_prompt`

```python
get_prompt(agent_type: str, prompt_name: str, variables: Optional[Dict[str, Any]] = None) -> Dict[str, str]
```

Get a prompt with template variable substitution.

**Parameters:**
- `agent_type`: Type of agent (e.g., 'concept_agent')
- `prompt_name`: Name of the prompt
- `variables`: Variables for template substitution

**Returns:** Dictionary with:
- `system_message`: System prompt for the LLM
- `user_prompt`: User prompt with variables substituted

## Migration Utilities

### LLMClient

Base interface for language model interactions.

**Location:** `src/plotweaver/migration/llm_client.py`

**Purpose:** Provides abstraction for different LLM providers.

### OpenRouterClient

Implementation of LLMClient for OpenRouter API.

**Location:** `src/plotweaver/migration/openrouter_client.py`

**Key Features:**
- Supports multiple language models
- Automatic retry logic
- Cost tracking

### ConfigAdapter

Adapts legacy configuration formats to current schema.

**Location:** `src/plotweaver/migration/config_adapter.py`

**Purpose:** Ensures backward compatibility with older project configurations.

## Usage Examples

### Creating a New Project

```python
from plotweaver.core import ProjectManager

# Initialize project manager
config = {
    "git": {"auto_commit": True},
    "project": {"default_branch": "main"}
}
pm = ProjectManager(config)

# Create new project
pm.initialize_project(
    name="My Story",
    repo_url="",  # Empty for new project
    token="github_token",
    local_path="/path/to/project"
)
```

### Running Agents

```python
from plotweaver.agents.setting import ConceptAgent, PlotAgent
from plotweaver.orchestration import AgentRunner
from plotweaver.agents.base import AgentContext

# Create agents
concept_agent = ConceptAgent()
plot_agent = PlotAgent()

# Create initial context
context = AgentContext(project_path="/path/to/project")

# Run agents
runner = AgentRunner()
results = runner.execute_agents([concept_agent, plot_agent], context)
```

### Using Prompt Manager

```python
from plotweaver.prompts import PromptManager

# Initialize prompt manager
pm = PromptManager()

# Get prompt with variables
prompt = pm.get_prompt(
    agent_type="concept_agent",
    prompt_name="generate_concepts",
    variables={"genre": "fantasy", "themes": ["adventure", "friendship"]}
)

print(prompt["system_message"])
print(prompt["user_prompt"])
```

## Error Handling

PlotWeaver uses a hierarchy of custom exceptions:

- `PlotWeaverError`: Base exception for all PlotWeaver errors
- `ConfigurationError`: Configuration-related errors
- `GitOperationError`: Git operation failures
- `StorageError`: File storage errors
- `AgentValidationError`: Agent context validation errors
- `AgentExecutionError`: Agent execution failures
- `AgentConfigurationError`: Agent configuration errors

## Best Practices

1. **Project Initialization**: Always use `ProjectManager.initialize_project()` to set up new projects
2. **Agent Execution**: Use `AgentRunner` for coordinating multiple agents
3. **Error Handling**: Catch specific exceptions to handle different error scenarios
4. **Configuration**: Store project-specific settings in the configuration dictionary
5. **Git Integration**: Let PlotWeaver handle git operations automatically

## Version Compatibility

This API reference covers PlotWeaver version 1.0.0. The library maintains backward compatibility within major versions.