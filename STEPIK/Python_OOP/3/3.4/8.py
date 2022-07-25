class Budget: # - для управления семейным бюджетом;
    def __init__(self, items=[]):
        self.items = items 

    def add_item(self, it): #  - добавление статьи расхода в бюджет (it - объект класса Item);
        self.items.append(it)

    def remove_item(self, indx): # - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
        self.items.remove(self.items[indx])

    def get_items(self): # - возвращает список всех статей расходов (список из объектов класса Item).
        return self.items


class Item: # - пункт расходов бюджета.
    def __init__(self, name, money):
        self.name = name
        self.money = money

    #################################
    # сумма
    def __add__(self, obj):
        if type(obj) in (int, float):
            s = self.money + obj
        elif type(obj) == Item:
            s = self.money + obj.money
        return s

    def __radd__(self, obj):
        return self + obj


it1 = Item('name', 100)
it2 = Item('name', 100)
s = it1 + it2 # сумма для двух статей расходов
s1 = it1 + it1 + 200 + it1
print(s1)

my_budget = Budget()

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
print(my_budget.get_items())
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
