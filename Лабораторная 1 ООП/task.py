# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Cat:
    """
            Создание и подготовка к работе объекта "Кот"

            :param color: Цвет кота
            :param age: Возраст кота

            Примеры:
            >>> Barsik = Cat('рыжий', 2)  # инициализация экземпляра класса
            """
    def __init__(self, color: str, age: int):
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
            # Атрибутам присваиваются значения аргументов конструктора объекта
        self.color = color
        self.age = age

    def is_old(self):
        """
               Функция которая проверяет стар ли котик

               :return: Стар ли кот

               Примеры:
               >>> Barsik = Cat('рыжий', 2)
               >>> Barsik.is_old()
               """
        ...

    def add_age(self) -> None:
        """
                Увеличение возраста кота на 1 год.

                Примеры:
                >>> Barsik = Cat('рыжий', 2)
                >>> Barsik.add_age()
                """
        ...


class Flower:
    """
                Создание и подготовка к работе объекта "Цветок"

                :param color: Цвет цветка
                :param kol_lep: Кол-во лепестков

                Примеры:
                >>> Vasilek = Flower('фиолетовый', 12)  # инициализация экземпляра класса
                """
    def __init__(self, color: str, kol_lep: int):
        if not isinstance(kol_lep, int):
            raise TypeError("Кол-во лепестков должно быть типа int")
        if kol_lep <= 0:
            raise ValueError("Кол-во лепестков должно быть положительным числом")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
            # Атрибутам присваиваются значения аргументов конструктора объекта
        self.color = color
        self.kol_lep = kol_lep

    def is_kol_lep_chetn(self) -> bool:
        """
        Функция которая проверяет является ли кол-во лепестков четным

        :return: Является ли кол-во лепестков четным

        Примеры:
        >>> Vasilek = Flower('фиолетовый', 12)
        >>> Vasilek.is_kol_lep_chetn()
        """
        ...

    def change_color(self, color: str) -> None:
        """
        Изменение цвета цветка.
        :param color: Цвет изменяемого цветка

        :raise ValueError: Если цвет не соответствует типу str, вызываем ошибку

        Примеры:
        >>> Vasilek = Flower('фиолетовый', 12)
        >>> Vasilek.change_color('Рыжий')
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        ...


class Cake:
    """
                Создание и подготовка к работе объекта "Торт"

                :param weight: Вес торта
                :param kol_layers: Кол-во слоев

                Примеры:
                >>> Napoleon = Cake(1000, 15)  # инициализация экземпляра класса
                """
    def __init__(self, weight: int, kol_layers: int):
        if not isinstance(kol_layers, int):
            raise TypeError("Кол-во слоев должно быть типа int")
        if kol_layers <= 0:
            raise ValueError("Кол-во слоев должно быть положительным числом")
        if not isinstance(weight, int):
            raise TypeError("Вес должен быть типа int")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
            # Атрибутам присваиваются значения аргументов конструктора объекта
        self.weight = weight
        self.kol_layers = kol_layers

    def is_big_cake(self) -> bool:
        """
        Функция которая проверяет является ли торт большим

        :return: Является ли торт большим

        Примеры:
        >>> Napoleon = Cake(1000, 15)
        >>> Napoleon.is_big_cake()
        """
        ...

    def add_layers_to_cake(self, kol: int) -> None:
        """
        Добавление слоев в торт. Соответственно с добавлением слоев увеличиваем вес торта. Считаем вес 1-го коржа и потом увеличиваем вес
        торта на кол-во добавляемых коржей * вес коржа

        :param kol: Кол-во добавляемых слоев в торте

        :raise ValueError: Если количество добавляемых слоев отрицательно, то вызываем ошибку

        Примеры:
        >>> Napoleon = Cake(1000, 10)
        >>> Napoleon.add_layers_to_cake(5)
        """
        if not isinstance(kol, int):
            raise TypeError("Кол-во слоев должно быть типа int")
        if kol < 0:
            raise ValueError("Кол-во добавляемых слоёв должно быть неотрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
