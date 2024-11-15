# put your python code here
n = int(input())
l = []
for i in range(n):
    s = list(map(lambda x : int(x), input().split()))
    average = sum(s) / len(s)
    l.append(sum(list(map(lambda x : average < x, s))))
    
print(*l, sep = '\n')
