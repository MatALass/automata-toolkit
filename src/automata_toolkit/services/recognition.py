from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton


def recognize_word(automaton: Automaton, word: str) -> bool:
    current_states = set(automaton.initial_states)
    for symbol in word:
        next_states = set()
        for state in current_states:
            next_states.update(automaton.get_targets(state, symbol))
        current_states = next_states
        if not current_states:
            return False
    return any(state in automaton.final_states for state in current_states)
