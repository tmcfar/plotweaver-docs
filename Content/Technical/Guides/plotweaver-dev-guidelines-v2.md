# PlotWeaver Development Guidelines

## Essential Development Setup

```bash
# Environment setup
python -m venv venv
source venv/bin/activate  # Always activate first

# Core quality tools
pip install black flake8 mypy pytest pytest-cov

# Pre-commit quality checks (run before every commit)
black .
flake8 .
mypy src/
pytest --cov=src --cov-report=term-missing
```

## Code Quality Standards

### Type Hints & Documentation
```python
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

class SceneWriterAgent(BaseAgent):
    """
    Generates narrative scenes with dependency-aware context.
    
    Args:
        llm_client: LLM interface for content generation
        config: Configuration for scene generation parameters
        
    Returns:
        Formatted scene content with metadata validation
    """
    
    def generate_scene(self, context: AgentContext) -> AgentResult:
        """Generate scene content with quality validation."""
        pass
```

### Error Handling Patterns
```python
# Specific exceptions for better debugging
class AgentExecutionError(Exception):
    """Raised when agent execution fails."""
    pass

# Context managers for resource cleanup
def execute_with_context(self, operation: str) -> Any:
    try:
        with self.activity_stream.operation(operation):
            return self._perform_operation()
    except (APIError, ValidationError) as e:
        logger.error(f"Agent {self.name} failed: {e}")
        raise AgentExecutionError(f"Operation {operation} failed") from e
```

### Performance & Memory Optimization
```python
# Use generators for large datasets
def process_scenes(self) -> Iterator[Scene]:
    for scene_path in self.scene_paths:
        yield self._load_scene(scene_path)

# Cache expensive operations
@lru_cache(maxsize=128)
def get_character_profile(self, character_id: str) -> Dict[str, Any]:
    return self._load_from_git(f"characters/{character_id}.yaml")

# Context managers for file operations
def save_scene_content(self, scene_id: str, content: str) -> None:
    scene_path = self.project_root / f"content/{scene_id}.md"
    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(content)
```

## Architecture Compliance

### Agent Pattern Implementation
```python
class BaseAgent(ABC):
    """
    Foundation for all PlotWeaver agents.
    Enforces consistent interface and permission management.
    """
    
    def __init__(self, name: str, permissions: AgentPermissions):
        self.name = name
        self.permissions = permissions
        self.activity_stream = ActivityStream()
    
    @abstractmethod
    def execute_agent(self, context: AgentContext) -> AgentResult:
        """Core agent execution logic - must be implemented."""
        pass
    
    def validate_permissions(self, operation: str) -> None:
        """Enforce agent permission boundaries."""
        if not self.permissions.can_perform(operation):
            raise PermissionError(f"{self.name} cannot perform {operation}")
```

### Git Integration Standards
```python
def commit_changes(self, message: str, files: List[str]) -> str:
    """
    Atomic git operations with proper attribution.
    
    Args:
        message: Descriptive commit message following conventional format
        files: List of file paths to stage and commit
        
    Returns:
        Commit hash for tracking
    """
    try:
        # Stage specific files only
        subprocess.run(['git', 'add'] + files, check=True)
        
        # Commit with agent attribution
        commit_msg = f"AI-{self.name}: {message}"
        result = subprocess.run(
            ['git', 'commit', '-m', commit_msg],
            capture_output=True, text=True, check=True
        )
        
        return self._extract_commit_hash(result.stdout)
    except subprocess.CalledProcessError as e:
        raise GitOperationError(f"Commit failed: {e.stderr}") from e
```

## Testing Strategy

### Test Structure
```python
# tests/agents/test_scene_writer_agent.py
import pytest
from unittest.mock import Mock, patch
from src.plotweaver.agents.scene_writer_agent import SceneWriterAgent

class TestSceneWriterAgent:
    """Test suite for SceneWriterAgent functionality."""
    
    @pytest.fixture
    def mock_context(self):
        """Standard test context fixture."""
        context = Mock(spec=AgentContext)
        context.scene_metadata = {"scene_id": "test_scene"}
        return context
    
    def test_scene_generation_success(self, mock_context):
        """Test successful scene generation with valid context."""
        # Arrange
        agent = SceneWriterAgent(Mock(), Mock())
        
        # Act
        result = agent.execute_agent(mock_context)
        
        # Assert
        assert result.success
        assert len(result.content) > 800  # Minimum scene length
        
    def test_permission_violation_raises_error(self):
        """Test that permission violations are properly enforced."""
        with pytest.raises(PermissionError):
            agent.modify_plot_beats({"invalid": "operation"})
```

### Test Coverage Requirements
```bash
# Minimum 90% coverage with detailed reporting
pytest --cov=src --cov-report=html --cov-fail-under=90

# Integration tests for critical paths
pytest tests/integration/ -v

# Performance benchmarks for search operations
pytest tests/performance/ --benchmark-only
```

## Development Workflow

### Daily Workflow Commands
```bash
# Start development session
source venv/bin/activate
git pull origin main

# Before making changes
git checkout -b feature/intelligent-context-ranking

# Development cycle (repeat frequently)
black . && flake8 . && mypy src/ && pytest
git add -A && git commit -m "feat: implement context ranking algorithm"

# End of session
git push origin feature/intelligent-context-ranking
```

### Aider Integration
```bash
# Standard development (uses .aider.conf.yml settings)
aider

# Complex architectural changes
aider --architect

# Focus on specific files
aider --file src/plotweaver/agents/scene_writer_agent.py --file tests/agents/test_scene_writer_agent.py

# Override model temporarily
aider --model openrouter/anthropic/claude-sonnet-4
```

**Configuration:** Project uses `.aider.conf.yml` with:
- Model: openrouter/anthropic/claude-3.7-sonnet
- Editor model: openrouter/anthropic/claude-3.7-sonnet  
- Auto-commits: false (manual commit control)
- Auto-lint: false (run quality checks manually)
- Cache prompts: true (reduce API costs)

### LLM Development

Document model selection and hyperparameters
Implement robust error handling
Add performance monitoring

### Python Standards

Context managers for resources
Specific exception handling
SOLID principles
Optimize for performance and memory

### Repository Configuration

Origin: https://github.com/tmcfar/PlotWeaver/
Feature branches from main

## Communication Style

Direct technical feedback
Concise responses
Specific code improvements
Minimal concise explanatory content unless requested

## Project Context
PlotWeaver is a multi-agent AI novelist designed to achieve the highest writing quality possible through thoughtful execution, custom agents, and precise instructions paired with frequent human touch points.

## Key Lessons Learned

Align with upstream architecture - don't fight it
Minimal changes > comprehensive refactoring
Test in isolation before full integration
Debug systematically (environment → API → parsing)
One fix per commit, one feature per PR

## Success Metrics

All commits pass CI/CD
Maintained test coverage
Clean code review process
Reduced technical debt

## Quality Check Aliases
```bash
alias q1="black . && flake8 ."
alias q2="black . && flake8 . && mypy src/"
alias q3="black . && flake8 . && mypy src/ && pytest"
```

## Naming Conventions

### Code Structure
- **Classes**: PascalCase (e.g., `BaseAgent`, `ConceptGeneratorAgent`)
- **Methods/Functions**: snake_case (e.g., `execute_agent`, `generate_outline`)
- **Variables**: snake_case (e.g., `llm_client`, `project_data`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_PROMPT_TEMPLATE`)
- **Private methods/attributes**: Prefixed with underscore (e.g., `_format_prompt`)

### Import Organization
```python
# Standard library imports
import os
import json
from typing import Dict, List, Optional

# Third-party imports
import openai
import pytest

# Internal imports
from plotweaver.utils.llm_client import LLMClient
from plotweaver.agents.base_agent import BaseAgent
```

## Continuous Improvement

### Code Review Focus Areas
- Agent permission boundaries properly enforced
- Git operations are atomic and reversible
- Search performance meets sub-second requirements
- Memory usage stays under 50MB for typical manuscripts
- Error messages provide actionable information for users

### Refactoring Guidelines
- Minimal changes over comprehensive rewrites
- Preserve existing test coverage during changes
- One logical change per commit
- Update documentation alongside code changes
- Consider backward compatibility for configuration changes

## Key Development Principles

### Architecture Alignment
- Align with upstream architecture - don't fight established patterns
- Minimal changes over comprehensive refactoring
- Test in isolation before full integration
- Debug systematically (environment → API → parsing)
- One fix per commit, one feature per PR

### Quality Assurance
- All commits pass CI/CD pipeline
- Maintain comprehensive test coverage
- Clean code review process
- Actively reduce technical debt
- Document rationale for architectural decisions