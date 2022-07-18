import sys
class StreamData:
    def create(self, fields, lst_values):
        
        if len(fields) != len(lst_values):
            return False
        
        else:    
            list_access = []
            for i, j in zip(fields, lst_values):
                setattr(self, i, j)
                list_access.append(hasattr(self, i))
            return all(list_access)
    
    
class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sd = StreamData()
print(sd.create(('id', 'title', 'pages'), ["Питон - основы мастерства", 512]))
