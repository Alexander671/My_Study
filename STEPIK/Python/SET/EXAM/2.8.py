# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику,
# либо информатику, либо оба этих предмета. У руководителя школы есть списки изучающих каждый предмет.
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.
# Формат входных данных
# На вход программе в первых двух строках подаются числа mmm и nnn – количества учеников,
# изучающих математику и информатику соответственно. Далее идут mmm строк — фамилии учеников,
# которые изучают математику и nnn строк с фамилиями учеников, изучающих информатику.
# Формат выходных данных
# Программа должна вывести количество учеников, которые изучают только один предмет.
# Если таких учеников не окажется, то необходимо вывести NO.
# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.



math = int(input())
info = int(input())

list_student_math = []
list_student_info = []

for i in range(math):
    stud = input()
    list_student_math.append(stud)

for i in range(info):
    stud = input()
    list_student_info.append(stud)

print(math - len((set(list_student_info)) & set(list_student_math)))

