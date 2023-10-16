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