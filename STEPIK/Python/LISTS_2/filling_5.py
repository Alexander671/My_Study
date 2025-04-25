list = list(map(lambda x: int(x), input().split()))

x = list[0]
y = list[1]

matrix = [[0] * y for _ in range(x)]
first_row = []

for i in range(y):
    first_row.append(i + 1)
    print(first_row[i], end = ' ')

print()

for i in range(x - 1):
    first_row = first_row + [first_row[0]]
    del first_row[0]
    print(* first_row, sep = ' ')