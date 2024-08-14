# Добавте возможность создания объектов классов на основе данных друг друга:
# из Page можно создать Book и обратно.
# Используйте classmethod или staticmethod (на ваше усмотрение)

class Page:

    def __init__(self, text: str):
        self.__text = text

    @property
    def content(self):
        return self.__text

    @staticmethod
    def from_book(book: "Book", page_num: int):
        text = Book.get_page(book, page_num)
        return Page(text)


class Book:

    def __init__(self, content: list[str]):
        self.__content = content
        self.pages = len(content)

    def read(self):
        return "\n".join(self.__content)

    def get_page(self, page_num: int):
        if 0 <= page_num <= self.pages:
            return self.__content[page_num - 1]

    @staticmethod
    def from_page(page: Page):
        return Book([page.content])


page1 = Page("Single page")
print(page1.content)

book1 = Book(["First page", "Second page", "Third page"])
print(book1.read())

page2 = Page.from_book(book1, 2)
print(page2.content)

book2 = Book.from_page(page1)
print(book2.read())


