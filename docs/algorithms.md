# Algorithms

## Property Checks

- **Integrity**: validates declared states, symbols, initials, finals, and transition consistency.
- **Determinism**: ensures exactly one initial state and at most one target per `(state, symbol)` pair.
- **Standardness**: ensures exactly one initial state and no incoming transition into that initial state from another state.
- **Completeness**: ensures every `(state, symbol)` pair has exactly one transition.

## Transformations

- **Standardization**: creates a fresh initial state and redirects the language-preserving outgoing transitions.
- **Determinization**: uses subset construction.
- **Completion**: adds a sink state when transitions are missing.
- **Complement**: determinizes and completes when needed, then inverts final states.
- **Minimization**: uses iterative partition refinement on a deterministic complete automaton.

## Recognition

- Simulates the automaton over the input word by propagating active states symbol by symbol.
