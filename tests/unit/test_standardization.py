from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.services.standardization import standardize
from automata_toolkit.validators.standardness import is_standard


def test_standardize_creates_single_clean_initial_state() -> None:
    automaton = Automaton(
        states={"q0", "q1"},
        alphabet={"a"},
        initial_states={"q0", "q1"},
        final_states={"q1"},
        transitions={("q0", "a"): {"q1"}, ("q1", "a"): {"q1"}},
    )
    result = standardize(automaton)

    assert is_standard(result) is True
    assert len(result.initial_states) == 1

def test_standardize_on_already_standard_automaton():
    automaton = Automaton(
        states={"0"},
        alphabet={"a"},
        initial_states={"0"},
        final_states={"0"},
        transitions={("0", "a"): {"0"}},
    )

    result = standardize(automaton)

    assert result.initial_states == {"0"}