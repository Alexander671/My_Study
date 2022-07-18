# Вам доступен текстовый файл nums.txt. В файле записано два целых числа,
# они могут быть разделены символами пробела и конца строки. 
# Напишите программу, выводящую на экран сумму этих чисел.
# 
# Формат входных данных
# На вход программе ничего не подается.
# 
# Формат выходных данных
# Программа должна вывести сумму чисел из указанного файла.
# 
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
# 
# Примечание 2. Не забудьте закрыть файл 🙂.
# 
# Примечание 3. Указанный файл можно скачать по ссылке.


file = open('nums.txt', 'r', )

print(sum((map(sum, map(lambda x: map(int, x.split()), file.readlines())))))
file.close()