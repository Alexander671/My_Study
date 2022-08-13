class ListInteger(list):
    def __init__(self, lst):# 
        super().__init__(lst)

    def __setitem__(self, key, value):# 
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        else:
            super().__setitem__(key,value)


    def append(self, value):# 
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        else:
            super().append(value)

li = ListInteger((1,2,3))

s = ListInteger((1, 2, 3))
print(s)
s[1] = 10
print(s[1])
s.append(11)
print(s)
s[0] = 10.5 # TypeError