from automata_toolkit.parsers.txt_parser import TxtAutomatonParser


def test_parse_text_builds_automaton() -> None:
    text = """
    states: q0,q1
    alphabet: a,b
    initial_states: q0
    final_states: q1
    transitions:
    q0,a,q1
    q0,b,q0
    q1,a,q1
    q1,b,q0
    """
    automaton = TxtAutomatonParser().parse_text(text)

    assert automaton.states == {"q0", "q1"}
    assert automaton.alphabet == {"a", "b"}
    assert automaton.initial_states == {"q0"}
    assert automaton.final_states == {"q1"}
    assert automaton.get_targets("q0", "a") == {"q1"}
