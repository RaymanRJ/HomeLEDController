from typing import Dict, List

from app.models.LEDStripLocation import LEDStripLocation
from app.models.LEDCabinetLocation import LEDCabinetLocation
from app.models.LEDStrip import LEDStrip


class LEDCabinet:
    __led_strip_locations: Dict[LEDStripLocation, LEDStrip]

    def __init__(self, led_strip_location_dict: Dict[LEDStripLocation, LEDStrip]):
        self.__led_strip_locations = led_strip_location_dict

    @property
    def led_strips(self) -> List[LEDStrip]: return list(self.__led_strip_locations.values())

    def led_strip(self, led_strip_location: LEDStripLocation) -> LEDStrip:
        return self.__led_strip_locations[led_strip_location]
