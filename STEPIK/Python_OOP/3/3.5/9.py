class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_mass(self):
        return self.ro * self.volume

    def __eq__(self, __o: object) -> bool:
        if type(__o) in (int, float):
            return self.get_mass() == __o
        else:
            return self.get_mass() == __o.get_mass()
    
    # <
    def __lt__(self, __o: object) -> bool:
        if type(__o) in (int, float):
            return self.get_mass() < __o
        else:
            return self.get_mass() < __o.get_mass()
    
    # <=
    def __le__(self, __o: object) -> bool:
        if type(__o) in (int, float):
            return self.get_mass() <= __o
        else:
            return self.get_mass() <= __o.get_mass()
    
b1 = Body('', 15, 80)
b2 = Body('', 10, 120)

print(b1 == b2)
