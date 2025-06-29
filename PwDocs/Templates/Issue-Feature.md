# Feature Template

ID: [number]
Ref: [reference if applicable]

[1-12 line description focusing on what the feature enables for users and why it matters to the product. Explain the problem being solved and how this creates value.]

## Classification
**Impact:** *[Must Have | Should Have | Could Have | Won't Have]*
**Complexity:** *[Small | Medium | Large | Extreme]*
**Strategic Value:** *[Core | Growth | Enhancement | Optional]*

Complexity Legend:
- Small: Single component, clear scope
- Medium: Multiple components, manageable dependencies
- Large: System-wide impact, complex dependencies
- Extreme: ⚠️ Architectural overhaul - requires scope reduction before consideration

## User Value
Problem:
- What user pain point or need does this address?
- How do users currently handle this?
- Why is current solution insufficient?

Solution:
- How does this solve the problem?
- What becomes possible?
- Why is this better?

## Product Value
Market Impact:
- How does this differentiate the product?
- What capabilities does it enable?
- Who does this attract?

Strategic Alignment:
- How does this advance product vision?
- What future capabilities does it enable?
- What becomes possible after this?

## Changes Required
- 🟢 [Component]: Simple modification or addition
- 🟡 [Component]: Moderate change requiring careful testing
- 🔴 [Component]: Complex change with significant impact

Complexity Legend:
🟢 Low: Isolated change, clear scope
🟡 Medium: Multiple components, manageable dependencies
🔴 High: System-wide impact, complex dependencies

## Implementation
Dependencies:
- Required: [components/features that must exist]
- Optional: [nice-to-have dependencies]
- Blocking: [what this blocks]

Scope:
- MVP: [minimal viable implementation]
- Boundaries: [what's explicitly NOT included]
- Future: [later extensions]

Integration:
- Pipeline: [agent workflow changes]
- Data: [storage/format changes]
- Contracts: [API/interface changes]

Migration:
- Strategy: [transition approach]
- Fallback: [rollback plan]

## Planning Review Outcomes
- [date] - [outcome]

-------------------------------------------
[Optional additional details, implementation notes, or background information below]