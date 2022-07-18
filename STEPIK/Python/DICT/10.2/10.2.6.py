#   На мобильных кнопочных телефонах текстовые сообщения можно отправлять 
# с помощью цифровой клавиатуры. Поскольку с каждой клавишей связано
# несколько букв, для большинства букв требуется несколько нажатий клавиш.
# При однократном нажатии цифры генерируется первый символ, указанный для
# этой клавиши.
# 1 	.,?!:
# 2 	ABC
# 3 	DEF
# 4 	GHI
# 5 	JKL
# 6 	MNO
# 7 	PQRS
# 8 	TUV
# 9 	WXYZ
# 0 	space (пробел)
# 
#   Напишите программу, которая отображает нажатия клавиш, 
# необходимые для введенного сообщения.
# Формат входных данных
#   На вход программе подается одна строка – текстовое сообщение.
# Формат выходных данных
#   Программа должна вывести нажатия клавиш, необходимых для введенного сообщения.
# Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные буквы.
# Примечание 2. Ваша программа должна игнорировать любые символы,
#               не указанные в приведенной выше таблице.
# Примечание 3. Nokia 3310, чтобы вспомнить как это было 😄

d={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
    "A":'2', "B":'22', "C":'222',
    "D":'3', "E":'33', "F":'333',
    "G":'4', "H":'44', "I":'444',
    "J":'5', "K":'55', "L":'555',
    "M":'6', "N":'66', "O":'666',
    "P":'7', "Q":'77', "R":'777', "S": '7777',
    "T":'8', "U":'88', "V":'888',
    "W":'9', "X":'99', "Y":'999', "Z": '9999',
    " ":'0'
}

s = input().upper()

for i in s:
    if not (i == '"'):
        print(d[i], end = '')