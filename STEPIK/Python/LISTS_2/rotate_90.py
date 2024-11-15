# put your python code here
a = int(input())
matrix  = []

for m in range(a):
    matrix.append(list(map(lambda x : int(x) , input().split())))

matrix = matrix[::-1]

for m in range(a - 1, -1):
    for n in range(a):
        print(matrix[m][n], end = ' ')
    print()

for m in range(a):
    for n in range(a):
        print(matrix[n][m], end = ' ')
    print()







