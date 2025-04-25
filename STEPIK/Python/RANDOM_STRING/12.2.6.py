# put your python code here
import random
def random_row():
    return( [random.randint(1,75) for i in range(25)])

m = random_row()
m[12] = 0

for i in range(25):
    if (i % 5 == 0):
        print()
        print(str(m[i]).ljust(3), end ='')
    else:
        print(str(m[i]).ljust(3), end ='')

