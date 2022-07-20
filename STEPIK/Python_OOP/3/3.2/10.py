class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            rend = self.render
            inp = func()
            return list(map(lambda x: rend(x), inp.split()))

            # здесь строчки программы
        return wrapper

class RenderDigit:
    def __call__(self, value):
        try:    
            int(value)
        except:
            return None
        return int(value)    

input_dg = InputValues(RenderDigit())(input)

res = input_dg()
print(res)
