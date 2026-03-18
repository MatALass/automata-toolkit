from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton


def is_standard(automaton: Automaton) -> bool:
    if len(automaton.initial_states) != 1:
        return False

    initial_state = next(iter(automaton.initial_states))
    for (source, _symbol), targets in automaton.transitions.items():
        if initial_state in targets and source != initial_state:
            return False
    return True
