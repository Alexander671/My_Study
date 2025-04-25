def qsort(array):
    if len(array) < 2: 
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        
        great = [i for i in array[1:] if i > pivot]
        
        return qsort(less) + [pivot] + qsort(great)

print(qsort([1,2,8,6,4,5]))