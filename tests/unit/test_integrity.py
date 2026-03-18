import pytest

from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.validators.integrity import IntegrityError, validate_integrity


def test_validate_integrity_accepts_valid_automaton() -> None:
    automaton = Automaton(
        states={"q0", "q1"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states={"q1"},
        transitions={("q0", "a"): {"q1"}, ("q1", "a"): {"q1"}},
    )
    validate_integrity(automaton)


def test_validate_integrity_rejects_unknown_target() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states=set(),
        transitions={("q0", "a"): {"q1"}},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_empty_states() -> None:
    automaton = Automaton(
        states=set(),
        alphabet={"a"},
        initial_states={"q0"},
        final_states=set(),
        transitions={},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_empty_alphabet() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet=set(),
        initial_states={"q0"},
        final_states=set(),
        transitions={},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_empty_initial_states() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet={"a"},
        initial_states=set(),
        final_states=set(),
        transitions={},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_unknown_initial_state() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet={"a"},
        initial_states={"q1"},
        final_states=set(),
        transitions={},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_unknown_final_state() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states={"q1"},
        transitions={},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_unknown_transition_source() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states=set(),
        transitions={("q1", "a"): {"q0"}},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_unknown_transition_symbol() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states=set(),
        transitions={("q0", "b"): {"q0"}},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)


def test_validate_integrity_rejects_empty_transition_targets() -> None:
    automaton = Automaton(
        states={"q0"},
        alphabet={"a"},
        initial_states={"q0"},
        final_states=set(),
        transitions={("q0", "a"): set()},
    )
    with pytest.raises(IntegrityError):
        validate_integrity(automaton)