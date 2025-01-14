from src.product import Product


class Category:
    name: str
    description: str
    list_products: list
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name, description, list_products=None):
        self.name = name
        self.description = description
        self.list_products = list_products or []
        self.category_count += 1  # увеличиваем количество категорий
        self.product_count += len(self.list_products)  # увеличиваем общее количество товаров


if __name__ == '__main__':
    product1 = Product('молоко', 'молоко ультрапастеризованное', 150, 1000)
    product2 = Product('творог', 'обезжиренный', 100, 500)
    product3 = Product('масло', 'жирность 82,5', 250, 700)

    category = Category('Молочные продукты', 'произведенные из молока или молочных продуктов',
                        [product1, product2, product3])

    print(category.name)
    print(category.description)
    print(category.category_count)
    print(category.product_count)
    for product in category.list_products:
        print(product.name, product.description)
