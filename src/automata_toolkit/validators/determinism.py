from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton


def is_deterministic(automaton: Automaton) -> bool:
    if len(automaton.initial_states) != 1:
        return False
    for targets in automaton.transitions.values():
        if len(targets) > 1:
            return False
    return True
