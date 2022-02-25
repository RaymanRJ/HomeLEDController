from typing import Dict

from models.LEDCabinet import LEDCabinet
from models.LEDCabinetLocation import LEDCabinetLocation
from models.LEDStrip import LEDStrip
from models.LEDStripLocation import LEDStripLocation
from states.LEDChangeSet import LEDChangeSet, LEDChange
from states.State import State


class LEDState(State):

    __cabinets: Dict[LEDCabinetLocation, LEDCabinet]

    def __init__(self):
        # TODO: This should be populated by reading from a config file, with defaults. Right now this is for testing.
        lstrip1 = LEDStrip()
        lstrip2 = LEDStrip()
        lstrip3 = LEDStrip()
        lstrip4 = LEDStrip()

        cabinet1 = LEDCabinet(
            {
                LEDStripLocation.UPPER_LEFT: lstrip1,
                LEDStripLocation.UPPER_RIGHT: lstrip2,
                LEDStripLocation.LOWER_LEFT: lstrip3,
                LEDStripLocation.LOWER_RIGHT: lstrip4
            }
        )

        self.__cabinets = {LEDCabinetLocation.OUTER_LEFT: cabinet1}

    def build_change_set(self, requested_state) -> LEDChangeSet:
        change_set = LEDChangeSet()
        for cabinet_location, cabinet in requested_state.items():
            state_cabinet = self.__cabinets[LEDCabinetLocation(cabinet_location)]
            for led_strip_location, led_strip in cabinet.items():
                state_led_strip = state_cabinet.led_strip(LEDStripLocation(led_strip_location))
                for led_id, led in led_strip.items():
                    state_led = state_led_strip.led(led_id)
                    change = LEDChange(state_cabinet, state_led_strip, state_led, led)
                    change_set.add(change)
        return change_set

    def execute_change_set(self, change_set: LEDChangeSet) -> None:
        # Build HTTP Request Data - one per. cabinet (one per chip)
        # Should add new esp8266 library to build the data
        pass
