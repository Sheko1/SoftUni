def get_matrix():
    rows, cols = [int(x) for x in input().split()]
    the_matrix = []

    for r in range(rows):
        the_matrix.append(input().split())

    return the_matrix


def print_matrix(matrix_1):
    for r in matrix_1:
        print(" ".join(r))


def check_size(matrix_1, rows, cols):
    if rows[0] in range(len(matrix_1)) and cols[0] in range(len(matrix_1[0])) \
            and rows[1] in range(len(matrix_1)) and cols[1] in range(len(matrix_1[0])):
        return True

    return False


matrix = get_matrix()

command = input()

while command != "END":
    data = command.split()
    is_valid = False

    if data[0] == "swap" and len(data) == 5:
        row = int(data[1])
        col = int(data[2])

        swap_row = int(data[3])
        swap_col = int(data[4])

        if check_size(matrix, (row, swap_row), (col, swap_col)):
            matrix[row][col], matrix[swap_row][swap_col] = matrix[swap_row][swap_col], matrix[row][col]
            print_matrix(matrix)
            is_valid = True

    if not is_valid:
        print("Invalid input!")

    command = input()
