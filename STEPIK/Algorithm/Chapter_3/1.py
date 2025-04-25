
# задача покрытия множеств
# похожа на задачу о раписании, из "Грокаем Алгоритмы"
def min_point(line_segments):
    first_left_point = line_segments[0][1]
    points = [first_left_point]
    current_point = first_left_point

    for segment in line_segments:
        if not (current_point >= segment[0] and current_point <= segment[1]):
            current_point = segment[-1]
            points.append(current_point)
    
    return points


def main():
    n = int(input())
    line_segments = []
    for _ in range(n):
        a, b = map(int, input().split())
        line_segments.append((a,b))

    result = min_point(sorted(line_segments, key=lambda x: x[-1]))

    print(len(result))
    print(*result)    


if __name__ == "__main__":
    main()