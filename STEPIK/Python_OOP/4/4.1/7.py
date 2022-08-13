class Singleton:
    flag_implemented = None
    def __new__(cls, *args):
        if not cls.flag_implemented:
            cls.flag_implemented = super().__new__(cls)
        return cls.flag_implemented
        
class Game:
    flag_implemented = None
    def __init__(self, name) -> None:
        if 'name' not in self.__dict__:
            self.name = name    
    
    def __new__(cls, *args):
        if not cls.flag_implemented:
            cls.flag_implemented = super().__new__(cls)
        return cls.flag_implemented
    



g = Game("1")
g1 = Game("2")

print(g.name)
print(g1.name)

