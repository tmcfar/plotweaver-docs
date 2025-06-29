# Agent Architecture

## System Overview

```mermaid
classDiagram
    BaseAgent <|-- ConceptAgent
    BaseAgent <|-- PlotAgent
    BaseAgent <|-- CharacterAgent
    BaseAgent <|-- SceneWriterAgent
    BaseAgent <|-- QualityAgent
    
    class BaseAgent {
        +AgentContext context
        +AgentResult result
        +execute()
        #validate_input()
        #process()
        #validate_output()
    }

    class AgentContext {
        +add_data()
        +get_data()
        +update_data()
    }

    class AgentResult {
        +content
        +metadata
        +success
        +errors
    }
```

## Core Components

### Base Infrastructure (agents/base/)

#### agent_context.py
- Shared state between agents
- Data passing and transformation
- Context validation
- History tracking

#### agent_result.py
- Standardized output format
- Success/failure tracking
- Error aggregation
- Metadata management

#### base_agent.py
- Core agent lifecycle
- Common validation
- Error handling
- LLM integration

#### exceptions.py
- Agent-specific errors
- Validation failures
- Processing errors
- Context errors

## Agent Types

### Setting Generation (agents/setting/)

#### ConceptAgent
- Purpose: Story foundation and world rules
- Input: User requirements
- Output: Initial story concept
- Key responsibilities:
  - Genre interpretation
  - Theme development
  - Core conflict definition

#### PlotAgent
- Purpose: Story structure and flow
- Input: Story concept
- Output: Scene specifications
- Key responsibilities:
  - Plot outline
  - Scene sequencing
  - Story arc management

#### CharacterAgent
- Purpose: Character development
- Input: Story and plot context
- Output: Character profiles
- Key responsibilities:
  - Character creation
  - Relationship mapping
  - Arc development

### Content Generation (agents/writing/)

#### SceneWriterAgent
- Purpose: Narrative content creation
- Input: Scene specifications
- Output: Scene content
- Key responsibilities:
  - Content generation
  - Style consistency
  - Narrative flow

### Quality Control (agents/quality/)
- Purpose: Content validation and improvement
- Input: Generated content
- Output: Quality assessment and fixes
- Key responsibilities:
  - Style checking
  - Consistency validation
  - Error detection

## Agent Lifecycle

```mermaid
sequenceDiagram
    participant Runner as AgentRunner
    participant Agent as BaseAgent
    participant Context as AgentContext
    participant LLM as LLMClient

    Runner->>Agent: execute(context)
    Agent->>Agent: validate_input()
    Agent->>Context: get_data()
    Agent->>LLM: generate_content()
    LLM-->>Agent: content
    Agent->>Agent: process()
    Agent->>Agent: validate_output()
    Agent->>Context: update_data()
    Agent-->>Runner: AgentResult
```

## Interaction Patterns

### Data Flow
```mermaid
flowchart TD
    Context[Agent Context]
    Input[Input Data]
    Output[Output Data]
    Validate[Validation]
    Process[Processing]
    
    Input --> Context
    Context --> Validate
    Validate --> Process
    Process --> Validate
    Validate --> Output
    Output --> Context
```

### Error Handling
```mermaid
flowchart TD
    Error[Error Detection]
    Validate[Validation Error]
    Process[Processing Error]
    Context[Context Error]
    Recovery[Recovery Strategy]
    
    Error --> Validate
    Error --> Process
    Error --> Context
    Validate --> Recovery
    Process --> Recovery
    Context --> Recovery
```

## Development Guide

### Adding New Agent
1. Create new class in appropriate directory
2. Inherit from BaseAgent
3. Implement required methods:
   ```python
   class NewAgent(BaseAgent):
       def validate_input(self, context: AgentContext) -> bool:
           # Input validation logic
           pass

       def process(self, context: AgentContext) -> AgentResult:
           # Core processing logic
           pass

       def validate_output(self, result: AgentResult) -> bool:
           # Output validation logic
           pass
   ```
4. Add corresponding tests
5. Update agent runner if needed

### Agent Best Practices
- Keep agents focused and single-purpose
- Use context for data passing
- Implement thorough validation
- Handle errors gracefully
- Document agent contracts
- Test all paths

### Common Patterns
1. Context Usage
   ```python
   def process(self, context: AgentContext) -> AgentResult:
       # Get input data
       input_data = context.get_data("input_key")
       
       # Process using LLM
       result = self._generate_content(input_data)
       
       # Update context
       context.add_data("output_key", result)
       
       return AgentResult(content=result)
   ```

2. Validation
   ```python
   def validate_input(self, context: AgentContext) -> bool:
       required_keys = ["story_concept", "plot_outline"]
       
       for key in required_keys:
           if not context.has_data(key):
               raise AgentValidationError(f"Missing required data: {key}")
               
       return True
   ```

3. Error Handling
   ```python
   def process(self, context: AgentContext) -> AgentResult:
       try:
           result = self._core_processing()
       except LLMError as e:
           return AgentResult(
               success=False,
               errors=[str(e)]
           )
       except ValidationError as e:
           return AgentResult(
               success=False,
               errors=[f"Validation failed: {str(e)}"]
           )
       
       return AgentResult(content=result)
   ```

## Testing Strategy

### Unit Tests
- Input validation
- Processing logic
- Output validation
- Error handling
- Context management

### Integration Tests
- Agent chains
- Context passing
- LLM integration
- Error propagation

### Functional Tests
- End-to-end flows
- Complex scenarios
- Edge cases
- Performance