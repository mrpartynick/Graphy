from tkinter import *
from tkinter import ttk
from UI.Constants import Constants


class GraphInfoWindow(Tk):

    k = Constants()

    def __init__(self, application, info_dict):
        super().__init__()

        self.application = application
        self.info_dict = info_dict

        info_array = self.parse_info()

        is_weighted_label = ttk.Label(self, text = info_array[0])
        is_oriented_label = ttk.Label(self, text = info_array[1])
        is_double_shared_label = ttk.Label(self, text = info_array[2])

        is_weighted_label.pack()
        is_oriented_label.pack()
        is_double_shared_label.pack()

    def parse_info(self):
        info_array = []

        if self.info_dict[self.k.is_weighted_graph_key]:
            info_array.append("Граф взвешенный")
        else:
            info_array.append("Граф не взвешенный")

        if self.info_dict[self.k.is_oriented_graph_key]:
            info_array.append("Граф ориентированный")
        else:
            info_array.append("Граф не ориентированный")

        if self.info_dict[self.k.is_double_shared_graph_key]:
            info_array.append("Граф двудольный")
        else:
            info_array.append("Граф не двудольный")

        return info_array
