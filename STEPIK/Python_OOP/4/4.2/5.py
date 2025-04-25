class  Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

class  Plants(Protists):
    pass
class  Animals(Protists):
    pass
class  Mosses(Plants):
    pass
class  Flowering(Plants):
    pass
class  Worms(Animals):
    pass
class  Mammals(Animals):
    pass
class  Human(Mammals):
    pass
class  Monkeys(Mammals):
    pass

class Monkey(Monkeys): # - наследуется от Monkeys и служит для описания обезьян;
    pass
class Person(Human): # - наследуется от Human и служит для описания человека;
    pass
class Flower(Flowering): # - наследуется от Flowering и служит для описания цветка;
    pass
class Worm(Worms): # - наследуется от Worms и служит для описания червей.
    pass

def subclass(lst_objs, cls):
    return list(filter(lambda x: isinstance(x, cls), lst_objs))

obj1 = Monkey("мартышка", 30.4, 7)
obj2 = Monkey("шимпанзе", 24.6, 8)
obj3 = Person("Балакирев", 88, 34)
obj4 = Person("Верховный жрец", 67.5, 45)
obj5 = Flower("Тюльпан", 0.2, 1)
obj6 = Flower("Роза", 0.1, 2)
obj7 = Worm("червь", 0.01, 1)
obj8 = Worm("червь 2", 0.02, 1)
lst_objs = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8]


lst_animals = subclass(lst_objs, Animals) # все объекты, относящиеся к животным (Animals);
lst_plants = subclass(lst_objs, Plants) # все объекты, относящиеся к растениям (Plants);
lst_mammals = subclass(lst_objs, Mammals) # все объекты, относящиеся к млекопитающим (Mammals).