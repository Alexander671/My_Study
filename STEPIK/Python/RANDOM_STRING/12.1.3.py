from random import *

length = int(input())    # длина пароля
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(length):
     print(chars[randint(0,length)], end = '')


