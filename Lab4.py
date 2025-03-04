class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        brand (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
        _mileage (int): Пробег транспортного средства (инкапсулированный атрибут).
    """

    def __init__(self, brand: str, model: str, year: int, mileage: int = 0):
        """
        Конструктор базового класса Vehicle.

        Аргументы:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
            mileage (int): Пробег транспортного средства (по умолчанию 0).
        """
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = mileage  # Инкапсулированный атрибут, так как пробег не должен изменяться напрямую.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строковое представление транспортного средства.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление транспортного средства.
        """
        return f"Vehicle(brand={self.brand}, model={self.model}, year={self.year}, mileage={self._mileage})"

    def get_mileage(self) -> int:
        """
        Возвращает текущий пробег транспортного средства.

        Возвращает:
            int: Пробег транспортного средства.
        """
        return self._mileage

    def drive(self, distance: int) -> None:
        """
        Увеличивает пробег транспортного средства на указанное расстояние.

        Аргументы:
            distance (int): Расстояние, на которое увеличивается пробег.
        """
        self._mileage += distance
        print(f"Пробег увеличен на {distance} км. Текущий пробег: {self._mileage} км.")