def validation(row, col, matrix_1):
    return 0 <= row < len(matrix_1) and 0 <= col < len(matrix_1[0])


def movement(q_row, q_col, matrix_1, *args):
    queens_list = []
    for movement_type in args:
        for i in range(len(movement_type)):
            curr_row = q_row
            curr_col = q_col

            while validation(curr_row, curr_col, matrix_1):
                if matrix_1[curr_row][curr_col] == "Q":
                    queens_list.append([curr_row, curr_col])
                    break

                curr_row += movement_type[i][0]
                curr_col += movement_type[i][1]

    return queens_list


def queens_that_can_capture_king(row, col, matrix_1):
    diagonal_movement = ((-1, -1), (+1, -1), (-1, +1), (+1, +1))
    horizontal_movement = ((0, -1), (0, +1))
    vertical_movement = ((+1, 0), (-1, 0))

    queens = movement(row, col, matrix_1, diagonal_movement, horizontal_movement, vertical_movement)

    return queens


matrix = [input().split() for _ in range(8)]


result = []

for r in range(len(matrix)):
    if "K" not in matrix[r]:
        continue

    for c in range(len(matrix[r])):
        if matrix[r][c] == "K":
            result = queens_that_can_capture_king(r, c, matrix)


if result:
    for r in result:
        print(r)

else:
    print("The king is safe!")
