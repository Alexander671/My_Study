from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj): # - добавление объекта в конец стека;
        pass
    
    @abstractmethod
    def pop_back(self): # - удаление последнего объекта из стека.
        pass 

class StackObj:
    def __init__(self, _data, _next=None):
        self._data = _data # - информация, хранящаяся в объекте (строка);
        self._next = _next # - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).

class Stack(StackInterface):
    def __init__(self, top:StackObj=None):
        self._top = top

   
    def push_back(self, obj): # - добавление объекта в конец стека;
        if self._top == None:
            self._top = obj
        else:
            iterate = self._top              # начинаем с самого начала
            while iterate._next != None:     # если значение уже последнее, либо это начало, либо нашли последний
                iterate = iterate._next      # двигаемся по списку, если уткнулись в последний, то изменяем его
        
            iterate._next = obj              # если изначально был None, то изменим просто top

    def pop_back(self): # - удаление последнего объекта из стека.
        if not self._top == None:            # есть первый элемент
            iterate = self._top              # запомнили его 
            
            if iterate._next == None:        # если всего один, 
                self._top = None             # то его и удалили
                return iterate

            else:
                while iterate._next._next != None: # если элементов >= 2, то ищем последний, который удалим
                    iterate = iterate._next # двигаемся по списку, если уткнулись в последний, то изменяем его
            returned_value = iterate._next
            iterate._next = None                 # если изначально был None, то изменим просто top
        return returned_value

    def get_data(self): # - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления).
        stack_to_list = []
        if not self._top == None:
            iterate = self._top            # начинаем с самого начала
            while iterate != None:        # если значение уже последнее, либо это начало, либо нашли последний
                stack_to_list.append(iterate._data)
                iterate = iterate._next # двигаемся по списку, если уткнулись в последний, то изменяем его
        return stack_to_list  

assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)
print(st.get_data())

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)
print(st.get_data())

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
print(st.get_data())
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
print(st.get_data())
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"