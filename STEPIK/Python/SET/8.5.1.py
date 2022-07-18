# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
# Формат входных данных
# На вход программе в первой строке подается число nnn – общее количество слов. Далее идут nnn строк с словами.
# Формат выходных данных
# Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.

n = int(input())

unique_char =[]
for i in range(n):
    unique_char.append(len(set(input().lower())))

print(*unique_char, sep = '\n')