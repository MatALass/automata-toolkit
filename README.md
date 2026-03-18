# Automata Toolkit

A Python toolkit for reading, validating, transforming, and testing finite automata from text-based definitions.

## Project Overview

Automata Toolkit is a command-line application designed to manipulate finite automata from a simple input format. It supports core operations from automata theory such as standardization, determinism checks, completion, complement construction, and word recognition.

The project was originally inspired by an academic formal-languages assignment and has been redesigned as a clean, testable software-engineering project focused on algorithmic correctness, reproducibility, and maintainability.

## Problem Statement

Finite automata exercises are often solved manually or with ad hoc scripts that are hard to verify, extend, or demonstrate. This project provides a structured engine to:

- load automata from text files,
- validate structural properties,
- apply formal transformations,
- test word recognition,
- produce readable transition tables and visual exports.

## Features

- Load automata from `.txt` files
- Display states, alphabet, initial/final states, and transition tables
- Check whether an automaton is:
  - standard
  - deterministic
  - complete
- Standardize a non-standard automaton
- Determinize and complete a non-deterministic automaton
- Minimize a deterministic complete automaton
- Recognize user-provided words
- Build the complementary automaton
- Export automata to Graphviz / JSON
- Run automated tests on reference automata

## Tech Stack

- **Python**
- **pytest** for testing
- **Typer** or **argparse** for CLI
- **Graphviz** for diagram export
- **GitHub Actions** for CI

## Architecture

The codebase is organized into five layers:

- `domain/` → automaton model and core entities
- `parsers/` → input file parsing
- `validators/` → property checks
- `services/` → automata transformations
- `renderers/` → console, JSON, and graph exports

This separation keeps the project easier to test, maintain, and extend.

## Installation

```bash
git clone https://github.com/MatALass/automata-toolkit.git
cd automata-toolkit
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
Usage
Run the CLI
python -m automata_toolkit.cli.main
Example workflow
python -m automata_toolkit.cli.main \
  --input data/raw/efrei_test_cases/BDX4-08.txt \
  --check-all \
  --determinize \
  --complete \
  --recognize aab
Example output
Automaton loaded successfully
States: [0, 1, 2, 3]
Alphabet: [a, b]
Initial states: [0]
Final states: [3]

Properties:
- Standard: No
- Deterministic: No
- Complete: No

Actions performed:
- Standardization: applied
- Determinization: applied
- Completion: applied

Word recognition:
- aab -> accepted
Example Results

The toolkit can be used to:

validate a full batch of reference automata,

compare original and transformed versions,

generate deterministic and minimized forms,

document algorithm behavior for teaching or demonstrations.

Screenshots
Suggested screenshots to add

CLI overview

Load an automaton and print its transition table

Property checks

Show standard / deterministic / complete results

Transformation result

Show original automaton vs determinized/complete version

Graph export

Render the transformed automaton as a diagram

Test report

Show passing unit tests and integration tests

Project Structure
src/automata_toolkit/
data/raw/efrei_test_cases/
tests/
docs/
assets/
Future Improvements

Add epsilon-transition support with explicit closure computation

Add batch processing for all test automata

Add JSON schema validation for input/output formats

Add web UI for educational visualization

Add complexity analysis and performance benchmarks

Add export of minimization steps and partition evolution

Limitations

The current implementation targets educational finite automata workflows

Input format is constrained to the project specification

Advanced regex conversion features are not yet included

Why this project matters

This repository demonstrates:

algorithm implementation,

CLI software design,

parser + transformation architecture,

test-driven validation of formal systems.

It is intended as a strong software-engineering complement to a portfolio centered on data, BI, and analytics projects.