# put your python code here

s = input()
s1 = input()

if sorted(set(s + s1)) == ['0','1','2','3','4','5','6','7','8','9']:
    print('YES')
else:
    print('NO')

