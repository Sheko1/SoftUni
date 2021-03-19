class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.values = [0]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.values) > self.count:
            raise StopIteration

        value = self.values[-1]
        self.values.append(self.values[-1] + self.step)
        return value


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
