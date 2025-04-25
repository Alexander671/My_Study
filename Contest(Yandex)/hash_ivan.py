from functools import lru_cache

m = int(input()) - 1

s = set(map(int, input().split()))

hashes = set()


@lru_cache(maxsize=None)
def func(m):
    while True:
        m += 1
        for i in s:
            mod_result = i % m
            if not (mod_result in hashes):
                hashes.add(mod_result)
            else:
                hashes.clear()
                break
            
        else:    
            print(m)
            break

func(m)
