class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        inp = self.func()
        return list(map(lambda x: int(x), inp.split()))



@InputDigits
def input_dg():
    return input()

res = input_dg()
print(res)