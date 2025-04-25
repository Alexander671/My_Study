class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period

class SolarSystem:
    flag_implemented = None
    __slots__ = \
                ('_mercury', # - ссылка на планету Меркурий (объект класса Planet);
                 '_venus', # - ссылка на планету Венера (объект класса Planet);
                 '_earth', # - ссылка на планету Земля (объект класса Planet);
                 '_mars', # - ссылка на планету Марс (объект класса Planet);
                 '_jupiter', # - ссылка на планету Юпитер (объект класса Planet);
                 '_saturn', # - ссылка на планету Сатурн (объект класса Planet);
                 '_uranus', # - ссылка на планету Уран (объект класса Planet);
                 '_neptune',) # - ссылка на планету Нептун (объект класса Planet).

    def __init__(self,):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)

    def __new__(cls, *args):
        if not cls.flag_implemented:
            cls.flag_implemented = super().__new__(cls)
        return cls.flag_implemented
        
s_system = SolarSystem()
