def sum(xs, total = 0):
    if xs == []:
        print(total)
    else:
        total += xs[0]
        sum(xs[1:], total)

print(sum([1,2,3,4]))

def length(xs, total = 0):
    if xs == []:
        print(total)
    else:
        total += 1
        length(xs[1:], total)


print(length([1,2,3,4]))


def biggest(xs, big = 0):
    if xs == []:
        print(big)
    elif xs[0] > big:
        big = xs[0]
        biggest(xs[1:], big)
    else:
        biggest(xs[1:], big)

print(biggest([1,2,3,5,4]))

