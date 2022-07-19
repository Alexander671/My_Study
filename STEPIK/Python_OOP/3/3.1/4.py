

class Shop: # - класс для управления магазином в целом;
    def __init__(self, name, goods=[]):
        self.name = name
        self.goods = goods
        
    def add_product(self, product): # - добавление нового товара в магазин (в конец списка goods);
        self.goods.append(product)

    def remove_product(self, product): # - удаление товара product из магазина (из списка goods);
        self.goods.remove(product)

class Product: # - класс для представления отдельного товара.
    def __init__(self, name, weight, price):
        self.id = 1 # - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
        self.name = name # - название товара (строка);
        self.weight = weight # - вес товара (целое или вещественное положительное число);
        self.price = price # - цена (целое или вещественное положительное число).

    def __setattr__(self, __name: str, __value) -> None:
        # атрибут name - строка, id - целое число
        if (__name in ('name') and type(__value) != str) or (__name in ('id') and type(__value) != int) or (__name in ('weight', 'price') and type(__value) not in (float, int)):
            raise TypeError("Неверный тип присваиваемых данных.")
        
        # атрибуты weight, price - число, если число, то должно быть больше нуля
        elif (__name in ('weight', 'price') and type(__value) in (float, int)):
            if  __value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, __name, __value)

    def __delattr__(self, __name: str) -> None:
        if (__name == 'id'):
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, __name)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")