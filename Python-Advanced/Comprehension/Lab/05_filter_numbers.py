def is_valid(num):
    return any(num % x == 0 for x in range(2, 11))


start = int(input())
end = int(input()) + 1

filtered_numbers = [num for num in range(start, end) if is_valid(num)]
print(filtered_numbers)
