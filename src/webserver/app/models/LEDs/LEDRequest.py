from typing import List

from app.models.LEDs.LEDAction import LEDAction
from app.models.LEDs.LEDStrip import LEDStrip


class LEDRequest:
    __action: LEDAction
    __strips: List[LEDStrip]
