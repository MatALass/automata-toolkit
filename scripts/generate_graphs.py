from pathlib import Path

from automata_toolkit.parsers.txt_parser import TxtAutomatonParser
from automata_toolkit.renderers.graphviz_renderer import save_dot


def main() -> None:
    input_dir = Path("data/raw/efrei_test_cases")
    output_dir = Path("assets/diagrams")
    output_dir.mkdir(parents=True, exist_ok=True)

    parser = TxtAutomatonParser()
    for txt_file in input_dir.glob("*.txt"):
        automaton = parser.parse_file(txt_file)
        save_dot(automaton, output_dir / f"{txt_file.stem}.dot")


if __name__ == "__main__":
    main()
