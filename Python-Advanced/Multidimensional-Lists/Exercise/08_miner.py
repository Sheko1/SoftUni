def player_start_and_coal_counter(matrix_1):
    player_start = None
    coal_counter = 0

    for r in range(len(matrix_1)):
        for c in range(len(matrix_1[r])):
            if matrix_1[r][c] == "s":
                player_start = (r, c)

            elif matrix_1[r][c] == "c":
                coal_counter += 1

    return player_start, coal_counter


def move(matrix_1, command_move, player_pos, coal_counter):
    row, col = player_pos
    new_pos = player_pos

    if command_move == "left":
        if col - 1 >= 0:
            new_pos = (row, col-1)

    elif command_move == "right":
        if col + 1 < len(matrix_1[0]):
            new_pos = (row, col+1)

    elif command_move == "up":
        if row - 1 >= 0:
            new_pos = (row-1, col)

    elif command_move == "down":
        if row + 1 < len(matrix_1):
            new_pos = (row+1, col)

    if matrix_1[new_pos[0]][new_pos[1]] == "c":
        coal_counter -= 1
        matrix_1[new_pos[0]][new_pos[1]] = "*"

    return new_pos, coal_counter


n = int(input())
commands = input().split()
matrix = [input().split() for _ in range(n)]

player_position, coal = player_start_and_coal_counter(matrix)
finished = False

for command in commands:
    player_position, coal = move(matrix, command, player_position, coal)

    if matrix[player_position[0]][player_position[1]] == "e":
        print(f"Game over! {player_position}")
        finished = True
        break

    elif coal == 0:
        print(f"You collected all coals! {player_position}")
        finished = True
        break

if not finished:
    print(f"{coal} coals left. {player_position}")
