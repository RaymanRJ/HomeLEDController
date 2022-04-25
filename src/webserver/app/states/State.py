from __future__ import annotations

from abc import abstractmethod
from typing import Dict

from states.ChangeSet import ChangeSet


class State:

    def update_state(self, cabinet: str, led_strip: str, rgb: Dict[str: int]) -> State:
        pass

    @abstractmethod
    def build_change_set(self, requested_state: Dict) -> ChangeSet:
        pass

    @abstractmethod
    def execute_change_set(self, change_set: ChangeSet):
        pass
