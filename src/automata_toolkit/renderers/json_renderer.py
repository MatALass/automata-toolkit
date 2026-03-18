from __future__ import annotations

import json
from pathlib import Path

from automata_toolkit.domain.automaton import Automaton


def to_json(automaton: Automaton) -> str:
    return json.dumps(automaton.to_dict(), indent=2, ensure_ascii=False)


def save_json(automaton: Automaton, output_path: str | Path) -> None:
    Path(output_path).write_text(to_json(automaton), encoding="utf-8")
