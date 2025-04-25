class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class House(SellItem): # - дома;
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem): # - квартиры;
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land(SellItem): # - земельные участки.
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.list_agency = []

    def add_object(self, obj): #  - добавление нового объекта недвижимости для продажи (один из объектов классов: House, Flat, Land);
        self.list_agency.append(obj)

    def remove_object(self, obj): #  - удаление объекта obj из списка объектов для продажи;
        del self.list_agency[self.list_agency.index(obj)]

    def get_objects(self): # - возвращает список из всех объектов для продажи.
        return self.list_agency