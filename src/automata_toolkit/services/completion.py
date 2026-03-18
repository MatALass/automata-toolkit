from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton


SINK_STATE = "P"


def complete(automaton: Automaton, sink_state: str = SINK_STATE) -> Automaton:
    result = automaton.copy()

    candidate = sink_state
    suffix = 0
    while candidate in result.states:
        suffix += 1
        candidate = f"{sink_state}_{suffix}"

    needs_sink = False
    for state in list(result.states):
        for symbol in result.alphabet:
            if len(result.get_targets(state, symbol)) == 0:
                needs_sink = True

    if not needs_sink:
        return result

    result.states.add(candidate)
    for symbol in result.alphabet:
        result.set_transition_targets(candidate, symbol, {candidate})

    for state in list(result.states):
        for symbol in result.alphabet:
            if len(result.get_targets(state, symbol)) == 0:
                result.set_transition_targets(state, symbol, {candidate})

    return result
