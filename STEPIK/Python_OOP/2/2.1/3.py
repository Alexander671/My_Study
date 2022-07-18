class Clock:
    def __init(self, time=0): #  приватная локальная переменная time для хранения текущего времени, целое число (своя для каждого объекта класса Clock с начальным значением 0);
        self.__time = time        
    
    def set_time(self, tm): #  публичный метод set_time(tm) для установки текущего времени (присваивает значение tm приватному локальному свойству time, если метод check_time(tm) возвратил True);
        if self.__check_time(tm):
            self.__time = tm
    
    def get_time(self): #  публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
        return self.__time
    
    @classmethod
    def __check_time(cls, tm): #  приватный метод класса check_time(tm) для проверки корректности времени в переменной tm (возвращает True, если значение корректно и False - в противном случае).
        # Проверка корректности выполняется по критерию: tm должна быть целым числом, больше или равна нулю и меньше 100 000.
        return type(tm) == int and 0 <= tm < 100000

clock = Clock()
clock.set_time(4530)
print(clock.get_time())