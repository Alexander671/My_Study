import sys


class ShopItem:
    objects = {}
    # name - название товара (строка);
    # weight - вес товара (число: целое или вещественное);
    # price - цена товара (число: целое или вещественное).
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.amount_of_hashes = 1
        self.last_hash = None

    def __hash__(self): # - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
        current_hash = hash((self.name, self.weight, self.price))
        if current_hash == self.last_hash:
            self.amount_of_hashes += 1
            self.last_hash = current_hash
            ShopItem.objects.setdefault(current_hash, 0)
            ShopItem.objects[current_hash] += 1
        self.last_hash = current_hash

        return current_hash

    def __eq__(self, obj): # - чтобы объекты с одинаковыми хэшами были равны.
        return (self.name.lower() == obj.name.lower()) & (self.weight == obj.weight) & (self.price == obj.price)


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst1 = map(lambda x: x.split(':'), lst_in)
lst2 = map(lambda x: [x[0]] + x[1].split(), lst1)
lst3 = list(map(lambda x: ShopItem(*x), lst2))
# d = {ShopItem: [ShopItem, amount]}
# dict(zip())
d = dict(zip(lst3, range(0,3)))
print(d)
print(list(d.keys())[2].objects)