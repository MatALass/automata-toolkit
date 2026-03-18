from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.validators.standardness import is_standard


NEW_INITIAL_STATE = "I"


def standardize(automaton: Automaton, new_initial_state: str = NEW_INITIAL_STATE) -> Automaton:
    if is_standard(automaton):
        return automaton.copy()

    result = automaton.copy()
    candidate = new_initial_state
    suffix = 0
    while candidate in result.states:
        suffix += 1
        candidate = f"{new_initial_state}_{suffix}"

    previous_initials = set(result.initial_states)
    result.states.add(candidate)
    result.initial_states = {candidate}

    if previous_initials.intersection(result.final_states):
        result.final_states.add(candidate)

    for old_initial in previous_initials:
        for symbol in result.alphabet:
            for target in result.get_targets(old_initial, symbol):
                result.add_transition(candidate, symbol, target)

    return result
