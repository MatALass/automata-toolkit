from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.validators.determinism import is_deterministic


def test_is_deterministic_returns_true_for_dfa() -> None:
    automaton = Automaton(
        states={"q0", "q1"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states={"q1"},
        transitions={("q0", "a"): {"q1"}, ("q1", "a"): {"q1"}},
    )
    assert is_deterministic(automaton) is True


def test_is_deterministic_returns_false_for_multiple_targets() -> None:
    automaton = Automaton(
        states={"q0", "q1", "q2"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states={"q2"},
        transitions={("q0", "a"): {"q1", "q2"}},
    )
    assert is_deterministic(automaton) is False
