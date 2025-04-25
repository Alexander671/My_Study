def fib_digit(n):
    f = list(range(0, n + 1))
    for i in range(2, n + 1):
        f[i] = (f[i-1] + f[i - 2]) % 10
    return f[-1]

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()