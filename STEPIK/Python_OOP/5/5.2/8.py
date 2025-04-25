class Rect:
    def __init__(self, x, y, width, height):
        self.validate_type(x,y,width,height)
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def validate_type(self,x,y,width,height):
        if type(x) == int and type(y) == int or type(width) in (int, float) and type(height) in (int, float):
            if width <= 0 or height <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')
        else:
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def is_collision(self, rect): 
        if self._y < rect._y - rect._height or  self._y - self._height < rect._y or  self._x + self._width < rect._x  or  self._x  > rect._x + self._width:
            raise TypeError('прямоугольники пересекаются')

lst_rect = [
Rect(0, 0, 5, 3),
Rect(6, 0, 3, 5),
Rect(3, 2, 4, 4),
Rect(0, 8, 8, 1),]

lst_not_collision = [lst_rect[3]]




r = Rect(1, 2, 10, 20)
assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

r2 = Rect(1.0, 2, 10.5, 20)

try:
    r2 = Rect(0, 2, 0, 20)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"


assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"

def not_collision(rect):
    for x in lst_rect:
        try:
            if x != rect:
                rect.is_collision(x)
        except TypeError:
            return False
    return True

f = list(filter(not_collision, lst_rect))
print(lst_not_collision, f)
assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

r = Rect(3, 2, 2, 5)
rr = Rect(1, 4, 6, 2)

try:
    r.is_collision(rr)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
