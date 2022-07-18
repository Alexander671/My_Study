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

list1 = list(map(lambda x: int(x), input().split()))

n = list1[0]
m = list1[1]

matrix_1 = []
matrix_2 = []

for i in range(n):
    str = input().split()
    list_m = []
    for j in range(m):
            list_m.append(int(str[j]))
    matrix_1.append(list_m) 

input()

list2 = list(map(lambda x: int(x), input().split()))

m1 = list2[0]
k = list2[1]

for i in range(m1):
    str = input().split()
    list_m = []
    for j in range(k):
            list_m.append(int(str[j]))
    matrix_2.append(list_m) 

print(*matrix_1)
print(*matrix_2) 

for i in range(k):
    print(*matrixmult(matrix_1, matrix_2)[i])   


