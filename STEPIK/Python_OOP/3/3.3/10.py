class PolyLine:
    def __init__(self, *args):
        self.list_line = list(args)

    def add_coord(self, x, y): # - добавление новой координаты (в конец);
        self.list_line.append((x,y))
        
    def remove_coord(self, indx): # - удаление координаты по индексу (порядковому номеру, начинается с нуля);
        self.list_line = self.list_line[:indx] + self.list_line[indx + 1:]
    
    def get_coords(self, ): # - получение списка координат (в виде списка из кортежей).
        return self.list_line