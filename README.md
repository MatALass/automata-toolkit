# Automata Toolkit

A Python toolkit for parsing, validating, transforming, and testing finite automata from text-based definitions.

## Project Overview

Automata Toolkit is a command-line application designed to manipulate finite automata from a simple text input format. It supports key automata-theory operations such as property validation, standardization, completion, complement construction, word recognition, and deterministic minimization.

The project started from an academic formal-languages assignment and is restructured here as a clean software-engineering project focused on algorithmic correctness, maintainability, reproducibility, and portfolio quality.

## Problem Statement

Finite automata exercises are often solved manually or through monolithic scripts that are hard to verify, extend, test, or demonstrate. This project provides a structured engine that can:

- ingest automata definitions from text files,
- validate structural properties,
- apply formal transformations,
- test input words,
- generate readable console output,
- export JSON and Graphviz-compatible DOT representations.

## Features

- Parse automata from `.txt` files
- Validate automaton integrity
- Check whether an automaton is:
  - standard,
  - deterministic,
  - complete
- Standardize an automaton
- Determinize an automaton
- Complete an automaton with a sink state
- Build the complementary automaton
- Minimize a deterministic complete automaton
- Recognize words from the automaton language
- Export to JSON
- Export to DOT / Graphviz format
- Run automated tests on the parser, validators, transformations, recognition logic, and CLI workflows

## Tech Stack

- **Python 3.10+**
- **argparse** for the CLI
- **pytest** for automated testing
- **GitHub Actions** for CI
- **DOT / Graphviz** export for diagrams

## Architecture

```text
src/automata_toolkit/
├── domain/        # core automaton model
├── parsers/       # file parsing and DTOs
├── validators/    # formal property and integrity checks
├── services/      # transformations and recognition logic
├── renderers/     # console / JSON / DOT outputs
└── cli/           # command-line entrypoint
```

This separation keeps the project easier to test, document, and extend.

## Installation

```bash
git clone https://github.com/MatALass/automata-toolkit.git
cd automata-toolkit
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Input File Format

Example:

```text
states: q0,q1,q2
alphabet: a,b
initial_states: q0
final_states: q2
transitions:
q0,a,q1
q0,b,q0
q1,a,q2
q1,b,q1
q2,a,q2
q2,b,q2
```

## Usage

### Run the CLI

```bash
automata-cli --input data/raw/efrei_test_cases/sample_automaton.txt --check-all
```

### Determinize and export to DOT

```bash
automata-cli \
  --input data/raw/efrei_test_cases/sample_automaton.txt \
  --determinize \
  --complete \
  --export-dot assets/diagrams/sample.dot
```

### Recognize a word

```bash
automata-cli \
  --input data/raw/efrei_test_cases/sample_automaton.txt \
  --word aab
```

## Example Output / Results

```text
Automaton loaded successfully.

States: q0, q1, q2
Alphabet: a, b
Initial states: q0
Final states: q2

Properties
- Integrity: valid
- Standard: yes
- Deterministic: yes
- Complete: yes

Word recognition
- aab -> accepted
```

## Screenshots

Suggested screenshots to add in `assets/screenshots/`:

1. **CLI overview**
   - Load an automaton and print its transition table.
2. **Property checks**
   - Show integrity, standardness, determinism, and completeness results.
3. **Transformation result**
   - Compare original automaton vs determinized / completed / minimized version.
4. **DOT / graph export**
   - Render the transformed automaton visually.
5. **CI proof**
   - Show a successful GitHub Actions pipeline.

## Project Structure

```text
automata-toolkit/
├── src/
├── data/
├── tests/
├── docs/
├── assets/
└── scripts/
```

## Future Improvements

- Add epsilon-transition support
- Add batch processing for all EFREI test cases
- Add HTML report generation for before/after comparisons
- Add performance benchmarks for determinization and minimization
- Add richer validation diagnostics with line-level parser errors
- Add a small educational web UI for visualization

## Why This Project Matters

This repository demonstrates:

- algorithm implementation,
- clean CLI software design,
- parser and transformation architecture,
- automated testing,
- reproducible engineering practices.

It is intended as a strong software-engineering complement to a portfolio centered on Data / BI / Analytics Engineering projects.
