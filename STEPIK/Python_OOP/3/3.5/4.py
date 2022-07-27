class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def validate(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, obj):
        Dimensions.validate(obj)
        self.__a = obj

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, obj):
        Dimensions.validate(obj)
        self.__b = obj

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, obj):
        Dimensions.validate(obj)
        self.__c = obj

class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim:Dimensions = dim

    def __le__(self, __o: object) -> bool:
        return self.dim.a * self.dim.b * self.dim.c < __o.dim.a * __o.dim.b * __o.dim.c


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]


lst_shop_sorted = sorted(lst_shop)  
