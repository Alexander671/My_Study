class Aircraft:
    def __init__(self, model, mass, speed, top):
        self.verify_types(model, mass, speed, top)
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def verify_types(self, model, mass, speed, top):
        for i in [mass, speed, top]:
            self.verify_positive(i)
        if not type(model) == str:
            raise TypeError('неверный тип аргумента')


    def verify_positive(self, number):
        if type(number) == int or type(number) == float:
            if number < 0:
                raise TypeError('неверный тип аргумента')
        else:
            raise TypeError('неверный тип аргумента')

    def verify_str(self, string):
        if type(string) != str:
            raise TypeError('неверный тип аргумента')

    def verify_int(self, number):
        if type(number) == int:
            if number < 0:
                raise TypeError('неверный тип аргумента')
        else:
            raise TypeError('неверный тип аргумента')

class PassengerAircraft(Aircraft): # - пассажирский самолет;
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top,)
        self.verify_int(chairs)
        self._chairs = chairs


class WarPlane(Aircraft): # - военный самолет.
    def __init__(self, model, mass, speed, top, weapons:dict):
        super().__init__(model, mass, speed, top,)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')

        map(lambda x: self.verify_positive(x), (weapons.values()))
        map(lambda x: self.verify_str(x), (weapons.keys()))
        
        self._weapons = weapons



obj1 = PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140)
obj2 = PassengerAircraft('SuperJet', 1145, 8640, 11034, 80)
obj3 = WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10})
obj4 = WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
planes = [obj1, obj2, obj3, obj4]