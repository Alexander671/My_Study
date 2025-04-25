def fib_mod(n, m):
    pizano_list = [0, 1]
    for i in range(2, 6 * m):
        pizano_list.append((pizano_list[i-1] + pizano_list[i - 2]) % m)
        if pizano_list[-1] == 0 and pizano_list[-2] == 1:
            return pizano_list, i
    return pizano_list, i

def main():
    n, m = map(int, input().split())
    if n == 0 or m == 1:
        print(0)
    elif n == 1 and m == 2:
        print(1)
    else:
        pizano_list, pizano_period = fib_mod(n, m)
        print(pizano_list[n % pizano_period])


if __name__ == "__main__":
    main()