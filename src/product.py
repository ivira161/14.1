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
