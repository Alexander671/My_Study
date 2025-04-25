# put your python code here

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y

def mod_multi_inverse(m,a):
    gcd, x, y = gcdExtended(a, m)
    if gcd == 1:
        return ((x % m + m) % m)
    else:
        return None


def dec(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a + b)

def gcd_1(x):
    y = 2
    while x != y:
        if dec(x,y) == 1:
            return y
        else:
            y += 1


a, b = input().split(' ')

a, b = int(a), int(b)

# module 
n = a * b

# function euler's function
fi = (a - 1) * (b - 1)

# coprime integers
d  = gcd_1(fi)

# аппликативно обратное
e  = mod_multi_inverse(fi,d)
print(f'открытый ключ: {(d, n)}')
print(f'закрытый ключ: {(e, n)}')

