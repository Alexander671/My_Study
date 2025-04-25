def gcd(a, b):
    while a != 0 or b != 0:
        if a % b == 0:
            return b
        if b % a == 0:
            return a
        if a > b:
            a = a % b
        else:
            b = b % a
    return a, b        


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))    


if __name__ == "__main__":
    main()