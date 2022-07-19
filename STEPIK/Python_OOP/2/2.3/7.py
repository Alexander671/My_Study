class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return (type(string) == str) and (self.min_length <= len(string) <= self.max_length)

class StringValue:
    def __init__(self, validator):
        self.validator = validator

st = StringValue(validator=ValidateString(3, 100))

validate = ValidateString(min_length=3, max_length=100)




class RegisterForm:
    login = StringValue() # - для ввода логина;
    password = StringValue() #  - для ввода пароля;
    email = StringValue()  # - для ввода Email.
    def __init__(self, login, password, email):
        self.login = login # - для ввода логина;
        self.password = password #  - для ввода пароля;
        self.email = email # - для ввода Email.
    
    def get_fields(self): # - возвращает список из значений полей в порядке [login, password, email];
        return [self.login, self.password, self.email]


    def show(self): # - выводит в консоль многострочную строку в формате:
        print(f'''<form>
Логин: {self.login}
Пароль: {self.password}
Email: {self.email}
</form>''') 

form = RegisterForm('login', 'password', 'email')