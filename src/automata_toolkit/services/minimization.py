from __future__ import annotations

from collections import defaultdict

from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.services.completion import complete
from automata_toolkit.services.determinization import determinize
from automata_toolkit.validators.completeness import is_complete
from automata_toolkit.validators.determinism import is_deterministic


def minimize(automaton: Automaton) -> Automaton:
    work = automaton.copy()
    if not is_deterministic(work):
        work = determinize(work)
    if not is_complete(work):
        work = complete(work)

    finals = set(work.final_states)
    non_finals = work.states.difference(finals)
    partitions = [group for group in [finals, non_finals] if group]

    changed = True
    while changed:
        changed = False
        new_partitions = []
        for group in partitions:
            buckets = defaultdict(set)
            for state in group:
                signature = []
                for symbol in sorted(work.alphabet):
                    target = next(iter(work.get_targets(state, symbol)))
                    target_partition = next(
                        index for index, partition in enumerate(partitions) if target in partition
                    )
                    signature.append((symbol, target_partition))
                buckets[tuple(signature)].add(state)
            new_partitions.extend(buckets.values())
            if len(buckets) > 1:
                changed = True
        partitions = new_partitions

    state_name_map = {
        index: "{" + ",".join(sorted(partition)) + "}"
        for index, partition in enumerate(partitions)
    }

    minimized = Automaton(
        states=set(state_name_map.values()),
        alphabet=set(work.alphabet),
        initial_states=set(),
        final_states=set(),
    )

    for index, partition in enumerate(partitions):
        new_name = state_name_map[index]
        if partition.intersection(work.initial_states):
            minimized.initial_states.add(new_name)
        if partition.intersection(work.final_states):
            minimized.final_states.add(new_name)

    for index, partition in enumerate(partitions):
        representative = next(iter(partition))
        source_name = state_name_map[index]
        for symbol in work.alphabet:
            target = next(iter(work.get_targets(representative, symbol)))
            target_index = next(i for i, part in enumerate(partitions) if target in part)
            minimized.add_transition(source_name, symbol, state_name_map[target_index])

    return minimized
