list = list(map(lambda x: int(x), input().split()))

x = list[0]
y = list[1]

matrix_1 = []
matrix_2 = []
matrix_r = [[0] * y for _ in range(x)]
for i in range(x):
    str = input().split()
    list_m = []
    for j in range(y):
            list_m.append(int(str[j]))
    matrix_1.append(list_m) 

input()

for i in range(x):
    str = input().split()
    list_m = []
    for j in range(y):
            list_m.append(int(str[j]))
    matrix_2.append(list_m) 


for i in range(x):
    for j in range(y):
        matrix_r[i][j] = matrix_1[i][j] + matrix_2[i][j]

for i in range(x):
    print(*matrix_r[i])