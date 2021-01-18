def get_matrix():
    row, column = [int(n) for n in input().split(", ")]
    result_matrix = []
    for r_1 in range(row):
        el = [int(el) for el in input().split(", ")]
        result_matrix.append(el)

    return result_matrix


def sub_matrix_sum(matrix_1, row, column):
    size = 2
    the_sum = 0
    sub_matrix = []

    for r in range(row, row + size):
        row = []
        for c in range(column, column + size):
            the_sum += matrix[r][c]
            row.append(matrix_1[r][c])

        sub_matrix.append(row)

    return the_sum, sub_matrix


def get_best_sub_matrix_sum(matrix_1):
    best_sum = sub_matrix_sum(matrix_1, 0, 0)

    for r in range(len(matrix_1) - 1):
        for c in range(len(matrix_1[r]) - 1):
            cur_sum = sub_matrix_sum(matrix_1, r, c)
            if best_sum[0] < cur_sum[0]:
                best_sum = cur_sum

    return best_sum


def print_result(best_sum_matrix):
    the_sum, sub_matrix = best_sum_matrix
    for r in sub_matrix:
        print(" ".join(str(x) for x in r))

    print(the_sum)


matrix = get_matrix()

result = get_best_sub_matrix_sum(matrix)
print_result(result)
