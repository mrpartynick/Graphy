from Model.DataStructures.Graph import Graph
from UI.Constants import Constants

class GraphManager:

    g = Graph()
    k = Constants()

    def build_graph_from_adjacency(self, matrix):
        self.g.build_from_adjacency_matrix(matrix)

    def draw(self):
        self.g.draw_graph()

    def build_graph_from_incidence(self, matrix):
        self.g.build_from_incidence_matrix(matrix)

    def show_graph_info(self):
        info_dict = {}

        self.g.is_double_shared = self.g.is_double_shared()

        info_dict[self.k.is_weighted_graph_key] = self.g.is_weighted
        info_dict[self.k.is_oriented_graph_key] = self.g.is_oriented
        info_dict[self.k.is_double_shared_graph_key] = self.g.is_double_shared

        return info_dict