class VideoRating:
    def __init__(self, rat=0):
        if 0 <= rat <= 5:
            self.__rating = rat
        else:
            raise ValueError('неверное присваиваемое значение')

    @property
    def rating(self,):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

class VideoItem:
    def __init__(self, title, descr, path) -> None:
        self.title = title # - заголовок видео (строка); 
        self.descr = descr # - описание видео (строка); 
        self.path = path # - путь к видеофайлу. В каждом объекте класса VideoItem должны создаваться соответствующие атрибуты: title, descr, path.
        self.rating = VideoRating()
