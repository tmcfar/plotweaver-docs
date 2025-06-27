# PlotWeaver Documentation Repository

## 🚀 Quick Start with GitHub Codespaces

1. **Open in Codespaces**:
   - Click the "Code" button on GitHub
   - Select "Codespaces" → "Create codespace on main"
   - Wait for the environment to set up automatically

2. **Configure API Key**:
   ```bash
   export OPENROUTER_API_KEY="your-api-key-here"
   echo 'export OPENROUTER_API_KEY="your-api-key-here"' >> ~/.bashrc
   ```

3. **Start Developing**:
   ```bash
   aider  # Start AI-assisted coding
   ```

📖 **Detailed Setup**: See [CODESPACES_SETUP.md](CODESPACES_SETUP.md)  
🔧 **Quick Reference**: See [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

## Overview

This repository contains automatically generated and curated documentation for the PlotWeaver AI-assisted novel writing platform. Documentation is generated via GitHub Actions triggered by issue creation in the main PlotWeaver repository.

## Purpose

- **Automated Documentation**: AI-generated technical specifications from GitHub issues
- **Feature Planning**: Structured evaluation and planning documents
- **API Documentation**: Comprehensive API references and examples
- **Sprint Management**: 20-hour sprint planning and tracking
- **Product Roadmap**: Strategic planning and feature pipeline management

## Repository Structure

```
plotweaver-docs/
├── README.txt                    # This file
├── active-features.md           # Currently active features
├── roadmap.md                   # Product roadmap overview
│
├── api/                         # API documentation
│   ├── agents/                  # Agent-specific API docs
│   ├── endpoints/               # REST API endpoints
│   └── examples/                # API usage examples
│
├── evaluations/                 # Feature evaluation matrices
│   ├── scoring/                 # Feature scoring results
│   └── analysis/                # Evaluation analysis
│
├── features/                    # Feature documentation
│   ├── proposed/                # New feature proposals
│   ├── in-development/          # Features under development
│   ├── completed/               # Completed features
│   └── archived/                # Archived/cancelled features
│
├── issues/                      # Issue tracking and analysis
│   ├── open/                    # Open issues documentation
│   ├── closed/                  # Closed issues documentation
│   └── analysis/                # Issue trend analysis
│
├── planning/                    # Strategic planning documents
│   ├── mvp/                     # MVP definitions and requirements
│   ├── sprints/                 # Sprint planning (20-hour cycles)
│   ├── milestones/              # Major milestone definitions
│   └── roadmap/                 # Detailed roadmap components
│
├── scripts/                     # Automation scripts
│   └── process-issue.py         # GitHub issue processing script
│
├── specifications/              # Technical specifications
│   ├── agents/                  # AI agent specifications
│   ├── algorithms/              # Algorithm documentation
│   ├── models/                  # Data model specifications
│   └── systems/                 # System architecture specs
│
└── templates/                   # Documentation templates
    ├── feature-evaluation.md    # Feature scoring matrix template
    ├── issue-tracking.md        # Issue documentation template
    ├── api-documentation.md     # API documentation template
    ├── sprint-planning.md       # 20-hour sprint template
    ├── system-specification.md  # System spec template
    ├── agent-specification.md   # Agent spec template
    ├── algorithm-documentation.md # Algorithm spec template
    ├── mvp-definition.md        # MVP planning template
    ├── product-roadmap.md       # Roadmap template
    └── feature-pipeline.md      # Feature pipeline template
```

## Automation System

### GitHub Actions Workflow

**Trigger**: New issue created in main PlotWeaver repository
**Location**: `.github/workflows/doc-manager.yml` (in main repo)
**Process**:

1. **Issue Detection**: Workflow triggers on new issue creation
2. **Data Extraction**: Extracts issue number, title, and body
3. **Repository Checkout**: Checks out plotweaver-docs repository
4. **AI Processing**: Calls OpenRouter API with Claude 3.5 Sonnet
5. **Documentation Generation**: Creates structured documentation
6. **File Creation**: Generates README.md and status.md files
7. **Commit & Push**: Automatically commits to plotweaver-docs

### Processing Script

**File**: `scripts/process-issue.py`
**Features**:
- Windows-safe path sanitization
- Character filtering for folder names
- OpenRouter API integration
- Structured prompt generation
- Error handling and logging

**Environment Variables**:
- `OPENROUTER_API_KEY`: API key for Claude access
- `ISSUE_NUMBER`: GitHub issue number
- `ISSUE_TITLE`: Issue title (sanitized for paths)
- `ISSUE_BODY`: Issue description content
- `EVENT_TYPE`: GitHub event type (usually "opened")

### Folder Naming Convention

Generated folders follow the pattern:
```
features/proposed/{issue_number}-{sanitized_title}/
```

**Sanitization Rules**:
- Invalid characters `<>:"|?*\\/` replaced with `-`
- Multiple consecutive dashes collapsed to single dash
- Spaces converted to dashes
- Leading/trailing dashes removed
- Converted to lowercase

## Templates System

### Available Templates

1. **Feature Evaluation** (`feature-evaluation.md`)
   - Scoring matrix (1-10 scale)
   - Technical complexity assessment
   - Business value analysis
   - Implementation timeline

2. **Issue Tracking** (`issue-tracking.md`)
   - Issue categorization
   - Priority assessment
   - Resolution tracking
   - Impact analysis

3. **API Documentation** (`api-documentation.md`)
   - Endpoint specifications
   - Request/response examples
   - Authentication requirements
   - Error handling

4. **Sprint Planning** (`sprint-planning.md`)
   - 20-hour sprint cycles
   - Task breakdown
   - Resource allocation
   - Success metrics

5. **System Specification** (`system-specification.md`)
   - Architecture overview
   - Component interactions
   - Data flow diagrams
   - Performance requirements

6. **Agent Specification** (`agent-specification.md`)
   - Agent behavior definition
   - Input/output contracts
   - Dependencies mapping
   - Quality metrics

7. **Algorithm Documentation** (`algorithm-documentation.md`)
   - Algorithm description
   - Implementation details
   - Performance characteristics
   - Test cases

8. **MVP Definition** (`mvp-definition.md`)
   - Core feature requirements
   - Success criteria
   - Timeline and milestones
   - Resource requirements

9. **Product Roadmap** (`product-roadmap.md`)
   - Strategic vision
   - Feature prioritization
   - Timeline planning
   - Dependencies mapping

10. **Feature Pipeline** (`feature-pipeline.md`)
    - Feature flow management
    - Stage definitions
    - Approval processes
    - Quality gates

## Usage Patterns

### Creating New Documentation

1. **Create Issue**: Create new issue in main PlotWeaver repository
2. **Wait for Processing**: GitHub Action processes issue (usually <2 minutes)
3. **Review Generated Docs**: Check `features/proposed/{issue-number}-{title}/`
4. **Edit if Needed**: Manual edits to generated documentation
5. **Move Through Pipeline**: Move folders as features progress

### Documentation Lifecycle

```
features/proposed/     →  features/in-development/  →  features/completed/
     ↓                           ↓                           ↓
Auto-generated docs    Manual updates/refinements    Final documentation
Issue-based content    Development notes added       Implementation details
AI-created structure   Human collaboration           Lessons learned
```

### Manual Documentation

For non-issue-based documentation:
1. Choose appropriate template from `templates/`
2. Create new file in relevant directory
3. Follow template structure
4. Commit manually to repository

### Search and Discovery

**By Feature Status**:
- `features/proposed/` - New ideas and proposals
- `features/in-development/` - Active development
- `features/completed/` - Finished features

**By Document Type**:
- `specifications/` - Technical specifications
- `planning/` - Strategic planning
- `api/` - API documentation
- `evaluations/` - Feature assessments

**By Timeline**:
- `planning/sprints/` - Current and past sprints
- `planning/milestones/` - Major deliverables
- `planning/roadmap/` - Long-term planning

## Configuration

### Required Secrets

Set in main PlotWeaver repository:
- `DOCS_REPO_TOKEN`: GitHub PAT with repository access
- `OPENROUTER_API_KEY`: OpenRouter API key for Claude access

### AI Model Configuration

**Current Setup**:
- Model: `anthropic/claude-3.5-sonnet`
- Max Tokens: 1000
- Temperature: Default (controlled by OpenRouter)
- Provider: OpenRouter

### Repository Access

- **Main Repository**: https://github.com/tmcfar/PlotWeaver (public)
- **Docs Repository**: https://github.com/tmcfar/plotweaver-docs (private)
- **Actions**: View at https://github.com/tmcfar/PlotWeaver/actions

## Troubleshooting

### Common Issues

1. **Invalid Path Names**: 
   - Issue titles with special characters
   - Fixed by character sanitization in process-issue.py

2. **API Rate Limits**:
   - OpenRouter API limits
   - Wait and retry, or upgrade API plan

3. **GitHub Token Expiration**:
   - PAT tokens expire
   - Update `DOCS_REPO_TOKEN` secret

4. **Workflow Failures**:
   - Check Actions tab in main repository
   - Review workflow logs for errors

### Manual Fixes

If automation fails:
1. Clone this repository locally
2. Create documentation manually using templates
3. Follow folder naming conventions
4. Commit and push manually

### Monitoring

Check these locations for system health:
- **GitHub Actions**: Main repo Actions tab
- **Output Logs**: Workflow execution logs
- **Recent Commits**: This repository's commit history
- **Issue Status**: Verify documentation created for new issues

## Contributing

### For PlotWeaver Team

1. **Use Issues**: Create issues in main repo for automatic documentation
2. **Review Generated Docs**: Check and refine AI-generated content
3. **Update Templates**: Improve templates as patterns emerge
4. **Organize Documentation**: Move features through pipeline stages

### For External Contributors

1. **Read Documentation**: Use this repository for understanding PlotWeaver
2. **Suggest Improvements**: Create issues in main repository
3. **Report Docs Issues**: Use main repository for documentation feedback

## License

This documentation repository follows the same license as the main PlotWeaver project.

---

**Last Updated**: June 26, 2025
**Automation Status**: Active and functioning
**Repository Access**: Private (PlotWeaver team only)
