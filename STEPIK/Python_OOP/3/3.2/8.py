class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods


    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if request.get('method', 'GET') in self.methods:
                return f'{request.get("method", "GET")}: {func(request)}'

        return wrapper


    def get():
        pass

    def post():
        pass




@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "POST", "url": "contact.html"})
print(res)