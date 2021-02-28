from math import sqrt


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        x = abs(self.x - x)
        y = abs(self.y - y)
        return sqrt((x ** 2) + (y ** 2))


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
