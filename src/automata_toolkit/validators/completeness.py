from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton


def is_complete(automaton: Automaton) -> bool:
    for state in automaton.states:
        for symbol in automaton.alphabet:
            if len(automaton.get_targets(state, symbol)) != 1:
                return False
    return True
