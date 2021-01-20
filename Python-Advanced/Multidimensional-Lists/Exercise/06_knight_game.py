def get_matrix():
    the_matrix = [list(input()) for _ in range(int(input()))]

    return the_matrix


def kill_counter(matrix_1, row_1, col_1):
    kill = 0
    rows = [-2, -2, 2, 2, 1, -1, 1, -1]
    cols = [-1, 1, -1, 1, -2, -2, 2, 2]

    row_size = len(matrix_1)
    col_size = len(matrix_1[0])

    for i in range(len(rows)):
        curr_row = row_1 + rows[i]
        curr_col = col_1 + cols[i]
        if 0 <= curr_row < row_size and 0 <= curr_col < col_size:
            if matrix_1[curr_row][curr_col] == "K":
                kill += 1

    return kill


def biggest_killer(matrix_1):
    the_most_kills = (0,)
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "K":
                kills = kill_counter(matrix_1, r, c)
                if kills > the_most_kills[0]:
                    the_most_kills = (kills, r, c)

    return the_most_kills


matrix = get_matrix()

counter = 0
while True:
    killer_to_remove = biggest_killer(matrix)
    if killer_to_remove[0] == 0:
        print(counter)
        break

    counter += 1
    row = killer_to_remove[1]
    col = killer_to_remove[2]
    matrix[row][col] = "0"
