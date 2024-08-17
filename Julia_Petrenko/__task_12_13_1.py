import json
#  1. Мы можем отправить пользователю книгу по электронной почте
#     (вывести в консоль какую книгу кому и на какой ящик отправляете)
#     или отправить посылкой (вывести в консоль какую книгу кому и каким сервисом отправляем)
#  2. Перед оправкой нужно получить книгу, которую заказал пользователь
#  3. Получать информации о заказе пользователя можно из словаря, файла или любого другого источника данных
#  4. При желании любой способ отправки книги или получения заказа можно заменить с минимальными изменениями в коде
#
# Советы: используйте абстракции, классы с фабринчными методами или цепочки наследований для решения поставленных задач


from abc import ABC, abstractmethod
import json


class Book(ABC):

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Mail(ABC):

    @abstractmethod
    def send_book(self, user: str, book: Book):
        ...

    @abstractmethod
    def get_book_stored_by_user(self, user: str) -> Book:
        ...


class EBook(Book):

    def __init__(self, title, author, genre, email: str):
        super().__init__(title, author, genre)
        self.email = email


class Email(Mail):

    def send_book(self, user: str, book: EBook):
        print(f"{book.genre.capitalize()} {book.title} by {book.author} "
              f" was send {user} via email to {book.email}")

    def get_book_stored_by_user(self, user: str) -> EBook:
        with open(f"order_{user.lower()}.json") as f:
            dict_order = json.loads(f.read())
        return EBook(dict_order["title"],
                     dict_order["author"],
                     dict_order["genre"],
                     dict_order["email"]
                     )


class PapeBook(Book):

    def __init__(self, title, author, genre, service: str, address: str):
        super().__init__(title, author, genre)
        self.service = service
        self.address = address


class ServiceMail(Mail):

    def send_book(self, user: str, book: PapeBook):
        print(f"{book.genre.capitalize()} {book.title} by {book.author} "
              f"was send {user} via {book.service} to {book.address}")

    def get_book_stored_by_user(self, user: str) -> PapeBook:
        with open(f"order_{user.lower()}.json") as f:
            dict_order = json.loads(f.read())
        return PapeBook(dict_order["title"],
                        dict_order["author"],
                        dict_order["genre"],
                        dict_order["service"],
                        dict_order["address"]
                        )


class App:
    def __init__(self, my_mail: Mail):
        self.__mail = my_mail

    def run(self):
        user = input("Enter user: ")
        book = self.__mail.get_book_stored_by_user(user)
        self.__mail.send_book(user, book)


mail = Email()
App(mail).run()

mail = ServiceMail()
App(mail).run()





