from typing import List

from app.models.LED import LED


class LEDStrip:
    __id: str
    __leds: List[LED]

    def __init__(self, num_leds: int = 16):
        self.__leds = list()
        for i in range(num_leds):
            self.__leds.append(LED(i))
