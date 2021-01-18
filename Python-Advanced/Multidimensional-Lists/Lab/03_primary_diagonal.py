def get_matrix():
    n = int(input())
    result = []
    for _ in range(n):
        result.append([int(n) for n in input().split()])

    return result


def primary_diagonal_sum(matrix_1):
    result = 0
    for i in range(len(matrix_1)):
        result += matrix_1[i][i]

    return result


matrix = get_matrix()
print(primary_diagonal_sum(matrix))

