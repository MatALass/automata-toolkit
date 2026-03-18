#!/usr/bin/env bash
set -e

python -m automata_toolkit.cli.main \
  --input data/raw/efrei_test_cases/sample_automaton.txt \
  --check-all \
  --word aa \
  --export-dot assets/diagrams/sample_automaton.dot \
  --export-json assets/diagrams/sample_automaton.json
