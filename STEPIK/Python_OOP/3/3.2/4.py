class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
        
    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")
        
    def is_validate(self):
        if not self.validators:
            return True
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
            
        return True

class LengthValidator: # - для проверки длины данных в диапазоне [min_length; max_length];
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def __call__(self, value):
        return self.min <= len(value) <= self.max

class CharsValidator: # - для проверки допустимых символов в строке.
    def __init__(self, string):
        self.string = string


    def __call__(self, value):
        return all(map(lambda x: x in self.string, value))


min_length = 5
max_length = 10
lv = LengthValidator(min_length, max_length) # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator('chars') # chars - строка из допустимых символов


from string import ascii_lowercase, digits

lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")

