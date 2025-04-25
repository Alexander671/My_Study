def qsort(array):
    if len(array) < 2: 
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        
        great = [i for i in array[1:] if i > pivot]
        
        return qsort(less) + [pivot] + qsort(great)

def main():
    a = list(map(int, input().split()))
    n = a[0]
    array_a = a[1:]
    b = list(map(int, input().split()))
    k = b[0]
    array_b = b[1:]
    for i in array_b:
        print(qsort(array_a), end=' ')
if __name__ == "__main__":
    main()