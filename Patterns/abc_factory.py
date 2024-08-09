from abc import ABC, abstractmethod


class Button(ABC):

    def click(self):
        pass

    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):

    def check(self):
        pass

    @abstractmethod
    def render(self):
        pass


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsButton(Button):

    def click(self):
        print("Click win button")

    def render(self):
        print("Рисуем кнопку для Windows")


class WindowsCheckbox(Checkbox):

    def check(self):
        print("Check")

    def render(self):
        print("Рисуем чекбокс для Windows")


class WinFactory(GUIFactory):

    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacButton(Button):

    def click(self):
        print("Click win button")

    def render(self):
        print("Рисуем кнопку для Mac")


class MacCheckbox(Checkbox):

    def check(self):
        print("Check")

    def render(self):
        print("Рисуем чекбокс для Mac")


class MacFactory(GUIFactory):

    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class App:

    def __init__(self, gui_factory: GUIFactory):
        self.__f = gui_factory

    def run(self):
        btn = self.__f.create_button()
        btn.render()
        btn.click()

        ck = self.__f.create_checkbox()
        ck.render()
        ck.check()


import os


os.name = "mac"
if os.name == "nt":
    f = WinFactory()
    App(f).run()
else:
    f = MacFactory()
    App(f).run()

