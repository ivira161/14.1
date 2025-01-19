from src.product import Product


class Category:
    name: str
    description: str
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name, description, list_products=None):
        self.name = name
        self.description = description
        self.__list_products = list_products or []  # приватный список товаров
        Category.category_count += 1  # увеличиваем количество категорий
        Category.product_count += len(self.__list_products)  # увеличиваем общее количество товаров

    def add_product(self, new_product):
        """Добавляет продукт в категорию."""
        if isinstance(new_product, Product):
            self.__list_products.append(new_product)
            Category.product_count += 1  # обновляем общее количество товаров
        else:
            raise ValueError("Объект должен быть экземпляром класса Product")

    @property
    def products(self):
        """Геттер для получения списка товаров."""
        return self.__list_products


if __name__ == '__main__':
    product1 = Product('молоко', 'молоко ультрапастеризованное', 150, 1000)
    product2 = Product('творог', 'обезжиренный', 100, 500)
    product3 = Product('масло', 'жирность 82,5', 250, 700)

    category = Category('Молочные продукты', 'произведенные из молока или молочных продуктов',
                        [product1, product2])

    # Добавляем новый продукт через метод add_product
    category.add_product(product3)

    print(category.name)
    print(category.description)
    print(category.category_count)
    print(category.product_count)

    # Получаем список товаров через геттер products
    print(category.products)
