from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.services.determinization import determinize
from automata_toolkit.services.recognition import recognize_word
from automata_toolkit.validators.determinism import is_deterministic


def test_determinize_keeps_deterministic_automaton_consistent() -> None:
    automaton = Automaton(
        states={"0", "1"},
        alphabet={"a", "b"},
        initial_states={"0"},
        final_states={"1"},
        transitions={
            ("0", "a"): {"1"},
            ("0", "b"): {"0"},
            ("1", "a"): {"1"},
            ("1", "b"): {"0"},
        },
    )

    result = determinize(automaton)

    assert is_deterministic(result) is True
    assert result.initial_states == {"{0}"}
    assert result.final_states == {"{1}"}
    assert result.get_targets("{0}", "a") == {"{1}"}
    assert result.get_targets("{0}", "b") == {"{0}"}
    assert result.get_targets("{1}", "a") == {"{1}"}
    assert result.get_targets("{1}", "b") == {"{0}"}


def test_determinize_converts_nfa_to_dfa() -> None:
    automaton = Automaton(
        states={"0", "1", "2"},
        alphabet={"a", "b"},
        initial_states={"0"},
        final_states={"2"},
        transitions={
            ("0", "a"): {"0", "1"},
            ("0", "b"): {"0"},
            ("1", "b"): {"2"},
            ("2", "a"): {"2"},
            ("2", "b"): {"2"},
        },
    )

    result = determinize(automaton)

    assert is_deterministic(result) is True
    assert "{0}" in result.states
    assert "{0,1}" in result.states
    assert "{0,2}" in result.states or "{0,1,2}" in result.states or "{2}" in result.states

    for targets in result.transitions.values():
        assert len(targets) == 1


def test_determinize_preserves_language_on_sample_words() -> None:
    automaton = Automaton(
        states={"0", "1", "2"},
        alphabet={"a", "b"},
        initial_states={"0"},
        final_states={"2"},
        transitions={
            ("0", "a"): {"0", "1"},
            ("0", "b"): {"0"},
            ("1", "b"): {"2"},
            ("2", "a"): {"2"},
            ("2", "b"): {"2"},
        },
    )

    determinized = determinize(automaton)

    sample_words = [
        "",
        "a",
        "b",
        "ab",
        "aab",
        "aaab",
        "abab",
        "bbb",
        "baab",
    ]

    for word in sample_words:
        assert recognize_word(automaton, word) == recognize_word(determinized, word)