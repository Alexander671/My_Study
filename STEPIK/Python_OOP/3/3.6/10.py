class NumValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        print(type(value))
        if type(value) in (int, float):
            if value <= 0:
                raise ValueError("длины сторон треугольника должны быть положительными числами")
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")



class Triangle:
    a = NumValue()
    b = NumValue()
    c = NumValue()
    
    def __init__(self, a, b, c) -> None:
        self.validate(a,b,c)
        self.a = a
        self.b = b
        self.c = c

    def validate(self, a,b,c):
        if not((a < b + c) & (b < a + c) & (c < a + b)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")


    def __len__(self,): # - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
        p = self.a + self.b + self.c
        return int(p)

    def __call__(self, *args, **kwds):
        p = len(self) / 2

        return (p * (p-self.a) * (p - self.b) * (p - self.c)) ** 0.5





tr = Triangle(5, 4, 3)

assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"


try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
 
