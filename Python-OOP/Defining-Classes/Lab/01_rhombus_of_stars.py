def draw_line(offset, symbol, count):
    spaces = offset * " "
    line = (f"{symbol} " * count).strip()
    print(f"{spaces}{line}")


def draw_rhombus(n):
    symbol = "*"
    for i in range(n):
        offset = n - i - 1
        draw_line(offset, symbol, i+1)

    for i in range(n-2, -1, -1):
        offset = n - i - 1
        draw_line(offset, symbol, i+1)


draw_rhombus(int(input()))
