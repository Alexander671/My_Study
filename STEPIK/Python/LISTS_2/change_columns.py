a = int(input())
matrix  = []

for m in range(a):
    matrix.append(list(map(lambda x : int(x) , input().split())))
    
for m in range(a - 1, -1):
    for n in range(a):
        print(matrix[m][n], end = ' ')
    print()



