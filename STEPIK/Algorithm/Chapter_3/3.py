
# По данному числу 1≤n≤10^9 найдите максимальное число k,
# для которого nn можно представить как сумму k различных натуральных слагаемых.
# Выведите в первой строке число k, во второй — k слагаемых.
def various_terms(n):
    changed_sum = 0
    addend = []
    for i in range(1, n + 1):
        changed_sum += i
        
        if changed_sum > n:
            addend = addend[:-1]
            addend.append(n - sum(addend))
            return addend
        
        addend.append(i)
    
    return addend


def main():
    n = int(input())

    result = various_terms(n)
    
    print(len(result))
    print(*result)


if __name__ == "__main__":
    main()