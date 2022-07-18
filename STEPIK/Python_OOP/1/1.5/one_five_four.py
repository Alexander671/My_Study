class Line:
    def __init__(self, a, b, c, d):
        self.sp, self.ep = (a,b), (c,d)

elements = [Line(1,1,1) for i in range(217)]
        