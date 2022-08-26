# В программе вводятся два значения в одну строчку через пробел.
# Значениями могут быть числа, слова, булевы величины (True/False).
# Необходимо прочитать эти значения из входного потока.
# Если оба значения являются числами,
# то вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк).
# Результат вывести на экран (в блоке finally).

def cast_type(_type, values):
    return list(map(_type, values))
    
values = input().split()
try:
    x, y = cast_type(int,values)
except:
    try:
        x, y = cast_type(float,values)
    except:
        x, y = cast_type(str,values)
finally:
    print(x + y)