# i + j == n -1 # значит заполняем 1
# i +j >= n # значит заполняем 2
# остальное заполняем 0

n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i + j == n - 1):
            matrix[i][j] = 1
        if (i + j >= n):
            matrix[i][j] = 2
        print(matrix[i][j], end = ' ')
    print()