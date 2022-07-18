# put your python code here
a = int(input())
b = int(input())
maximum = -100
max_i = 0
max_j = 0
for i in range(a):
    s = list(map(lambda x : int(x), input().split()))

    for j in range(b):
        if(s[j] > maximum):
            maximum = s[j]
            max_i = i
            max_j = j
print(max_i, max_j)
