def get_matrix():
    row, column = [int(x) for x in input().split()]
    the_matrix = []

    for r in range(row):
        the_matrix.append([x for x in input().split()])

    return the_matrix


def get_sub_matrix(matrix_1, row, coll):
    size = 2
    sub_matrix = []

    for r in range(row, row + size):
        for c in range(coll, coll + size):
            sub_matrix.append(matrix_1[r][c])

    return sub_matrix


def is_chars_equal(sub_matrix):
    char = sub_matrix[0]

    for ch in sub_matrix:
        if char == ch:
            pass

        else:
            return False

    return True


def equal_chars_in_matrix_finder(matrix_1):
    counter = 0

    for r in range(len(matrix_1) - 1):
        for c in range(len(matrix_1[r]) - 1):
            sub_matrix = get_sub_matrix(matrix_1, r, c)
            if is_chars_equal(sub_matrix):
                counter += 1

    return counter


matrix = get_matrix()
print(equal_chars_in_matrix_finder(matrix))
