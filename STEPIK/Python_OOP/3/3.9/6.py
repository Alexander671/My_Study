

from functools import reduce


class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.general_list = reduce(lambda x, y: x + y, self.lst)
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.general_list):
            raise StopIteration
        return self.general_list[self.index - 1]
lst = [[1],
       [2, 3],
       [4, 5, 6],
       [7, 8, 9, 10],]
it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)