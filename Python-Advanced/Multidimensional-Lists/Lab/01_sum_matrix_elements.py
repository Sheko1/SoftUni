def get_matrix():
    row, column = [int(n) for n in input().split(", ")]
    result = []
    for r_1 in range(row):
        el = [int(el) for el in input().split(", ")]
        result.append(el)

    return result


matrix = get_matrix()

matrix_sum = 0

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        matrix_sum += matrix[r][c]

print(matrix_sum)
print(matrix)
