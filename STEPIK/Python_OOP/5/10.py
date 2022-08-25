class FloatValidator:
    type = float
    def __init__(self,min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != self.__class__.type:
            raise ValueError('значение не прошло валидацию') 
        if not self.min_value <= value <= self.max_value:
            raise ValueError('значение не прошло валидацию')

class IntegerValidator(FloatValidator):
    type = int


def around_exception(value, validators):
    for v in validators:
        try:
            v(value)
            return value
        except:
            pass


def is_valid(lst, validators): 
    return list(filter(lambda x: around_exception(x, validators) != None, lst))

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 10, 0.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]

print(lst_out)