from typing import Dict, Tuple

from app.models.LEDCabinet import LEDCabinet
from app.models.LEDCabinetLocation import LEDCabinetLocation
from app.states.LEDState import LEDState
from app.models.LEDStrip import LEDStrip
from app.models.LEDStripLocation import LEDStripLocation


class StateManager:
    __current_state: LEDState

    def __init__(self):
        # TODO: This should be populated by reading from a config file, with defaults. Right now this is for testing.
        lstrip1 = LEDStrip()
        lstrip2 = LEDStrip()
        lstrip3 = LEDStrip()
        lstrip4 = LEDStrip()

        cabinet1 = LEDCabinet(LEDCabinetLocation.OUTER_LEFT,
                              {
                                  lstrip1: LEDStripLocation.UPPER_LEFT,
                                  lstrip2: LEDStripLocation.UPPER_RIGHT,
                                  lstrip3: LEDStripLocation.LOWER_LEFT,
                                  lstrip4: LEDStripLocation.LOWER_RIGHT
                              })
        self.__current_state = LEDState(cabinet1, cabinet1)

    def update_state(self, requested_state: Dict) -> Tuple[int, str]:
        print(requested_state)
        return 200, "OK"
