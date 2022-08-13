class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def get_info(self,):
        attritubes = ", ".join(map(str, (list(self.__dict__.values())[2:])))
        return f"{self.name}: {self.old}, {attritubes}"

class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

class Cat(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

c = Cat("пирожок", 3, "полосатый", 4.5)

print(c.get_info())