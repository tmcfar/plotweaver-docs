# PlotWeaver Architecture Specification
Version: 1.0.0
Last Updated: 2025-06-28
Status: Active

## 1. System Overview

### 1.1 Purpose
| Aspect | Description |
|--------|-------------|
| System Name | PlotWeaver |
| Purpose | AI-first collaborative manuscript dependency management platform |
| Primary Functions | Story generation, quality control, manuscript management |
| Target Users | Solo writers, small writing teams |

### 1.2 Architecture Style
| Aspect | Implementation |
|--------|---------------|
| Primary Pattern | Multi-agent system with git-native storage |
| Data Flow | Event-driven pipeline with quality gates |
| State Management | Git-based with YAML contracts |
| Integration Style | Modular components with clear boundaries |

## 2. Core Components

### 2.1 Agent System
| Agent | Purpose | Input | Output |
|-------|---------|--------|--------|
| ConceptAgent | Story foundation | Project requirements | Story concept YAML |
| PlotAgent | Scene planning | Story concept | Scene specifications |
| CharacterAgent | Character development | Story context | Character profiles |
| SceneWriterAgent | Content generation | Scene specs | Narrative content |
| SettingEnrichmentAgent | World details | Base scene | Enhanced scene |

### 2.2 Quality System
| Component | Purpose | Domain | Validation |
|-----------|---------|--------|------------|
| CharacterVoiceAgent | Dialogue authenticity | Speech patterns | Voice consistency |
| BodyLanguageAgent | Non-verbal elements | Physical actions | Gesture authenticity |
| SubtextAgent | Hidden meanings | Power dynamics | Relationship consistency |
| ContinuityAgent | World consistency | Environment | Setting coherence |
| StyleAgent | Writing style | Prose patterns | Style adherence |

## 3. Technical Infrastructure

### 3.1 Storage System
| Component | Purpose | Implementation | Format |
|-----------|---------|----------------|--------|
| Git Core | Version control | Native git integration | Git repository |
| Scene Storage | Content management | File system | Markdown + YAML |
| Metadata Store | Contract management | YAML files | Structured YAML |
| Search Index | Content discovery | SQLite FTS5 | Database |

### 3.2 Integration Points
| System | Purpose | Protocol | Format |
|--------|---------|----------|--------|
| OpenRouter | LLM access | REST API | JSON |
| Git Provider | Storage | Git protocol | Git |
| Local FS | Content storage | File system | Various |
| SQLite | Search/cache | SQL | Binary |

## 4. Component Dependencies

### 4.1 Critical Paths
| Component | Dependencies | Fallback | Recovery |
|-----------|--------------|----------|-----------|
| SceneWriter | Plot, Character | Cached data | Regenerate |
| QualityCheck | Original content | Skip check | Manual review |
| Search | SQLite, Index | Simple grep | Rebuild index |
| Storage | Git, FS | Local only | Push when ready |

### 4.2 Performance Requirements
| Component | Target Latency | Resource Limit | Scaling |
|-----------|---------------|----------------|---------|
| Agent Execution | < 30s | 1GB RAM | Horizontal |
| Quality Checks | < 10s | 500MB RAM | Parallel |
| Search Operations | < 100ms | 200MB RAM | Cache |
| Storage Operations | < 1s | Disk space | Archive |

## 5. Data Contracts

### 5.1 Agent Contracts
| Agent | Input Contract | Output Contract | Validation |
|-------|---------------|-----------------|------------|
| Concept | Project YAML | Concept YAML | Schema check |
| Plot | Concept YAML | Plot YAML | Structure check |
| Character | Context YAML | Character YAML | Profile check |
| Scene | Specs YAML | Markdown + YAML | Content check |

### 5.2 File Formats
| Type | Format | Location | Purpose |
|------|---------|----------|---------|
| Content | Markdown | content/*.md | Narrative text |
| Metadata | YAML | *.yaml | Configuration |
| Contracts | YAML | specs/*.yaml | Interfaces |
| Cache | SQLite | .cache/*.db | Performance |

## 6. Security Controls

### 6.1 Access Controls
| Resource | Access Level | Authentication | Audit |
|----------|--------------|----------------|-------|
| Content | Read/Write | Git credentials | Git log |
| Config | Read only | Local file | Version control |
| API Keys | No access | Environment vars | Usage logs |
| Cache | Local only | File system | None |

### 6.2 Data Protection
| Data Type | Protection | Storage | Backup |
|-----------|------------|---------|--------|
| Content | Git encryption | Repository | Remote |
| Credentials | Env vars | Local only | Manual |
| Cache | None | Temporary | None |
| Contracts | Git standard | Repository | Remote |

## 7. Monitoring Points

### 7.1 Health Checks
| Component | Check Type | Frequency | Alert |
|-----------|------------|-----------|-------|
| Agents | Heartbeat | 5 min | Error |
| Quality | Success rate | Per run | Warning |
| Storage | Disk space | 15 min | Warning |
| Search | Response time | Per query | None |

### 7.2 Metrics
| Metric | Type | Collection | Retention |
|--------|------|------------|-----------|
| Agent latency | Histogram | Per execution | 30 days |
| Quality scores | Gauge | Per check | 90 days |
| Error rates | Counter | Continuous | 30 days |
| Cost tracking | Counter | Per request | 365 days |

## 8. Recovery Procedures

### 8.1 Failure Modes
| Component | Failure | Impact | Recovery |
|-----------|---------|--------|----------|
| Agent | Crash | Pause generation | Restart agent |
| Quality | False positive | Manual review | Override |
| Storage | Git conflict | Block save | Manual merge |
| Search | Index corrupt | Slow search | Rebuild index |

### 8.2 Backup Strategy
| Data | Method | Frequency | Retention |
|------|--------|-----------|-----------|
| Content | Git push | On commit | Permanent |
| Config | Git push | On change | Permanent |
| Cache | None | N/A | None |
| Indexes | Auto rebuild | On corrupt | None |

## 9. Development Guidelines

### 9.1 Code Standards
| Aspect | Standard | Tool | Enforcement |
|--------|----------|------|-------------|
| Style | PEP 8 | Black | Pre-commit |
| Types | Static | MyPy | CI check |
| Lint | Strict | Flake8 | CI check |
| Test | 80% coverage | Pytest | CI check |

### 9.2 Documentation
| Type | Format | Location | Update |
|------|--------|----------|--------|
| API | OpenAPI | docs/api/ | Auto |
| Architecture | YAML+MD | docs/arch/ | Manual |
| User Guide | MD | docs/guide/ | Manual |
| Contracts | YAML | specs/ | Manual |