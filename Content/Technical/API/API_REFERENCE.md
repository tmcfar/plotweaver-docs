# PlotWeaver API Reference

**Last Updated:** 2025-06-29

PlotWeaver is a Python library for AI-powered story generation using a sophisticated multi-agent architecture. This document provides a comprehensive reference for all public APIs and components.

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

#### SettingEnrichmentAgent

Enhances scenes with environmental and sensory details.

**Location:** `src/plotweaver/agents/enhancement/setting_enrichment_agent.py`

**Purpose:** Adds environmental descriptions, sensory details, and atmospheric elements to scenes.

### Quality Control Agents

#### CharacterVoiceAgent

Validates dialogue authenticity and character voice consistency.

**Location:** `src/plotweaver/agents/quality/character_voice_agent.py`

**Purpose:** Ensures character dialogue maintains consistent voice, speech patterns, and vocabulary throughout the story.

**Key Methods:**
- `validate_input(context)`: Validates scene content contains character dialogue
- `process(context)`: Analyzes dialogue for voice consistency
- `validate_output(result)`: Ensures quality assessment is complete

#### CharacterBodyLanguageAgent

Validates physical actions and non-verbal communication.

**Location:** `src/plotweaver/agents/quality/character_body_language_agent.py`

**Purpose:** Ensures physical descriptions, gestures, and body language are appropriate and consistent.

**Key Methods:**
- `validate_input(context)`: Validates scene content contains physical descriptions
- `process(context)`: Analyzes body language and physical actions
- `validate_output(result)`: Ensures action consistency assessment is complete

#### CharacterSubtextAgent

Analyzes hidden meanings and relationship dynamics.

**Location:** `src/plotweaver/agents/quality/character_subtext_agent.py`

**Purpose:** Validates subtext, power dynamics, and emotional undertones in character interactions.

**Key Methods:**
- `validate_input(context)`: Validates scene content contains character interactions
- `process(context)`: Analyzes subtext and relationship dynamics
- `validate_output(result)`: Ensures subtext analysis is complete

#### SensoryContinuityAgent

Validates environmental consistency and sensory details.

**Location:** `src/plotweaver/agents/quality/sensory_continuity_agent.py`

**Purpose:** Ensures environmental descriptions and sensory elements maintain consistency throughout the story.

**Key Methods:**
- `validate_input(context)`: Validates scene content contains environmental descriptions
- `process(context)`: Analyzes sensory continuity and environmental consistency
- `validate_output(result)`: Ensures continuity assessment is complete

#### StyleAgent

Validates writing style consistency across scenes.

**Location:** `src/plotweaver/agents/quality/style_agent.py`

**Purpose:** Ensures prose style, tone, and narrative voice remain consistent throughout the story.

**Key Methods:**
- `validate_input(context)`: Validates scene content for style analysis
- `process(context)`: Analyzes writing style and narrative voice
- `validate_output(result)`: Ensures style consistency assessment is complete

## Core Services

### FileManager

Handles file system operations and content management.

**Location:** `src/plotweaver/storage/file_manager.py`

#### Key Methods

- `save_file(path, content)`: Save content to specified file path
- `load_file(path)`: Load content from specified file path
- `ensure_directory(path)`: Create directory structure if it doesn't exist
- `list_files(directory, pattern)`: List files matching pattern in directory
- `delete_file(path)`: Remove file from file system

### MetadataManager

Manages YAML metadata and validation.

**Location:** `src/plotweaver/storage/metadata_manager.py`

#### Key Methods

- `save_metadata(path, metadata)`: Save metadata as YAML file
- `load_metadata(path)`: Load and validate metadata from YAML file
- `validate_schema(metadata, schema)`: Validate metadata against schema
- `merge_metadata(base, updates)`: Merge metadata dictionaries
- `get_metadata_schema(type)`: Get validation schema for metadata type

### SearchService

Provides content search and indexing capabilities.

**Location:** `src/plotweaver/search/search_service.py`

#### Key Methods

- `index_content(content_id, content)`: Add content to search index
- `search(query, filters)`: Search indexed content with optional filters
- `update_index(content_id, content)`: Update existing content in index
- `remove_from_index(content_id)`: Remove content from search index
- `rebuild_index()`: Rebuild entire search index

### ValidationService

Provides data validation and schema checking.

**Location:** `src/plotweaver/utils/validation.py`

#### Key Methods

- `validate_data(data, schema)`: Validate data against JSON schema
- `validate_yaml(yaml_content)`: Validate YAML syntax and structure
- `validate_agent_context(context)`: Validate agent context completeness
- `validate_agent_result(result)`: Validate agent result format
- `get_validation_errors(data, schema)`: Get detailed validation error messages

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

##### `execute_single_agent`

```python
execute_single_agent(agent: BaseAgent, context: AgentContext) -> AgentResult
```

Execute a single agent with error handling and logging.

**Parameters:**
- `agent`: Agent to execute
- `context`: Agent context

**Returns:** Agent execution result

### QualityLoop

Manages iterative quality improvement process.

**Location:** `src/plotweaver/orchestration/quality_loop.py`

#### Constructor

```python
QualityLoop(quality_agents: List[BaseAgent], max_iterations: int = 3, quality_threshold: float = 0.8)
```

**Parameters:**
- `quality_agents`: List of quality control agents to run
- `max_iterations`: Maximum number of improvement iterations
- `quality_threshold`: Minimum quality score to accept content

#### Key Methods

##### `run_quality_check`

```python
run_quality_check(content: str, context: AgentContext) -> Dict[str, Any]
```

Run all quality agents on content and return aggregated results.

**Parameters:**
- `content`: Content to validate
- `context`: Agent context with project information

**Returns:** Dictionary containing:
- `overall_score`: Aggregated quality score (0.0-1.0)
- `agent_results`: Individual results from each quality agent
- `passed`: Boolean indicating if quality threshold was met
- `improvements`: List of suggested improvements

##### `iterate_improvements`

```python
iterate_improvements(content: str, context: AgentContext) -> str
```

Iteratively improve content until quality threshold is met.

**Parameters:**
- `content`: Initial content to improve
- `context`: Agent context

**Returns:** Improved content that meets quality standards

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
from plotweaver.agents.setting import ConceptAgent, PlotAgent, CharacterAgent
from plotweaver.agents.writing import SceneWriterAgent
from plotweaver.agents.enhancement import SettingEnrichmentAgent
from plotweaver.orchestration import AgentRunner
from plotweaver.agents.base import AgentContext

# Create agents
concept_agent = ConceptAgent()
plot_agent = PlotAgent()
character_agent = CharacterAgent()
scene_writer = SceneWriterAgent()
setting_enrichment = SettingEnrichmentAgent()

# Create initial context
context = AgentContext(project_path="/path/to/project")

# Run foundation agents
foundation_agents = [concept_agent, plot_agent, character_agent]
runner = AgentRunner()
foundation_results = runner.execute_agents(foundation_agents, context)

# Run content generation
content_agents = [scene_writer, setting_enrichment]
content_results = runner.execute_agents(content_agents, context)
```

### Running Quality Loop

```python
from plotweaver.agents.quality import (
    CharacterVoiceAgent, CharacterBodyLanguageAgent, CharacterSubtextAgent,
    SensoryContinuityAgent, StyleAgent
)
from plotweaver.orchestration import QualityLoop
from plotweaver.agents.base import AgentContext

# Create quality agents
quality_agents = [
    CharacterVoiceAgent(),
    CharacterBodyLanguageAgent(),
    CharacterSubtextAgent(),
    SensoryContinuityAgent(),
    StyleAgent()
]

# Create quality loop
quality_loop = QualityLoop(
    quality_agents=quality_agents,
    max_iterations=3,
    quality_threshold=0.85
)

# Run quality validation
context = AgentContext(project_path="/path/to/project")
scene_content = "Your scene content here..."

quality_results = quality_loop.run_quality_check(scene_content, context)
print(f"Quality Score: {quality_results['overall_score']}")
print(f"Passed: {quality_results['passed']}")

# Iteratively improve content
improved_content = quality_loop.iterate_improvements(scene_content, context)
```

### Using Core Services

```python
from plotweaver.storage import FileManager, MetadataManager
from plotweaver.search import SearchService
from plotweaver.utils import ValidationService

# File operations
file_manager = FileManager()
file_manager.save_file("scenes/chapter1/scene1.md", scene_content)
loaded_content = file_manager.load_file("scenes/chapter1/scene1.md")

# Metadata management
metadata_manager = MetadataManager()
scene_metadata = {
    "chapter": 1,
    "scene": 1,
    "characters": ["Alice", "Bob"],
    "setting": "Forest clearing"
}
metadata_manager.save_metadata("scenes/chapter1/scene1.yaml", scene_metadata)

# Search functionality
search_service = SearchService()
search_service.index_content("scene_1_1", scene_content)
results = search_service.search("forest", {"chapter": 1})

# Validation
validation_service = ValidationService()
is_valid = validation_service.validate_agent_context(context)
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

**Base Exceptions:**
- `PlotWeaverError`: Base exception for all PlotWeaver errors

**Configuration Exceptions:**
- `ConfigurationError`: Configuration-related errors
- `AgentConfigurationError`: Agent configuration errors

**Execution Exceptions:**
- `AgentExecutionError`: Agent execution failures
- `AgentValidationError`: Agent context validation errors
- `QualityLoopError`: Quality validation process errors

**Storage Exceptions:**
- `StorageError`: File storage errors
- `GitOperationError`: Git operation failures
- `MetadataError`: YAML metadata processing errors

**Service Exceptions:**
- `SearchServiceError`: Search indexing and query errors
- `ValidationError`: Data validation failures
- `PromptManagerError`: Prompt template processing errors

**External Integration Exceptions:**
- `LLMClientError`: Language model API errors
- `OpenRouterError`: OpenRouter-specific API errors
- `RateLimitError`: API rate limiting errors

### Exception Handling Examples

```python
from plotweaver.core.exceptions import (
    AgentExecutionError, QualityLoopError, StorageError
)

try:
    # Run agent execution
    result = agent_runner.execute_agents(agents, context)
except AgentExecutionError as e:
    print(f"Agent execution failed: {e.message}")
    print(f"Failed agent: {e.agent_name}")
except QualityLoopError as e:
    print(f"Quality validation failed: {e.message}")
    print(f"Quality score: {e.quality_score}")
except StorageError as e:
    print(f"Storage operation failed: {e.message}")
    print(f"File path: {e.file_path}")
```

## Best Practices

### Project Management
1. **Project Initialization**: Always use `ProjectManager.initialize_project()` to set up new projects
2. **Configuration Management**: Store project-specific settings in the configuration dictionary
3. **Git Integration**: Let PlotWeaver handle git operations automatically
4. **Directory Structure**: Use the standard PlotWeaver project structure for consistency

### Agent Execution
1. **Sequential Execution**: Run foundation agents (Concept, Plot, Character) before content generation
2. **Context Management**: Ensure AgentContext contains all required data before agent execution
3. **Quality Validation**: Always run QualityLoop after content generation for consistency
4. **Error Handling**: Catch specific exceptions to handle different error scenarios appropriately

### Performance Optimization
1. **Parallel Quality Checks**: QualityLoop runs quality agents in parallel for better performance
2. **Caching**: Cache frequently accessed metadata and search results
3. **Batch Operations**: Process multiple scenes in batches when possible
4. **Resource Management**: Monitor LLM API usage and implement rate limiting

### Quality Assurance
1. **Quality Thresholds**: Set appropriate quality thresholds based on project requirements
2. **Iterative Improvement**: Use QualityLoop's iterative improvement for consistent results
3. **Validation**: Validate all inputs and outputs using ValidationService
4. **Testing**: Implement comprehensive testing for custom agents and workflows

### Security and Privacy
1. **API Key Management**: Store API keys securely and never commit them to version control
2. **Data Validation**: Always validate user inputs and external data
3. **Access Control**: Implement appropriate access controls for multi-user projects
4. **Audit Logging**: Log all significant operations for debugging and compliance

## Version Compatibility

This API reference covers PlotWeaver version 1.0.0. The library maintains backward compatibility within major versions.
