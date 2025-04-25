import time

l = list(range(2 ** 25 - 4))

def timeit(func):
    def wrapper(l, obj):
            before = time.time()
            func(l, obj)
            after = time.time()
            print('Time is:', after - before)

    return wrapper

@timeit
def append_one(l:list, obj):
      l.append(obj)
    

append_one(l, 1022)
append_one(l, 1022)
append_one(l, 1022)
append_one(l, 1022)


import sys

data = []
prev_size = sys.getsizeof(data)

for i in range(2000):
    data.append(i)
    new_size = sys.getsizeof(data)
    if new_size != prev_size:
        print(f"Added {i}: Size increased from {prev_size} to {new_size}")
        prev_size = new_size