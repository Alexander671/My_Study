class Graph:
    LIMIT_Y = [0, 10]
    def set_data(self, data):
        self.data = data

    def draw(self):
        range_n = self.LIMIT_Y[0]
        range_m = self.LIMIT_Y[1]
        r_list = range(range_n,range_m + 1)

        return ' '.join(map(str, filter(lambda x: x in r_list, self.data)))
    
graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
print(graph_1.draw())