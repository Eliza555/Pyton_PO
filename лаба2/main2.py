class Book:
    def __init__(self, id_, name, pages):
        """
        Конструктор класса Book.

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает удобочитаемое строковое представление объекта Book.

        :return: Строка вида 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает официальное строковое представление объекта Book,
        которое может быть использовано для создания идентичного объекта.

        :return: Строка вида "Book(id_=1, name='test_name_1', pages=200)"
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library.

        :param books: Необязательный список книг. Если не передан, инициализируется пустым списком.
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, возвращает 1.
        Иначе, возвращает идентификатор последней книги увеличенный на 1.

        :return: Целое число - следующий идентификатор книги
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по заданному идентификатору.
        Если книга с таким идентификатором не существует, вызывает ValueError.

        :param book_id: Идентификатор книги для поиска
        :return: Целое число - индекс книги в списке
        :raises ValueError: Если книга с заданным id не найдена
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Ваша база данных книг
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


if __name__ == '__main__':
    # Инициализируем пустую библиотеку
    empty_library = Library()
    print("Следующий ID для пустой библиотеки:", empty_library.get_next_book_id())  # Ожидается 1

    # Инициализируем список книг из базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Инициализируем библиотеку с книгами
    library_with_books = Library(books=list_books)
    print("Следующий ID для библиотеки с книгами:", library_with_books.get_next_book_id())  # Ожидается 3

    # Проверяем индекс книги с id = 1
    try:
        index = library_with_books.get_index_by_book_id(1)
        print(f"Индекс книги с id=1: {index}")  # Ожидается 0
    except ValueError as e:
        print(e)

    # Проверим поиск несуществующей книги
    try:
        library_with_books.get_index_by_book_id(3)
    except ValueError as e:
        print(e)  # Ожидается сообщение об ошибке





