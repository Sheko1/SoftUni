def get_magic_triangle(n, a=1, matrix=[]):
    if a > n:
        return matrix
    matrix.append([1] * a)
    if len(matrix[a - 1]) > 2:
        index = 1
        while index < len(matrix[a - 2]):
            matrix[a - 1][index] = matrix[a - 2][index - 1] + matrix[a - 2][index]
            index += 1

    return get_magic_triangle(n, a+1)


print(get_magic_triangle(5))
