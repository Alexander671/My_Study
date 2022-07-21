from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.vector = args[0] * [0]
        else:
            self.vector = list(args)

    def set_coords(self, *args): # - для изменения координат радиус-вектора;
        self.vector = list(args) + self.vector[(len(args)):]
    
    def get_coords(self): # - для получения текущих координат радиус-вектора (в виде кортежа).
        return tuple(self.vector)

    def __len__(self): # - возвращает число координат радиус-вектора (его размерность);
        return len(self.vector)


    def __abs__(self): # - возвращает длину радиус-вектора (вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N) - корень квадратный из суммы квадратов координат).    
        return sqrt(sum(map(lambda x: x ** 2, self.vector)))

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
print(vector3D.get_coords())

vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.get_coords())
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
