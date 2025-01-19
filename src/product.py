from src.category import Category


class Product:
    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для приватного атрибута цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_info):
        """Создает новый объект Product из словаря."""
        return cls(
            name=product_info['name'],
            description=product_info['description'],
            price=product_info['price'],
            quantity=product_info['quantity']
        )


if __name__ == '__main__':
    product1 = Product('молоко', 'молоко ультрапастеризованное', 150, 1000)
    product2 = Product('творог', 'обезжиренный', 100, 500)
    product3 = Product('масло', 'жирность 82,5', 250, 700)

    category = Category('Молочные продукты', 'произведенные из молока или молочных продуктов',
                        [product1, product2])

    # Добавляем новый продукт через метод add_product
    category.add_product(product3)

    # Создаем продукт через класс-метод new_product
    product_data = {
        'name': 'йогурт',
        'description': 'натуральный',
        'price': 120,
        'quantity': 300
    }
    new_product = Product.new_product(product_data)
    category.add_product(new_product)

    print(category.name)
    print(category.description)
    print(f"Количество продуктов: {Category.product_count}")

    # Получаем список товаров через геттер products
    print(category.products)
