from typing import List

from app.models.LEDCabinet import LEDCabinet


class LEDState:
    __cabinets: List[LEDCabinet]

    def __init__(self, *cabinets: LEDCabinet):
        self.__cabinets = [*cabinets]
