class Record:
    def __init__(self, *args, **kwargs):
        self.list_kwargs = list(map(lambda x: list(x), list(kwargs.items())))
        for i, j in kwargs.items():
            setattr(self, i, j)

    def __getitem__(self, indx):
        return self.list_kwargs[indx][1]

    def __setitem__(self, key, value):
        self.list_kwargs[key][1] = value
        setattr(self, self.list_kwargs[key][0], value)
        

r = Record(pk=1, title='Python ООП', author='Балакирев')
# print(r.__dict__)

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError

