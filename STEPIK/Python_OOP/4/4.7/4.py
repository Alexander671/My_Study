class Person:
    __slots__ = ('fio', 'old', 'job')
    def __init__(self,fio,old,job):
        self._fio = fio # - ФИО сотрудника (строка);
        self._old = old # - возраст сотрудника (целое положительное число);
        self._job = job # - занимаемая должность (строка).

persons = [Person('Суворов', 52, 'полководец'),
           Person('Рахманинов', 50, 'пианист, композитор'),
           Person('Балакирев', 34, 'программист и преподаватель'),
           Person('Пушкин', 32, 'поэт и писатель')
           ]