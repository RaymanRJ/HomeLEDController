from typing import List

from models.LED import LED


class LEDStrip:
    __leds: List[LED]

    def __init__(self, num_leds: int = 16):
        self.__leds = list()
        led_color = {
            'r': 0,
            'g': 0,
            'b': 0
        }
        for _ in range(num_leds):
            self.__leds.append(LED(led_color))

    @property
    def leds(self) -> List[LED]: return self.__leds

    def led(self, led_location: int) -> LED:
        return self.__leds[led_location]
