"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, text):
        super.__init__()


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass
