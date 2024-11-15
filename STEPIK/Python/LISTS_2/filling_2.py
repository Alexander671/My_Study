list = list(map(lambda x: int(x), input().split()))

x = list[0]
y = list[1]

matrix = [[0] * y for _ in range(x)]


for i in range(y):
    for j in range(x):
        matrix[j][i] = i * x + (j + 1)

for i in range(x):
    for j in range(y):
        print(matrix[i][j], end = ' ')
    print()