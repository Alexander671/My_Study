class Money:
# - приватная локальная переменная money (целочисленная) для хранения количества денег (своя для каждого объекта класса Money);
    def __init__(self, money):
        self.__money = money

# - публичный метод set_money(money) для передачи нового значения приватной локальной переменной money (изменение выполняется только если метод check_money(money) возвращает значение True);
    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
        
# - публичный метод get_money() для получения текущего объема средств (денег);
    def get_money(self):
        return self.__money

# - публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
    def add_money(self, mn):
        self.__money += mn._Money__money

# - приватный метод класса check_money(money) для проверки корректности объема средств в параметре money (возвращает True, если значение корректно и False - в противном случае).
    def __check_money(self, mn):
        # Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или равным нулю.
        return type(mn) == int and mn >= 0

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120