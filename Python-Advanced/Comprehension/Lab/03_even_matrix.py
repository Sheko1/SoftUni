def get_row():
    return [int(x) for x in input().split(", ")]


def get_even_row(row):
    return [x for x in row if x % 2 == 0]


rows = int(input())
matrix = [get_row() for _ in range(rows)]
even_matrix = [get_even_row(row) for row in matrix]
print(even_matrix)
