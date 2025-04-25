# не доделана
class IntegerValue: # - дескриптор данных для работы с целыми числами.
    
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        IntegerValue.validate(value)
        instance.__dict__[self.name] = value

    @classmethod
    def validate(cls, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')


class CellInteger: # - для операций с целыми числами;
    value = IntegerValue()
    def __init__(self, value=0):
        self.value = value

class TableValues: # - для работы с таблицей в целом;
    def __init__(self, rows:int, cols:int, cell):
        if not cell:
            raise ValueError('параметр cell не указан')
        else:
            self.rows = rows
            self.cols = cols
            self.cells = ((CellInteger(),) * cols,) * rows

    def __getitem__(self, keys):
        key1, key2 = keys
        return self.cells[key1][key2].value

    def __setitem__(self, keys, value):
        key1, key2 = keys
        new_list = list(map(list, self.cells))
        new_list[key1][key2] = CellInteger(value)
        self.cells = tuple(map(tuple,new_list))
