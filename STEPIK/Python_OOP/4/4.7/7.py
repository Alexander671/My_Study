class Note:
    def __init__(self, name, ton):
        if (not type(name) == str) or (not type(ton) == int):
            raise ValueError('недопустимое значение аргумента') 
        if (ton not in (-1, 0, 1)) or (name not in ('до','ре','ми','фа','соль','ля','си')):
            raise ValueError('недопустимое значение аргумента')
        self._name = name
        self._ton = ton

    def __setattr__(self, __name: str, __value) -> None:
        if __name == '_name':
            if (not type(__value) == str):
                raise ValueError('недопустимое значение аргумента') 
            if __value not in ('до','ре','ми','фа','соль','ля','си'):
                raise ValueError('недопустимое значение аргумента')
            
        if __name == '_ton':
            if (not type(__value) == int):
                raise ValueError('недопустимое значение аргумента') 
            if __value not in (-1, 0, 1):
                raise ValueError('недопустимое значение аргумента')
        super().__setattr__(__name,__value)
        
class Notes:
    __slots__ = ('_do' ,'_re' ,'_mi' ,'_fa' ,'_solt' ,'_la' ,'_si')
    flag_implemented = None
    def __init__(self):
        self._do = Note('до',0) #  - ссылка на ноту до (объект класса Note);
        self._re = Note('ре',0) #  - ссылка на ноту ре (объект класса Note);
        self._mi = Note('ми',0) #  - ссылка на ноту ми (объект класса Note);
        self._fa = Note('фа',0) #  - ссылка на ноту фа (объект класса Note);
        self._solt = Note('соль',0) #  - ссылка на ноту соль (объект класса Note);
        self._la = Note('ля',0) #  - ссылка на ноту ля (объект класса Note);
        self._si = Note('си',0) #  - ссылка на ноту си (объект класса Note).
    
    def __new__(cls, *args):
        if not cls.flag_implemented:
            cls.flag_implemented = super().__new__(cls)
        return cls.flag_implemented

    def __getitem__(self, k):
        if k > 6 or k < 0:
            raise IndexError('недопустимый индекс')
        return [self._do, self._re, self._mi, self._fa, self._solt, self._la, self._si][k]


notes = Notes()
nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа
print(nota._name)
print(notes[3]._ton)