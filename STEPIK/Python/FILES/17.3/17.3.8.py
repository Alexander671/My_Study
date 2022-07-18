# Вам доступны два текстовых файла first_names.txt и last_names.txt,
# один с именами, другой с фамилиями.
# 
# Напишите программу, которая c помощью модуля random создает 3
# случайные пары имя + фамилия, а затем выводит их,
# каждую на отдельной строке.
# 
# Формат входных данных
# На вход программе ничего не подается.
# 
# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.


from random import choice

with open('first_names.txt', 'r') as file1, open('last_names.txt', 'r') as file2:
    lines1 = list(map(lambda x: x.strip('\n'), file1.readlines()))
    lines2 = list(map(lambda x: x.strip('\n'), file2.readlines()))
    for i in range(3):
        print(lines1[i], lines2[i])
    
       