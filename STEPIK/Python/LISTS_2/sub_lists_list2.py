# Sample Input 4:
#
#1 2 3 0
#
#
#Sample Output 4:#
#
#[[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']]

res = [[]]
s = input().split()
n = len(s)
n1 = n
for j in range(1, n + 1):
    n1 -= 1
    for i in range(len(s) - j + 1):
        res.append(s[i : i + j])

print(res)