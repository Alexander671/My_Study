class Mechanical: # - для очистки от крупных механических частиц;
    def __init__(self, date):
        self.date = date

class Aragon: # - для последующей очистки воды;
    def __init__(self, date):
        self.date = date

class Calcium: # - для обработки воды на третьем этапе.
    def __init__(self, date):
        self.date = date

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def add_filter(self, slot_num, filter): # - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3), если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только объекты класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.
        pass
    def remove_filter(self, slot_num): # - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
        pass 
    def get_filters(self): # - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
        pass 
    def water_on(self): # - включение воды: возвращает True, если вода течет и False - в противном случае.    
        pass 