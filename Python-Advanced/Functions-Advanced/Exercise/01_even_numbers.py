numbers = [int(num) for num in input().split()]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
