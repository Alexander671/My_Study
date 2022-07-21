from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    def set_real(self, obj):
        self.__real = obj
    
    def get_real(self):
        return self.__real

    def set_img(self, obj):
        self.__img = obj
    
    def get_img(self):
        return self.__img 

    real = property(get_real, set_real)
    img = property(get_img, set_img)

    def __setattr__(self, key, value) -> None:
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        else:
            object.__setattr__(self, key, value)

    def __abs__(self,):
        return sqrt(self.real * self.real + self.img * self.img)

cmp = Complex(7,8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
