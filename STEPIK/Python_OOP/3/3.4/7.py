class Lib: # - для представления библиотеки в целом;
    def __init__(self, ):
        self.book_list = []

    #################################
    # сумма
    def __add__(self, obj):
        self.book_list.append(obj)
        return self
        
    #################################
    # вычитание
    def __sub__(self, obj):
        if type(obj) == int:
            self.book_list.remove(self.book_list[obj])
        else:
            self.book_list.remove(obj)
        
        return self

    def __len__(self):
        return len(self.book_list)
class Book: # - для описания отдельной книги.
    
    # где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


book = Book('title', 'author', 'year')
lib = Lib()
lib = lib + book # добавление новой книги в библиотеку
lib += book

print(lib.book_list)
lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

print(lib.book_list)
lib = lib + book + book + book + book # добавление большого колиества книг
lib = lib - 1 # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= 1
print(lib.book_list)

n = len(lib) # n - число книг
print(n)