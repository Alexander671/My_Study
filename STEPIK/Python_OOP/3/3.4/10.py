
from math import sqrt


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2,2)) -> None:
        self.step = step
        self.size = size

    def __call__(self, matrix):
        if any(map(lambda x: sqrt(len(x)) - int(sqrt(len(x))) != 0,  matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")
        check_matrix = filter(lambda x: self.step[0] * self.step[1] <= len(x), matrix)
        return map(max,check_matrix)

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(list(res))