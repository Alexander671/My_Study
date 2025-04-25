class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y # - координаты центра окружности (вещественные или целые числа);
        self.__radius = radius # - радиус окружности (вещественное или целое положительное число).

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def x_get(self):
        return self.__x        
        
    def x_set(self, value):
        self.__x = value  
    
    def y_get(self):
        return self.__y


    def y_set(self, value):
        self.__y = value    

    def radius_get(self):
        return self.__radius

    def radius_set(self, value):
        if (value > 0):
            self.__radius = value    
    
    x = property(x_get, x_set)
    y = property(y_get, y_set)
    radius = property(radius_get, radius_set)


circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим

print(circle.radius)
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
print(res)