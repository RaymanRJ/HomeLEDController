from typing import Dict, Tuple

from states.LEDState import LEDState
from states.State import State


class StateManager:
    __current_LED_state: LEDState

    def __init__(self):
        self.__current_LED_state = LEDState()

    def update_state(self, requested_state: Dict) -> Tuple[int, State]:
        cabinet = requested_state['cabinet_id']
        led_strip = requested_state['selectedLEDStrip']
        rgb = requested_state['background']['rgb']
        new_state = self.__current_LED_state.update_state(cabinet=cabinet, led_strip=led_strip, rgb=rgb)
        return 200, new_state

    def get_cabinet_state(self, cabinet_id: str):
        cabinet_color = self.__current_LED_state.get_LED_color(cabinet_id)
        status = {
            "cabinet": cabinet_id,
            "strip_id": "ALL",
            "background": {
                "r": 48,
                "g": 63,
                "b": 159
            }
        }
        return status

    def get_led_strip_status(self, cabinet_id: str, strip_id: str):
        cabinet_color = self.__current_LED_state.get_LED_color(cabinet_id)
        status = {
            "cabinet": cabinet_id,
            "strip_id": strip_id,
            "background": {
                "r": 48,
                "g": 63,
                "b": 159
            }
        }
        return status

    def register_device(self, device: Dict) -> Tuple[int, Dict]:
        pass
