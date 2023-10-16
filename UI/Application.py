from Constants import Constants
from UI.Windows.MainWindow import MainWindow
from UI.Windows.SizeWindow import SizeWindow
from UI.Windows.MatrixWindow import MatrixWindow
from UI.Windows.GraphInfoWindow import GraphInfoWindow


class Application:

    is_adjacency_chosen = True

    def __init__(self):
       self.__main_window = MainWindow(self)

    def run(self):
        self.__main_window.mainloop()

    def go_to_size_window(self):
        self.size_window = SizeWindow(self)
        self.size_window.geometry("300x100")
        self.size_window.resizable(False, False)
        self.size_window.grab_set()

    def go_to_matrix(self, rows, columns):
        self.dismiss_window(self.size_window)

        self.matrix_window = MatrixWindow(self, rows, columns)
        self.matrix_window.resizable(False, False)
        self.matrix_window.grab_set()

    def go_to_info(self, info_dict):
        self.dismiss_window(self.matrix_window)

        self.info_window = GraphInfoWindow(self, info_dict)
        self.info_window.grab_set()

    def dismiss_window(self, window):
        window.grab_release()
        window.destroy()