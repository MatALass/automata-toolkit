from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.services.minimization import minimize


def test_minimize_preserves_language_shape_on_simple_dfa() -> None:
    automaton = Automaton(
        states={"q0", "q1", "q2"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states={"q2"},
        transitions={
            ("q0", "a"): {"q1"},
            ("q1", "a"): {"q2"},
            ("q2", "a"): {"q2"},
        },
    )
    result = minimize(automaton)

    assert len(result.states) <= len(automaton.states)
    assert len(result.initial_states) == 1
