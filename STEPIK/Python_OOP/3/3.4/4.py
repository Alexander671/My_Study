# странное поведение, с которым я пока не знаю и не хочу решать эту задачу.
# 1 in [True] => True


from copy import deepcopy


class NewList:
    def __init__(self, new_list=[]):
        self.new_list = new_list[:]

    def __sub__(self, obj):

        # создали первый список (Any, Type)
        # чтобы проводить более точное сравнение между значениями
        first_list  = list(zip(self.new_list,
                               (map(type, self.new_list))))
        

        # создаем второй список в зависимости от типа параметра
        if type(obj) == list:
            second_list = list(zip(obj, (map(type, obj))))
    
        elif type(obj) == NewList:
            second_list = zip(obj.new_list,
                                 (map(type, obj.new_list)))
        
        # удаляем значения
        for i in second_list:
            if i in first_list:
                first_list.remove(i)
        
        # возвращаем первые значения кортежа [(Any, Type)] -> [Any]
        return NewList(list(map(lambda x: x[0], first_list)))


    def __rsub__(self, obj):

        if type(obj) == list:
            return NewList(obj) - self
            
        elif type(obj) == NewList:
            return obj - self

    def __isub__(self, obj):
        return self - obj 


    def get_list(self):
        return self.new_list

lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]

 
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"


rez = NewList([0, 1, 1, True, True, "1"]) - [True, 0, 1]
lst1 = NewList([0, 1, 1, True, True, "1"])
lst1 -= [True, 0, 1]
lst1 = NewList([0, 1, 1, True, True, "1"])
lst1 -= NewList([True, 0, 1])
