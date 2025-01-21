class Category:
    product_count = 0  # Счётчик количества товаров

    def __init__(self, name, description, list_products=None):
        self.name = name
        self.description = description
        self.__list_products = list_products or []  # приватный список товаров
        Category.product_count += len(self.__list_products)  # Увеличиваем счётчик при инициализации

    def add_product(self, product):
        from src.product import Product  # Локальный импорт
        if not isinstance(product, Product):
            raise ValueError("Object must be an instance of Product")
        self.__list_products.append(product)
        Category.product_count += 1  # Увеличиваем счётчик при добавлении продукта

    @property
    def products(self):
        """Геттер для получения списка товаров."""
        return self.__list_products

    def get_products_as_string(self):
        """Возвращает список товаров в формате строки."""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__list_products
        )


if __name__ == '__main__':
    from src.product import Product

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
