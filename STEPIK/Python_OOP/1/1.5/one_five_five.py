class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def is_triangle(self):
        a = self.a
        b = self.b
        c = self.c
        
        if any(map(lambda x : not (isinstance(x, int) or isinstance(x, float)), [a,b,c])):
            return 1
        elif any(map(lambda x : x <= 0, [a,b,c])):
            return 1
        elif a + b < c or b + c < a or a + c < b:
            return 2
        else:
            return 3
a, b, c = map(int, input().split())


tr = TriangleChecker(a, b, c)
print(tr.is_triangle())