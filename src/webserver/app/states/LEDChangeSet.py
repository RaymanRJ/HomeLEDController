from typing import Dict

from models.LED import LED
from models.LEDCabinet import LEDCabinet
from models.LEDStrip import LEDStrip
from states.ChangeSet import ChangeSet, Change


class LEDChange(Change):
    __cabinet: LEDCabinet
    __led_strip: LEDStrip
    __led: LED
    __led_change: Dict[str, int]

    def __init__(self, cabinet: LEDCabinet, led_strip: LEDStrip, led: LED, led_change: Dict[str, int]):
        self.__cabinet = cabinet
        self.__led_strip = led_strip
        self.__led = led
        self.__led_change = led_change


class LEDChangeSet(ChangeSet):
    pass