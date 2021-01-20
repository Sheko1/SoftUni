def get_matrix():
    row, coll = [int(x) for x in input().split()]
    the_matrix = []

    for r in range(row):
        the_matrix.append([int(x) for x in input().split()])

    return the_matrix


def get_sub_matrix_sum(matrix_1, row, coll):
    size = 3
    sub_matrix = []
    the_sum = 0
    for r in range(row, row + size):
        cur_row = []
        for c in range(coll, coll + size):
            cur_row.append(matrix_1[r][c])
            the_sum += matrix_1[r][c]
        sub_matrix.append(cur_row)

    return sub_matrix, the_sum


def find_biggest_sub_matrix_sum(matrix_1):
    biggest_sum = get_sub_matrix_sum(matrix_1, 0, 0)

    for r in range(len(matrix_1) - 2):
        for c in range(len(matrix_1[r]) - 2):
            sub_matrix_data = get_sub_matrix_sum(matrix_1, r, c)

            if biggest_sum[1] < sub_matrix_data[1]:
                biggest_sum = sub_matrix_data

    return biggest_sum


def print_result(data):
    print(f"Sum = {data[1]}")

    for row in data[0]:
        print(" ".join(str(r) for r in row))


matrix = get_matrix()
result_data = find_biggest_sub_matrix_sum(matrix)
print_result(result_data)
