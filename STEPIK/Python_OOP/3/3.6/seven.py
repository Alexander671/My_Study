import sys


class Record:
    pk = 0
    def __init__(self, fio, descr, old) -> None:
        self.fio = fio # - ФИО некоторого человека (строка); 
        self.descr = descr # - характеристика человека (строка); 
        self.old = old # - возраст человека (целое число).
    
    def __new__(cls, *args):
        obj = super().__new__(cls)
        obj.pk = cls.pk
        cls.pk += 1
        return obj        
    
    def __hash__(self) -> int:
        current_hash = hash((self.fio.lower(), self.old))
        return current_hash

    def __eq__(self, __o: object) -> bool:
        return hash(self) == hash(__o)



class DataBase:
    def __init__(self, path) -> None:
        self.path = path
        self.dict_db = {}
    
    def write(self, record): # - для добавления новой записи в БД, представленной объектом record;
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk): # - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)
        from functools import reduce
        return list(filter(lambda y: y.pk == pk, reduce(lambda x, y: x + y, self.dict_db.values())))[0]


# преобразование строк к заданному формату
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst1 = map(lambda x: x.split(';')[:2] + [int(x.split(';')[2])], lst_in)

# создание базы данных
db = DataBase('path')


### {object Record - один общий объект:[object Record] список из всех объектов}
for j in lst1:
    record = Record(*j)
    db.write(record)



db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
d = v[0][0]
assert type(d.descr) == str and type(d.fio) == str and type(d.old) == int, "значениями словаря должен быть список с типами данных: [строка, строка, целое число]"
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"
    
if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"

'''

Балакирев С.М.; программист; 33
Кузнецов Н.И.; разведчик-нелегал; 35
Суворов А.В.; полководец; 42
Иванов И.И.; фигурант всех подобных списков; 26
Балакирев С.М.; преподаватель; 33

'''