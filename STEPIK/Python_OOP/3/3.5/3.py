from math import sqrt


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.list_track = [TrackLine(start_x, start_y, 0)]
    def add_track(self, tr): # - добавление линейного сегмента маршрута (следующей точки);
        self.list_track.append(tr)

    def get_tracks(self): # - получение кортежа из объектов класса TrackLine.
        return tuple(self.list_track)


    def __len__(self):
        sum = 0
        iter_list = self.list_track

        for i in range(0, len(iter_list) - 1):
            # L = sqrt((x1-x0)^2 + (y1-y0)^2) 
            first = (iter_list[i + 1].to_x - iter_list[i].to_x) ** 2
            second = (iter_list[i + 1].to_y - iter_list[i].to_y) ** 2         
            sum += sqrt(first + second)     
        return int(sum) 

    def __eq__(self, __o: object) -> bool:
        return len(self) == len(__o)

    def __lt__(self, __o: object) -> bool:
        return len(self) < len(__o)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed) -> None:
        self.to_x = to_x #
        self.to_y = to_y # - координаты следующей точки маршрута (целые или вещественные числа); 
        self.max_speed = max_speed # - максимальная скорость на данном участке (целое число).

track1, track2 = Track(0,0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))


track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
