def closest_center_point(x_1, y_1, x_2, y_2):
    if abs(x_1) + abs(y_1) <= abs(x_2) + abs(y_2):
        return f"({int(x_1)}, {int(y_1)})"

    else:
        return f"({int(x_2)}, {int(y_2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_center_point(x1, y1, x2, y2))
