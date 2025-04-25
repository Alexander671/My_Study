from functools import reduce
from typing import List
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self,max_weight, things:List[Thing]=[]):
        self.max_weight = max_weight
        self.__things = things

    @property
    def things(self,):
        return self.__things

    @things.setter
    def things(self, v):
        self.__things = v

    def add_thing(self, thing:Thing): # - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
        if self.get_total_weight() + thing.weight < self.max_weight: 
            self.things.append(thing)

    def remove_thing(self, indx): # - удаление предмета по индексу списка __things;
        del self.things[indx]

    def get_total_weight(self): #возвращает суммарный вес предметов в рюкзаке.
        return reduce(lambda x, y: x + y.weight, self.things, 0)

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")