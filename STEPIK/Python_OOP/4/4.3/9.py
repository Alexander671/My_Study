class StringDigit(str):
    def __init__(self, string):
        self.validate(string)

        super().__init__()

    def validate(self , __value:str):
        if not __value.isnumeric():
            raise ValueError("в строке должны быть только цифры")


    def __add__(self, _o):
        self.validate(_o)
        self = super().__add__(_o)
        return StringDigit(self)

    def __radd__(self, _o):
        return StringDigit(_o.__add__(self))


sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


print(id(sd))
sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"
print(id(sd))

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"
print(id(sd))


sd = "0" + sd
assert sd == "00123345", "неверно отработал оператор +"
print(id(sd))


try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
    
try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"