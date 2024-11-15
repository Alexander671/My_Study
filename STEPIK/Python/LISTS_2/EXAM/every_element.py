# put your python code here
str = input().split()
n = int(input())

array_every = []
for i in range(0, n):
    array_every.append((str[i:])[::n])



print(array_every)