from collections import Counter


def count(string):
    
    return dict(Counter(string))


print(count("aba"))