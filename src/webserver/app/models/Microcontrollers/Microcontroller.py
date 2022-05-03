class Microcontroller:

    __ip_address: str
    __mac_address: str
    __pin_to_led_strip: dict()

    def __init__(self, ip_address: str, mac_address: str):
        self.__ip_address = ip_address
        self.__mac_address = mac_address
