from abc import ABC, abstractmethod
from typing import List, Optional

class MaterialObject(ABC):
    """
    Абстрактный класс, описывающий материальный объект.
    """

    def __init__(self, weight: float, dimensions: List[float]):
        """
        Инициализация материального объекта.

        :param weight: Вес объекта в килограммах. Должен быть положительным числом.
        :param dimensions: Размеры объекта в метрах (длина, ширина, высота). Все значения должны быть положительными.
        """
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        if any(dim <= 0 for dim in dimensions):
            raise ValueError("Все размеры должны быть положительными числами.")
        self.weight = weight
        self.dimensions = dimensions

    @abstractmethod
    def move(self, new_location: str) -> None:
        """
        Перемещает объект в новое место.

        :param new_location: Новое местоположение объекта.
        :return: None

        >>> obj = ConcreteMaterialObject(10, [1, 1, 1])
        >>> obj.move("Склад")
        """
        ...

    @abstractmethod
    def calculate_volume(self) -> float:
        """
        Вычисляет объем объекта.

        :return: Объем объекта в кубических метрах.

        >>> obj = ConcreteMaterialObject(10, [1, 1, 1])
        >>> obj.calculate_volume()
        1.0
        """
        ...

class ConcreteMaterialObject(MaterialObject):
    """
    Конкретный класс, реализующий абстрактный класс MaterialObject.
    """

    def move(self, new_location: str) -> None:
        """
        Перемещает объект в новое место.

        :param new_location: Новое местоположение объекта.
        :return: None
        """
        print(f"Объект перемещен в {new_location}")

    def calculate_volume(self) -> float:
        """
        Вычисляет объем объекта.

        :return: Объем объекта в кубических метрах.
        """
        return self.dimensions[0] * self.dimensions[1] * self.dimensions[2]

class DigitalPlatform(ABC):
    """
    Абстрактный класс, описывающий цифровую платформу.
    """

    def __init__(self, name: str, user_count: int):
        """
        Инициализация цифровой платформы.

        :param name: Название платформы.
        :param user_count: Количество пользователей. Должно быть неотрицательным числом.
        """
        if user_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным числом.")
        self.name = name
        self.user_count = user_count

    @abstractmethod
    def add_user(self) -> None:
        """
        Добавляет нового пользователя на платформу.

        :return: None

        >>> platform = ConcreteDigitalPlatform("Facebook", 1000)
        >>> platform.add_user()
        """
        ...

    @abstractmethod
    def get_statistics(self) -> dict:
        """
        Возвращает статистику по платформе.

        :return: Словарь с данными о платформе.

        >>> platform = ConcreteDigitalPlatform("Facebook", 1000)
        >>> platform.get_statistics()
        {'name': 'Facebook', 'user_count': 1001}
        """
        ...

class ConcreteDigitalPlatform(DigitalPlatform):
    """
    Конкретный класс, реализующий абстрактный класс DigitalPlatform.
    """

    def add_user(self) -> None:
        """
        Добавляет нового пользователя на платформу.

        :return: None
        """
        self.user_count += 1

    def get_statistics(self) -> dict:
        """
        Возвращает статистику по платформе.

        :return: Словарь с данными о платформе.
        """
        return {"name": self.name, "user_count": self.user_count}

class NaturalObject(ABC):
    """
    Абстрактный класс, описывающий природный объект.
    """

    def __init__(self, age: int, location: str):
        """
        Инициализация природного объекта.

        :param age: Возраст объекта в годах. Должен быть неотрицательным числом.
        :param location: Местоположение объекта.
        """
        if age < 0:
            raise ValueError("Возраст должен быть неотрицательным числом.")
        self.age = age
        self.location = location

    @abstractmethod
    def grow(self) -> None:
        """
        Увеличивает возраст объекта на 1 год.

        :return: None

        >>> tree = ConcreteNaturalObject(10, "Лес")
        >>> tree.grow()
        """
        ...

    @abstractmethod
    def change_location(self, new_location: str) -> None:
        """
        Изменяет местоположение объекта.

        :param new_location: Новое местоположение объекта.
        :return: None

        >>> tree = ConcreteNaturalObject(10, "Лес")
        >>> tree.change_location("Парк")
        """
        ...

class ConcreteNaturalObject(NaturalObject):
    """
    Конкретный класс, реализующий абстрактный класс NaturalObject.
    """

    def grow(self) -> None:
        """
        Увеличивает возраст объекта на 1 год.

        :return: None
        """
        self.age += 1

    def change_location(self, new_location: str) -> None:
        """
        Изменяет местоположение объекта.

        :param new_location: Новое местоположение объекта.
        :return: None
        """
        self.location = new_location

if __name__ == "__main__":
    import doctest
    doctest.testmod()