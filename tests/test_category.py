import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def category():
    product1 = Product('молоко', 'ультрапастеризованное', 150, 1000)
    product2 = Product('творог', 'обезжиренный', 100, 500)
    return Category('Молочные продукты', 'произведенные из молока или молочных продуктов', [product1, product2])


def test_category_initialization(category):
    assert category.name == 'Молочные продукты'
    assert category.description == 'произведенные из молока или молочных продуктов'
    assert len(category.products) == 2


def test_add_product_to_category(category):
    new_product = Product('масло', 'жирность 82,5', 250, 700)
    category.add_product(new_product)
    assert len(category.products) == 3
    assert new_product in category.products


def test_invalid_product_addition(category):
    with pytest.raises(ValueError):
        category.add_product("не продукт")  # Передаём некорректный объект
