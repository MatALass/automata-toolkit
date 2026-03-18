from __future__ import annotations

from pathlib import Path

from automata_toolkit.domain.automaton import Automaton
from automata_toolkit.parsers.dto import RawAutomatonDTO, RawTransitionDTO


REQUIRED_KEYS = {"states", "alphabet", "initial_states", "final_states", "transitions"}


class ParseError(ValueError):
    pass


class TxtAutomatonParser:
    def parse_file(self, path: str | Path) -> Automaton:
        content = Path(path).read_text(encoding="utf-8")
        return self.parse_text(content)

    def parse_text(self, content: str) -> Automaton:
        dto = self._parse_to_dto(content)
        automaton = Automaton(
            states=set(dto.states),
            alphabet=set(dto.alphabet),
            initial_states=set(dto.initial_states),
            final_states=set(dto.final_states),
        )
        for transition in dto.transitions:
            automaton.add_transition(transition.source, transition.symbol, transition.target)
        return automaton

    def _parse_to_dto(self, content: str) -> RawAutomatonDTO:
        lines = [line.strip() for line in content.splitlines() if line.strip() and not line.strip().startswith("#")]
        if not lines:
            raise ParseError("Input file is empty.")

        sections: dict[str, list[str]] = {}
        i = 0
        while i < len(lines):
            line = lines[i]
            if ":" not in line:
                raise ParseError(f"Invalid line: '{line}'. Expected '<key>: <value>' or 'transitions:'.")
            key, value = [part.strip() for part in line.split(":", 1)]
            if key not in REQUIRED_KEYS:
                raise ParseError(f"Unknown section '{key}'.")
            if key != "transitions":
                sections[key] = [value]
                i += 1
                continue

            transition_lines: list[str] = []
            i += 1
            while i < len(lines) and ":" not in lines[i]:
                transition_lines.append(lines[i])
                i += 1
            sections[key] = transition_lines

        missing = REQUIRED_KEYS.difference(sections.keys())
        if missing:
            raise ParseError(f"Missing required sections: {', '.join(sorted(missing))}.")

        dto = RawAutomatonDTO(
            states=self._split_csv(sections["states"][0]),
            alphabet=self._split_csv(sections["alphabet"][0]),
            initial_states=self._split_csv(sections["initial_states"][0]),
            final_states=self._split_csv(sections["final_states"][0]),
            transitions=[self._parse_transition_line(line) for line in sections["transitions"]],
        )
        return dto

    @staticmethod
    def _split_csv(value: str) -> list[str]:
        return [item.strip() for item in value.split(",") if item.strip()]

    @staticmethod
    def _parse_transition_line(line: str) -> RawTransitionDTO:
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 3:
            raise ParseError(f"Invalid transition line '{line}'. Expected 'source,symbol,target'.")
        return RawTransitionDTO(source=parts[0], symbol=parts[1], target=parts[2])
