# Напишите программу, которая с помощью модуля random моделирует броски монеты.
# Программа принимает на вход количество попыток и выводит результаты бросков:
# Орел или Решка (каждое на отдельной строке).
# Примечание. Например, при n=7n=7n=7 ваша программа может выводить:
# Орел
# Решка
# Решка
# Орел
# Орел
# Орел
# Решка

from random import *

n = int(input())    # количество попыток

for i in range(n):
    if (randint(i, n)) % 2 == 0:
        print('Орел')
    else:
        print('Решка')



