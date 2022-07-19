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