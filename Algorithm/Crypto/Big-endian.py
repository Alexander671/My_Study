
n = int(input())
n = bin(n)[2:]

addition_to28 = "0" * (28-len(n))

n = addition_to28 + n
new_list = []
for i in range(4):
    new_list.extend(n[i*7:(i+1)*7][::-1])

print(*new_list[::-1], sep="")


# 1111111 1111111 1111110 1101001
# 1101001 1111110 1111111 1111111