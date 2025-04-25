"""
В первой строке задано два целых числа 
1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно.
Следующие nn строк содержат по два целых числа ai и bi​ (ai≤biai​≤bi​) — координаты концов отрезков.
Последняя строка содержит mm целых чисел — координаты точек.
Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""

def binary_search_lte(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2

        if len(list) == mid + 1:
                return len(list)        

        guess = list[mid]
        guess_one_more = list[mid + 1]
        if guess <= item < guess_one_more:
            return mid + 1
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return mid


def binary_search_lt(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2

        if len(list) == mid + 1:
                return len(list)        

        guess = list[mid]
        guess_one_more = list[mid + 1]
        if guess < item <= guess_one_more:
            return mid + 1
        if guess >= item:
            high = mid - 1
        else:
            low = mid + 1
    return mid

def find_elements_lte(i, left_bounds):
    amount = binary_search_lte(left_bounds, i)
    return amount

def find_elements_lt(i, right_bounds):
    amount = binary_search_lt(right_bounds, i)
    return amount


def input_data():
    n, m = list(map(int, input().split()))
    left_bounds = []
    right_bounds = []
    
    for _ in range(n):
        a, b = list(map(int, input().split()))
        left_bounds.append(a)
        right_bounds.append(b)
    left_bounds = sorted(left_bounds)
    right_bounds = sorted(right_bounds)

    list_m = list(map(int, input().split()))

    if n == 1:
        for m in list_m:
            if left_bounds[0] <= m <= right_bounds[0]:
                print(1, end=' ')
            else:
                print(0, end=' ')                
        return None

    for m in list_m:
        lte = find_elements_lte(m, left_bounds)
        lt = find_elements_lt(m, right_bounds)
        print(lte - lt, end=' ')

def main():
    input_data()


def test_binary_search_elements_that_lt():
    assert binary_search_lte([1,2,3,4,5,8,10,15], 9) == 6, binary_search_lte([1,2,3,4,5,8,10,15], 9)
    assert binary_search_lte([1,2,3,4], 10) == 4
    assert binary_search_lte([0,1,2,3,3,3,3], 1) == 2, binary_search_lte([0,1,2,3,3,3,3], 1)
    assert binary_search_lt([3,3,3,4,5,6], 3) == 0, binary_search_lt([3,3,3,4,5,6], 3)
    assert binary_search_lt([3,3,3,4,5,6], 4) == 3, binary_search_lt([3,3,3,4,5,6], 4)
    assert binary_search_lt([3,3,3,4,5,6], 5) == 4, binary_search_lt([3,3,3,4,5,6], 5)

if __name__ == "__main__":
    test_binary_search_elements_that_lt()
    main()
