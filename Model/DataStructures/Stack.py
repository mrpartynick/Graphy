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