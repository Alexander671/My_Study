class AppStore:
    app = []
    
    def add_application(self, app): # - добавление нового приложения app в магазин;
        self.app.append(app)

    def remove_application(self, app): # - удаление приложения app из магазина;
        index = self.app.index(app)
        self.app = self.app[:index] + self.app[index+1:]

    def block_application(self, app): # - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
        index = self.app.index(app)
        self.app[index].blocked = True

    def total_apps(self): # - возвращает общее число приложений в магазине.
        return len(self.app)

class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked



store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
print(AppStore.app)