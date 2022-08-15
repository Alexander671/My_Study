class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, v):
        self.__name = v

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, v):
        self.__kind = v

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, v):
        self.__old = v

animals = [Animal('Васька', 'дворовый кот', 5),
           Animal('Рекс', 'немецкая овчарка', 8),
           Animal('Кеша', 'попугай',  3)]