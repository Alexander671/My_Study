class AppVK: # - класс приложения ВКонтаке;
    def __init__(self):
        self.name = "ВКонтакте"

class AppYouTube: # - класс приложения YouTube;
    def __init__(self, memory_max):
        self.name = 'YouTube'
        self.memory_max = memory_max

class AppPhone: # - класс приложения телефона.
    def __init__(self, phone_list):
        self.name = 'Phone'
        self.phone_list = phone_list

class SmartPhone:
    def __init__(self, model):
        self.model = model # - марка смартфона (строка);
        self.apps = [] # - список из установленных приложений (изначально пустой).

    
    def add_app(self, app): # - добавление нового приложения на смартфон (в конец списка apps);
        if app.name not in map(lambda x: x.name, self.apps):
            self.apps.append(app)
    
    def remove_app(self, app): # - удаление приложения по ссылке на объект app.
        if app.name not in map(lambda x: x.name, self.apps):
            self.apps.remove(app)

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)