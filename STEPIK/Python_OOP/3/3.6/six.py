import sys


class ShopItem:
    objects_of_hashes = {}
    # name - название товара (строка);
    # weight - вес товара (число: целое или вещественное);
    # price - цена товара (число: целое или вещественное).
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self._current_hash = None
    def __hash__(self): # - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
        current_hash = hash((self.name.lower(), self.weight, self.price))
        ShopItem.objects_of_hashes.setdefault(current_hash, 0)
        ShopItem.objects_of_hashes[current_hash] += 1
        self._current_hash = current_hash
        return current_hash

    def __eq__(self, obj): # - чтобы объекты с одинаковыми хэшами были равны.
        return (self.name.lower() == obj.name.lower()) & (self.weight == obj.weight) & (self.price == obj.price)

    def get_list_of_object_amount(self):
        object_hash = self.objects_of_hashes[self._current_hash]
        i = 1
        while object_hash != 1:
            object_hash -= 2
            i += 1
        return [self, i]

# преобразование строк к заданному формату
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst1 = map(lambda x: x.split(':'), lst_in)
lst2 = map(lambda x: [x[0]] + x[1].split(), lst1)



shop_items = {}
for j in lst2:
    shop = ShopItem(*j)
    shop_items[shop] = None
    shop_items[shop] = shop.get_list_of_object_amount()

print(shop_items)




it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
print(hash(it1), hash(it2))
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"

'''

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000


'''