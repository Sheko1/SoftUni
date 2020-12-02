def horizontal_win_check(player, lines_1):
    for index in range(3):
        if lines_1[index][0] == lines_1[index][1] == lines_1[index][2]:
            if lines_1[index][index] == "1":
                player[0] = "First"

            elif lines_1[index][index] == "2":
                player[0] = "Second"

            else:
                return False

            return True


def vertical_win_check(player, lines_1):
    for index in range(3):
        if lines_1[0][index] == lines_1[1][index] == lines_1[2][index]:
            if lines_1[index][index] == "1":
                player[0] = "First"

            elif lines_1[index][index] == "2":
                player[0] = "Second"

            else:
                return False

            return True


def diagonal_win_check(player, lines_1):
    if lines_1[0][0] == lines_1[1][1] == lines_1[2][2]:
        if lines_1[0][0] == "1":
            player[0] = "First"

        elif lines_1[0][0] == "2":
            player[0] = "Second"

        else:
            return False

        return True

    elif lines_1[0][-1] == lines_1[1][1] == lines_1[2][0]:
        if lines_1[0][-1] == "1":
            player[0] = "First"

        elif lines_1[0][-1] == "2":
            player[0] = "Second"

        else:
            return False

        return True


lines = [
    input().split(),
    input().split(),
    input().split()
]

winner = [""]

if horizontal_win_check(winner, lines):
    print(f"{winner[0]} player won")

elif vertical_win_check(winner, lines):
    print(f"{winner[0]} player won")

elif diagonal_win_check(winner, lines):
    print(f"{winner[0]} player won")

else:
    print("Draw!")