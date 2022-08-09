class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, key):
        return_value = self.coords[key]
        if type(key) == slice:
            return tuple(return_value)
        else:
            return return_value

    def __setitem__(self, key, value):
        self.coords[key] = value

v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
print(v[::2] )
v[0] = 10.5