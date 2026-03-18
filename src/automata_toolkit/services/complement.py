from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.services.completion import complete
from automata_toolkit.services.determinization import determinize
from automata_toolkit.validators.completeness import is_complete
from automata_toolkit.validators.determinism import is_deterministic


def complement(automaton: Automaton) -> Automaton:
    result = automaton.copy()
    if not is_deterministic(result):
        result = determinize(result)
    if not is_complete(result):
        result = complete(result)

    result.final_states = result.states.difference(result.final_states)
    return result
