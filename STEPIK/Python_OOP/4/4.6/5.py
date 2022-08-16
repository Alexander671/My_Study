
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView

class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


class ShopGenericView(Book): # - для отображения всех локальных атрибутов объектов любых дочерних классов (не только Book);
    def __str__(self,):
        return ('\n'.join(map(lambda x: f'{x[0]}: {x[1]}', self.__dict__.items())))

class ShopUserView(Book): # - для отображения всех локальных атрибутов, кроме атрибута _id, объектов любых дочерних классов (не только Book).
    def __str__(self,):
        return ('\n'.join(map(lambda x: f'{x[0]}: {x[1]}', list(self.__dict__.items())[1:])))

sgv = ShopGenericView('title','author', 2005)
print(sgv)