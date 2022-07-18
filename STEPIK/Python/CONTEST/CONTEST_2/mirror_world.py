n = input().split()

x = int(n[0])
y = int(n[1])

world = [list(input()) for i in range(x)]

def find_indexes_of_box(xs):
    matches = [i for i, j in enumerate(xs) if j == "|"]
    return matches

indexes_of_boxes = (map(find_indexes_of_box, world))


def concate_box_to_one(level, index_of_boxes):
    while len(index_of_boxes) >= 2:
        # нашли края коробки
        j = index_of_boxes[:2]

        # содержимое коробки
        box = ["".join(level[j[0] : j[1] + 1])]
        
        # сформировали новый уровень
        level = level[:j[0]] + box + level[(j[1]):]
        
        # число на которое изменятся индексы
        n = len(["".join(level[j[0] : j[1] + 1])]) + 2
        index_of_boxes = list(map(lambda x: x - n, index_of_boxes))
        
        # перешли к следующим двум индексам
        index_of_boxes = index_of_boxes[1:]
    return "".join(level[::-1]).replace("||", "|")


print(*map(lambda x, y: concate_box_to_one(x, y), world, indexes_of_boxes), sep = '\n')

