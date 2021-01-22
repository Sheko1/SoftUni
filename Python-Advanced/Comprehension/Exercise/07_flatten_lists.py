data = input().split("|")

result = [value for str_nums in reversed(data) for value in str_nums.split()]
print(*result)
