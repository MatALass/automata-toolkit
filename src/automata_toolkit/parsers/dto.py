from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class RawTransitionDTO:
    source: str
    symbol: str
    target: str


@dataclass
class RawAutomatonDTO:
    states: List[str] = field(default_factory=list)
    alphabet: List[str] = field(default_factory=list)
    initial_states: List[str] = field(default_factory=list)
    final_states: List[str] = field(default_factory=list)
    transitions: List[RawTransitionDTO] = field(default_factory=list)
