def get_matrix():
    result = []
    for _ in range(int(input())):
        result.append([int(i) for i in input().split()])

    return result


def primary_diagonal(matrix_1):
    result = 0

    for i in range(len(matrix_1)):
        result += matrix_1[i][i]

    return result


def secondary_diagonal(matrix_1):
    result = 0

    for i in range(len(matrix_1)):
        result += matrix_1[i][len(matrix_1) - i - 1]

    return result


def print_result(pri_dia, sec_dia):
    print(abs(pri_dia - sec_dia))


matrix = get_matrix()

primary_diagonal_sum = primary_diagonal(matrix)
secondary_diagonal_sum = secondary_diagonal(matrix)
print_result(primary_diagonal_sum, secondary_diagonal_sum)
