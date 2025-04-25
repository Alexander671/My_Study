class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __add__(self, obj):
        if len(self) == len(obj):
            return Vector(*list(map(lambda x,y: x + y, self.coords, obj.coords)))
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __sub__(self, obj):
        if len(self) == len(obj):
            return Vector(*list(map(lambda x,y: x - y, self.coords, obj.coords)))
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __mul__(self, obj):
        if len(self) == len(obj):
            return Vector(*list(map(lambda x,y: x * y, self.coords, obj.coords)))
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __iadd__(self, obj):
        if type(obj) == Vector:
            for i, object in zip(range(len(self.coords)), obj.coords):
                self.coords[i] += object
        else:
            for i in range(len(self.coords)):
                self.coords[i] += obj
        return self
    
    def __isub__(self, obj):
        if type(obj) == Vector:
            for i, object in zip(range(len(self.coords)), obj.coords):
                self.coords[i] -= object
        else:
            for i in range(len(self.coords)):
                self.coords[i] -= obj
        return self

    def __eq__(self, obj):
        return all(map(lambda x, y: x == y, self.coords, obj.coords))

    def __len__(self):
        return len(self.coords)
v1 = Vector(1,2,3)
v2 = Vector(1,2,3)
print(v1.coords)
print(v2.coords)

r1 = v1 + v2 # суммирование соответствующих координат векторов
print(r1.coords)
r2 = v1 - v2 # вычитание соответствующих координат векторов
print(r2.coords)

r3 = v1 * v2 # умножение соответствующих координат векторов
print(r3.coords)
v1 += 10 # прибавление ко всем координатам вектора числа 10
print(v1.coords)
v1 -= 10 # вычитание из всех координат вектора числа 10
print(v1.coords)
v1 += v2
print(v1.coords)
v2 -= v1
print(v2.coords)
r9  = v1 == v2 # True, если соответствующие координаты векторов равны
r10 = v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
print(r9)
print(r10)

