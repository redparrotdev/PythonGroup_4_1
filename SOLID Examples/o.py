"""
Open-closed principle
Принцип открытости-закрытости

Класс должен быть открыт для расширения
но закрыт для модификации
"""


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_area(self) -> float:
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.r = radius

    def get_area(self) -> float:
        return 3.14 * self.r ** 2


class Rect(Shape):

    def __init__(self, a):
        self.a = a

    def get_area(self) -> float:
        return self.a ** 2

