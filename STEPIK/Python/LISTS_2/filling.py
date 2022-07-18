list = list(map(lambda x: int(x), input().split()))

x = list[0]
y = list[1]

for i in range(1, x * y + 1):
    if(i % y == 0):
        print(i, end = ' ')
        print()
    else:
        print(i, end = ' ')