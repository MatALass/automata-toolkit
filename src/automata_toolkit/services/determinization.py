from __future__ import annotations

from collections import deque
from typing import FrozenSet

from automata_toolkit.domain.automaton import Automaton


def _subset_name(subset: FrozenSet[str]) -> str:
    if not subset:
        return "EMPTY"
    return "{" + ",".join(sorted(subset)) + "}"


def determinize(automaton: Automaton) -> Automaton:
    initial_subset: FrozenSet[str] = frozenset(automaton.initial_states)
    queue: deque[FrozenSet[str]] = deque([initial_subset])
    visited: set[FrozenSet[str]] = {initial_subset}

    result = Automaton(
        states={_subset_name(initial_subset)},
        alphabet=set(automaton.alphabet),
        initial_states={_subset_name(initial_subset)},
        final_states=set(),
    )

    while queue:
        current_subset = queue.popleft()
        current_name = _subset_name(current_subset)

        if any(state in automaton.final_states for state in current_subset):
            result.final_states.add(current_name)

        for symbol in automaton.alphabet:
            next_subset = frozenset(
                target
                for state in current_subset
                for target in automaton.get_targets(state, symbol)
            )
            next_name = _subset_name(next_subset)
            result.states.add(next_name)
            result.add_transition(current_name, symbol, next_name)
            if next_subset not in visited:
                visited.add(next_subset)
                queue.append(next_subset)

    return result
