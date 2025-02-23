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
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверяем метод __str__
    for book in list_books:
        print(book)

    # Проверяем метод __repr__
    print(list_books)
