import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def first_category():
    return Category(
        name='Молочные продукты',
        description='произведенные из молока или молочных продуктов',
        list_products=[
            Product('молоко', 'молоко ультрапастеризованное', 150, 1000),
            Product('творог', 'обезжиренный', 100, 500),
            Product('масло', 'жирность 82,5', 250, 700),
        ]
    )


@pytest.fixture()
def second_category():
    return Category(
        name='Хлебные изделия',
        description='Хлеб, выпечка, торты',
        list_products=[
            Product('хлеб', 'бородинский', 80, 100),
            Product('хлеб', 'ржаной', 75, 200),
            Product('булочка', 'сдобная', 50, 120),
        ]
    )


@pytest.fixture()
def product():
    return Product('молоко', 'ультрапастеризованное', 150, 1000)
