# Aider Development Patterns for Complex Module Creation

## Problem Observed
When creating new modules with dependencies, aider can add imports before creating the actual module, causing temporary import errors during the creation process.

## Recommended Patterns

### Pattern A: Shell-First Approach (Safer)
**Best for:** New modules with existing code dependencies

**Pass 1: Create Module Shell**
```bash
aider --architect --message "Create empty module structure: src/plotweaver/digital_humanities/__init__.py with placeholder classes DigitalHumanitiesCore and VoiceFingerprinter. No implementation, just class definitions with docstrings."
```

**Pass 2: Add Implementation**
```bash
aider --message "Implement DigitalHumanitiesCore and VoiceFingerprinter with full statistical voice analysis methods, proper type hints, and integration patterns."
```

**Pass 3: Integration**
```bash
aider --message "Integrate VoiceFingerprinter into CharacterVoiceAgent for computational pre-filtering."
```

### Pattern B: Isolated Creation (Current)
**Best for:** Independent modules, smaller changes

**Single Pass:**
```bash
aider --architect --message "Create complete digital humanities module with implementation"
```

**Risk:** Temporary import errors during creation

### Pattern C: Dependencies-Last
**Best for:** Complex integrations

**Pass 1: Create Module**
```bash
aider --architect --message "Create digital_humanities module without modifying existing files"
```

**Pass 2: Add Dependencies**
```bash
aider --message "Add digital_humanities imports to CharacterVoiceAgent after module exists"
```

## When to Use Each Pattern

| Scenario | Recommended Pattern | Reason |
|----------|-------------------|---------|
| New module + existing file changes | **Shell-First (A)** | Prevents import errors |
| Independent module creation | **Isolated (B)** | Faster, less complexity |
| Complex multi-file integration | **Dependencies-Last (C)** | Clean separation of concerns |
| Performance-critical components | **Shell-First (A)** | Allows incremental testing |

## Key Principle
**Avoid creating imports before the target module exists** - this causes the exact import errors we saw.

## PlotWeaver-Specific Recommendation
For future DH components (RepetitionAnalyzer, ComputationalQualityGates), use **Shell-First** pattern:

1. Create empty classes with proper interfaces
2. Implement statistical methods
3. Integrate with existing agents

This prevents test breakage during development and allows incremental validation.
