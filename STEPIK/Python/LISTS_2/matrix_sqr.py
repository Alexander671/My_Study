def matrixmult(m1,m2):
    r=[]
    m=[]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums=0
            for k in range(len(m2)):
                sums=sums+(m1[i][k]*m2[k][j])
            r.append(sums)
        m.append(r)
        r=[]
    return m

n = int(input())


matrix_1 = []
matrix_2 = []

for i in range(n):
    str = input().split()
    list_m = []
    for j in range(n):
            list_m.append(int(str[j]))
    matrix_1.append(list_m) 

sqr_n = int(input())

matrix_sqr = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if (i == j):
            matrix_sqr[i][j] = 1
        

for i in range(sqr_n):
    matrix_sqr = matrixmult(matrix_sqr, matrix_1)   

for i in range(n):
    print(*matrix_sqr[i])