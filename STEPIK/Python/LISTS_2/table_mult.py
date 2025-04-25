# put your python code here
a = int(input())
b = int(input())
matrix = [[0] * b for _ in range(a)]
for i in range(a):
    for j in range(b):
        matrix[i][j] = i * j
    print(*matrix[i])
