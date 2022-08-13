class Thing:
    unique_id = 0
    def __init__(self, name, price):
        Thing.unique_id += 1
        self.id = Thing.unique_id
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self): # - для получения кортежа в формате (id, name, price, weight, dims, memory, frm)
        return self.__dict__.values()

class Table(Thing): # - для столов;
    def __init__(self,name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing): # - для электронных книг.
    def __init__(self,name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())