# put your python code here
s = input()
s_set = set(s)
if sorted(list(s_set)) == sorted(s):
    print('YES')
else:
    print('NO')
