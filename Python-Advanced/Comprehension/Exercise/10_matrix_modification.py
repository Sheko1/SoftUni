def is_valid(r, c, matrix_1):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True

    return False


rows = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(rows)]

command = input()
while command != "END":
    data = command.split()

    type_command = data[0]
    row = int(data[1])
    col = int(data[2])
    value = int(data[3])

    if is_valid(row, col, matrix):
        if type_command == "Add":
            matrix[row][col] += value

        elif type_command == "Subtract":
            matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    command = input()

[print(" ".join(str(x) for x in row)) for row in matrix]
