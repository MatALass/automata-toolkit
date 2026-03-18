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
