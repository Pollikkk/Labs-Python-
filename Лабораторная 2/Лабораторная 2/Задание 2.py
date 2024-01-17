BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id  # id книги
        self.name = name  # название
        self.pages = pages  # кол-во страниц


    def __str__(self) -> str:
        # self.__class__.__name__ вместо явного указания названия класса
        return f"Книга \"{self.name}\""


    def __repr__(self) -> str:
        # self.__class__.__name__ вместо явного указания названия класса
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books = []):
        self.books = books  # id книги

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return len(self.books)+1

    def get_index_by_book_id(self, ind):
        if ind < 0 or ind >= len(self.books):
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            a = -1

            book = self.books[ind-1]
            return self.books.index(book)


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
