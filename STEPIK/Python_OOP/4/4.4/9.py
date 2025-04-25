
def integer_params_decorated(vector, name, fn):
    def wrapper(*args, **kwargs):
        vector.append(name)
        return fn(*args, **kwargs)
    return wrapper

def class_log(vector):
    def wrapper(cls):
        
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, integer_params_decorated(vector, k, v))
        return cls    
    return wrapper


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)