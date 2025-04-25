# put your python code here
import functools
s = list(map(lambda x: sorted(set(x)), input().split()))

if(all(list(map((lambda x: x == s[0]), s)))):
    print('YES')
else:
    print('NO')

