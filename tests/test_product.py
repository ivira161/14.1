import pytest
from src.product import Product


# Фикстура для создания тестового продукта
@pytest.fixture
def product_data():
    return {
        'name': 'хлеб',
        'description': 'цельнозерновой',
        'price': 50,
        'quantity': 20
    }


def test_product_creation():
    product = Product('молоко', 'ультрапастеризованное', 150, 1000)
    assert product.name == 'молоко'
    assert product.description == 'ультрапастеризованное'
    assert product.price == 150
    assert product.quantity == 1000


def test_new_product(product_data):
    product = Product.new_product(product_data)
    assert product.name == 'хлеб'
    assert product.description == 'цельнозерновой'
    assert product.price == 50
    assert product.quantity == 20


def test_price_validation():
    product = Product('молоко', 'ультрапастеризованное', 150, 1000)

    # Устанавливаем корректную цену
    product.price = 200
    assert product.price == 200

    # Попытка установить некорректную цену
    product.price = -50
    assert product.price == 200  # Цена не должна измениться
