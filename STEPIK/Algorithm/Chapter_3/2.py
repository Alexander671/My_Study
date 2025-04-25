
# задача о рюкзаке
def min_point(supplies, capacity):
    sum = 0
    for supplie in supplies:
        if capacity > supplie['capacity']:
            capacity -= supplie['capacity'] 
            sum += supplie['cost']

        else:      
            sum += supplie['cost'] * (capacity/supplie['capacity'])
            return sum
    return sum


def main():
    amount, capacity = map(int, input().split())
    supplies = []
    for _ in range(amount):
        a, b = map(int, input().split())
        supplies.append({'cost' : a, 'capacity' : b, 'cost_per_kg' : a/b})

    result = min_point(sorted(supplies, key=lambda x: x['cost_per_kg'], reverse=True), capacity)

    print(result)


if __name__ == "__main__":
    main()