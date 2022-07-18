# Напишите программу для определения общего количества различных слов в строке текста.
# Формат входных данных
# Nа вход программе подается строка текста.
# Формат выходных данных
# Программа должна вывести одно число – общее количество различных слов в строке без учета регистра.
# Примечание 1. Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним или большим числом пробелов.
# Примечание 2. Знаками препинания .,;:-?! пренебрегаем.

n = list(input().lower())

punct = '.,;:-?!'

for i in n:
    for j in punct:
        if (i == j):
            n.remove(i)

print(len(set(''.join(n).split())))