# Как известно, математики странные люди. 
# Не составляет исключения и Тимур — автор данного курса. 
# Каждый день Тимур решает ровно две сложные математические задачи.
# Решая первую задачу, он записывает на первом листочке все числа, которые в ней встречаются.
# Далее он делает паузу и берется за вторую задачу.
# Затем записывает на втором листочке все числа, которые в ней встречаются.
# После этого он берет еще один листок и выписывает на него все совпадающие числа из первых двух листочков. 
# Если такие числа есть, день удался, если общих чисел нет, Тимур считает день неудачным.
# Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏
# Формат входных данных
# На вход программе подаются две строки с числами: в первой строке числа с первого листочка, во второй со второго.
# Формат выходных данных
# Программа должна вывести числа, встретившиеся на обоих листках в отсортированном по убыванию
# порядке, либо словосочетание BAD DAY, если таких чисел нет.

list1 = set(input().split())
list2 = set(input().split())


if list1 & list2 == set():
    print('BAD DAY')
else:
    list1_list2 = list(map(lambda x : int(x), list(list1 & list2)))
    print(*(sorted(list1_list2, reverse = True)))

