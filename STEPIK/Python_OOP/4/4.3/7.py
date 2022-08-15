
def integer_params_decorated(fn):
    def wrapper(*args):
        if all((map(lambda x: type(x) == int, args[1:]))):
            return fn(*args)
        else:
            raise TypeError("аргументы должны быть целыми числами") 
    return wrapper

def integer_params(cls):

    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]

vector = Vector(1, 2)
print(vector[1])
vector[1] = 20.4 # TypeError