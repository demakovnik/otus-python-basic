"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02 import base, exceptions


class Plane(base.Vehicle):

    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        result = self.cargo + cargo
        if result <= self.max_cargo:
            self.cargo = result
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result
