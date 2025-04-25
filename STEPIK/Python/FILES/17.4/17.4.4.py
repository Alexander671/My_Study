# Вам доступен текстовый файл class_scores.txt с оценками
# за итоговый тест на строках вида: фамилия оценка 
# (фамилия и оценка разделены пробелом). 
# Оценка - целое число от 000 до 100100100 включительно.
# 
# Напишите программу для добавления 555 баллов к каждому результату
# теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.
# 
# Формат входных данных
# На вход программе ничего не подается.
# 
# Формат выходных данных
# Программа должна создать файл с именем new_scores.txt 
# в соответствии с условием задачи.
# 
# Примечание 1. Считайте, что исполняемая программа и
#  указанные файлы находятся в одной папке.
# 
# Примечание 2. Если бы файл class_scores.txt содержал строки:
# 
# Washington 83
# Adams 86
# Kingsman 100
# MacDonald 95
# Thomson 98
# 
# то файл new_scores.txt имел бы вид:
# 
# Washington 88
# Adams 91
# Kingsman 100
# MacDonald 100
# Thomson 100

with open('class_scores.txt', 'r') as input, open('new_scores.txt', 'w', encoding='utf-8') as output:

    table = map(lambda x: x.split(), input.readlines())
    for i in table:
        if(int(i[1]) > 95):
            print(f'{i[0]} 100', end = '\n', file=output)
        else:
            print(f'{i[0]} {int(i[1]) + 5}', end = '\n', file=output)
