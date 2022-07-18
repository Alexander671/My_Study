# объявляем функцию Фибоначчи
def fibonacci(n):
    result = [0] # создаём нулевой элемент
    fib1 = 0
    fib2 = 1
    while n > 1: # цикл, который находит все четные
                  # числа последовательности
        fib1, fib2 = fib2, fib1 + fib2
        if (fib2 % 2 == 0):
            result.append(fib2)
            n -= 1 # если нашли четное, уменьшили на 1
    return(result)

x = int(input())
print(*fibonacci(x)[:x], sep = ',') # срез


# --------------------------------------------------------
# проверка равенства
# длины результирующего списка числу n
def test1(x):
    return len(fibonacci(x)[:x]) == x

# проверка на отрицательные числа не проводилась, 
# так как область определния фунции натуральные числа
test_result1 = test1(5) and test1(10) and test1(12) and test1(0)
print(test_result1)


# --------------------------------------------------------
# проверка на условие четности всех чисел
def test2(x):
    return all(lambda x: x % 2 == 0 for i in fibonacci(x))

# проверка на отрицательные числа не проводилась, 
# так как область определния фунции натуральные числа
test_result2 = test2(5) and test2(10) and test2(12) and test2(0)
print(test_result2)


# дополнительное свойство из множества свойств ряда Фибоначчи
# которые могут быть проверены
# Натуральное число N является числом Фибоначчи тогда и только тогда,
# когда 5 * N ^ 2 + 4;
# или   5 * N ^ 2 − 4
# является квадратом.

from math import sqrt
def test3(x):
    n = fibonacci(x + 1)[x - 1]
    n_2 = n * n
    condition_1 = sqrt(5 * n_2 + 4)
    condition_2 = sqrt(abs(5 * n_2 - 4))
    return condition_1.is_integer() or condition_2.is_integer()

x = 4

test_result3 =test3(4) and test3(5) and test3(10) and test3(200) and test3(0)
print(test_result3)
