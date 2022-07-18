import random

import string

def generate_index():
    i = random.randint(0, 99)
    return( string.ascii_uppercase[i % 26] + string.ascii_uppercase[i % 26] + str(i) + '_' + str(i) + string.ascii_uppercase[-i % 26] + string.ascii_uppercase[i % 26] )

print(generate_index())



