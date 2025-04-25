import itertools

def count_elements(list_elements):
    values_dict = dict()
    for el in list_elements:

        if not el in values_dict:
            values_dict.update({el : 0})

        values_dict[el] += 1

    return values_dict

def count_sort(list_elements):
    values_dict = count_elements(list_elements)
    list_values = list(map(lambda x: [x[0]] * x[1], sorted(values_dict.items(), key= lambda x: x[0])))

    return list(itertools.chain.from_iterable(list_values))

def main():
    n = int(input())

    list_elements = list(map(int, input().split()))
    print(*count_sort(list_elements), sep=' ')
    
if __name__ == "__main__":
    main()