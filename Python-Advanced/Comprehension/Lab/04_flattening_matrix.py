def get_row():
    return [int(x) for x in input().split(", ")]


rows = int(input())
matrix = [get_row() for _ in range(rows)]
flat_matrix = [x for row in matrix for x in row]
print(flat_matrix)
