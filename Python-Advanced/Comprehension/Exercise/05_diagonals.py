rows = int(input())
matrix = [[int(row) for row in input().split(", ")] for _ in range(rows)]

first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]

print(f"First diagonal: {', '.join(str(x) for x in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {sum(second_diagonal)}")
