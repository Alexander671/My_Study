# put your python code here
n = int(input())
matrix = []
for i in range(n):
    list = input().split()
    matrix.append(list)

for i in range(n):
    print(*[[row[i] for row in matrix] for i in range(len(matrix[0]))][i])




