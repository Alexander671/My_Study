from string import ascii_uppercase


class CardCheck:

    @staticmethod
    def check_card_number(number:str): #  - проверяет строку с номером карты и возвращает булево значение True, если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
        return all(map(lambda x: x.isnumeric() and len(x) == 4, number.split('-')))
        
    
    @staticmethod
    def check_name(name:str): #- проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно и False - в противном случае.
        return all(map(lambda x: all(map(lambda y: y in ascii_uppercase, x)) and x.isupper(), name.split())) and len(name.split()) == 2


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("CЕРГЕЙ BALAKIREV")
print(is_number, is_name)