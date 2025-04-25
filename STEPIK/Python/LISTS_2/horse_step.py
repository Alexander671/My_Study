

coor_j = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
coor_i = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
a = input()

letter = coor_j[a[0]]
number = coor_i[a[1]]

matrix  = [['.'] * 8 for _ in range(8)]

matrix[letter][number] = 'N'

x1,y1 = letter, number
for x in range(8):
    for y in range(8):
        if ((abs (x - x1)) == 1 and  (abs (y - y1)) == 2) or ((abs (x - x1)) == 2 and  (abs (y - y1)) == 1) :
            matrix[x][y] = '*'

for m in range(8):
    for n in range(8):
        print(matrix[n][m], end = ' ')
    print()







