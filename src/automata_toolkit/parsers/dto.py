from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class AutomatonDTO:
    alphabet: List[str]
    states: List[str]
    initial_states: List[str]
    final_states: List[str]
    transitions: List[Tuple[str, str, str]]