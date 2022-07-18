from string import ascii_lowercase, digits


class Check:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    
    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size
    
    def get_html(self, type):
        return f"<p class='{type}'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name:str):
        name.replace(' ', '')
        if not (3 <= len(name) <= 50 and name.isalnum()):
            raise ValueError("некорректное поле name")
        return True

class TextInput(Check):
    def get_html(self):
        return super().get_html('login')

class PasswordInput(Check):
    def get_html(self):
        return super().get_html('password')

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

login = TextInput('name1', 5)
psw = PasswordInput('name2', 5)