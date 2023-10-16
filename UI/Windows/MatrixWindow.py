from tkinter import *
from tkinter import ttk
from UI.Constants import Constants
from Model.GraphManager import GraphManager


class MatrixWindow(Toplevel):

    model = GraphManager()

    def __init__(self, application, rows, columns):
        super().__init__()

        self.application = application
        self.rows = rows
        self.columns = columns

        self.__matrix = []

        for row_number in range(self.rows):
            self.__matrix.append([])

            for column_number in range(self.columns):
                text_field = ttk.Entry(master= self)
                text_field.insert(0, "0")
                text_field.grid(row = row_number, column = column_number)

                self.__matrix[row_number].append(text_field)

        make_analiz_button = ttk.Button(self,
                                            text="Выполнить анализ",
                                            command= self.make_analiz)
        make_analiz_button.grid(row = self.rows, column= self.columns)

    def make_analiz(self):
        matrix_for_model = [ [] for _ in range(self.rows)]

        for row_number in range(self.rows):
            for column_number in range(self.columns):
                text_field = self.__matrix[row_number][column_number]

                value = int(text_field.get())

                matrix_for_model[row_number].append(value)

        if self.application.is_adjacency_chosen:
            self.model.build_graph_from_adjacency(matrix_for_model)
        else:
            self.model.build_graph_from_incidence(matrix_for_model)

        self.application.go_to_info(self.model.show_graph_info())
        self.model.draw()


