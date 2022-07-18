list = list(map(lambda x: int(x), input().split()))

x = list[0]
y = list[1]


for i in range(x):
    for j in range(y):
        if(i % 2 == 0):
            print(y * i + (j + 1) , end = ' ')
        else:
            print(y * (i + 1) - j, end = ' ')
    print()