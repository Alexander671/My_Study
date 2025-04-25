TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"
    
    def __new__(cls, name):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

class DialogLinux:
    name_class = "DialogLinux"
    
    def __new__(cls, name):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

class Dialog:
    def __new__(cls, name):
        if TYPE_OS == 1:
            return DialogWindows(name)
        else:
            return DialogLinux(name)
            
    def __init__(self, name):
        self.name = name

dlg_1 = Dialog("name1")
dlg_2 = Dialog("name2")
print(isinstance(dlg_1, DialogWindows))
print(isinstance(dlg_2, DialogLinux))
print(dlg_1.name)
print(dlg_2.name)
print(dlg_1)
print(dlg_2)
