import random
def generate_ip():
    return( '.'.join([str(random.randint(0,255)) for i in range(4)]) )




print(generate_ip())