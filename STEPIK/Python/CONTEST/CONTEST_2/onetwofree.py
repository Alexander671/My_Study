
from math import log

n = int(input())

x1 = 0
x2 = 0

c1 = 0
c2 = 0

list_ = [int(i * '9') for i in range(1,51)]
for a, b, c in zip(range(1,51), [10 ** i * 9 for i in range(0,50)], list_):
    x2 = a * b
    c2 = c
    if x1 <= n and n <= x2:
        range_ = ((x1,x2),(c1,c2))
        break
    else:
        x1 = x2
        c1 = c

print("".join(list(map(lambda x : str(x)[::-1], range(*range_[1]))))[n - range_[1][0]])
