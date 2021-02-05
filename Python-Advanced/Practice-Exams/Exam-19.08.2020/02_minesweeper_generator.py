def is_pos_valid(r, c, matrix):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


def calculate_bomb_position(r, c, matrix):
    bomb_range = ((-1, -1), (-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1))

    for pos in bomb_range:
        curr_row = pos[0] + r
        curr_col = pos[1] + c

        if is_pos_valid(curr_row, curr_col, matrix) and matrix[curr_row][curr_col] != "*":
            matrix[curr_row][curr_col] += 1

    return matrix


row_col = int(input())
field = [[0] * row_col for _ in range(row_col)]

bomb_count = int(input())
bombs = [eval(input()) for _ in range(bomb_count)]

for bomb in bombs:
    row, col = bomb
    field[row][col] = "*"
    field = calculate_bomb_position(row, col, field)

[print(*r) for r in field]
