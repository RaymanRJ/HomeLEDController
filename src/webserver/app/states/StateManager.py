from typing import Dict, Tuple

from states.LEDState import LEDState
from states.State import State


class StateManager:
    __current_LED_state: LEDState

    def __init__(self):
        self.__current_LED_state = LEDState()

    def update_state(self, requested_state: Dict) -> Tuple[int, State]:
        state_type = requested_state['state_type']
        if state_type == 'LED_STATE':
            new_state = self.__current_LED_state.update_state(requested_state['state_changes'])
            return 200, new_state
