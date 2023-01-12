

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    step = 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return (mid, step + 1)
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        step += 1
    return None



test1 = binary_search([1,2,3], 2)
test2 = binary_search([1,2,3,3,4,5,5,5,5,6,7,8,8,8,8,8,12], 6)

print(test1, test2)        