class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        mileage (int): Пробег автомобиля.
        num_doors (int): Количество дверей у автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, num_doors: int, mileage: int = 0):
        """
        Конструктор дочернего класса Car.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            num_doors (int): Количество дверей у автомобиля.
            mileage (int): Пробег автомобиля (по умолчанию 0).
        """
        super().__init__(brand, model, year, mileage)
        self.num_doors = num_doors

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строковое представление легкового автомобиля.
        """
        return f"{self.brand} {self.model} ({self.year}), {self.num_doors} дверей"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление легкового автомобиля.
        """
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, num_doors={self.num_doors}, mileage={self.get_mileage()})"

    def drive(self, distance: int) -> None:
        """
        Перегруженный метод для увеличения пробега автомобиля.
        Добавляет проверку на максимальное расстояние для легковых автомобилей.

        Аргументы:
            distance (int): Расстояние, на которое увеличивается пробег.
        """
        if distance > 1000:
            print("Легковые автомобили не предназначены для поездок на такие большие расстояния.")
        else:
            super().drive(distance)

    def honk(self) -> None:
        """
        Метод, который позволяет автомобилю сигналить.
        """
        print("Beep beep!")