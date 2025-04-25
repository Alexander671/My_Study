d = dict([('foo', 100), ('bar', 200), ('baz', 300)])
print(type(d))
d = dict(foo=100, bar=200, baz=300)
print(type(d))

d = {'foo': 100, 'bar': 200, 'baz': 300}
print(type(d))

d = {('foo', 100), ('bar', 200), ('baz', 300)}
print(type(d))

d = {}
d['foo'] = 100
d['bar'] = 200
d['baz'] = 300 
print(type(d))
