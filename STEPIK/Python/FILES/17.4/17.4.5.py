# Загадка от Жака Фреско 🌶️
# 
# Однажды Жака Фреско спросили:
# 
# "Если ты такой умный, почему не богатый?"
# 
# Жак не стал отвечать на столь провокационный вопрос, 
# вместо этого он задал загадку спрашивающему:
# 
# "Были разноцветные козлы. Сколько?"
# 
# "Сколько чего?"
# 
# "Сколько из них составляет более 7% от общего количества козлов?"
# 
# Вам доступен текстовый файл goats.txt в первой строке 
# которого написано слово COLOURS, далее идет список всех 
# возможных цветов козлов. Затем идет строка со словом GOATS, 
# и далее непосредственно перечисление козлов разных цветов. 
# Перечень козлов включает только строки из первого списка.
# 
# Напишите программу создания файла answer.txt и вывода в него списка козлов,
# которые удовлетворяют условию загадки от Жака Фреско.
# 
# Формат входных данных
# На вход программе ничего не подается.
# 
# Формат выходных данных
# Программа должна создать файл с именем answer.txt и вывести 
# в него в алфавитном порядке названия цветов козлов, 
# которые удовлетворяют условию загадки Жака Фреско.
# 
# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
# 
# Примечание 2. Если бы файл goats.txt содержал строки:
# 
# COLOURS
# Pink goat
# Green goat
# Black goat
# GOATS
# Pink goat
# Pink goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Green goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# 
# то файл answer.txt имел бы вид:
# 
# Black goat
# Pink goat

# with open('goats.txt', 'r') as input, open('answer.txt', 'w', encoding='utf-8') as output:
#     dict = {}
#     table = map(lambda x: x.split(), input.readlines())
#     for i in table:
#         if(len(i) > 1):
#             dict.setdefault(i[0], -1) 
#             dict[i[0]] += 1 
#     bigger_7 = list(map(lambda y: (y[0], (y[1] / sum(dict.values()) * 100) > 7), dict.items()))
#     x = sorted(map(lambda x: x[0], filter(lambda x:x[1] == True, bigger_7)))
#     y = list(map(lambda x: x + ' goat\n', x))
#     output.writelines(y[:-1] + [(y[-1][:-1])])
# 

with open('goats.txt') as fin, open('answer.txt', 'w') as fout:
    colors, total = {}, 0
    for line in fin:
        if line not in ('COLOURS\n', 'GOATS\n'):
            colors[line] = colors.get(line, -1) + 1
            total += 1
    [fout.write(k) for k in colors if colors[k] >= total * .07]
