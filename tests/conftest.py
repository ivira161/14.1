import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сбрасывает счётчики Category перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product1():
    return Product('молоко', 'ультрапастеризованное', 150, 1000)


@pytest.fixture
def product2():
    return Product('творог', 'обезжиренный', 100, 500)


@pytest.fixture
def product3():
    return Product('масло', 'жирность 82,5', 250, 700)


@pytest.fixture
def category(product1, product2, product3):
    return Category('Молочные продукты', 'произведенные из молока или молочных продуктов',
                    [product1, product2, product3])
