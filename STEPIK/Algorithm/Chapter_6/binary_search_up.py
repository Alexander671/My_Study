def binary_search(list, item):
    low = 0
    high = len(list) - 1
    step = 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid + 1
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        step += 1
    return -1

def main():
    a = list(map(int, input().split()))
    n = a[0]
    array_a = a[1:]
    b = list(map(int, input().split()))
    k = b[0]
    array_b = b[1:]
    for i in array_b:
        print(binary_search(array_a, i), end=' ')
if __name__ == "__main__":
    main()

