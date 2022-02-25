from typing import Tuple, List


class LED:
    __color: Tuple[int, int, int]
    __brightness: int

    def __init__(self, color: Tuple[int, int, int] = (0, 0, 0), brightness: int = 0):
        self.__color = color
        self.__brightness = brightness

    @property
    def color(self) -> Tuple[int, int, int]: return self.__color
    @property
    def brightness(self) -> int: return self.__brightness

    def update(self, update_details: List[int, int, int, int]):
        self.__color = (update_details[0], update_details[1], update_details[2])
        self.__brightness = update_details[3]
