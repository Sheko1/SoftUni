MOVE_COMMANDS = {"up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)}


def is_move_valid(matrix_1, pos):
    row, col = pos
    return 0 <= row < len(matrix_1) and 0 <= col < len(matrix_1[0])


def get_field_and_snake_pos(size):
    matrix_to_return = []
    snake_pos_to_return = None

    for i in range(size):
        curr_row = list(input())
        matrix_to_return.append(curr_row)

        if "S" in curr_row:
            snake_pos_to_return = (i, curr_row.index("S"))

    return matrix_to_return, snake_pos_to_return


def get_other_burrow_pos(matrix_1):
    for row in range(len(matrix_1)):
        if "B" in matrix_1[row]:
            index = matrix_1[row].index("B")
            matrix_1[row][index] = "-"
            return row, index


def movement(move_command, food_quantity_1, pos, matrix_1):
    row, col = pos
    matrix_1[row][col] = "."

    row += MOVE_COMMANDS[move_command][0]
    col += MOVE_COMMANDS[move_command][1]

    if is_move_valid(matrix_1, (row, col)):
        if matrix_1[row][col] == "*":
            matrix_1[row][col] = "."
            food_quantity_1 += 1

        elif matrix_1[row][col] == "B":
            matrix_1[row][col] = "."
            row, col = get_other_burrow_pos(matrix_1)

        matrix_1[row][col] = "S"
        return (row, col), food_quantity_1, matrix_1


matrix, snake_pos = get_field_and_snake_pos(int(input()))

food_quantity = 0
win = False

while True:
    command = input()
    data = movement(command, food_quantity, snake_pos, matrix)
    if data:
        snake_pos, food_quantity, matrix = data

        if food_quantity == 10:
            win = True
            break

        continue

    break

if win:
    print("You won! You fed the snake.")

else:
    print("Game over!")

print(f"Food eaten: {food_quantity}")
[print("".join(row)) for row in matrix]
