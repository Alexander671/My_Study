

class Track:
    def __init__(self, start_x, start_y, speed=None):
        self.start_x = start_x 
        self.start_y = start_y 
        self.coords = []

    def add_point(self, x, y, speed): # - добавление новой точки маршрута (линейный сегмент), который можно пройти со средней скоростью speed.
        self.coords.append([(x,y), speed])

    def __getitem__(self, indx):
        if type(indx) == int and 0 <= indx <= len(self.coords):
            return self.coords[indx]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if type(key) == int and 0 <= key <= len(self.coords):
            self.coords[key][1] = value
        else:
            raise IndexError('некорректный индекс')

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2


coord, speed = tr[1] # получение координаты (кортеж с двумя числами) и скорости (число) для линейного сегмента маршрута с индексом indx
tr[2] = 60
x = tr[2]
print(x)