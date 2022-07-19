class Course: # - класс, отвечающий за управление курсом в целом;
    def __init__(self, name):
        self.name = name # - название курса (строка);
        self.modules = [] # - список модулей в курсе (изначально список пуст).        

    def add_module(self, module): # - добавление нового модуля в конце списка modules;
        self.modules.append(module) 

    def remove_module(self, indx): # - удаление модуля из списка modules по индексу в этом списке.
        self.modules = self.modules[:indx] + self.modules[indx + 1:] 

class Module: # - класс, описывающий один модуль (раздел) курса;
    def __init__(self, name):
        self.name = name # - название модуля;
        self.lessons = [] # - список из уроков (объектов класса LessonItem), входящих в модуль (изначально список пуст).         


    def add_lesson(self, lesson): # - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
        self.lessons.append(lesson) 

    def remove_lesson(self, indx): # - удаление урока по индексу в списке lessons.
        self.lessons = self.lessons[:indx] + self.lessons[indx + 1:] 

class LessonItem: # - класс одного занятия (урока).
    dct_type = {'title': (str,), 'practices': (int,), 'duration': (int,),}
    def __init__(self, title, practices, duration):
        self.title = title # - название урока (строка);
        self.practices = practices # - число практических занятий (целое положительное число);
        self.duration = duration # - общая длительность урока (целое положительное число).


    def __getattr__(self, item):
        return False

    def __delattr__(self, __name: str) -> None:
        if not (__name in ('title', 'practices', 'duration')):
            object.__delattr__(self, __name)
        else:
            raise AttributeError(f"Атрибут {__name} удалять запрещено.")

    def __setattr__(self, key, value):
        if type(value) not in self.dct_type[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
print(module_1.lessons)
course.add_module(module_1)
print(course.modules)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
print(course.modules)

print(module_2.lessons)
