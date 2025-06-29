# PlotWeaver SaaS User Experience Flow & Interface Design (DRAFT)

## Overview

PlotWeaver's user interface provides dual paths: a streamlined experience for writers who want minimal friction, and a comprehensive guided journey for storytellers who need structure and assistance. The interface draws inspiration from VS Code's professional IDE approach while remaining accessible to non-technical users.

## Core User Flows

### Account Setup Flow
1. **Account Creation** → Basic user information
2. **Account Configuration** → Payment, model selection, tiers (details TBD)
3. **Project Creation** → New manuscript initialization

### Dual-Path Approach

#### Path A: "Just Let Me Write"
- Skip setup → Direct to editor
- Access tools from menus as needed
- Minimal friction for experienced writers

#### Path B: "Guided Creation"
- Comprehensive step-by-step process
- Each step optional but encouraged
- Ideal for dreamers, editors, and those who need structure

## Guided Creation Flow

### 1. Concept Development

**Brainstorming Screen:**
- Large text area for freeform concept entry
- Concept can be as brief or detailed as desired
- Optional tools:
  - Genre selector
  - Idea generator
  - "What if..." prompts
  - Reference external works/characters for inspiration

**Process:**
1. User submits concept seed
2. ConceptAgent generates 3-5 variations
3. Options presented:
   - Original submission (always valid)
   - AI variations
   - "Let AI decide" option

**Output:** 1-2 paragraph story concept

### 2. Character Creation (Optional)

**Character Definition Screen:**
- Define character archetypes
- Set growth arcs (fed to PlotAgent)
- Physical/mental/emotional characteristics
- Creates character profile stubs

**Note:** Future releases may include dedicated character creation UI

### 3. Story Configuration

**Collected any time before PlotAgent:**
- Story length (word count target)
- Story type:
  - Novel
  - Series/Trilogy
  - Anthology
  - Web Serial
  - Other

### 4. Setting & Worldbuilding

**Progressive Worldbuilding Approach:**

**Required Questions:**
- When: [Modern day ▼] 
- Where: [Earth ▼]
- Genre: [Select ▼]

**Smart Context Inference:**
- "1850 England" → Automatically populates Victorian culture, technology, social structures
- No time specified → Assumes modern day
- Real-world settings → Minimal worldbuilding required

**Optional Deep Worldbuilding:**
All elements presented but skippable:
- Geography/Locations
- Culture
- Narrative tone
- Language/Lexicon
- Government
- Religion
- Economy
- Technology
- Magic systems
- Cartography

**Key Features:**
- Standard options with custom prompt override
- "Let AI decide" available
- Can import settings from existing novels (fanfiction support)
- Fantasy/Sci-fi requires more investment than contemporary

### 5. Plot Development

**Story Arc Selection:**
- Choose from 6 common story arcs
- Combine multiple arcs
- May be determined from concept phase

**Plot Complexity:**
- Gauge against genre standards
- Avoid intricate plots for children's books
- Ensure appropriate complexity for mysteries

**Interactive Plot Builder:**
- Chapter-by-chapter construction
- Visual pacing representation (future release)
- Iterate until satisfied
- Edit and recreate as needed

### 6. Scene Generation
- Transitions to SceneAgent
- Begins actual manuscript writing
- Quality loop engagement

## Interface Design

### VS Code-Inspired Layout

```
┌─────────┬────────────────────────────────────┬─────────┐
│ PROJECT │        Main Editor Window          │ TOOLS   │
│ SIDEBAR │                                    │ SIDEBAR │
├─────────┼────────────────────────────────────┼─────────┤
│         │                                    │         │
│ Concept │    [Locked by default - Click     │ Activity│
│         │     to edit or press Cmd+E]       │ Stream  │
│ ▼Plot   │                                    │         │
│  ├─Ch 1 │    Chapter 3, Scene 2 Content     │ Helpers │
│  │ ├─S1 │                                    │         │
│  │ └─S2 │                                    │ Context │
│  └─Ch 2 │                                    │         │
│         │                                    │ AI Chat │
│         │                                    │         │
├─────────┴────────────────────────────────────┴─────────┤
│ Console: > plotweaver generate --chapter 3              │
└─────────────────────────────────────────────────────────┘
```

### Left Sidebar (Project Navigation)
- Expandable/collapsible sections
- Major headings: Concept, Character, Setting, Plot
- Plot section contains:
  - Chapter outline
  - Scene sub-outlines
- Each item has mini-buttons for file access

### File Structure Per Scene
Each scene/chapter has three files:
1. **Config file** (metadata/contracts)
2. **Description** (plot intentions, scene goals)
3. **Content** (actual prose)

### Right Sidebar (Tools & Assistance)
- Helper tools
- Suggestions
- Activity stream
- Staged messages
- Context assistance

### Bottom Panel
- Console for CLI commands
- Power user tools access

### Main Editor
- Lock/unlock toggle (locked by default)
- Click-out triggers save prompt
- Change detection for dependency management
- Split-screen for diffs and version comparison

### User Menu
- Profile picture in corner
- Links to settings and preferences

## Key UX Principles

### Progressive Disclosure
- Start simple, reveal complexity as needed
- Every screen has "Skip" option
- Advanced features in menus, not mandatory flow

### Dual User Support
1. **Writers**: Quick path to writing, tools available when needed
2. **Dreamers/Editors**: Full guidance through story creation process

### Smart Defaults
- Context-aware suggestions (1850 England → Victorian setting)
- Genre-appropriate complexity
- Intelligent skip options

### Escape Hatches
- Save & Continue Later (every screen)
- Skip This Step
- Help tooltips
- Back without losing work

## Change Management
- Files locked by default
- Unlock triggers dependency awareness
- Git integration for version control
- Visual diff comparisons

## Modular Development Approach

### Phase 1: Core Writing
- Basic flow: concept → plot → write
- Simple editor
- Essential features only

### Phase 2: Guided Creation
- Concept brainstorming
- Basic worldbuilding
- Character templates

### Phase 3: Power Tools
- Deep worldbuilding
- Complex plotting
- Advanced features

### Phase 4: Editorial Suite
- Revision tools
- Style matching
- Beta reader features

## Success Metrics
- Both user types can achieve their goals
- Writers can skip to writing quickly
- Non-writers get sufficient guidance
- Complex features don't overwhelm simple use cases

---

**Status**: DRAFT - Requires design review and user testing
**Priority**: Core UX flow is Phase 1, enhanced features phased over time
**Key Innovation**: Dual-path approach serving both writers and storytellers