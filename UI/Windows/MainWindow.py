from tkinter import *
from tkinter import ttk
from UI.Windows.SizeWindow import SizeWindow
from UI.Constants import Constants


class MainWindow(Tk):
    k = Constants()

    def __init__(self, application):
        super().__init__()

        self.application = application

        self.title(self.k.application_title)
        self.geometry(self.k.application_metrics())

        self.adjacency_button = ttk.Button(self, text = self.k.adjacency_button_text,
                                           width = self.k.buttons_width,
                                           command = self.adjacency_button_pressed)
        self.incidence_button = ttk.Button(self,
                                           text = self.k.incidence_button_text,
                                           width = self.k.buttons_width,
                                           command = self.incidence_button_pressed)
        self.adjacency_button.pack()
        self.incidence_button.pack()

    def adjacency_button_pressed(self):
        self.application.go_to_size_window()

    def incidence_button_pressed(self):
        self.application.is_adjacency_chosen = False
        self.application.go_to_size_window()

