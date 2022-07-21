class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__data = data # - ссылка на строку с данными;
        self.__prev = prev # - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
        self.__next = next # - ссылка на следующий объект связного списка (если объекта нет, то __next = None).


    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj;
        """
        self.__next = obj
    
    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj;
        """
        self.__prev = obj
    
    def get_next(self):
        """получение значения приватного свойства __next;
        """
        return self.__next
    
    def get_prev(self):
        """получение значения приватного свойства __prev;
        """
        return self.__prev
    
    def set_data(self, data):
        """изменение приватного свойства __data на значение data;
        """
        self.__data = data
    
    def get_data(self):
        """получение значения приватного свойства __data.
        """
        return self.__data

    data = property(get_data, set_data)
    next = property(get_next, set_next)
    prev = property(get_prev, set_prev)
    
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head # - ссылка на первый объект связного списка (если список пуст, то head = None);
        self.tail = tail # - ссылка на последний объект связного списка (если список пуст, то tail = None).

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;
        """
        if self.head == None and self.tail == None:
            self.head = obj
        elif self.head != None and self.tail == None:
            self.tail = obj
            
            self.tail.prev = self.head
            self.head.next = self.tail

        elif self.head != None and self.tail != None:
            old_tail_obj = self.tail
            old_tail_obj.next = obj
            self.tail = obj
            self.tail.prev = old_tail_obj
        
                

    def remove_obj(self, indx):
        """удаление последних объектов по индексу из связного списка;
       """
        first = self.head
        while first and indx != 1:
            indx -= 1
            first = first.next
        else:
            first.next = None
            self.tail = first


    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.
        """
        first = self.head
        list_data = []
        while first != None:
            list_data.append(first.get_data())
            first = first.get_next()            
        return list_data

    
    def __len__(self,): # - возвращает число объектов в связном списке;
        return len(self.get_data())
    
    def linked_lst(self, indx): # - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).
        return self.get_data()[indx]

    def __call__(self, indx):
        return self.linked_lst(indx)

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
linked_lst.add_obj(ObjList("Python ООП"))
linked_lst.add_obj(ObjList("Python ООП"))
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
