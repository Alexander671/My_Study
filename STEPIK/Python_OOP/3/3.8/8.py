class Cell:
    def __init__(self, is_free = True, value = 0) -> None:
        self.is_free = is_free # - True, если клетка свободна; False в противном случае;
        self.value = value # - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

    def __bool__(self,):
        return self.is_free

class TicTacToe:
    def __init__(self,) -> None:
        self.pole = ((Cell(),) * 3,) * 3


    def clear(self,):
        self.pole = ((Cell(),) * 3,) * 3

    def __validate(self, key):
        if len(self.get_data()) < key + 1 or key + 1 < 0 or not type(key) == int:
            raise IndexError('неверный индекс')
        
        if not self.pole[key].is_free:
            raise ValueError('клетка уже занята')

    def __getitem__(self, keys):
        self.__validate
        key1, key2 = keys
        if type(key1) == int and type(key2) == slice:
            return (tuple(map(lambda x:x[key1].value, self.pole)))[key2]
        
        if type(key1) == slice and type(key2) == int:
            return tuple(map(lambda x: x.value, self.pole[key2][key1]))

        
        if type(key1) == int and type(key2) == int:
            return self.pole[key2][key1].value

    def __setitem__(self, keys, value):
        self.__validate
        key1, key2 = keys
        new_list = list(map(list, self.pole))
        new_list[key2][key1] = Cell(False, value)
        self.pole = tuple(map(tuple,new_list))


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"