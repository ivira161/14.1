class Product:
    name: str
    description: str
    quantity: int
    _price: float  # Приватный атрибут для цены

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price  # Используем сеттер для установки цены
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_info):
        """Создает новый объект Product из словаря."""
        return cls(
            name=product_info['name'],
            description=product_info['description'],
            price=product_info['price'],
            quantity=product_info['quantity']
        )

    @property
    def price(self):
        """Геттер для приватного атрибута цены."""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для приватного атрибута цены с проверкой на значение."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value


def add_product_to_list(products, product):
    """Добавляет продукт в список."""
    if isinstance(product, Product):
        products.append(product)
    else:
        raise ValueError("Объект должен быть экземпляром класса Product")


def get_products_as_string(products):
    """Возвращает строку со списком товаров."""
    return "".join(
        f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        for product in products
    )


if __name__ == '__main__':
    product1 = Product('молоко', 'молоко ультрапастеризованное', 150, 1000)
    product2 = Product('творог', 'обезжиренный', 100, 500)
    product3 = Product('масло', 'жирность 82,5', 250, 700)

    category_name = 'Молочные продукты'
    category_description = 'произведенные из молока или молочных продуктов'
    product_list = [product1, product2]

    # Добавляем новый продукт через функцию add_product_to_list
    add_product_to_list(product_list, product3)

    # Создаем продукт через класс-метод new_product
    product_data = {
        'name': 'йогурт',
        'description': 'натуральный',
        'price': 120,
        'quantity': 300
    }
    new_product = Product.new_product(product_data)
    add_product_to_list(product_list, new_product)

    print(category_name)
    print(category_description)
    print(f"Количество продуктов: {len(product_list)}")

    # Получаем список товаров через функцию get_products_as_string
    print(get_products_as_string(product_list))

    # Проверяем работу сеттера и геттера для цены
    print(product1.price)  # Используем геттер

    # Попробуем установить неправильную цену
    product1.price = -100  # Сообщение об ошибке и цена не изменится
    print(product1.price)  # Цена не изменится

    # Устанавливаем правильную цену
    product1.price = 200
    print(product1.price)  # Теперь цена изменится на 200
