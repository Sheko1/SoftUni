def get_matrix():
    rows, columns = [int(x) for x in input().split()]
    the_matrix = [[""] * columns for x in range(rows)]

    return the_matrix


def print_result(filled_matrix):
    [print("".join(row)) for row in filled_matrix]


matrix = get_matrix()
snake = input()
snake_index = 0

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if snake_index not in range(len(snake)):
            snake_index = 0
        matrix[r][c] = snake[snake_index]
        snake_index += 1

    if r % 2 != 0:
        matrix[r].reverse()

print_result(matrix)
