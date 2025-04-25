import sys


class ListObject:
    def __init__(self, data, next_obj=None):
        self.next_obj = next_obj #- ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);

        self.data = data  #- данные объекта в виде строки.

    def link(self, obj):
        self.next_obj = obj

    def show_list(self):
        iterate = self
        while iterate.next_obj != None:
            print(iterate.data)
            iterate = iterate.next_obj
        print(iterate.data)

lst_in = list(map(str.strip, sys.stdin.readlines()))

def create_list(lst_in):
        if lst_in == []:
            return None
        else:
            iterate = lst_in[0]
            return ListObject(data=iterate, next_obj=create_list(lst_in[1:]))

head_obj = create_list(lst_in)
head_obj.show_list()