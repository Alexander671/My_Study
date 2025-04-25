class Integer:
    def __init__(self, start_value=0):
        self.__start_value = start_value

    @property
    def start_value(self):
        return self.__start_value

    @start_value.setter
    def start_value(self, value):
        if type(value) == int:
            self.__start_value = value
        else:
            raise ValueError('должно быть целое число')
    
    def __repr__(self):
        return str(self.start_value)


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length # - максимальное количество элементов в массиве;
        self.cell = cell # - ссылка на класс, описывающий отдельный элемент этого массива (см. далее, класс Integer). Начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0.
        self.list_of_value = [self.cell() for _ in range(self.max_length)]

    def __check(self, indx):
        if type(indx) != int or  not (-self.max_length <= indx < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, indx):
        self.__check(indx)
        return self.list_of_value[indx].start_value
        
    # self.cell
    def __setitem__(self, key, value):
        self.__check(key)
        if type(value) != int:
            raise ValueError('должно быть целое число')
        else:
            self.list_of_value[key].start_value = value
        
    def __repr__(self):
        return ' '.join(map(str, self.list_of_value))

ar_int = Array(10, cell=Integer)
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError