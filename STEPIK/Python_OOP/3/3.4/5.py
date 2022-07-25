from functools import reduce

class ListMath:
    def __init__(self, lst_math=[]):
        self.lst_math = list(filter(lambda x: type(x) in (int, float), lst_math))
    
    #################################
    # вычитание
    def __sub__(self, obj):

        return ListMath(list(map(lambda x: x - obj,self.lst_math)))

    def __rsub__(self, obj):
        return ListMath(list(map((lambda x: obj - x), self.lst_math)))
        
    def __isub__(self, obj):
        for i in range(len(self.lst_math)):
            self.lst_math[i] -= obj
        return self
    #################################


    #################################
    # сумма
    def __add__(self, obj):

        return ListMath(list(map(lambda x: x + obj,self.lst_math)))

    def __radd__(self, obj):
        
        return ListMath(list(map((lambda x: obj + x), self.lst_math)))
        
    def __iadd__(self, obj):
        for i in range(len(self.lst_math)):
            self.lst_math[i] += obj
        return self
    ##################################


    ##################################
    # умножение
    def __mul__(self, obj):

        return ListMath(list(map(lambda x: x * obj,self.lst_math)))

    def __rmul__(self, obj):
        
        return ListMath(list(map((lambda x: obj * x), self.lst_math)))
        
    def __imul__(self, obj):
        for i in range(len(self.lst_math)):
            self.lst_math[i] *= obj
        return self
    #################################

    
    ##################################
    # деление
    def __truediv__(self, obj):

        return ListMath(list(map(lambda x: x / obj,self.lst_math)))

    def __rtruediv__(self, obj):
        
        return ListMath(list(map((lambda x: obj / x), self.lst_math)))
        
    def __itruediv__(self, obj):
        for i in range(len(self.lst_math)):
            self.lst_math[i] /= obj
        return self
    #################################


    def get_list(self):
        return self.lst_math


lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
assert lst.lst_math == [1, -5, 7.68], "аттрибут lst_math не убрал лишние типы данных"

lst = 76 - lst
print(lst.get_list())


lst = lst + 76 # сложение каждого числа списка с определенным числом
print(lst.get_list())

lst = 6.5 + lst # сложение каждого числа списка с определенным числом
print(lst.get_list())

lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst.get_list())

lst = lst - 76 # вычитание из каждого числа списка определенного числа
print(lst.get_list())

lst = 7.0 - lst # вычитание из числа каждого числа списка
print(lst.get_list())

lst -= 76.3
print(lst.get_list())

lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0