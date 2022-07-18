class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color
points = [Point(1,1), Point(3,3,'yellow')] + [Point(i,i) for i in range(5, 2000, 2)]
print(points)
    