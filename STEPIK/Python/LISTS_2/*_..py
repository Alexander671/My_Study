# put your python code here
list = list(map(lambda x: int(x), input().split()))

x = list[0]
y = list[1]


print(x, y)

for i in range(x):
    for j in range(y):
        if(i % 2 == 0):
            if(j % 2 == 0):
                print('.', end = ' ')
            else:
                print('*', end = ' ')
        else:
            if(j % 2 == 0):
                print('*', end = ' ')
            else:
                print('.', end = ' ')
        
    print()