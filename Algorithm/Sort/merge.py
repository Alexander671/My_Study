def merge_sort(a, left_index, right_index):
    if left_index >= right_index:
        return a

    middle = (left_index + right_index)//2
    merge_sort(a, left_index, middle)
    merge_sort(a, middle + 1, right_index)
    merge(a, left_index, middle, right_index)

def merge(a, left_index, middle, right_index):
    
    # создаем левую и правую копии массива
    left_copy = a[left_index:middle + 1]
    right_copy = a[middle+1:right_index+1]

    # Начальные значения для переменных
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Проходим обе копии, пока не закончатся элементы в одной из
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # Если у нашей left_copy есть меньший элемент, 
        # поместите его в отсортированную часть, 
        # а затем двигайтесь вперед в left_copy (увеличивая указатель)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            a[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # наоборот
        else:
            a[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Независимо от того, откуда мы взяли наш элемент
        # двигаться вперед в отсортированной части
        sorted_index = sorted_index + 1

    # У нас закончились элементы либо в left_copy, либо в right_copy.
    # поэтому мы пройдемся по оставшимся элементам и добавим их 
    while left_copy_index < len(left_copy):
        a[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        a[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

a = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(a, 0, len(a))
print(a)