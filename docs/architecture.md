# Architecture

## Objective

The project is structured as a small but maintainable software product rather than a single academic script.

## Layers

- `domain/`: core automaton model
- `parsers/`: text input parsing and DTO normalization
- `validators/`: integrity and formal property checks
- `services/`: transformations and recognition logic
- `renderers/`: console, JSON, and DOT outputs
- `cli/`: command-line orchestration

## Design Principles

1. Separate business logic from input/output.
2. Keep the CLI thin.
3. Make every major algorithm independently testable.
4. Preserve a path toward future extensions such as epsilon transitions, batch processing, and web visualization.
