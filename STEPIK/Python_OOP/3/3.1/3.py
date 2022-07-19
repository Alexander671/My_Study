class Book:
    def __init__(self, title="", author="", pages = 0, year = 0):
        self.title = title # - заголовок книги (строка, по умолчанию пустая строка);
        self.author = author # - автор книги (строка, по умолчанию пустая строка);
        self.pages = pages # - число страниц (целое число, по умолчанию 0);
        self.year = year # - год издания (целое число, по умолчанию 0).

    def __setattr__(self, key, value):
        if (key in ('title', 'author') and type(value) != str) or (key in ('pages', 'year') and type(value) != int):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)
book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
