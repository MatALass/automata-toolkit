from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.services.complement import complement


def test_complement_inverts_final_states_on_complete_dfa() -> None:
    automaton = Automaton(
        states={"q0", "q1"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states={"q1"},
        transitions={("q0", "a"): {"q1"}, ("q1", "a"): {"q1"}},
    )
    result = complement(automaton)

    assert result.final_states == {"q0"}

def test_complement_twice_returns_original_language():
    automaton = Automaton(
        states={"0"},
        alphabet={"a"},
        initial_states={"0"},
        final_states=set(),
        transitions={("0", "a"): {"0"}},
    )

    comp1 = complement(automaton)
    comp2 = complement(comp1)

    assert comp2.final_states == automaton.final_states