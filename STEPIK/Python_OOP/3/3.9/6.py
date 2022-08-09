class Square:
    def __init__(self, side=0):
        self.side = side
        
class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square
        self.width = self.square.side
        self.height = self.square.side


x = Square(2)
y = x.side
a = SquareToRectangleAdapter(x)
x.side = 10
print(a.height)


