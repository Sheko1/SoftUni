def closest_center_point(x_1, y_1, x_2, y_2):
    if abs(x_1) + abs(y_1) <= abs(x_2) + abs(y_2):
        return f"({int(x_1)}, {int(y_1)})({int(x_2)}, {int(y_2)})"

    else:
        return f"({int(x_2)}, {int(y_2)})({int(x_1)}, {int(y_1)})"


def longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    first_line = (abs(x_1) + abs(x_2)) + (abs(y_1) + abs(y_2))
    second_line = (abs(x_3) + abs(x_4)) + (abs(y_3) + abs(y_4))

    if first_line >= second_line:
        return closest_center_point(x_1, y_1, x_2, y_2)

    else:
        return closest_center_point(x_3, y_3, x_4, y_4)


x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())

x4 = float(input())
y4 = float(input())


print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))