class Money:
    def __init__(self,  volume=0, cb=None):
        self.__cb:CentralBank = cb
        self.__volume = volume
    
    @property
    def cb(self):
        return self.__cb
    
    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, value):
        self.__volume = value

    def get_comparable(self):
        try:
            get_str_of_valute = self.cb.class_to_str[type(self).__name__]
            get_rate = self.cb.rates[get_str_of_valute]
            return ((self.volume / get_rate) * 0.9, (self.volume / get_rate) * 1.1)
        except:
            raise ValueError("Неизвестен курс валют.")

    # ==
    def __eq__(self, __o: object) -> bool:
        sorted_segment = sorted((self.get_comparable(), __o.get_comparable()))
        return sorted_segment[0][1] > sorted_segment[1][0]

    # <
    def __lt__(self, __o: object) -> bool:
        return self.get_comparable() < __o.get_comparable()
    
    # <=
    def __le__(self, __o: object) -> bool:
        return self.get_comparable() <= __o.get_comparable()



class MoneyR(Money): # - для рублевых кошельков
    pass
    
class MoneyD(Money): # - для долларовых кошельков
    pass

class MoneyE(Money): # - для евро-кошельков
    pass


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    class_to_str = {'MoneyR': 'rub','MoneyE': 'euro', 'MoneyD': 'dollar'}
    def __new__(cls):
        return None    

    from typing import Union
    @classmethod
    def register(cls, money:Union[MoneyR, MoneyD, MoneyE]): # - для регистрации объектов классов MoneyR, MoneyD и MoneyE.
        money.cb = cls



CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(1450000)
e = MoneyE(23000.0)

CentralBank.register(r)
CentralBank.register(e)

if r == e:
    print("неплохо")
else:
    print("нужно поднажать")

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(4500)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")

print(MoneyR(7250) < MoneyD(100), MoneyD(100) >= MoneyE(115), MoneyE(115) > MoneyR(7250))