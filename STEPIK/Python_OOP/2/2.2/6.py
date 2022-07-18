class StackObj:
    def __init__(self, data, next=None):
        self.__data = data # - ссылка на строку с данными, указанными при создании объекта;
        self.__next = next # - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next):
        if type(self.__next) == StackObj or self.__next == None:
            self.__next = next
        

    data = property(get_data, set_data) # - для записи и считывания информации из локального приватного свойства __data.
    next = property(get_next, set_next) # - для записи и считывания информации из локального приватного свойства __next;
    
class Stack: # - для управления односвязным списком.
    def __init__(self, top:StackObj = None):
        self.top = top

    def push(self, obj:StackObj):              # добавление объекта класса StackObj в конец односвязного списка;
        if self.top == None:
            self.top = obj
        else:
            iterate = self.top            # начинаем с самого начала
            while iterate.get_next() != None:        # если значение уже последнее, либо это начало, либо нашли последний
                iterate = iterate.get_next() # двигаемся по списку, если уткнулись в последний, то изменяем его
        
            iterate.set_next(obj)                 # если изначально был None, то изменим просто top
        
    def pop(self): # - извлечение последнего объекта с его удалением из односвязного списка;
        if not self.top == None:            # есть первый элемент
            iterate = self.top              # запомнили его 
            if iterate.get_next() == None:  # если всего один, 
                self.top = None             # то его и удалили
            else:
                while iterate.get_next().get_next() != None: # если элементов >= 2, то ищем последний, который удалим
                    iterate = iterate.get_next() # двигаемся по списку, если уткнулись в последний, то изменяем его
        
            iterate.set_next(None)                 # если изначально был None, то изменим просто top
        
    def get_data(self): # - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления).
        stack_to_list = []
        if not self.top == None:
            iterate = self.top            # начинаем с самого начала
            while iterate != None:        # если значение уже последнее, либо это начало, либо нашли последний
                stack_to_list.append(iterate.get_data())
                iterate = iterate.get_next() # двигаемся по списку, если уткнулись в последний, то изменяем его
        return stack_to_list        
            
    
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(res)


st1 = Stack()

st1.pop()
res = st1.get_data()    # ['obj1', 'obj2']
print(res)
