n = int(input())

trib_list = [1,1,1]
for i in range(3, n):
    trib_list.append(trib_list[-1] + trib_list[-2] + trib_list[-3])

print(*trib_list[:n])
