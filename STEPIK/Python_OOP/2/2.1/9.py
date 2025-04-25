

class LinkedList:
    """объявите класс LinkedList, который будет представлять связный список в целом 
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;
        """
        if self.head == None and self.tail == None:
            self.head = obj
        elif self.head != None and self.tail == None:
            self.tail = obj
            
            self.tail.set_prev(self.head)
            self.head.set_next(self.tail)

        elif self.head != None and self.tail != None:
            old_tail_obj = self.tail
            old_tail_obj.set_next(obj)
            self.tail = obj
            self.tail.set_prev(old_tail_obj)
        
                

    def remove_obj(self):
        """удаление последнего объекта из связного списка;
       """
        if self.tail != None:
            prev_object = self.tail.get_prev()
            self.tail = prev_object
            prev_object.set_next(None)


        if self.tail == None:
            self.head = None


    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.
        """
        first = self.head
        list_data = []
        while first != None:
            list_data.append(first.get_data())
            first = first.get_next()            
        return list_data


    def show_list(self):
        first = self.head
        list_data = []
        while first != None:

            list_data.append((first.get_prev(), first.get_data(), first.get_next()))
            first = first.get_next()            
        print(list_data)


class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
    """
    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev
        
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
    
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
lst.show_list()

lst.remove_obj()
lst.show_list()
lst.remove_obj()
lst.show_list()

ls_one = LinkedList()
ls_one.add_obj(ObjList(1))

ls_one.remove_obj()
