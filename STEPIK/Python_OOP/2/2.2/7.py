class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    @classmethod
    def validate(cls, x, default):
        if type(x) in (int,float) and cls.MIN_COORD <= x <= cls.MAX_COORD:
            return x
        else:
            return default
    # __x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).
    def __init__(self, x=0, y=0):
        self.__x = RadiusVector2D.validate(x, 0)
        self.__y = RadiusVector2D.validate(y, 0)
    
    def get_x(self):
        return self.__x   
    
    def set_x(self, x):
        self.__x = RadiusVector2D.validate(x, self.get_x())
    
    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__y = RadiusVector2D.validate(y, self.get_y())

    @staticmethod
    def norm2(vector):
        return vector.get_x() ** 2 + vector.get_y() ** 2


    x = property(get_x, set_x)
    y = property(get_y, set_y)
    

    

v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
v3.MAX_COORD = 100
print(v3.MAX_COORD)