class Point:
    def __init__(self, x=0, y=0,):
        self._x = x
        self._y = y

def cast_type(_type, values):
    return list(map(_type, values))
    
values = input().split()
try:
    x, y = cast_type(int,values)
    pt = Point(x,y)
except:
    try:
        x, y = cast_type(float,values)
    except:
        pt = Point()
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")