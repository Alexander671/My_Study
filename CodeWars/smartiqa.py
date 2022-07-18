class Soda():
    def __init__(self, added: str=None):
        self.added = added
    
    def show_my_drink(self):
        if self.added:
            return f'ГАЗИРОВКА и {self.added}'
        else:
            return 'Обычная газировка'

drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
print(drink1.show_my_drink())
print(drink2.show_my_drink())
print(drink3.show_my_drink())
print()

class TriangleChecker():
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        if not isinstance(self.a, (int,float)) or not isinstance(self.b, (int,float)) or not isinstance(self.c, (int,float)):        
            return "Нужно вводить только числа"

        if self.a < 0 or self.b < 0 or self.c < 0:
            return "С отрицательными числами ничего не выдйет!"

        if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            return "Жаль, но из этого треугольник не сделать!"

        return "Ура, можно построить треугольник!"


triangle1 = TriangleChecker(1)
triangle2 = TriangleChecker('малина')
triangle3 = TriangleChecker(1,2,3)

triangle4 = TriangleChecker(3,4,5)
triangle5 = TriangleChecker(1,1,5)
triangle6 = TriangleChecker(1.2,2,3)

print(triangle1.is_triangle())
print(triangle2.is_triangle())
print(triangle3.is_triangle())
print(triangle4.is_triangle())
print(triangle5.is_triangle())
print(triangle6.is_triangle())



class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg
    def to_pounds(self):
        return self.__kg * 2.205
    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
    
    def get_kg(self):
        return self.__kg 