class Vertex: # - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.);
    def __init__(self,):
        self._links = None #  - список связей с другими вершинами графа (список объектов класса Link).

    @property
    def links(self,):
        return self._links

    @links.setter
    def links(self, v):
        self._links = v

class Link: # - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.);
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2 # ссылки на объекты класса Vertex, которые соединяются данной связью;
        self._dist = dist # - длина связи (по умолчанию 1); это может быть длина пути, время в пути и др.

class LinkedGraph: # - для представления связного графа в целом (карта целиком).
    def __init__(self,links:list, vertex:list):
        self._links = links # - список из всех связей графа (из объектов класса Link);
        self._vertex = vertex # - список из всех вершин графа (из объектов класса Vertex).

    def add_vertex(self, v): # ... - для добавления новой вершины v в список _vertex (если она там отсутствует);
        self._vertex.append(v)

    def add_link(self, link): # ... - для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует);
        self._links.append(link)

    def find_path(self, start_v,  stop_v): # ... - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v.
        self._vertex[start_v]