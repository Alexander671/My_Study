# put your python code here

import random

print(*(list({random.randint(1000000, 9999999) for c in range(1, 150)}))[:100], sep= '\n')


