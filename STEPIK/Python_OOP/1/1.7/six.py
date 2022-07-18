# Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:

# build_sequence() - для создания пустого списка (метод возвращает пустой список);
# build_number(string) - для преобразования строки (string) в целое число (метод возвращает полученное целочисленное значение).

class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

# И предполагается его использовать следующим образом:

res = Loader.parse_format("4, 5, -6", Factory)