class ItemAttrs:
    def __getitem__(self, key): # - для получения значения атрибута по индексу;
        return (list(self.__dict__.values()))[key]
    
    def __setitem__(self, key, value): # - для изменения значения атрибута по индексу.
        self.__dict__[key] = value

class Point(ItemAttrs):
    def __init__(self, *args):
        self.__dict__.update(zip((i for i in range(0, 10)), list(args)))

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10

print(pt.__dict__)