class Factory:




    def build_sequence(self): # - для создания начального пустого списка (метод должен возвращать пустой список);
        return []

    def build_number(self, string): # - для преобразования переданной в метод строки (string) в вещественное значение (метод должен возвращать полученное вещественное число).
        return float(string)



class Loader:
    def parse_format(self, string, factory:Factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
print(res)