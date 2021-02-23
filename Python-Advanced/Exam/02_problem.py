from math import floor

DELTAS = {"up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)}


def in_range(row, col, matrix):
    return 0 <= row < len(matrix[0]) and 0 <= col < len(matrix[0])


def get_field(n):
    player_pos = None
    matrix = []
    for r in range(n):
        row = input().split()
        if "P" in row:
            player_pos = (r, row.index("P"))

        matrix.append(row)

    return player_pos, matrix


def movement(type_movement, matrix, player_pos):
    row, col = player_pos

    row += DELTAS[type_movement][0]
    col += DELTAS[type_movement][1]

    if in_range(row, col, matrix):
        return row, col

    return False


def print_path(path_list):
    [print(x) for x in path_list]


player_position, field = get_field(int(input()))
coins = 0
path = []

while True:
    command = input()
    if command in DELTAS:
        player_position = movement(command, field, player_position)

        if player_position:
            r, c = player_position

            if field[r][c].isdigit():
                coins += int(field[r][c])

            elif field[r][c] == "X":
                coins = floor(coins * 0.5)
                break

        else:
            coins = floor(coins * 0.5)
            break

    path.append([player_position[0], player_position[1]])

    if coins >= 100:
        break


if coins >= 100:
    print(f"You won! You've collected {coins} coins.")

else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
print_path(path)
