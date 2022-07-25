class Stack: # - для управления односвязным списком в целом;
    def __init__(self, top=None):
        self.top:StackObj = top 

    def push_back(self, obj): # - добавление объекта класса StackObj в конец односвязного списка;
        if self.top == None:
            self.top = obj
        else:
            iterate_obj:StackObj = self.top
            while iterate_obj.next:
                iterate_obj = iterate_obj.next
            else:
                iterate_obj.next = obj

    def pop_back(self): # - удаление последнего объекта из односвязного списка.
        if self.top.next == None:
            self.top = None
        else:
            iterate_obj:StackObj = self.top
            while iterate_obj.next.next:
                iterate_obj = iterate_obj.next
            else:
                iterate_obj.next = None
    
    def to_list(self):
        if self.top == None:
            return []
        else:
            iterate_obj = self.top
            list_objects = []
            while iterate_obj.next:
                list_objects.append(iterate_obj.data)
                iterate_obj = iterate_obj.next
            list_objects.append(iterate_obj.data)
            return list_objects

    # # добавление нового объекта класса StackObj в конец односвязного списка st
    #st = st + obj 
    # st += obj
    # 
    # # добавление нескольких объектов в конец односвязного списка
    # st = st * ['data_1', 'data_2', ..., 'data_N']
    # st *= ['data_1', 'data_2', ..., 'data_N']
    
    #################################
    # сумма
    def __add__(self, obj):
        self.push_back(obj)
        return self

    def __radd__(self, obj):
        self.push_back(obj)
        return self

    def __iadd__(self, obj):
        self.push_back(obj)
        return self
    

    ##################################
    # умножение
    def __mul__(self, obj):
        for i in obj:
            self.push_back(StackObj(i))
        return self




class StackObj: # - для представления отдельных объектов в односвязным списком.
    
    def __init__(self, data, next=None):
        self.__data = data # - ссылка на строку с переданными данными;
        self.__next:StackObj = next # - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

    def next_get(self):
        return self.__next

    def next_set(self, obj):
        self.__next = obj

    def data_get(self):
        return self.__data

    def data_set(self, obj):
        self.__data = obj
        

    next = property(next_get, next_set)
    data = property(data_get, data_set)

h = StackObj('5')
print(h.data) # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
print(st.to_list()) # 1 2 3
st.pop_back()
print(st.to_list()) # 1 2
st.pop_back()
print(st.to_list()) # 1
st.pop_back()
print(st.to_list()) # []
st.push_back(StackObj('3'))
print(st.to_list()) # 3 

st = st + StackObj('4')
print(st.to_list()) # 3 4 

st += StackObj('5')
print(st.to_list()) # 3 4 5

st = st * [str(i) for i in range(6, 9)]
print(st.to_list()) # 3 4 5 6 7 8 

st *= [str(i) for i in range(9, 12)]
print(st.to_list()) # 3 4 5 6 7 8 9 10 11 
