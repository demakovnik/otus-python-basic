"""
создайте класс `Car`, наследник `Vehicle`
"""
import homework_02.base as base


class Car(base.Vehicle):

    engine = None

    def set_engine(self, engine):
        self.engine = engine
