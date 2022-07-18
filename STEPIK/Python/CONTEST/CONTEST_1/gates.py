# Безумный ученый изобрел машину времени, подключив микроволновку к телефону,
# и с помощью этого телефона отправляет письма в прошлое.
# Однако она получилась настолько ужасной, 
# что мало того что в отправленном сообщении могут перемешиваться символы,
# так еще и добавляется один лишний. Но, если вы найдете этот символ,
# быть может, неисправность будет обнаружена? 
# 
# Напишите программу, которая находит лишний символ в измененном сообщении.
# 
# Формат входных данных
# На вход программе подаются две строки – исходная и измененная,
# в которой добавлен один лишний символ. Длины строк не превышают 45000 символов.
# 
# Формат выходных данных
# Программа должна найти лишний символ во второй строке и вывести его.

str1 = input() + '  '
str2 = input()

def gates(str1,str2):
    for j in str2:
        if(j not in str1 ):
            return(j)
            
    for i, j in zip(str1, str2):
        if  (i != j):
            return(j)

print(gates(str1,str2))