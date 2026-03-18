from __future__ import annotations

from pathlib import Path

from automata_toolkit.domain.automaton import Automaton


def to_dot(automaton: Automaton) -> str:
    lines = [
        "digraph Automaton {",
        "  rankdir=LR;",
        "  node [shape=circle];",
        '  __start__ [shape=point, label=""];',
    ]

    for state in sorted(automaton.states):
        if state in automaton.final_states:
            lines.append(f'  "{state}" [shape=doublecircle];')
        else:
            lines.append(f'  "{state}" [shape=circle];')

    for initial_state in sorted(automaton.initial_states):
        lines.append(f'  __start__ -> "{initial_state}";')

    for (source, symbol), targets in sorted(automaton.transitions.items()):
        for target in sorted(targets):
            lines.append(f'  "{source}" -> "{target}" [label="{symbol}"];')

    lines.append("}")
    return "\n".join(lines)


def save_dot(automaton: Automaton, output_path: str | Path) -> None:
    Path(output_path).write_text(to_dot(automaton), encoding="utf-8")
