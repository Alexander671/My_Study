lst_in = input().split()

def numeric_int_float_str(value):
    try:
        if str(float(value)) == value:
            return float(value)
        if str(int(value)) == value:
            return int(value)
    except:
        return value

lst_out = list(map(numeric_int_float_str, lst_in))
print(lst_out)