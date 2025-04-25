class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data): # - для передачи нового списка данных в текущий график;
        self.data = data

    def check_permission_to_show(self, data):
        if self.is_show:
            return data
        else: 
            return "Отображение данных закрыто"

    def show_table(self):  # - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
        return self.check_permission_to_show(' '.join(map(str, self.data)))

    def show_graph(self): # - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
        return self.check_permission_to_show(f'Графическое отображение данных: {self.show_table()}')

    def show_bar(self): # - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
        return self.check_permission_to_show(f'Столбчатая диаграмма: {self.show_table()}')

    def set_show(self, fl_show): # - метод для изменения локального свойства is_show на переданное значение fl_show.
        self.is_show = fl_show

data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
print(gr.show_bar())
gr.set_show(fl_show=False)
print(gr.show_table())
