def get_matrix():
    n = int(input())
    result = []
    for _ in range(n):
        result.append([i for i in input()])

    return result


def search_symbol(matrix_1, symbol):
    for r in range(len(matrix_1)):
        for c in range(len(matrix_1[r])):
            if matrix_1[r][c] == symbol:
                return r, c


def print_result(search_result, symbol):
    if search_result:
        print(search_result)

    else:
        print(f"{symbol} does not occur in the matrix")


matrix = get_matrix()

symbol_to_search = input()
result_search = search_symbol(matrix, symbol_to_search)
print_result(result_search, symbol_to_search)
