from typing import Dict

from app.models.LEDStripLocation import LEDStripLocation
from app.models.LEDCabinetLocation import LEDCabinetLocation
from app.models.LEDStrip import LEDStrip


class LEDCabinet:
    __led_strip_locations: Dict[LEDStrip, LEDStripLocation]
    __cabinet_location: LEDCabinetLocation

    def __init__(self, cabinet_location: LEDCabinetLocation, led_strip_location_dict: Dict[LEDStrip, LEDStripLocation]):
        self.__led_strip_locations = led_strip_location_dict
        self.__cabinet_location = cabinet_location

    @property
    def cabinet_id(self) -> LEDCabinetLocation: return self.__cabinet_location
    @property
    def led_strip_and_locations(self) -> Dict[LEDStrip, LEDStripLocation]: return self.__led_strip_locations

