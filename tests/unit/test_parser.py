import pytest

from automata_toolkit.parsers.txt_parser import ParseError, TxtAutomatonParser


def test_parse_text_builds_automaton_from_efrei_format() -> None:
    content = """3
5
1 1
1 1
14
0b1
0a3
0c3
1a0
1b2
2a1
2b4
2c4
4a4
4b4
4c4
3a3
3b3
3c3
"""

    parser = TxtAutomatonParser()
    automaton = parser.parse_text(content)

    assert automaton.states == {"0", "1", "2", "3", "4"}
    assert automaton.alphabet == {"a", "b", "c"}
    assert automaton.initial_states == {"1"}
    assert automaton.final_states == {"1"}

    assert automaton.get_targets("0", "a") == {"3"}
    assert automaton.get_targets("0", "b") == {"1"}
    assert automaton.get_targets("0", "c") == {"3"}
    assert automaton.get_targets("4", "a") == {"4"}
    assert automaton.get_targets("4", "b") == {"4"}
    assert automaton.get_targets("4", "c") == {"4"}


def test_parse_text_rejects_too_short_input() -> None:
    content = """3
5
"""

    with pytest.raises(ParseError):
        TxtAutomatonParser().parse_text(content)


def test_parse_text_rejects_non_integer_header() -> None:
    content = """abc
5
1 0
1 0
0
"""

    with pytest.raises(ParseError):
        TxtAutomatonParser().parse_text(content)


def test_parse_text_rejects_invalid_initial_state_count() -> None:
    content = """2
3
2 0
1 1
0
"""

    with pytest.raises(ParseError):
        TxtAutomatonParser().parse_text(content)


def test_parse_text_rejects_transition_count_mismatch() -> None:
    content = """2
2
1 0
1 1
4
0a1
0b0
1a1
"""

    with pytest.raises(ParseError):
        TxtAutomatonParser().parse_text(content)


def test_parse_text_rejects_unknown_target_state() -> None:
    content = """2
2
1 0
1 1
1
0a9
"""

    with pytest.raises(ParseError):
        TxtAutomatonParser().parse_text(content)


def test_parse_text_rejects_symbol_outside_alphabet() -> None:
    content = """2
2
1 0
1 1
1
0c1
"""

    with pytest.raises(ParseError):
        TxtAutomatonParser().parse_text(content)