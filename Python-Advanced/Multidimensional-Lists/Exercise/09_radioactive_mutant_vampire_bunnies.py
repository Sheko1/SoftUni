from copy import deepcopy


def player_start(matrix_1):
    player_position = None

    for r in range(len(matrix_1)):
        for c in range(len(matrix_1[r])):
            if matrix_1[r][c] == "P":
                player_position = (r, c)
                break

    return player_position


def multiply_bunnies(matrix_1):
    the_matrix = deepcopy(matrix_1)
    for r in range(len(the_matrix)):
        for c in range(len(the_matrix[r])):

            if the_matrix[r][c] == "B":
                if r - 1 >= 0:
                    matrix_1[r - 1][c] = "B"

                if r + 1 < len(matrix_1):
                    matrix_1[r + 1][c] = "B"

                if c - 1 >= 0:
                    matrix_1[r][c - 1] = "B"

                if c + 1 < len(matrix_1[0]):
                    matrix_1[r][c + 1] = "B"


def move(matrix_1, command_move, player_position):
    r, c = player_position
    new_pos = player_position

    if command_move == "L":
        new_pos = (r, c - 1)

    elif command_move == "R":
        new_pos = (r, c + 1)

    elif command_move == "U":
        new_pos = (r - 1, c)

    elif command_move == "D":
        new_pos = (r + 1, c)

    multiply_bunnies(matrix_1)

    if new_pos[0] not in range(len(matrix_1)) or new_pos[1] not in range(len(matrix_1[0])):
        return True

    return new_pos


row, col = input().split()
matrix = [list(input()) for _ in range(int(row))]
commands = list(input())

player_pos = player_start(matrix)
matrix[player_pos[0]][player_pos[1]] = "."
for command in commands:
    new_player_pos = move(matrix, command, player_pos)

    if new_player_pos is True:
        [print("".join(r)) for r in matrix]
        print(f"won: {' '.join(str(x) for x in player_pos)}")
        break

    elif matrix[new_player_pos[0]][new_player_pos[1]] == "B":
        [print("".join(r)) for r in matrix]
        print(f"dead: {' '.join(str(x) for x in new_player_pos)}")
        break

    player_pos = new_player_pos
