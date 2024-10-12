class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float (weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        products = open(self.__file_name, 'r')
        data = products.read()
        products.close()
        return data.strip()

    def add(self, *products):
        """Добавляет продукты в файл, если их ещё нет."""
        existing_products = self.get_products().splitlines() # Получаем существующие продукты
        existing_names = [line.split(', ')[0] for line in existing_products]  # Извлекаем названия
        for product in products:
            if product.name in existing_names:
                print(f"Продукт {product.name} уже есть в магазине")  # Сообщение о существующем продукте
            else:
                file = open(self.__file_name, 'a')  # Открываем файл для добавления
                file.write(str(product) + '\n')  # Записываем новый продукт в файл
                file.close()  # Закрываем файл


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Вывод: Spaghetti, 3.4, Groceries

    s1.add(p1, p2, p3)  # Добавляем продукты

    print(s1.get_products())  # Выводит все продукты из файла