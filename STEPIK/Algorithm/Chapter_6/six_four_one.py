#Задача на программирование: число инверсий
# 
# 
# Первая строка содержит число 1≤n≤1051≤n≤105, вторая — массив A[1…n]A[1…n],
# содержащий натуральные числа, не превосходящие 109109. 
# Необходимо посчитать число пар индексов 1≤i<j≤n1≤i<j≤n, для которых A[i]>A[j]A[i]>A[j].
# (Такая пара элементов называется инверсией массива.
# Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: 
# например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве,
# упорядоченном по убыванию, инверсию образуют каждые два элемента.)

def merge_sort(a, left_index, right_index, inverses=0):
    if left_index >= right_index:
        return inverses

    middle = (left_index + right_index)//2
    inverses_1 = merge_sort(a, left_index, middle, inverses)
    inverses_2 = merge_sort(a, middle + 1, right_index, inverses)
    inverses_sum = merge(a, left_index, middle, right_index, inverses=inverses_1 + inverses_2)
    return inverses_sum

def merge(a, left_index, middle, right_index, inverses=0):
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
            inverses = inverses + len(left_copy) - left_copy_index
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

    return inverses

def disorder_measure(lst, lst_len):
    return (merge_sort(lst, 0, lst_len))

def main():
    a = int(input())
    lst = list(map(int, input().split()))
    print((disorder_measure(lst, a)))

def test():
    assert disorder_measure([10,8,6,2,4,5], 6) == 12, "test1"
    assert disorder_measure([1,9,8,1,4,1], 6) == 8, "test2"
    assert disorder_measure([6,2,3,7,5,8], 6) == 4, "test3"
    assert disorder_measure([6,4,5,0,0,2], 6) == 11, "test4"
    assert disorder_measure([8,9,10,7,4,0], 6) == 12, "test5"

if __name__ == "__main__":
    main()

