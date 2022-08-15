class Furniture:
    def __init__(self, name, weight) -> None:
        self.__verify_name(name)
        self.__verify_weight(weight)
        
        self._name = name
        self._weight = weight
        

    def __verify_name(self, name): # - для проверки корректности имени;
        if not type(name) == str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight): # - для проверки корректности веса.
        if not (weight > 0):
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self):
        return tuple(self.__dict__.values())
        
class Closet(Furniture): # - для представления шкафов;
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

class Chair(Furniture): # - для представления стульев;
    def __init__(self, name, weight, height):
        super().__init__(name, weight,)
        self._height = height
        
class Table(Furniture): # - для представления столов.
    def __init__(self, name, weight,height, square):
        super().__init__(name, weight,)
        self._height = height
        self._square = square
