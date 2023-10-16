from tkinter import *
from tkinter import ttk
from UI.Constants import Constants


class SizeWindow(Toplevel):
    __k = Constants()
    __sizes = [str(i) for i in range(1,11)]

    def __init__(self, application):
        super().__init__()

        self.application = application
        self.title("title")
        self.geometry(self.__k.application_metrics())

        self.info_label = ttk.Label(self, text=self.__k.matrix_size_info)

        self.rows_combobox = ttk.Combobox(self, values= self.__sizes)
        self.columns_combobox = ttk.Combobox(self, values=self.__sizes)

        self.continue_button = ttk.Button(self, text="Продолжить",
                                          command=self.continue_button_pressed)

        self.info_label.pack(anchor=N)
        self.rows_combobox.pack()
        self.columns_combobox.pack()
        self.continue_button.pack(anchor=S)

    def continue_button_pressed(self):
        rows = int(self.rows_combobox.get())
        columns = int(self.columns_combobox.get())

        self.application.go_to_matrix(rows, columns)
