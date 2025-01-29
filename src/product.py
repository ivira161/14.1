class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта с проверкой входных данных."""
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для приватного атрибута цены с проверкой типа и значения."""
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    @classmethod
    def new_product(cls, product_info: dict):
        """
        Создание нового продукта на основе словаря.
        Проверяется наличие обязательных полей и корректность типов.
        """
        required = ['name', 'description', 'price', 'quantity']
        for field in required:
            if field not in product_info:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

        # Дополнительная проверка типов — по желанию
        if not isinstance(product_info['name'], str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(product_info['description'], str):
            raise TypeError("Описание должно быть строкой")
        if not isinstance(product_info['price'], (int, float)):
            raise TypeError("Цена должна быть числом")
        if not isinstance(product_info['quantity'], int):
            raise TypeError("Количество должно быть целым числом")

        return cls(
            name=product_info['name'],
            description=product_info['description'],
            price=product_info['price'],
            quantity=product_info['quantity']
        )

    def __add__(self, other):
        """Возвращает сумму произведений цены на количество для двух продуктов.
        Складывает товары только из одинаковых классов продуктов."""

        # Проверка, что объекты одного типа
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")

        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: int, color: str):
        # Передаём основные атрибуты в родительский класс
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Модель: {self.model}, Память: {self.memory} ГБ, Цвет: {self.color}, Производительность: {self.efficiency}"


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        # Передаём основные атрибуты в родительский класс
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Страна: {self.country}, Срок прорастания: {self.germination_period} дней, Цвет: {self.color}"



