
class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        FloatValue.validate(value)
        instance.__dict__[self.name] = value

    @classmethod
    def validate(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

class Cell:
    value = FloatValue()
    def __init__(self, value):
        self.value = value

class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell(float(i + 1 + j * m)) for i in range(m)] for j in range(n)]


table = TableSheet(5,3)
