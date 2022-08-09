class Cell:
    def __init__(self, value):
        self.value = value
class SparseTable:

    def __init__(self, rows=0, cols=0) -> None:
        # Хранить ячейки следует в словаре, 
        # ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell.
        self.rows = rows # - общее число строк таблицы (начальное значение 0);
        self.cols = cols # - общее число столбцов таблицы (начальное значение 0).
        self.dict_values = {}

    def update_index(self,):
        self.rows = max(i[0] for i in self.dict_values.keys()) + 1
        self.cols = max(i[1] for i in self.dict_values.keys()) + 1

    def add_data(self, row, col, data): # - добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа);
        self.dict_values[(row, col)] = data
        self.update_index()
    
    
    def remove_data(self, row, col): # - удаление ячейки (объект класса Cell) с индексами (row, col).
        try:
            del self.dict_values[(row, col)]
            self.update_index()
        except:
            raise IndexError('ячейка с указанными индексами не существует')


    def __getitem__(self, key):
        try:
            return self.dict_values[key].value
        except:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, keys, value):
        self.dict_values[keys] = Cell(value)
        self.update_index()


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError

st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
print(st[3,2])
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"


st = SparseTable()
st[3, 2] = 100
st[4, 6] = 100
st[11, 5] = 100
st.remove_data(11,5)
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
print(st.rows, st.cols)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"
