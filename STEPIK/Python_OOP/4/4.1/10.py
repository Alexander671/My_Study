class Vector:
    def __init__(self, *args):
        self.coords = tuple(args)

    def valid_size(self, o):
        if not len(self.coords) == len(o.coords):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, o):
        self.valid_size(o)
        return o.__class__(*(map(lambda x, y: x + y, self.coords, o.coords)))

    def __sub__(self, o):
        self.valid_size(o)
        return o.__class__(*(map(lambda x, y: x - y, self.coords, o.coords)))

    def get_coords(self):
        return self.coords

class VectorInt(Vector):
    def __init__(self, *args):
        if all(map(lambda x: type(x) == int, args)):
            super().__init__(*args)
        else:
            raise ValueError('координаты должны быть целыми числами')
