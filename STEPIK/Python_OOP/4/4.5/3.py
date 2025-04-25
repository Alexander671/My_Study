class Student:
    def __init__(self, fio, group):
        self._fio = fio  # ФИО студента (строка)
        self._group = group # группа (строка)
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

    def __str__(self):
        print(f"{self.name} {self._fio}: предмет {self._subject}")

class Lector(Mentor): # - для описания лекторов;
    name = "Лектор"
    
    def set_mark(self, student:Student, mark): 
        student.add_lect_marks(mark)

class Reviewer(Mentor): # - для описания экспертов.
    name = "Эксперт"
    def set_mark(self, student:Student, mark): 
        student.add_house_marks(mark)



l = Lector("fio", "subject")
print(l._fio)