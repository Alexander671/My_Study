class WindowDlg:
    def __init__(self, header, width, height):
        self.__width = width
        self.__height = height
        self.__header = header

    def show(self):
        print(f"{self.__header}: {self.__width}, {self.__height}")

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if type(height) == int:
            if 0 <= height <= 10000:
                self.__height = height
                self.show()


    def get_width(self):
        return self.__width

    def set_width(self, width):
        if type(width) == int:
            if 0 <= width <= 10000:
                self.__width = width   
                self.show()

    

    width = property(get_width, set_width)
    height = property(get_height, set_height)