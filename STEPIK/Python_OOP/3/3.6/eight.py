import sys


class BookStudy:
    def __init__(self, name, author, year) -> None:
        self.name = name # -- название пособия (строка)
        self.author = author # -- автор пособия (строка);
        self.year = year # -- год издания (целое число).
         
    
    def __hash__(self) -> int:
        current_hash = hash((self.name.lower(), self.author.lower()))
        return current_hash

    def __eq__(self, __o: object) -> bool:
        return hash(self) == hash(__o)


# преобразование строк к заданному формату
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = map(lambda x: BookStudy(*(x.split(';')[:2] + [int(x.split(';')[2])])), lst_in)
unique_books = len(set(map(hash, lst_bs)))
