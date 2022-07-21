class Clock:
    def __init__(self,hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self): # - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
        return self.hours * 3600 + self.minutes * 60 + self.seconds

        
class DeltaClock:
    def __init__(self, clck1, clck2):
        self.clock1 = clck1
        self.clock2 = clck2

    def minus(self):
        clck1:Clock = self.clock1
        clck2:Clock = self.clock2
        
        delta_hours = clck1.hours - clck2.hours
        delta_minutes = clck1.minutes - clck2.minutes
        delta_seconds = clck1.seconds - clck2.seconds
        if any(filter(lambda x: x> 0, [delta_hours, delta_minutes, delta_seconds])):
            return delta_hours, delta_minutes, delta_seconds
        else:
            return 0,0,0


    def __str__(self):
        
        hours, mins, secs = self.minus()
        return f'{hours//10}{hours%10}: {mins//10}{mins%10}: {secs//10}{secs%10}'
    
    def __len__(self):    
        return Clock(*self.minus()).get_time()

dt = DeltaClock(Clock(10,2,3), Clock(1,2,5))
str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)