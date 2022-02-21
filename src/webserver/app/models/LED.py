from typing import Tuple


class LED:
    __position: int
    __color: Tuple[int, int, int]
    __brightness: int

    def __init__(self, position: int, color: Tuple[int, int, int] = (0, 0, 0), brightness: int = 0):
        self.__position = position
        self.__color = color
        self.__brightness = brightness

    @property
    def position(self) -> int: return self.__position
    @property
    def color(self) -> Tuple[int, int, int]: return self.__color
    @property
    def brightness(self) -> int: return self.__brightness

