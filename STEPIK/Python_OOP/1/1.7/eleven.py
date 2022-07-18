

class Viber:
    messages = []

    @classmethod
    def add_message(cls, app): # - добавление нового приложения app в магазин;
        cls.messages.append(app)
    
    @classmethod
    def remove_message(cls, app): # - удаление приложения app из магазина;
        index = cls.messages.index(app)
        cls.messages = cls.messages[:index] + cls.messages[index+1:]

    @classmethod
    def set_like(cls, msg): # - поставить/убрать лайк для сообщения msg (если лайка нет то он ставится, если уже есть, то убирается);
        index = cls.messages.index(msg)
        cls.messages[index].fl_like = not cls.messages[index].fl_like
    
    @classmethod
    def show_last_message(cls, index): # - отображение последних сообщений;
        print(cls.messages[index:])
    
    @classmethod
    def total_messages(cls): # - возвращает общее число приложений в магазине.
        return len(cls.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)