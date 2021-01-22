def position(x):
    return chr(x+97)


def palindrome_rows(curr_row, row_i):
    row_char = position(row_i)
    return [f"{row_char}{position(row_i+i)}{row_char}" for i in range(len(curr_row))]


row, col = [int(x) for x in input().split()]
matrix = [[""]*col for _ in range(row)]

matrix = [palindrome_rows(matrix[row], row) for row in range(len(matrix))]

[print(*row) for row in matrix]
