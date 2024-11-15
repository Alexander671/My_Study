# put your python code here
def rotate(a, matrix):
            # put your python code here

    matrix = matrix[::-1]

    for m in range(a - 1, -1):
        for n in range(a):
            print(matrix[m][n], end = ' ')
        print()
    return matrix


n = int(input())
matrix = []
for i in range(n):
    list = input().split()
    matrix.append(list)

matrix = rotate(n,matrix)
    
flag = True
for i in range(n):
    for j in range(n):
        if not (matrix[i][j] == matrix[j][i]):
            flag = False
            break
if flag:
    print('YES')
else:
    print('NO')



