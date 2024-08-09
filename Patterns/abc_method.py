from abc import ABC, abstractmethod


class Sender(ABC):

    @abstractmethod
    def send(self, message):
        pass


class SenderCreator(ABC):

    @abstractmethod
    def create_sender(self) -> Sender:
        pass


class ConsoleSender(Sender):

    def send(self, message):
        print(f"[MESSAGE] {message}")


class ConsoleCreator(SenderCreator):

    def create_sender(self) -> Sender:
        sender = ConsoleSender()
        return sender


class FileSender(Sender):

    def __init__(self, file_path):
        self.__fp = file_path

    def send(self, message):
        with open(self.__fp, "a", encoding="utf-8") as f:
            f.write(message + "\n")


class FileSenderCreator(SenderCreator):

    def __init__(self, file_path):
        self.file_path = file_path

    def create_sender(self) -> Sender:
        sender = FileSender(self.file_path)
        return sender


class App:

    def __init__(self, creator: SenderCreator):
        self.__creator = creator

    def run(self):
        sender = self.__creator.create_sender()
        msg = input("Message to send: ")
        sender.send(msg)


creator = FileSenderCreator("text.txt")
App(creator).run()
