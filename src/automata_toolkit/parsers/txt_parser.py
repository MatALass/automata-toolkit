from __future__ import annotations

from pathlib import Path
from string import ascii_lowercase
from typing import List, Tuple

from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.parsers.dto import AutomatonDTO


class ParseError(Exception):
    """Raised when an automaton text file has an invalid format."""


class TxtAutomatonParser:
    """
    Parser for the EFREI automata text format.

    Expected format:
    line 1: number of alphabet symbols
    line 2: number of states
    line 3: initial states -> "k s1 s2 ..."
    line 4: final states   -> "k s1 s2 ..."
    line 5: number of transitions
    next lines: transitions like "0a1", "12b3", etc.
    """

    def parse_file(self, path: str | Path) -> Automaton:
        file_path = Path(path)
        if not file_path.exists():
            raise ParseError(f"File not found: {file_path}")

        content = file_path.read_text(encoding="utf-8")
        return self.parse_text(content)

    def parse_text(self, content: str) -> Automaton:
        dto = self._parse_to_dto(content)
        return self._dto_to_automaton(dto)

    def _parse_to_dto(self, content: str) -> AutomatonDTO:
        lines = [line.strip() for line in content.splitlines() if line.strip()]

        if len(lines) < 5:
            raise ParseError(
                "Invalid file: expected at least 5 non-empty lines "
                "(alphabet size, state count, initial states, final states, transition count)."
            )

        try:
            alphabet_size = int(lines[0])
            state_count = int(lines[1])
        except ValueError as exc:
            raise ParseError("First two lines must be integers.") from exc

        if alphabet_size < 0:
            raise ParseError("Alphabet size cannot be negative.")
        if state_count < 0:
            raise ParseError("State count cannot be negative.")
        if alphabet_size > len(ascii_lowercase):
            raise ParseError(
                f"Alphabet size {alphabet_size} is too large. "
                f"Maximum supported size is {len(ascii_lowercase)}."
            )

        alphabet = list(ascii_lowercase[:alphabet_size])
        states = [str(i) for i in range(state_count)]

        initial_states = self._parse_state_list_line(
            lines[2],
            line_name="initial states",
            allowed_states=states,
        )
        final_states = self._parse_state_list_line(
            lines[3],
            line_name="final states",
            allowed_states=states,
        )

        try:
            transition_count = int(lines[4])
        except ValueError as exc:
            raise ParseError("Line 5 must be the number of transitions.") from exc

        if transition_count < 0:
            raise ParseError("Transition count cannot be negative.")

        transition_lines = lines[5:]
        if len(transition_lines) != transition_count:
            raise ParseError(
                f"Transition count mismatch: declared {transition_count}, "
                f"found {len(transition_lines)} transition lines."
            )

        transitions = [
            self._parse_transition_line(
                line=transition_line,
                allowed_states=states,
                allowed_symbols=alphabet,
            )
            for transition_line in transition_lines
        ]

        return AutomatonDTO(
            alphabet=alphabet,
            states=states,
            initial_states=initial_states,
            final_states=final_states,
            transitions=transitions,
        )

    def _parse_state_list_line(
        self,
        raw_line: str,
        line_name: str,
        allowed_states: List[str],
    ) -> List[str]:
        parts = raw_line.split()

        if not parts:
            raise ParseError(f"Invalid {line_name} line: empty line.")

        try:
            expected_count = int(parts[0])
        except ValueError as exc:
            raise ParseError(
                f"Invalid {line_name} line: first value must be an integer."
            ) from exc

        state_values = parts[1:]

        if len(state_values) != expected_count:
            raise ParseError(
                f"Invalid {line_name} line: declared {expected_count} states, "
                f"but found {len(state_values)}."
            )

        for state in state_values:
            if state not in allowed_states:
                raise ParseError(
                    f"Invalid {line_name} line: unknown state '{state}'."
                )

        return state_values

    def _parse_transition_line(
        self,
        line: str,
        allowed_states: List[str],
        allowed_symbols: List[str],
    ) -> Tuple[str, str, str]:
        for symbol in allowed_symbols:
            if symbol in line:
                parts = line.split(symbol)
                if len(parts) != 2:
                    raise ParseError(
                        f"Invalid transition '{line}': malformed transition structure."
                    )

                source, target = parts[0], parts[1]

                if source not in allowed_states:
                    raise ParseError(
                        f"Invalid transition '{line}': unknown source state '{source}'."
                    )
                if target not in allowed_states:
                    raise ParseError(
                        f"Invalid transition '{line}': unknown target state '{target}'."
                    )

                return source, symbol, target

        raise ParseError(
            f"Invalid transition '{line}': no valid symbol found in alphabet {allowed_symbols}."
        )

    def _dto_to_automaton(self, dto: AutomatonDTO) -> Automaton:
        automaton = Automaton(
            states=set(dto.states),
            alphabet=set(dto.alphabet),
            initial_states=set(dto.initial_states),
            final_states=set(dto.final_states),
        )

        for source, symbol, target in dto.transitions:
            automaton.add_transition(source, symbol, target)

        return automaton