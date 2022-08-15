CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

class FileDialogFactory:
    def __init__(self, title, path, exts):
        self.title = title
        self.path = path
        self.exts = exts

    def __new__(self, title, path, exts):
        if CURRENT_OS == 'windows':
            return self.create_windows_filedialog(title, path, exts)
        else:
            return  self.create_linux_filedialog(title, path, exts)

    @staticmethod
    def create_windows_filedialog(title, path, exts): # - для создания объектов класса WindowsFileDialog;
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts): # - для создания объектов класса LinuxFileDialog.
        return LinuxFileDialog(title, path, exts)

dlg = FileDialogFactory('title', 'path', 'exts')
print(dlg)