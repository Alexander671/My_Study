filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

class FileAcceptor:
    def __init__(self, *args):
        self.extensions = list(args)

    def __eq__(self, __o: str) -> bool: 
        # __o - filename, i.e. one file
        # example - 'boat.jpg'
        return __o.split('.')[-1] in self.extensions

    def __call__(self, file):
        return file == self


    #################################
    # сумма
    def __add__(self, obj):
        new_list = self.extensions + obj.extensions
        return FileAcceptor(*sorted(set(new_list), key=new_list.index))
    ##################################


acceptor1 = FileAcceptor('jpg')

acceptor2 = FileAcceptor('png')


filenames = list(filter(acceptor1, filenames))
print(filenames)

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
