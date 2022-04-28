from typing import Dict

from models.LEDCabinet import LEDCabinet
from models.LEDCabinetLocation import LEDCabinetLocation
from models.LEDStrip import LEDStrip
from models.LEDStripLocation import LEDStripLocation
from states.LEDChangeSet import LEDChangeSet, LEDChange
from states.State import State


class LEDState(State):

    __cabinets: Dict[LEDCabinetLocation, LEDCabinet] = dict()

    def __init__(self):
        # TODO: This should be populated by reading from a config file, with defaults. Right now this is for testing.
        for cabinet_location in LEDCabinetLocation:
            led_locations = dict()
            for led_location in LEDStripLocation:
                led_locations[led_location] = LEDStrip()
            self.__cabinets[cabinet_location] = LEDCabinet(led_locations)

    def get_LED_color(self, cabinet_id: str):
        led_cabinet_location = LEDCabinetLocation[cabinet_id]
        return self.__cabinets[led_cabinet_location].led_strips[0].leds[0].color

    def update_state(self, cabinet: str, led_strip: Dict[str, str], rgb: Dict[str, int]) -> State:
        led_cabinet = LEDCabinetLocation[cabinet]
        led_strip_location = LEDStripLocation.ALL if led_strip == "ALL" else LEDStripLocation[led_strip['id']]
        # TODO: Pass params to micrcontrollers - 'execute_change' method
        return {
            'background': rgb,
            'cabinet': led_cabinet.value,
            'strip_id': led_strip_location.value
        }

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
