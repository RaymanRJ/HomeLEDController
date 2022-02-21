from typing import List

from app.models.LEDAction import LEDAction
from app.models.LEDStrip import LEDStrip


class LEDRequest:
    __action: LEDAction
    __strips: List[LEDStrip]
