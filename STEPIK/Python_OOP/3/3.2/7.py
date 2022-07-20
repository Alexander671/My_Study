class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, value:dict):
        if value.get('method', 'GET') == "GET":
            return 'GET: ' + self.func(value)
        else:
            return None

@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})

print(res)