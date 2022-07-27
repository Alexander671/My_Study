class Thing:
    def __init__(self, name, mass):
        # где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
        self.name = name
        self.mass = mass

    def __eq__(self, __o: object) -> bool:
        return (self.name.lower() == __o.name.lower()) & (self.mass == __o.mass)

class Box:
    def __init__(self,):
        self.objects = []

    def add_thing(self, obj): # - добавление предмета obj (объект другого класса Thing) в ящик;
        self.objects.append(obj)
    
    def get_things(self): # - получение списка объектов ящика.
        return self.objects

    def __eq__(self, __o: object) -> bool:
        return sum(map(lambda x: x in self.objects, __o.objects)) == \
               sum(map(lambda x: x in __o.objects, self.objects)) == \
               len(self.objects)

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)

# class Rect:
#     def __init__(self, x):
#             self.x = x
#     def __hash__(self):
#             return hash(self.x)
#     def __eq__(self, obj):
#             return self.x == obj.x
# 
# r1 = Rect(1)
# r2 = Rect(1)
# d = {r1 : r2}
# d[r1]
# #main__.Rect object at 0x7f480ffdee80>
# d[r2]
# #main__.Rect object at 0x7f480ffdee80>
# r1.x = 3
# d[r2]