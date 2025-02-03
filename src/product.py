from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass


class MiXinInfo:
    def __init__(self, *args, **kwargs):
        # Вызов конструктора следующего класса в цепочке MRO.
        super().__init__(*args, **kwargs)
        # Вывод информации об объекте
        self.show_info_product()

    def show_info_product(self):
        print(
            f'Объект был создан от класса: {self.__class__.__name__} с параметрами: '
            f'name={getattr(self, "name", None)}, description={getattr(self, "description", None)}'
        )


class Product(MiXinInfo, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым или отрицательным количеством не может быть создан")
        self.name = name
        self.description = description
        super().__init__()

        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name == other.name and
                self.description == other.description and
                self.price == other.price and
                self.quantity == other.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    @classmethod
    def new_product(cls, product_info: dict):
        required = ['name', 'description', 'price', 'quantity']
        for field in required:
            if field not in product_info:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

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
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя складывать {type(self).__name__} и {type(other).__name__}"
            )
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
        return (f"{base_info}, Модель: {self.model}, Память: {self.memory} ГБ, Цвет: {self.color}, "
                f"Производительность: {self.efficiency}")


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
        return (f"{base_info}, Страна: {self.country}, Срок прорастания: {self.germination_period} дней, "
                f"Цвет: {self.color}")
