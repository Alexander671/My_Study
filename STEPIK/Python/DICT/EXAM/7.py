
def merge(values):      
    result = {}
    for v in values:
        for key, value in v.items():
            result.setdefault(key, []).append(value)
    for key,value in result.items():
        result[key] = set(value)
    return result


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])

print(result)
