class WordString:
    def __init__(self,):
        self.__string = ""
    

    def __str__(self) -> str:
        return self.string_get()

    def __repr__(self) -> str:
        return self.string_get()

    def words(indx): # - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).
        pass

    def string_get(self):
        return self.__string

    def string_set(self, obj):
        self.__string = obj

    string = property(string_get, string_set)

    @staticmethod
    def len(words): # - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
        return words.split()


words = WordString()
words.string = "Курс по Python ООП"
print(len(words))
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
