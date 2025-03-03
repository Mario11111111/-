class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0  # Пробег (инкапсулирован, так как не должен изменяться напрямую)

    def drive(self, distance: float) -> None:
        """
        Увеличивает пробег транспортного средства на указанное расстояние.

        :param distance: Расстояние, на которое переместилось транспортное средство.
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным.")
        self._mileage += distance

    def get_mileage(self) -> float:
        """
        Возвращает текущий пробег транспортного средства.

        :return: Пробег транспортного средства.
        """
        return self._mileage

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строка формата 'Марка Модель (Год выпуска)'.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'Vehicle(brand="Марка", model="Модель", year=Год)'.
        """
        return f'Vehicle(brand="{self.brand}", model="{self.model}", year={self.year})'

    Дочерний класс

    class Car(Vehicle):
        """
        Класс, представляющий легковой автомобиль.
        """

        def __init__(self, brand: str, model: str, year: int, num_doors: int):
            """
            Инициализация легкового автомобиля.

            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска автомобиля.
            :param num_doors: Количество дверей.
            """
            super().__init__(brand, model, year)
            self.num_doors = num_doors

        def honk(self) -> str:
            """
            Сигналит автомобиль.

            :return: Строка с сообщением о сигнале.
            """
            return "Beep beep!"

        def __str__(self) -> str:
            """
            Возвращает строковое представление легкового автомобиля.

            :return: Строка формата 'Легковой автомобиль: Марка Модель (Год выпуска)'.
            """
            return f"Легковой автомобиль: {super().__str__()}"

        def __repr__(self) -> str:
            """
            Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

            :return: Строка формата 'Car(brand="Марка", model="Модель", year=Год, num_doors=Количество дверей)'.
            """
            return f'Car(brand="{self.brand}", model="{self.model}", year={self.year}, num_doors={self.num_doors})'