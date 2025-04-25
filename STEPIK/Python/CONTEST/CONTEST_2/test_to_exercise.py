

n = input()
sum = 0
for i in n:
    sum += int(i)


def digits_number(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count

print(sum + digits_number(int(n)))