from abc import ABCMeta, abstractmethod
class Super(metaclass=ABCMeta):
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()   # Стандартное поведение
                        # Ожидается определение метода
    
class Inheritor(Super):
    pass # Буквальное наследование метода

class Replacer(Super) :
    def method(self):
        print('in Replacer.method') # Полное замещение метода

class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method') # Расширение поведения метода


# в Replacer .method
# начало Extender.method
# конец Extender.method
@abstractmethod
class Provider(Super):
    # Заполнение обязательного метода
    def action(self):
        print('in Provider.action')
        # в Provider.method

if __name__ == '__main__' :
    for klass in (Inheritor, Replacer, Extender):
        print(f'\n{klass.__name__} ...')
        klass().method()
        print('\nProvider...')
        x = Provider()
        x.delegate()



class DataBase:
    pk = 1
    title= "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12

db = DataBase()
print(db.pk)