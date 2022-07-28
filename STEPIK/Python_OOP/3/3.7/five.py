import sys


class MailItem:
    def __init__(self, mail_from, title, content):

        self.mail_from = mail_from # - email отправителя (строка);
        self.title = title # - заголовок письма (строка),
        self.content = content # - содержимое письма (строка). 
        self.is_read = False # (прочитано ли) с начальным значением False.

    def set_read(self, fl_read): # - для отметки, что письмо прочитано (метод должен устанавливать атрибут is_read = fl_read, если True, то письмо прочитано, если False, то не прочитано).
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class MailBox:
    def __init__(self, inbox_list=[]):
        self.inbox_list = inbox_list

    def receive(self): # - прием новых писем
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        
        self.inbox_list = list(map(lambda x: MailItem(*x.split(';')), lst_in))

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(len(inbox_list_filtered))