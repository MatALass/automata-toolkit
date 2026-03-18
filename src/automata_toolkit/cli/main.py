from __future__ import annotations

import argparse
from pathlib import Path

from automata_toolkit.parsers.txt_parser import TxtAutomatonParser
from automata_toolkit.renderers.console_renderer import render_summary, render_transition_table
from automata_toolkit.renderers.graphviz_renderer import save_dot
from automata_toolkit.renderers.json_renderer import save_json
from automata_toolkit.services.complement import complement
from automata_toolkit.services.completion import complete
from automata_toolkit.services.determinization import determinize
from automata_toolkit.services.minimization import minimize
from automata_toolkit.services.recognition import recognize_word
from automata_toolkit.services.standardization import standardize
from automata_toolkit.validators.completeness import is_complete
from automata_toolkit.validators.determinism import is_deterministic
from automata_toolkit.validators.integrity import IntegrityError, validate_integrity
from automata_toolkit.validators.standardness import is_standard


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Finite automata toolkit CLI")
    parser.add_argument("--input", required=True, help="Path to the input .txt automaton file")
    parser.add_argument("--check-all", action="store_true", help="Validate and print automaton properties")
    parser.add_argument("--standardize", action="store_true", help="Standardize the automaton")
    parser.add_argument("--determinize", action="store_true", help="Determinize the automaton")
    parser.add_argument("--complete", action="store_true", help="Complete the automaton")
    parser.add_argument("--complement", action="store_true", help="Build the complementary automaton")
    parser.add_argument("--minimize", action="store_true", help="Minimize the automaton")
    parser.add_argument("--word", help="Word to recognize")
    parser.add_argument("--export-json", help="Path to save JSON output")
    parser.add_argument("--export-dot", help="Path to save DOT output")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    parser = TxtAutomatonParser()
    automaton = parser.parse_file(args.input)

    print("Automaton loaded successfully.\n")
    print(render_summary(automaton))
    print()
    print(render_transition_table(automaton))
    print()

    try:
        validate_integrity(automaton)
        integrity_status = "valid"
    except IntegrityError as exc:
        integrity_status = f"invalid ({exc})"

    if args.check_all:
        print("Properties")
        print(f"- Integrity: {integrity_status}")
        print(f"- Standard: {'yes' if is_standard(automaton) else 'no'}")
        print(f"- Deterministic: {'yes' if is_deterministic(automaton) else 'no'}")
        print(f"- Complete: {'yes' if is_complete(automaton) else 'no'}")
        print()

    work = automaton
    if args.standardize:
        work = standardize(work)
    if args.determinize:
        work = determinize(work)
    if args.complete:
        work = complete(work)
    if args.complement:
        work = complement(work)
    if args.minimize:
        work = minimize(work)

    if any([args.standardize, args.determinize, args.complete, args.complement, args.minimize]):
        print("Transformed automaton")
        print(render_summary(work))
        print()
        print(render_transition_table(work))
        print()

    if args.word is not None:
        accepted = recognize_word(work, args.word)
        print("Word recognition")
        print(f"- {args.word} -> {'accepted' if accepted else 'rejected'}")
        print()

    if args.export_json:
        Path(args.export_json).parent.mkdir(parents=True, exist_ok=True)
        save_json(work, args.export_json)
        print(f"JSON exported to {args.export_json}")

    if args.export_dot:
        Path(args.export_dot).parent.mkdir(parents=True, exist_ok=True)
        save_dot(work, args.export_dot)
        print(f"DOT exported to {args.export_dot}")


if __name__ == "__main__":
    main()
