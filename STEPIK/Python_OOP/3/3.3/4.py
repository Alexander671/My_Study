class WordString:
    def __init__(self, string=""):
        self.__string = string
    

    def __len__(self,):
        return len(self.__string.replace('  ', ' ').split())

    def words(self, indx): # - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).
        print()
        return self.__string.replace('  ', ' ').split()[indx]


    def __call__(self, indx):
        return self.words(indx)

    def string_get(self):
        return self.__string

    def string_set(self, obj):
        self.__string = obj

    string = property(string_get, string_set)



words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
