def log(x):
    print("Logger!")
    x(5)

@log
def func(x):
    print(x + 5)


class Car():
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

car = Car(color='green', speed=150)
print(car.speed)



class CoffeeShop:
    specialty = 'espresso'
    
    def __init__(self, coffee_price):
        self.coffee_price = coffee_price
    
    # instance method
    def make_coffee(self):
        print(f'Making {self.specialty} for ${self.coffee_price}')
    
    # static method    
    @staticmethod
    def check_weather():
        print('Its sunny')

    # class method
    @classmethod
    def change_specialty(cls, specialty):
        cls.specialty = specialty
        print(f'Specialty changed to {specialty}')

cofshop = CoffeeShop('5')
cofshop.make_coffee()
cofshop.change_specialty('copuchino')
cofshop.check_weather()
cofshop.make_coffee()


def func():
    print("Hello")
    return 5

print(func)
print(func())

def add_three(x):
    return x + 3
li = [1,2,3]
list_data = [i for i in map(add_three, li)]
print(list_data)


from functools import reduce
def add_three(x,y):
    return x + y
li = [1,2,3,5]
reduce(add_three, li)


def add_three(x):
    if x % 2 == 0:
        return True        
    else:
        return False
li = [1,2,3,4,5,6,7,8]
new_listdata = [i for i in filter(add_three, li)]
print(new_listdata)


name = 'chr'
def add_chars(s):
    s += 'is'
    print(s)
    
add_chars(name)    
print(name)