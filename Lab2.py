class Book:
    """
    Класс, представляющий книгу.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата 'Книга "название_книги"'.

        >>> book = Book(id_=1, name='test_name_1', pages=200)
        >>> str(book)
        'Книга "test_name_1"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'Book(id_=1, name="test_name_1", pages=200)'.

        >>> book = Book(id_=1, name='test_name_1', pages=200)
        >>> repr(book)
        'Book(id_=1, name="test_name_1", pages=200)'
        """
        return f'Book(id_={self.id}, name="{self.name}", pages={self.pages})'


class Library:
    """
    Класс, представляющий библиотеку.
    """

    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.

        :param books: Список книг. По умолчанию пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Идентификатор последней книги + 1 или 1, если книг нет.

        >>> library = Library()
        >>> library.get_next_book_id()
        1
        >>> library.books = [Book(id_=1, name='test_name_1', pages=200)]
        >>> library.get_next_book_id()
        2
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с таким идентификатором не существует.

        >>> library = Library([Book(id_=1, name='test_name_1', pages=200)])
        >>> library.get_index_by_book_id(1)
        0
        >>> library.get_index_by_book_id(2)
        Traceback (most recent call last):
        ...
        ValueError: Книги с запрашиваемым id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == "__main__":
    import doctest
    doctest.testmod()