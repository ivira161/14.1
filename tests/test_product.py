import pytest
from src.product import Product


def test_product_init_valid():
    """Тест корректного создания продукта."""
    product = Product("Товар", "Описание", 100, 10)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100
    assert product.quantity == 10


def test_product_init_invalid_price():
    """Тест выброса ValueError при недопустимой цене."""
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        Product("Товар", "Описание", 0, 10)
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        Product("Товар", "Описание", -5, 10)


def test_price_setter_valid():
    """Тест корректной установки цены сеттером."""
    product = Product("Товар", "Описание", 100, 10)
    product.price = 200
    assert product.price == 200


def test_price_setter_invalid_type():
    """Тест выброса TypeError при установке цены не числом."""
    product = Product("Товар", "Описание", 100, 10)
    with pytest.raises(TypeError, match="Цена должна быть числом"):
        product.price = "сто"


def test_price_setter_invalid_value():
    """Тест выброса ValueError при установке нулевой или отрицательной цены."""
    product = Product("Товар", "Описание", 100, 10)
    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = 0


def test_str_representation():
    """Тест строкового представления продукта."""
    product = Product("Хлеб", "Булка", 50, 5)
    assert str(product) == "Хлеб, 50 руб. Остаток: 5 шт."


def test_new_product_valid():
    """Тест класса-метода new_product при корректных данных."""
    data = {
        'name': 'Сыр',
        'description': 'Гауда',
        'price': 300,
        'quantity': 5
    }
    product = Product.new_product(data)
    assert product.name == 'Сыр'
    assert product.description == 'Гауда'
    assert product.price == 300
    assert product.quantity == 5


def test_new_product_missing_field():
    """Тест выброса ValueError при отсутствии обязательного поля."""
    data = {
        'name': 'Сыр',
        'description': 'Гауда',
        'price': 300
        # 'quantity' отсутствует
    }
    with pytest.raises(ValueError, match="Отсутствует обязательное поле: quantity"):
        Product.new_product(data)


@pytest.mark.parametrize("data, error_message", [
    (
            {'name': 123, 'description': 'Гауда', 'price': 300, 'quantity': 5},
            "Имя должно быть строкой"
    ),
    (
            {'name': 'Сыр', 'description': ['Описание'], 'price': 300, 'quantity': 5},
            "Описание должно быть строкой"
    ),
    (
            {'name': 'Сыр', 'description': 'Гауда', 'price': '300', 'quantity': 5},
            "Цена должна быть числом"
    ),
    (
            {'name': 'Сыр', 'description': 'Гауда', 'price': 300, 'quantity': 5.5},
            "Количество должно быть целым числом"
    ),
])
def test_new_product_invalid_types(data, error_message):
    """Тест выброса TypeError при некорректном типе одного из полей."""
    with pytest.raises(TypeError, match=error_message):
        Product.new_product(data)


def test_product_add(product1, product2, product3):
    """
    Тест магического метода __add__ в классе Product.
    Проверяем, что product1 + product2 возвращает сумму произведений цены на количество
    и аналогично для других пар.
    """

    # product1 + product2
    # 150 * 1000 + 100 * 500 = 150000 + 50000 = 200000
    assert product1 + product2 == 200000

    # product1 + product3
    # 150 * 1000 + 250 * 700 = 150000 + 175000 = 325000
    assert product1 + product3 == 325000

    # product2 + product3
    # 100 * 500 + 250 * 700 = 50000 + 175000 = 225000
    assert product2 + product3 == 225000


def test_product_add_type_error(product1):
    """
    Проверяем, что при попытке сложения с объектом неподходящего типа
    возникает исключение TypeError.
    """
    with pytest.raises(TypeError, match="Складывать можно только объекты класса Product"):
        # Пытаемся сложить product1 (Product) со строкой
        invalid_result = product1 + "не продукт"
