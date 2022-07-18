class Point: 
    __instance = None
    def __new__(cls, x, y):
            return super().__new__(cls)
        
    def clone(self):
        new_obj = self.__new__(Point, self.x, self.y)
        new_obj.__init__(self.x, self.y)
        return new_obj
        return         
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(1, 2)
pt_clone = pt.clone()
print(pt.x, pt_clone.x)

# Traceback (most recent call last):
# File "jailed_code", line 20, in <module>
#    assert id(pppttt) != id(pt), "метод clone не создает новый объект"
# AssertionError: метод clone не создает новый объект



# Error:
# Traceback (most recent call last):
#   File "jailed_code", line 19, in <module>
#     assert pppttt.__dict__ == pt.__dict__, "объект, созданный через метод clone не соответствует исходному"
# AssertionError: объект, созданный через метод clone не соответствует исходному
