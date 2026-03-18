from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Set, Tuple

State = str
Symbol = str
TransitionKey = Tuple[State, Symbol]
TransitionValue = Set[State]


@dataclass
class Automaton:
    states: Set[State]
    alphabet: Set[Symbol]
    initial_states: Set[State]
    final_states: Set[State]
    transitions: Dict[TransitionKey, TransitionValue] = field(default_factory=dict)

    def add_transition(self, source: State, symbol: Symbol, target: State) -> None:
        key = (source, symbol)
        self.transitions.setdefault(key, set()).add(target)

    def set_transition_targets(self, source: State, symbol: Symbol, targets: Iterable[State]) -> None:
        self.transitions[(source, symbol)] = set(targets)

    def get_targets(self, source: State, symbol: Symbol) -> Set[State]:
        return set(self.transitions.get((source, symbol), set()))

    def all_transitions(self) -> Dict[TransitionKey, TransitionValue]:
        return {key: set(value) for key, value in self.transitions.items()}

    def copy(self) -> "Automaton":
        return Automaton(
            states=set(self.states),
            alphabet=set(self.alphabet),
            initial_states=set(self.initial_states),
            final_states=set(self.final_states),
            transitions=self.all_transitions(),
        )

    def is_accepting_state(self, state: State) -> bool:
        return state in self.final_states

    def to_dict(self) -> dict:
        return {
            "states": sorted(self.states),
            "alphabet": sorted(self.alphabet),
            "initial_states": sorted(self.initial_states),
            "final_states": sorted(self.final_states),
            "transitions": {
                f"{source},{symbol}": sorted(targets)
                for (source, symbol), targets in sorted(self.transitions.items())
            },
        }
