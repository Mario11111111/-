class Book:
    """
    Базовый класс, представляющий книгу.
    """

    def __init__(self, name: str, author: str):
        """
        Инициализация книги.

        :param name: Название книги.
        :param author: Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        Возвращает название книги.

        :return: Название книги.
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги.

        :return: Автор книги.
        """
        return self._author

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата 'Книга "название_книги"'.

        >>> book = Book(name="1984", author="George Orwell")
        >>> str(book)
        'Книга "1984"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'Book(name="1984", author="George Orwell")'.

        >>> book = Book(name="1984", author="George Orwell")
        >>> repr(book)
        'Book(name="1984", author="George Orwell")'
        """
        return f'Book(name="{self.name}", author="{self.author}")'


class PaperBook(Book):
    """
    Класс, представляющий бумажную книгу.
    """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация бумажной книги.

        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц в книге.

        :return: Количество страниц.
        """
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """
        Устанавливает количество страниц в книге.

        :param value: Количество страниц.
        :raises ValueError: Если количество страниц меньше или равно 0.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление бумажной книги.

        :return: Строка формата 'Бумажная книга "название_книги"'.

        >>> paper_book = PaperBook(name="1984", author="George Orwell", pages=328)
        >>> str(paper_book)
        'Бумажная книга "1984"'
        """
        return f'Бумажная книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'PaperBook(name="1984", author="George Orwell", pages=328)'.

        >>> paper_book = PaperBook(name="1984", author="George Orwell", pages=328)
        >>> repr(paper_book)
        'PaperBook(name="1984", author="George Orwell", pages=328)'
        """
        return f'PaperBook(name="{self.name}", author="{self.author}", pages={self.pages})'


class AudioBook(Book):
    """
    Класс, представляющий аудиокнигу.
    """

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация аудиокниги.

        :param name: Название книги.
        :param author: Автор книги.
        :param duration: Продолжительность аудиокниги в часах.
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """
        Возвращает продолжительность аудиокниги.

        :return: Продолжительность аудиокниги в часах.
        """
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """
        Устанавливает продолжительность аудиокниги.

        :param value: Продолжительность аудиокниги в часах.
        :raises ValueError: Если продолжительность меньше или равна 0.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self) -> str:
        """
        Возвращает строковое представление аудиокниги.

        :return: Строка формата 'Аудиокнига "название_книги"'.

        >>> audio_book = AudioBook(name="1984", author="George Orwell", duration=10.5)
        >>> str(audio_book)
        'Аудиокнига "1984"'
        """
        return f'Аудиокнига "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'AudioBook(name="1984", author="George Orwell", duration=10.5)'.

        >>> audio_book = AudioBook(name="1984", author="George Orwell", duration=10.5)
        >>> repr(audio_book)
        'AudioBook(name="1984", author="George Orwell", duration=10.5)'
        """
        return f'AudioBook(name="{self.name}", author="{self.author}", duration={self.duration})'


if __name__ == "__main__":
    import doctest
    doctest.testmod()