class StackObj: # - для представления отдельных объектов стека.
    def __init__(self, data, next=None) -> None:
        self.data = data  # - ссылка на данные объекта;
        self.next = next  # - ссылка на следующий объект стека (если его нет, то next = None).

class Stack: # - для представления стека в целом;
    def __init__(self, top:StackObj=None):
        self.top = top


    def push_back(self, obj:StackObj): # - для добавления нового объекта obj в конец стека;
        if self.top == None:
            self.top = obj
        iterate = self.top
        while iterate.next:
            iterate = iterate.next
        else:
            iterate.next = obj
            obj.next = None

    def push_front(self, obj:StackObj): # - для добавления нового объекта obj в начало стека.
        obj.next = self.top
        self.top = obj

    def __iter__(self):
        self.value = self.top
        return self

    def __next__(self):
        self.value = self.value.next
        if self.value == None:
            raise StopIteration
        return self.value

    def __getitem__(self, key):
        if key < 0:
            raise IndexError('неверный индекс')
        i = 0
        iterate = self.top
        while i < key:
            i += 1
            iterate = iterate.next
            if iterate == None:
                raise IndexError('неверный индекс')

        else:
            return iterate.data

    def __setitem__(self, key, value):
        if key < 0:
            raise IndexError('неверный индекс')
        i = 0
        iterate = self.top
        while i < key:
            i += 1
            iterate = iterate.next
            if iterate == None:
                raise IndexError('неверный индекс')
        else:
            iterate.data = value


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))


assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
 
