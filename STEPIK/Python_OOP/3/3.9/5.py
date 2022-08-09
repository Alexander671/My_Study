class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.list_value = [fio, job, old, salary, year_job, ""]
        self.dict_value = {0:'fio', 1:'job', 2:'old', 3:'salary', 4:'year_job'}

    def __validate(self, key):
        if not (type(key) == int and 0 <= key <= 4):
            raise IndexError('неверный индекс')

    def __getitem__(self,key):
        self.__validate(key)
        return self.list_value[key]

    def __setitem__(self,key,value):
        self.__validate(key)
        self.list_value[key] = value
        self.__setattr__(self.dict_value[key], value)

    def __iter__(self):
        self.value = self.fio
        return self

    def __next__(self):
        old_value = self.value
        try:
            self.value = self.list_value[self.list_value.index(self.value) + 1]
        except:
            raise StopIteration
        return old_value
p = Person('Matveev A.S.', 'Programmer', 25, 2000000, 2022)
data = p[1] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[1] = 'Programmer 2' # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
