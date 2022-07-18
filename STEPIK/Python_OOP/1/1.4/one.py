import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))  

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        self.lst_data.extend(map(lambda x: dict(zip(self.FIELDS, x.split())), data))
        
    def select(self, a, b):
        return list(filter(lambda l: a <= (int(l['id']) - 1) <= b, self.lst_data))


db = DataBase()
db.insert(lst_in)
