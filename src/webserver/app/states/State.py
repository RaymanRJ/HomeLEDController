from __future__ import annotations

from abc import abstractmethod
from typing import Dict

from states.ChangeSet import ChangeSet


class State:

    def update_state(self, requested_state: Dict) -> State:
        # Convert the JSON data from user to usable objects:
        change_set = self.build_change_set(requested_state)
        # Convert the changes into JSON data that will work with esp8266:
        # i.e. convert "cabinet/stip/led locations" to chip & pin combos
        self.execute_change_set(change_set)
        return self

    @abstractmethod
    def build_change_set(self, requested_state: Dict) -> ChangeSet:
        pass

    @abstractmethod
    def execute_change_set(self, change_set: ChangeSet):
        pass
