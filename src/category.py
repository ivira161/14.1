from src.product import Product


class Category:
    product_count = 0  # Счётчик всех продуктов во всех категориях
    category_count = 0  # Счётчик созданных категорий

    def __init__(self, name: str, description: str, list_products=None):
        """
        Инициализация категории. Принимает список товаров (объектов Product).
        Увеличивает счётчик продуктов на длину переданного списка.
        """
        self.name = name
        self.description = description
        self.__list_products = list_products or []

        # Проверка переданных продуктов при инициализации
        for product in self.__list_products:
            if not isinstance(product, Product):
                raise ValueError("Все элементы списка должны быть экземплярами класса Product или его наследников")

        Category.product_count += len(self.__list_products)

    def __str__(self):
        # Подсчёт общей суммы количеств всех товаров
        total_quantity = sum(product.quantity for product in self.__list_products)
        return f"{self.name}, общее количество единиц товара: {total_quantity} шт."

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию. Увеличивает общий счётчик продуктов.
        """
        if not isinstance(product, Product):
            raise ValueError("Object must be an instance of Product or its subclasses")
        self.__list_products.append(product)
        Category.product_count += 1

    def remove_product(self, product: Product):
        """
        Удаляет товар из категории (если он там есть).
        Уменьшает общий счётчик продуктов.
        """
        if product in self.__list_products:
            self.__list_products.remove(product)
            Category.product_count -= 1

    @property
    def products_list(self):
        """
        Возвращает внутренний список товаров (как объекты).
        """
        return self.__list_products

    @property
    def products(self):
        """
        Возвращает строковое представление всех товаров в категории,
        каждый товар на новой строке.
        """
        return "\n".join(str(product) for product in self.__list_products)

    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров в категории.
        Если товаров нет или возникла ошибка, возвращает 0.0.
        """
        try:
            total_price = sum(product.price for product in self.__list_products)
            avg_price = total_price / len(self.__list_products)
            return avg_price
        except ZeroDivisionError:
            print("Ошибка: Нельзя делить на ноль. В категории нет товаров.")
            return 0.0
        except Exception as e:
            print(f"Ошибка при вычислении средней цены: {e}")
            return 0.0
