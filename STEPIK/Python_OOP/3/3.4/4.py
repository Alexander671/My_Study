# странное поведение, с которым я пока не знаю и не хочу решать эту задачу.
# 1 in [True] => True

class NewList:
    def __init__(self, new_list=[]):
        self.new_list = new_list

    def __sub__(self, obj):
        if type(obj) == list:
            new_listed = self.new_list[:]

            first_list  = list(zip(self.new_list, (map(type, self.new_list))))
            second_list = list(zip(obj, (map(type, obj))))
            
            for i in first_list:
                
                if i not in second_list:
                    new_listed.append(i[0])

            
        elif type(obj) == NewList:
            new_listed = self.new_list[:]

            first_list  = list(zip(self.new_list, list(map(type, self.new_list))))
            second_list = list(zip(obj.new_list, list(map(type, obj.new_list))))
            
            for i in first_list:

                if i in second_list:
                    new_listed.remove(i[0])
                    
        return NewList(new_listed)

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

print(res1.get_list())
assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
print(lst_1.get_list())
lst_2 = NewList([10, True, False, True, 1, 7.87])
print(lst_2.get_list())

res = lst_1 - lst_2
print(res.get_list())
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"