# На вход программе подается строка, содержащая строки-идентификаторы. 
# Напишите программу, которая исправляет их так, 
# чтобы в результирующей строке не было дубликатов. Для этого необходимо
# прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз,
# сколько такой идентификатор уже встречался.
# Формат входных данных
# На вход программе подается строка текста, содержащая строки-идентификаторы, 
# разделенные символом пробела.
# Формат выходных данных
# Программа должна вывести исправленную строку, не содержащую дубликатов 
# сохранив при этом исходный порядок.

s = input().split()


result = {}
for num in range(len(s)):
    if(s[:num].count(s[num]) != 0):
        n = s[:num].count(s[num])
        print(s[num] + '_' + str(n), end = ' ')
    else:
        print(s[num], end = ' ')
    