class Thing:
    def __init__(self, name, weight):#
        # name - название предмета (строка); 
        # weight - вес предмета (вещественное или целочисленное значение). 
        # В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []

    def validate_weight(self, thing):
        if not sum(map(lambda x: x.weight, self.things)) + thing.weight <= self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
    
    def validate_index(self, key):
        if len(self.things) < key:
            raise IndexError('неверный индекс')

    def add_thing(self, thing): # - добавление нового объекта thing класса Thing в сумку.
        self.validate_weight(thing)
        self.things.append(thing)    

    def __getitem__(self, key):
        self.validate_index(key)
        return self.things[key]

    def __setitem__(self, key, value):
        self.things[key].weight = 0
        self.validate_weight(value)
        self.validate_index(key)
        self.things[key] = value

    def __delitem__(self, key):
        self.validate_index(key)
        del self.things[key]




b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
 
