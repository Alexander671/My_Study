
class PointTrack:
    def __init__(self, x, y):
        self.validate(x)
        self.validate(y)
        
        self.x = x
        self.y = y

    def validate(self, value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"
class Track:
    def __init__(self, *args):
        if len(args) == 2:
            
            self.__points = PointTrack(args[0], args[1])
            
        else:
            self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)


    def add_back(self, pt): # - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
        self.__points.append(pt)

    def add_front(self, pt): # - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
        self.__points.insert(pt, 0)

    def pop_back(self): # - удаление последней точки из маршрута;
        del self.__points[-1]

    def pop_front(self): # - удаление первой точки из маршрута.
        del self.__points[0]
