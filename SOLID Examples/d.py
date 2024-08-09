"""
Dependency inversion principle
Принцип инверсии зависимости

Модули верхнего уровня не должны зависеть от модулей нижнего уровня
Оба должны зависеть от абстракций
Абстракции не должны зависель от деталей
Детали должны зависеть от абстракций
"""
from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def get_data(self) -> str:
        pass


class RSS(DataSource):

    def get_data(self) -> str:
        return "Data from RSS"


class API(DataSource):

    def get_data(self) -> str:
        return "Data from API"


class App:

    def display_data(self, data_source: DataSource):
        data = data_source.get_data()
        print(f"[DISPLAY] {data}")


app = App()

app.display_data(RSS())
app.display_data(API())
