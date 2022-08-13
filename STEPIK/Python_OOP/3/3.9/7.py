from functools import reduce

class IterColumn:
    def __init__(self, lst, col):
        self.lst = lst
        self.col = col
        self.row = len(self.lst)

    def __iter__(self):
        self.general_list = reduce(lambda x, y: x + y, self.lst)
        self.index = 0
        self.rows = len(self.lst)
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.general_list) or self.rows < self.index:
            raise StopIteration

        self.step = len(self.lst[0])
        return self.lst[self.index - 1][self.col]


lst = [[7, 8, 9, 10],
       [7, 8, 9, 10],
       [7, 8, 9, 10],
       [7, 8, 9, 10],]

it = IterColumn(lst, 2)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)