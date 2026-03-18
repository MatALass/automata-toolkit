from __future__ import annotations

from automata_toolkit.domain.automaton import Automaton


class IntegrityError(ValueError):
    pass


def validate_integrity(automaton: Automaton) -> None:
    if not automaton.states:
        raise IntegrityError("Automaton must contain at least one state.")
    if not automaton.alphabet:
        raise IntegrityError("Automaton alphabet must not be empty.")
    if not automaton.initial_states:
        raise IntegrityError("Automaton must contain at least one initial state.")
    if not automaton.initial_states.issubset(automaton.states):
        raise IntegrityError("Initial states must belong to the set of states.")
    if not automaton.final_states.issubset(automaton.states):
        raise IntegrityError("Final states must belong to the set of states.")

    for (source, symbol), targets in automaton.transitions.items():
        if source not in automaton.states:
            raise IntegrityError(f"Transition source '{source}' is not a declared state.")
        if symbol not in automaton.alphabet:
            raise IntegrityError(f"Transition symbol '{symbol}' is not in the alphabet.")
        if not targets:
            raise IntegrityError(f"Transition ({source}, {symbol}) has no targets.")
        unknown_targets = targets.difference(automaton.states)
        if unknown_targets:
            raise IntegrityError(
                f"Transition ({source}, {symbol}) targets unknown states: {sorted(unknown_targets)}."
            )
