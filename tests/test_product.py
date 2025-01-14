def test_product_creation(product1):
    assert product1.name == 'молоко'
    assert product1.description == 'ультрапастеризованное'
    assert product1.price == 150
    assert product1.quantity == 1000


def test_product_details(product2):
    assert product2.name == 'творог'
    assert product2.description == 'обезжиренный'
    assert product2.price == 100
    assert product2.quantity == 500
