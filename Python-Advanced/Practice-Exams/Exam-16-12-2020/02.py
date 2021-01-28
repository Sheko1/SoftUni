def get_player_pos(matrix_1):
    for r in range(len(matrix_1)):
        for c in range(len(matrix_1[r])):
            if matrix_1[r][c] == "P":
                return r, c


def movement(position, command_1, matrix_1):
    r, c = position

    if command_1 == "up":
        if r - 1 >= 0:
            r -= 1

    elif command_1 == "down":
        if r + 1 < len(matrix_1):
            r += 1

    elif command_1 == "left":
        if c - 1 >= 0:
            c -= 1

    elif command_1 == "right":
        if c + 1 < len(matrix_1[0]):
            c += 1

    return r, c


def print_matrix(matrix_1):
    [print("".join(r)) for r in matrix_1]


string = input()
rows = int(input())

matrix = [list(input()) for _ in range(rows)]

commands_n = int(input())
commands = [input() for _ in range(commands_n)]

player_pos = get_player_pos(matrix)

for command in commands:
    row, col = player_pos
    matrix[row][col] = "-"

    new_player_pos = movement(player_pos, command, matrix)
    row, col = new_player_pos

    if player_pos == new_player_pos:
        string = string[:-1]

    if matrix[row][col].isalpha():
        string += matrix[row][col]

    matrix[row][col] = "P"
    player_pos = new_player_pos

print(string)
print_matrix(matrix)
