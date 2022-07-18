from string import ascii_letters, digits
class EmailValidator:
    
    def __new__(cls):
        return None

    @classmethod
    def check_email(cls, email): # - возвращает True, если email записан верно и False - в противном случае;
        email_parts =  email.split('@')
        correct_char = ascii_letters + digits + '_@.'
        return cls.__is_email_str(email) and len(email_parts[0]) <= 100 and len(email_parts[1]) <= 50 and '.' in email_parts[1] and '..' not in email and all(map(lambda x: x in correct_char, email))
    
    @classmethod
    def get_random_email(cls): # - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).
        return "xxxxxxx.xxx@gmail.com"

    def __is_email_str(email):
        return type(email) is str