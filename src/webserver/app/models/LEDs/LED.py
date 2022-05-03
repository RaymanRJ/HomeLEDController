from typing import Tuple, List, Dict


class LED:
    __color: Dict[str, int]
    __brightness: int

    def __init__(self, color: Dict[str, int], brightness: int = 0):
        self.__color = color
        self.__brightness = brightness

    @property
    def color(self) -> Dict[str, int]: return self.__color
    @property
    def brightness(self) -> int: return self.__brightness

    def update(self, update_details: List[int]):
        self.__color = (update_details[0], update_details[1], update_details[2])
        self.__brightness = update_details[3]
