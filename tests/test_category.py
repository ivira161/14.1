import pytest
from src.product import Product
from src.category import Category


def test_category_init():
    """Тест инициализации категории и увеличения счетчика продуктов."""
    p1 = Product("Товар1", "Описание1", 100, 10)
    p2 = Product("Товар2", "Описание2", 200, 5)

    # Сбрасываем общий счетчик перед тестом (для независимости тестов)
    Category.product_count = 0

    category = Category("Категория1", "Описание категории", [p1, p2])
    assert category.name == "Категория1"
    assert category.description == "Описание категории"
    assert len(category.products_list) == 2
    assert Category.product_count == 2


def test_add_product():
    """Тест добавления продукта в категорию и увеличения счетчика."""
    Category.product_count = 0
    category = Category("Категория", "Описание")

    p = Product("Товар", "Описание", 100, 10)
    category.add_product(p)

    assert len(category.products_list) == 1
    assert category.products_list[0] == p
    assert Category.product_count == 1


def test_add_product_invalid():
    """Тест выброса ValueError при добавлении объекта неверного типа."""
    Category.product_count = 0
    category = Category("Категория", "Описание")

    with pytest.raises(ValueError, match="Object must be an instance of Product"):
        category.add_product("Not a product")  # type: ignore


def test_remove_product():
    """Тест удаления продукта из категории и уменьшения счетчика."""
    Category.product_count = 0
    p1 = Product("Товар1", "Описание1", 100, 10)
    p2 = Product("Товар2", "Описание2", 200, 5)
    category = Category("Категория", "Описание", [p1, p2])

    assert Category.product_count == 2

    category.remove_product(p1)
    assert len(category.products_list) == 1
    assert category.products_list[0] == p2
    assert Category.product_count == 1


def test_remove_product_not_in_list():
    """Тест удаления продукта, которого нет в категории (счетчик не меняется)."""
    Category.product_count = 0
    p1 = Product("Товар1", "Описание1", 100, 10)
    p2 = Product("Товар2", "Описание2", 200, 5)
    p3 = Product("Товар3", "Описание3", 300, 1)
    category = Category("Категория", "Описание", [p1, p2])

    assert Category.product_count == 2

    category.remove_product(p3)  # p3 нет в списке
    assert len(category.products_list) == 2
    assert Category.product_count == 2


def test_products_property():
    """Тест строкового вывода всех продуктов в категории."""
    Category.product_count = 0
    p1 = Product("Товар1", "Описание1", 100, 10)
    p2 = Product("Товар2", "Описание2", 200, 5)
    category = Category("Категория", "Описание", [p1, p2])

    product_str = category.products
    # Проверяем, что каждое из строковых представлений есть в общем выводе.
    assert str(p1) in product_str
    assert str(p2) in product_str


def test_category_str(product1, product2):
    """
    Тест метода __str__ в классе Category,
    используя заранее определённые фикстуры product1 и product2.
    """
    category = Category("Молочные продукты", "Разные товары", [product1, product2])

    # Ожидаем, что количество продуктов = 1500
    expected_str = "Молочные продукты, общее количество единиц товара: 1500 шт."
    assert str(category) == expected_str


def test_category_initialization_with_invalid_product():
    """Тест выброса исключения при передаче некорректного продукта в конструктор."""
    with pytest.raises(ValueError,
                       match="Все элементы списка должны быть экземплярами класса Product или его наследников"):
        Category('Некорректная категория', 'Тестовое описание', ['не продукт'])


def test_middle_price():
    # Создаем категорию без товаров
    category = Category("Категория", "Описание", [])

    # Проверяем, что средняя цена равна 0.0, а не выбрасывается исключение
    assert category.average_price() == 0.0
