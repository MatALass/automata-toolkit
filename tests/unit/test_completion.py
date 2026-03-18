from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.services.completion import complete
from automata_toolkit.validators.completeness import is_complete


def test_complete_adds_sink_state_for_missing_transitions() -> None:
    automaton = Automaton(
        states={"q0", "q1"},
        alphabet={"a", "b"},
        initial_states={"q0"},
        final_states={"q1"},
        transitions={("q0", "a"): {"q1"}, ("q1", "a"): {"q1"}},
    )
    result = complete(automaton)

    assert is_complete(result) is True
    assert any(state.startswith("P") for state in result.states)
