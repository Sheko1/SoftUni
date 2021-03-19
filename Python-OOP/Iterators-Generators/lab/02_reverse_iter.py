class reverse_iter:
    def __init__(self, iterable):
        self.list = list(iterable)
        self.index = len(self.list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.list[self.index]
        self.index -= 1
        return value


for i in reverse_iter([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(i)
