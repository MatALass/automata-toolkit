from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton


def render_summary(automaton: Automaton) -> str:
    lines = [
        f"States: {', '.join(sorted(automaton.states))}",
        f"Alphabet: {', '.join(sorted(automaton.alphabet))}",
        f"Initial states: {', '.join(sorted(automaton.initial_states))}",
        f"Final states: {', '.join(sorted(automaton.final_states))}",
    ]
    return "\n".join(lines)


def render_transition_table(automaton: Automaton) -> str:
    header = ["State"] + sorted(automaton.alphabet)
    rows = [header]

    for state in sorted(automaton.states):
        row = [state]
        for symbol in sorted(automaton.alphabet):
            targets = sorted(automaton.get_targets(state, symbol))
            row.append("{" + ", ".join(targets) + "}" if targets else "-")
        rows.append(row)

    column_widths = [max(len(row[i]) for row in rows) for i in range(len(header))]
    formatted_rows = []
    for row in rows:
        formatted_rows.append(" | ".join(cell.ljust(column_widths[i]) for i, cell in enumerate(row)))
    return "\n".join(formatted_rows)
