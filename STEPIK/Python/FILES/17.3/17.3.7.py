# Вам доступен текстовый файл file.txt, набранный латиницей.
# Напишите программу, которая выводит количество букв латинского алфавита,
# слов и строк. Выведите три найденных числа в формате, приведенном в примере.
# 
# Формат входных данных
# На вход программе ничего не подается.
# 
# Формат выходных данных
# Программа должна вывести три найденных числа в формате, 
# приведенном в примере.
# 
# Примечание 1. Если бы файл file.txt содержал строки:
# 
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# 
# то результатом было бы:
# 
# Input file contains:
# 108 letters 
# 20 words 
# 4 lines 
# 
# Примечание 2. Словом называется последовательность из непробельных символов.
# Например, строка:
# 
# abc a21 67pop    qwert bo7ok 83456
# 
# содержит 6 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

from re import findall
with open('file.txt', 'r', encoding='utf-8') as file:
    lines = list(map(lambda x: x.strip('\n'), file.readlines()))
    lines_only_letters = [findall(r'[a-zA-Z]', line) for line in lines]
    alphabet = sum(map(len, lines_only_letters))
    string = len(lines)
    words = sum(map(lambda x: len(x.split()) ,lines))
    print(f'''Input file contains:
{alphabet} letters 
{words} words 
{string} lines ''')
        

