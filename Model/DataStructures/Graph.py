import networkx
import matplotlib.pyplot as plt

class Stack:
    stack = []

    def __init__(self, arr=None):
        if arr is None:
            pass
        else:
            self.stack = arr

    def __str__(self):
        return str(self.stack)

    def __bool__(self):
        if self.stack == []:
            return False
        else:
            return True

    def remove_value(self):
        return self.stack.pop(-1)

    def clear(self):
        self.stack = []

    def add_value(self, value):
        self.stack = [value] + self.stack

    def add_arr(self, arr):
        self.stack = arr + self.stack

class Queue:
    queue = []

    # Инициализатор))))90)))(090)))
    def __init__(self, arr=None):
        if arr is None:
            pass
        else:
            self.queue = arr

    def __str__(self):
        return self.queue

    # Объект вернет истину, если очередь не пуста
    def __bool__(self):
        if self.queue == []:
            return False
        else:
            return True

    # Вернет длину очереди
    def __len__(self):
        return len(self.queue)

    # Добавить значение в очередь
    def add_value(self, value):
        self.queue.append(value)

    # Добавить массив значений в очередь
    def add_arr(self, arr):
        self.queue += arr

    # Удаление значения из очереди
    def remove_value(self):
        return self.queue.pop(0)

    # Удаление всех значений из очереди
    def clear(self):
        self.queue = []

class Kek:
    """Граф будет храниться в виде списка словарей смежности.
    Каждый элемент списка - словарь, предоставляющий информацию о вершине с соот. номером.
    В каждом словаре ключ - номер вершины, с которой смежна данная. Значение - вес ребра между вершинами.
    """
    _graph = []

    is_oriented = False
    is_weighted = False

    # Метод для построения графа из матрицы смежности
    def build_from_adjacency_matrix(self, adjacency_matrix):

        # Получаем кол-во вершин нашего графа
        value_of_nodes = len(adjacency_matrix)

        for node_index in range(value_of_nodes):
            self._graph.append({})

            for subnode_index in range(value_of_nodes):
                there_is_a_path = adjacency_matrix[node_index][subnode_index]

                if there_is_a_path != 0:

                    if there_is_a_path != 1:
                        self.is_weighted = True

                    self._graph[node_index][subnode_index] = adjacency_matrix[node_index][subnode_index]

        return self._graph

    # Метод для отрисовки графа
    def draw_graph(self):
        graph = networkx.Graph()
        nodes = [i for i in range(len(self._graph))]
        edges = []

        for node_index in range(len(self._graph)):
            bound_nodes = list(self._graph[node_index].keys())

            for bound_node in bound_nodes:
                edges.append((node_index, bound_node))

        graph.add_nodes_from(nodes)
        graph.add_edges_from(edges)

        networkx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()

    def there_is_a_path(self, node1, node2):
        pass

    def is_oriented(self):
        pass

    def get_graph(self):
        return self._graph


class Graph:
    hard_model = {}

    visited_peaks = {}
    queue = Queue()
    stack = Stack()
    searched_peak = None

    value_of_peaks = 0
    value_of_ribs = 0

    is_oriented = False
    is_weighted = False
    is_double_shared = False

    # Метод для построения графа из матрицы смежности
    def build_from_adjacency_matrix(self, adjacency_matrix):

        # Получаем кол-во вершин нашего графа
        self.value_of_peaks = len(adjacency_matrix)
        value_of_nodes = len(adjacency_matrix)

        for node_index in range(value_of_nodes):
            self.hard_model[node_index] = []

            for subnode_index in range(value_of_nodes):
                there_is_a_path = adjacency_matrix[node_index][subnode_index]

                if there_is_a_path != 0:

                    if there_is_a_path != 1:
                        self.is_weighted = True

                    self.hard_model[node_index].append(subnode_index)

    def build_from_incidence_matrix(self, matrix):
        self.hard_model = {}
        self.value_of_peaks = len(matrix)

        for node_index in range(self.value_of_peaks):
            self.hard_model[node_index] = []

            for subnode_index in range(self.value_of_peaks):
                there_is_a_path = matrix[node_index][subnode_index]

                if there_is_a_path != 0:

                    if there_is_a_path != 1:
                        self.is_weighted = True

                    if there_is_a_path == -1:
                        self.is_oriented = True

                    self.hard_model[node_index].append(subnode_index)

    def set_default_stage(self):
        self.hard_model = {}
        self.is_weighted = False
        self.is_oriented = False
        self.is_double_shared = False

    def draw_graph(self):
        graph = networkx.Graph()
        nodes = [i for i in range(self.value_of_peaks)]
        edges = []

        print(self.value_of_peaks)
        for node_index in range(self.value_of_peaks):
            bound_nodes = self.hard_model[node_index]


            for bound_node in bound_nodes:
                edges.append((node_index, bound_node))

        graph.add_nodes_from(nodes)
        graph.add_edges_from(edges)

        networkx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()


    def is_double_shared(self):
        def switch_color(color):
            if color == "red":
                return "blue"
            else:
                return "red"

        def paint_peak(peak, color):
            peak_color = colors_of_peaks[peak]
            new_color = switch_color(color)

            # Если вершина не покрашена - красим
            if peak_color is None:
                colors_of_peaks[peak] = new_color

                bounded_peaks = self.hard_model.get(peak, None)
                print(bounded_peaks)

                if bounded_peaks is not None:
                    for b_p in bounded_peaks:
                        result = paint_peak(b_p, new_color)

                        if result is False:
                            return False
            # Иначе...
            else:
                # Если цвет вершины не совпадает с тем, в который мы должны красить
                if peak_color != new_color:
                    print(peak)
                    return False
                else:
                    return True

            return True

        colors_of_peaks = [None for i in range(1,self.value_of_peaks+2)]
        color_for_painting = "blue"

        for peak in self.hard_model.keys():
            result = paint_peak(peak, color_for_painting)

            if not result:
                print("lol")
                print(colors_of_peaks)
                return False

        return True

    def new_paint(self):
        # Функция смены цвета
        def switch_color(color):
            if color == "red":
                return "blue"
            else:
                return "red"

        # Функция окрашивания вершины. Передаем вершину, которую окрашиваем и цвет В который окрашиваем
        def rec_paint(peak, color):
            # Смотрим цвет вершины, которую собираемся окрашивать
            color_of_current_peak = colors_of_peaks[peak]

            # Если вершина не окрашена - просто красим
            if color_of_current_peak is None:
                # Красим вершину
                colors_of_peaks[peak] = color
                # Меняем цвет
                new_color = switch_color(color)

                # Берем детей вершины
                bounded_peaks = self.hard_model.get(peak, None)

                # Если дети есть
                if bounded_peaks is not None:
                    # Красим каждого из детей
                    for bounded_peak in bounded_peaks:
                        rec_paint(bounded_peak, new_color)



        # Номер вершины, с которой мы начинаем
        first_peak = 1
        # Массив, в котором хранится текущий цвет каждой вершины
        colors_of_peaks = [None for i in range(1, self.value_of_peaks+2)]
        color_of_first_peak = "red"

        # Красим первую вершину
        rec_paint(first_peak, color_of_first_peak)

        # Нам нужно пройтись по каждой вершине и убедиться, что она окрашена в разные цвета со своими детьми
        print(colors_of_peaks)

        for peak in self.hard_model.keys():
            bounded_peaks = self.hard_model.get(peak, None)

            if bounded_peaks is not None:
                for b_p in bounded_peaks:
                    if colors_of_peaks[b_p] == colors_of_peaks[peak]:

                        return False
        return True
