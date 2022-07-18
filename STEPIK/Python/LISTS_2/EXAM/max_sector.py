# put your python code here
n = int(input())

matrix_1 = []
for i in range(n):
   
    str = input().split()
    list_m = []
    for j in range(n):
            list_m.append(int(str[j]))
    matrix_1.append(list_m) 


list_sector = []
for i in range(n):
    for j in range(n):
        if(i > n - j - 1):
            list_sector.append(matrix_1[i][j])

print(max(list_sector))
