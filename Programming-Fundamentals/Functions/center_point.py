def closest_center_point(x_1, y_1, x_2, y_2):
    if abs(float(x_1)) + abs(float(y_1)) <= abs(float(x_2)) + abs(float(y_2)):
        return f"({x_1}, {y_1})"

    else:
        return f"({x_2}, {y_2})"


x1 = input()
y1 = input()
x2 = input()
y2 = input()

print(closest_center_point(x1, y1, x2, y2))