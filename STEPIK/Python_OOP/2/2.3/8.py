class PriceValue:
    def __init__(self, max_value):
        self.max_value = max_value ####????????????????

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value


    def validate(self, string):
        if type(string) == int or type(string) == float:
            return string <= self.max_value

class StringValue:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value


    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value

    def validate(self, string):
        if type(string) == str:
            return self.min_value <= len(string) <= self.max_value 


class Product:
    name = StringValue(2, 50)    # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
    price = PriceValue(10000)    # max_value - максимально допустимое значение
    
    def __init__(self, name:str, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name, goods:list=[]):
        self.name = name # - название магазина (строка);
        self.goods = goods # - список из товаров.

    def add_product(self, product): # - добавление товара в магазин (в конец списка goods);
        self.goods.append(product)

    def remove_product(self, product): # - удаление товара из магазина (из списка goods).
        self.goods.remove(product)



shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))
assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"

t = Product("name 123", 1000)
shop.add_product(t)
shop.remove_product(t)
assert len(shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')

t = Product(1000, "name 123")
if hasattr(t, '_name'):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, '_price'):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"
 
