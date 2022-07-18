n = int(input())
list_sector = []
for i in range(n):
    s = (list(map(lambda x : int(x), input().split())))
    for j in range(n):
        if (i >= j):
            list_sector.append(s[j])
print(max(list_sector))
