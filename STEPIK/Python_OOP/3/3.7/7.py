class Ellipse:
    # где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла. Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. Вторая команда создает объект с локальными атрибутами 
    
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if x1:
            self.x1 = x1 #
        if y1:
            self.y1 = y1 #
        if x2:
            self.x2 = x2 #
        if y2:
            self.y2 = y2 # и соответствующими переданными значениями.

    def __bool__(self):
        return len(self.__dict__) == 4

    def get_coords(self): # - для получения кортежа текущих координат объекта.     
        if not self:
            raise AttributeError('нет координат для извлечения')
        else:
            return (self.x1, self.y1, self.x2, self.y2)

lst_geom = [Ellipse(),Ellipse(),Ellipse(1,2,3,4),Ellipse(5,6,7,8)]
for i in lst_geom:
    if i:
        i.get_coords()