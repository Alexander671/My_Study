input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

class Triangle:
    def __init__(self, a, b, c):
        Triangle.validate_type(a, b, c)
        Triangle.validate(a,b,c)
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def validate(a,b,c):
        if not((a < b + c) & (b < a + c) & (c < a + b)):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')        
        else:
            return a,b,c
    
    @staticmethod
    def validate_type(a,b,c):
        if type(a) in (int, float) and type(b) in (int, float) and type(c) in (int, float):
            if a <= 0 or b <= 0 or c <= 0:
                raise TypeError('стороны треугольника должны быть положительными числами')
            else:
                return a,b,c
        else:
            raise TypeError('стороны треугольника должны быть положительными числами')
            
def filter_triangles(*xs):
    try:
        return Triangle(*xs[0])
    except:
        return
lst_tr = list(map(lambda x: Triangle(*x), filter(lambda x: filter_triangles(x) != None, input_data)))
