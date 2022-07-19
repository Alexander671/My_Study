class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number # - номер телефона (число);
        self.fio = fio # - ФИО владельца номера телефона.

class PhoneBook:
    def __init__(self, *args):
        self.book:list[PhoneNumber] = list(args)

    def add_phone(self, phone): # - добавление нового номера телефона (в список);
        self.book.append(phone)

    def remove_phone(self, indx): #  - удаление номера телефона по индексу списка;
        self.book = self.book[:indx] + self.book[indx + 1:]

    def get_phone_list(self): #- получение списка из объектов всех телефонных номеров.
        return self.book


    
p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

print(phones)