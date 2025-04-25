# put your python code here
n = int(input())

matrix = []
for i in range(n):
   
    str = input().split()
    list_m = []
    for j in range(n):
            list_m.append(int(str[j]))
    matrix.append(list_m) 

flag = True


for i in range(n):
    for j in range(n):
        if(matrix[i][j] > n):
            flag = False
            break
           
for i in range(0, n):
    row_number = sorted(matrix[i])
    for j in range(0, len(row_number) - 1):
        if not (row_number[j + 1] - row_number[j] == 1):
            flag = False
            break

matrix = ([[row[i] for row in matrix] for i in range(len(matrix[0]))])

for i in range(0, n):
    row_number = sorted(matrix[i])
    for j in range(0, len(row_number) - 1):
        if not (row_number[j + 1] - row_number[j] == 1):
            flag = False
            break



if flag:
    print('YES')
else:
    print('NO')