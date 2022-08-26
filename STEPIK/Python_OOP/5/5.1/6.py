lst_in = input().split()

def check_int(value):
    try:
        int(value)
        return True
    except:
        return False

print(sum(map(int, filter(check_int, lst_in))))