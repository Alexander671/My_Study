res = []
s = input().split()
n = int(input())
i = n
for el in s:
    if res and i % n != 0:
        res[-1].append(el)
    else:
        res.append([el])
    i += 1
print(res)