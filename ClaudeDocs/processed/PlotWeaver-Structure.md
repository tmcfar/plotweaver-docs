# PlotWeaver Project Structure
# Last updated: June 24, 2025
# This document describes the current state of the PlotWeaver project

project:
  name: PlotWeaver
  description: "AI-first collaborative manuscript dependency management platform"
  repository: "https://github.com/tmcfar/PlotWeaver/"
  
root_files:
  config:
    - pyproject.toml
    - pytest.ini
    - .flake8
    - setup.py
    - requirements.txt
  scripts:
    - check_environment.py
    - start_aider.sh
    - safety_check.py
  project_files:
    - README.md
    - STAGED_ENRICHMENT_STATUS.md
    
top_level_dirs:
  - docs/         # Documentation directory
  - prompts/      # Prompt templates
  - src/          # Source code
  - tests/        # Test suite
  - world/        # World building data
  - venv/         # Virtual environment

directory_structure:
  src:
    plotweaver:
      agents:
        base:
          - agent_context.py
          - agent_result.py
          - base_agent.py
          - exceptions.py
        enhancement:
          - setting_enrichment_agent.py
        quality:
          - __init__.py
        setting:
          - character_agent.py
          - concept_agent.py
          - plot_agent.py
        writing:
          - scene_writer_agent.py
      change_detection:
          - __init__.py
      context:
        - contextual_search_manager.py
        - git_context_loader.py
        - rich_context.py
      core:
        - git_manager.py
        - project_config.py
        - project_manager.py
        - storage.py
      metadata:
        - converter.py
        - schemas.py
        - validator.py
      migration:
        - config_adapter.py
        - llm_client.py
        - openrouter_client.py
        - utilities.py
      orchestration:
        - agent_runner.py
      prompts:
        - prompt_manager.py
        character:
          - __init__.py
        concept:
          - __init__.py
        plot:
          - __init__.py
        prompts:
          - __init__.py
        quality:
          - __init__.py
        scene:
          - __init__.py
      quality:
        - activity_stream.py
        - intelligent_quality_orchestrator.py
        - quality_loop_manager.py
        agents:
          - character_body_language_agent.py
          - character_subtext_agent.py
          - character_voice_agent.py
          - sensory_continuity_agent.py
          - style_calibration_agent.py
      search:
        - narrative_context_ranker.py
        - search_cache_manager.py
        - search_models.py
        - sqlite_search_index.py
      ui:
        - __init__.py
      utils:
        - exceptions.py
  tests:
    agents:
      base:
        - test_agent_context.py
        - test_agent_result.py
        - test_base_agent.py
        - test_exceptions.py
      setting:
        - test_character_agent.py
        - test_concept_agent.py
        - test_plot_agent.py
      writing:
        - test_scene_writer_agent.py
    context:
      - test_contextual_search_manager_integration.py
      - test_git_context_loader.py
    functional.disabled:
      - __init__.py
    integration:
      - __init__.py
    migration:
      - test_config_adapter.py
      - test_llm_client.py
      - test_openrouter_client.py
      - test_utilities.py
    orchestration:
      - __init__.py
    prompts:
      - test_prompt_manager.py
    search:
      - test_narrative_context_ranker.py
      - test_search_cache_manager.py
      - test_sqlite_search_index.py

components:
  agents:
    ConceptAgent:
      description: "Story concept development and foundational narrative structure"
      input: "Project requirements (genre, length, etc.)"
      output: "Story concept in plot/concept.yaml"
    
    PlotAgent:
      description: "Chapter and scene outline generation with metadata contracts"
      input: "Story concept from ConceptAgent"
      output: "Scene specifications for SceneWriterAgent"
    
    CharacterAgent:
      description: "Character profile generation with classification system"
      input: "New characters from PlotAgent or SceneWriterAgent"
      output: "Character profiles in characters/*.yaml"
    
    SceneWriterAgent:
      description: "Generate 800-1500 word narrative scenes with dynamic rhythm"
      input: "Scene specifications from PlotAgent"
      output: "Scene content"
      
    SettingEnrichmentAgent:
      description: "Adds environmental and cultural details to lean narrative"
      input: "Lean scene from SceneWriterAgent"
      output: "Enriched scene with environmental details"
      
  quality_agents:
    CharacterVoiceAgent:
      description: "Ensures dialogue authenticity and voice consistency"
      domain: "Words spoken in dialogue, speech patterns, vocabulary"
      
    CharacterBodyLanguageAgent:
      description: "Handles non-verbal communication and physical manifestations"
      domain: "Gestures, posture, micro-expressions, physical tells"
      
    CharacterSubtextAgent:
      description: "Manages unspoken tensions and implications"
      domain: "What's not being said, power dynamics, hidden meanings"
      
    SensoryContinuityAgent:
      description: "Ensures environmental and sensory experience consistency"
      domain: "Weather, lighting, sounds, smells, temperature, atmosphere"
      
    StyleCalibrationAgent:
      description: "Learns from human approval patterns to improve generation"
      domain: "Style patterns, approved/rejected content analysis"
  
  orchestration:
    AgentRunner:
      description: "Coordinates agent execution and workflow"
      functionality: "Manages the agent pipeline and execution flow"
      
    IntelligentQualityOrchestrator:
      description: "Makes impact-based restart decisions"
      functionality: "Analyzes change impact to determine restart necessity"
      
    QualityLoopManager:
      description: "Enforces restart limits and dependencies"
      functionality: "Prevents infinite loops and manages quality cycles"
      
  search:
    SQLiteSearchIndex:
      description: "High-performance search using SQLite's FTS5 full-text search engine"
      functionality: "Full-text search across the entire manuscript"
    
    SearchCacheManager:
      description: "Two-tier caching for search results"
      functionality: "Caching system with memory and disk levels"
    
    NarrativeContextRanker:
      description: "LLM-based curation for meaning and context"
      functionality: "Ranks search results by relevance to the current scene"
  
  context:
    RichContext:
      description: "Enhanced context structure with search results"
      functionality: "Combines base context with ranked search results"
    
    ContextualSearchManager:
      description: "Manages contextual search across the manuscript"
      functionality: "Provides relevant context for scene generation"
    
    GitContextLoader:
      description: "Loads context from git repository"
      functionality: "Loads characters, plot, and scene metadata from git"
  
  metadata:
    Converter:
      description: "Converts between data formats"
      functionality: "Transforms between different metadata representations"
      
    Schemas:
      description: "Defines metadata schemas"
      functionality: "Schema definitions for metadata validation"
      
    Validator:
      description: "Validates metadata against schemas"
      functionality: "Ensures metadata conformance to defined schemas"
  
  storage:
    SceneStorage:
      description: "File system operations for scene storage"
      functionality: "Creates and manages scene files in content directory"
  
  core:
    GitManager:
      description: "Git operations manager"
      functionality: "Handles all git operations with authentication"
    
    ProjectManager:
      description: "Project initialization and management"
      functionality: "Sets up and manages project structure"
    
    ProjectConfig:
      description: "Configuration management"
      functionality: "Loads and saves project configuration"
  
  prompts:
    PromptManager:
      description: "Manages prompt templates"
      functionality: "Loads prompts from YAML files with variable substitution"
  
  llm:
    LLMClient:
      description: "LLM integration client"
      functionality: "Generates content using LLMs"
    
    OpenRouterClient:
      description: "Integration with OpenRouter API"
      functionality: "Connects to OpenRouter for LLM inference"
      
  quality:
    ActivityStream:
      description: "Real-time hierarchical progress display"
      functionality: "Shows agent decisions, modifications, and reasoning"

workflows:
  scene_generation:
    - "ConceptAgent creates story concept"
    - "PlotAgent generates chapter and scene outlines"
    - "CharacterAgent creates character profiles"
    - "SceneWriterAgent generates lean narrative scenes focusing on plot and characters"
    - "SettingEnrichmentAgent adds environmental and sensory details"
    - "Quality agents enhance and validate content:"
    - "  - CharacterVoiceAgent ensures dialogue authenticity"
    - "  - CharacterBodyLanguageAgent adds non-verbal communication"
    - "  - CharacterSubtextAgent adds unspoken tensions"
    - "  - SensoryContinuityAgent ensures sensory consistency"
    - "IntelligentQualityOrchestrator manages any restarts"

file_formats:
  yaml:
    - "Character profiles: characters/*.yaml"
    - "Plot outlines: plot/*.yaml"
    - "Concept data: plot/concept.yaml"
    - "Scene metadata: content/chapters/*/scene-*-metadata.yaml"
    - "Prompts: prompts/**/*.yaml"
  
  markdown:
    - "Scene content: content/chapters/*/scene-*.md"
    - "Documentation: *.md"

config_structure:
  project:
    - "name: Project name"
    - "description: Project description"
    - "genre: Story genre"
    - "target_length: Target manuscript length"
  
  git:
    - "repo_url: Repository URL"
    - "auth_token: GitHub Personal Access Token"
  
  generation:
    - "model: LLM model to use"
    - "temperature: Generation temperature"
    - "max_tokens: Maximum tokens per generation"
  
  structure:
    - "root_dir: Root directory for project"
    - "content_dir: Content directory path"
    - "characters_dir: Characters directory path"
    - "plot_dir: Plot directory path"