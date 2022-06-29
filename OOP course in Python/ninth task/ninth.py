from random import randint


class Iterator:
    def __init__(self, quantity, min, max):
        self.qua = quantity
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.qua > 0:
            number = randint(self.min, self.max)
            self.qua -= 1
            return number
        else:
            raise StopIteration


a = Iterator(10, 0, 50)
for item in a:
    print(item)