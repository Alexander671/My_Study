# Наилучший случай: О(n)
# Средний, наихудший случаи: 0 (п ^ 2)
# 
def sort (xs):
    for i in range(1, len(xs)):
        insert(xs, i, xs[i])
    else:
        return xs

    



def insert(xs,i,value):
    j = i - 1
    while j >= 0 and xs[j] > value:
        xs[j+1] = xs[j]
        j -= 1
    xs[j+1] = value
    return xs


print(sort([5,2,1,3,4,7,5]))