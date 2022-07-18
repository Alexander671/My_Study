def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello, World!'


print(greet())

def proxy(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper
    
def trace(func):
    def wrapper(*args,**kwargs):
        print(f'ТРАССИРОВКА: вызвана функция {func.__name__}() '
                f'c {args}, {kwargs}')
        
        original_result = func(*args,**kwargs)

        print(f'ТРАССИРОВКА: функция {func.__name__}() '
                f'вернула {original_result!r}')
        return original_result
    return wrapper




@trace 
def say(name, line):
    return f'{name}: {line}'
    
say('123', '12')

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    else:
        print(kwargs)



print(foo(1))
print(foo(1,2,3,4,5,6, key1 = 'znach', key2 = 999))
