def get_matrix():
    row, column = [int(n) for n in input().split(", ")]
    result = []
    for r_1 in range(row):
        el = [int(el) for el in input().split()]
        result.append(el)

    return result


def print_result(matrix_1):
    for c in range(len(matrix_1[0])):
        column_sum = 0
        for r in range(len(matrix_1)):
            column_sum += matrix_1[r][c]

        print(column_sum)


matrix = get_matrix()
print_result(matrix)