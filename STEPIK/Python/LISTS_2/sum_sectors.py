# put your python code here
n = int(input())
list_sector = []
sector_sum_1 = 0
sector_sum_2 = 0
sector_sum_3 = 0
sector_sum_4 = 0

for i in range(n):
    s = (list(map(lambda x : int(x), input().split())))
    for j in range(n):
        if ((i > j) and (i < n - 1 - j)):
            sector_sum_1 += s[j]
        if ((i < j) and (i > n - 1 - j)):
            sector_sum_2 += s[j]
        if ((i < j) and (i < n - 1 - j)):
            sector_sum_3 += s[j]
        if ((i > j) and (i > n - 1 - j)):
            sector_sum_4 += s[j]
        
print('Верхняя четверть:', sector_sum_3)
print('Правая четверть:', sector_sum_2)
print('Нижняя четверть:', sector_sum_4)
print('Левая четверть:', sector_sum_1)



