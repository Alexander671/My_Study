# put your python code here
s1 = input().lower()
s2 = input().lower()

s1_result = []
s2_result = []

for i in s1:
    if i in 'abcdefghijklmnopqrstuvwxyz0123456789яфйцычсвукамипенртьогшлбюдщзжэхъ':
        s1_result.append(i)

for i in s2:
    if i in 'abcdefghijklmnopqrstuvwxyz0123456789яфйцычсвукамипенртьогшлбюдщзжэхъ':
        s2_result.append(i)

if sorted(s2_result) == sorted(s1_result):
    print('YES') 
else: print('NO')


