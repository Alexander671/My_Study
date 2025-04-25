from math import sqrt
class LineTo:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class PathLines:
    def __init__(self, *args):
        self.list_line_to:list[LineTo] = [LineTo()] + list(args)

    def get_path(self): # - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
        return self.list_line_to

    def get_length(self): # - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
        sum = 0
        iter_list = self.list_line_to

        for i in range(0, len(iter_list) - 1):
            # L = sqrt((x1-x0)^2 + (y1-y0)^2) 
            first = (iter_list[i].x - iter_list[i + 1].x) ** 2
            second = (iter_list[i].y - iter_list[i + 1].y) ** 2         
            sum += sqrt(first + second)      
        return sum

    def add_line(self, line): # - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
        self.list_line_to.append(line) 



p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print((dist))