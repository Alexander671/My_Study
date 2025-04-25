class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string): 
        if not self.min_length < len(string) < self.max_length:
            raise ValueError('недопустимая строка')
        if self.chars == "":
            return True
        for c in self.chars:
            if c in string:
                return True
        else:
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = self._password = None
    def form(self, request): 
        try:
            login = request['login']
            password = request['password']
        except:
            raise TypeError('в запросе отсутствует логин или пароль')
        self._login    = login if self.login_validator.is_valid(login) else None
        self._password = password if self.password_validator.is_valid(password) else None
            

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(5, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)