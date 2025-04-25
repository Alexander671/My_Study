class Ball(object):
    def __init__(self, type = "regular"):
        self.ball_type = type
    def __repr__(self):
        return repr("__repr__")
    def __str__(self):
        return "__str__"


ball1 = Ball()
ball1
ball2 = Ball("super")
print(ball2)

print(str(ball1.ball_type))  #=> "regular"
print(str(ball2.ball_type))  #=> "super"