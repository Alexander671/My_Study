class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):
    def __init__(self, methods=('GET', )):
        super().__init__(methods)

    def get(self, request):
        if not type(request) == dict:
            raise TypeError('request не является словарем')
        try:
            return f"url: {request['url']}"
        except:
            raise TypeError('request не содержит обязательного ключа url')


    def render_request(self, request, method:str):
        if not method in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        return getattr(self, method.lower())(request)


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
print(html)