from src.category import Category
from src.product import Product
def test_category_init(first_category):
    expected_products = [
        ('молоко', 'молоко ультрапастеризованное', 150, 1000),
        ('творог', 'обезжиренный', 100, 500),
        ('масло', 'жирность 82,5', 250, 700),
    ]

    for product, expected in zip(first_category.list_products, expected_products):
        assert product.name == expected[0]
        assert product.description == expected[1]
        assert product.price == expected[2]
        assert product.quantity == expected[3]


def test_product_count():
    product1 = Product('молоко', 'ультрапастеризованное', 150, 1000)
    product2 = Product('творог', 'обезжиренный', 100, 500)

    category = Category('Молочные продукты', 'Продукты из молока', [product1, product2])
    assert category.product_count == 2