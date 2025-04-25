from bitcoin import hex_to_b58check

f = open('text_base58.txt')
xs = []
for line in f:
    if len(hex(int((line[16:])[:-1], 2))[2:]) % 2 == 0:
        xs.append(hex_to_b58check(hex(int((line[16:])[:-1], 2))[2:]))
    else:
        xs.append(hex_to_b58check('0' + hex(int((line[16:])[:-1], 2))[2:]))
        

ys = []
for i in xs:
    ys.extend(i)



d = {}
for i in ys:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i]=1

sorted_tuples = sorted(d.items(), key=lambda item: item[1])

sorted_dict = {k: v for k, v in sorted_tuples}
x = (list(sorted_dict.keys()))[-1]
y = (list(sorted_dict.keys()))[-2]
print(x,y)
if x == '1':
    y
else:
    x
