class Digit:
    def __init__(self, val):
        Digit.validate(self, val)
        self.value = val
    
    def validate(self, val):
        if not (type(val) == int or type(val) == float):
            raise TypeError('значение не соответствует типу объекта')
    

class Integer(Digit):
    def __init__(self, val):
        super().__init__(val)
        Integer.validate(self, val)
        
    def validate(self, val):
        if not type(val) == int:
            raise TypeError('значение не соответствует типу объекта')
    
class Float(Digit):
    def __init__(self, val):
        super().__init__(val)
        Float.validate(self, val)
        
    def validate(self, val):
        if not type(val) == float:
            raise TypeError('значение не соответствует типу объекта')
    
class Positive(Digit):
    def __init__(self, val):
        super().__init__(val)
        Positive.validate(self, val)
    
    def validate(self, val):
        if val < 0:
            raise TypeError('значение не соответствует типу объекта')

class Negative(Digit):
    def __init__(self, val):
        super().__init__(val)
        self.__class__.validate(self, val)
        
    def validate(self, val):
        if not val < 0:
            raise TypeError('значение не соответствует типу объекта')

class PrimeNumber(Integer,Positive): # - простые числа; наследуется от классов Integer и Positive;
    pass
class FloatPositive(Float, Positive): # - наследуется от классов Float и Positive.
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = filter(lambda x: isinstance(x, Positive), digits) # - все объекты, относящиеся к классу Positive;
lst_float = filter(lambda x: isinstance(x, Float), digits) # - все объекты, относящиеся к классу Float.
