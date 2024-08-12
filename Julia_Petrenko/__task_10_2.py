# Добавте возможность создания объектов классов на основе данных друг друга:
# из Page можно создать Book и обратно.
# Используйте classmethod или staticmethod (на ваше усмотрение)

class Page:

    def __init__(self, text: str):
        self.__text = text

    @property
    def content(self):
        return self.__text


class Book:

    def __init__(self, content: list[str]):
        self.__content = content
        self.pages = len(content)

    def read(self):
        return "\n".join(self.__content)

    def get_page(self, page_num: int):
        if 0 <= abs(page_num) <= self.pages:
            return self.__content[page_num]

    @staticmethod
    def from_page(page: Page):
        return Book([page.content])

    def from_book(self, page_num: int):
        return Page(self.get_page(page_num))


Page1 = Page("Single page")
# print(Page1.content)

Book1 = Book(["First page", "Second page", "Third page"])
# print(Book1.read())

Book2 = Book.from_page(Page1)
# print(Book2.read())

Page2 = Book1.from_book(1)
print(Page2.content)

