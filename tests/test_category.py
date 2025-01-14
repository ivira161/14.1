from src.category import Category


def test_category_initialization(category):
    assert category.name == 'Молочные продукты'
    assert category.description == 'произведенные из молока или молочных продуктов'
    assert len(category.list_products) == 3
    assert category.list_products[0].name == 'молоко'
    assert category.list_products[1].name == 'творог'
    assert category.list_products[2].name == 'масло'


def test_product_count(category):
    assert Category.product_count == 3  # Проверяем общее количество продуктов


def test_product_details(category):
    product_names = [product.name for product in category.list_products]
    assert 'молоко' in product_names
    assert 'творог' in product_names
    assert 'масло' in product_names
