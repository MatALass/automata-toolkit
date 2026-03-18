# Architecture Overview

## Design Principles

- Separation of concerns
- Pure domain model
- Stateless services
- Testable components

---

## Layers

### Domain
Core representation of automata

### Parsers
Convert external formats → internal model

### Validators
Ensure automata correctness

### Services
Algorithms:
- determinization
- minimization
- completion
- complement

### CLI
User interaction layer

---

## Flow

Input file
→ Parser
→ Validation
→ Transformations
→ Output (console / JSON / DOT)