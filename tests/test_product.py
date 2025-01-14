def test_product_init(product):
    assert product.name == 'молоко'
    assert  product.description == 'ультрапастеризованное'
    assert  product.price == 150
    assert product.quantity == 1000
