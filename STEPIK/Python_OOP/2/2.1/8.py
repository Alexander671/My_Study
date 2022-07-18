class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self): # - возвращение кортежа текущих координат __x, __y
        return self.__x, self.__y

    

class Rectangle:
    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(args[0],args[1])
            self.__ep = Point(args[2],args[3])
            
        elif len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
    
    def set_coords(self, sp, ep): # - изменение текущих координат, где sp, ep - объекты класса Point;
        self.__sp = sp
        self.__ep = ep
    
    def get_coords(self): # - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника (ссылки на локальные свойства __sp и __ep);
        return self.__sp, self.__ep

    def draw(self): # - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
        sp_coord = self.__sp.get_coords()
        ep_coord = self.__ep.get_coords()
        print(f"Прямоугольник с координатами: ({sp_coord[0]}, {sp_coord[1]}) ({ep_coord[0]}, {ep_coord[1]})")


rect = Rectangle(Point(0, 0),  Point(20, 34))
