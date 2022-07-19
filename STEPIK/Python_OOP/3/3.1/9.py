class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c # - габаритные размеры (целые или вещественные числа).

    def a_get(self):
        return self.__a

    def a_set(self, value):
        if Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION:
            self.__a = value

    def b_get(self):
        return self.__b

    def b_set(self, value):
        if Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION:
            self.__b = value

    def c_get(self):
        return self.__c

    def c_set(self, value):
        if Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION:
            self.__c = value

            
    a = property(a_get, a_set)
    b = property(b_get, b_set)
    c = property(c_get, c_set)

    def __setattr__(self, __name: str, __value) -> None:
        if __name in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            object.__setattr__(self, __name, __value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
