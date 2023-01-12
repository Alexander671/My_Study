
from functools import total_ordering


@total_ordering
class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

    def __eq__(self, other):
        return len(self) == len(other)

        
    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

a = Word("ab")
b = Word("ab")
print(a != b)
a = Word("ab")
b = Word("ac")
print(a != b)

class WordWithNe(Word):
    def __ne__(self, __x: object) -> bool:
        return len(self) != len(__x)


a = WordWithNe("ab")
b = WordWithNe("ab")
print(a != b)
a = WordWithNe("ab")
b = WordWithNe("ab")
print(a == b)
